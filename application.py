from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from unstoppable_domains import Resolution
import boto3
from ai_analysis import analyze_transactions

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
db = SQLAlchemy(app)
jwt = JWTManager(app)
resolution = Resolution()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message="User registered successfully"), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.password == data['password']:
        access_token = create_access_token(identity=user.username)
        return jsonify(access_token=access_token), 200
    return jsonify(message="Invalid credentials"), 401

@app.route('/analyze', methods=['POST'])
@jwt_required()
def analyze_wallet():
    current_user = get_jwt_identity()
    data = request.json
    domain = data.get('domain')
    wallet_address = resolve_domain(domain)
    transactions = data.get('transactions')
    analysis_result = analyze_transactions(transactions)
    return jsonify({
        'user': current_user,
        'wallet_address': wallet_address,
        'analysis': analysis_result
    })

@app.route('/search', methods=['POST'])
@jwt_required()
def search():
    data = request.json
    query = data.get('query')
    search_results = search_kendra(query)
    return jsonify(search_results)

def resolve_domain(domain):
    try:
        address = resolution.addr(domain, 'ETH')
        return address
    except Exception as e:
        return str(e)

def search_kendra(query):
    client = boto3.client('kendra', region_name='your-region')
    index_id = 'your-index-id'

    response = client.query(
        IndexId=index_id,
        QueryText=query
    )
    return response['ResultItems']

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
