**AI-Powered Wallet Analysis Tool**

```Overview```:

The AI-Powered Wallet Analysis Tool is an innovative solution designed to provide cryptocurrency users with comprehensive insights into their wallet transactions and activities. By leveraging cutting-edge AI models, Unstoppable Domains APIs, and AWS services, this tool transforms raw blockchain data into actionable insights, enhancing the user experience and facilitating smarter financial decisions.



```Key Features```:

1.Domain Resolution: Simplifies wallet interactions by replacing complex wallet addresses with human-readable domain names using Unstoppable Domains API.

2.Transaction Analysis: Utilizes advanced AI algorithms to analyze transaction data, offering insights into spending patterns, potential security risks, and personalized recommendations.

3.Search Functionality: Leverages AWS Kendra to provide an intelligent search experience, allowing users to quickly find and retrieve relevant transaction information.

4.User-Friendly Interface: Features an intuitive and responsive interface designed to enhance user experience and accessibility.





```Built With```:

Languages: Python, JavaScript

Frameworks: Flask (backend), React (frontend)

Platforms: AWS Elastic Beanstalk

Cloud Services: AWS Kendra, AWS RDS (PostgreSQL)

Databases: PostgreSQL

APIs: Unstoppable Domains API, AWS Kendra API

Other Technologies: SQLAlchemy (ORM), Flask-JWT-Extended (authentication)






```Prerequisites```:

Python 3.8 or higher

Node.js and npm

AWS CLI

AWS Elastic Beanstalk CLI

PostgreSQL





$Installation$

##Clone the Repository:



git clone https://github.com/shraddhha/Aws-project.git
cd Aws-project





##Set Up the Backend:


cd backend
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt






##Set Up the Frontend:

cd ../frontend
npm install




##Configure Environment Variables:

Create a .env file in the backend directory with your configuration (e.g., database URL, API keys).
Run the Application Locally:





##Start the backend server:


cd backend
flask run





##Start the frontend server:


cd ../frontend
npm start






##Deployment
Deploying to AWS Elastic Beanstalk





##Initialize Elastic Beanstalk Application:


eb init -p python-3.8 flask-app --region us-west-2





##Create an Environment:


eb create flask-env






##Deploy the Application:

eb deploy






```Usage```:

User Authentication: Secure registration and login processes.
Transaction Insights: Detailed analysis of wallet transactions including categorization, trend analysis, and anomaly detection.
Domain Management: Easy domain registration and management through Unstoppable Domains.
Search Capabilities: Efficient search of transaction histories and wallet activities using natural language processing.



```Future Enhancements```:
Enhanced AI Models: Incorporate more sophisticated AI and machine learning models to improve transaction analysis.
Broader Integration: Expand support for other blockchain platforms and domain services.
Mobile Application: Develop a mobile app version for broader accessibility.
Real-Time Alerts: Implement real-time transaction monitoring and alerting.
Financial Planning Tools: Introduce budgeting and financial planning feature.




##Step-by-Step Guide to Initialize Elastic Beanstalk Application
1. Install AWS CLI and EB CLI
If you haven't already, install the AWS CLI and Elastic Beanstalk CLI (EB CLI).

Install AWS CLI:


pip install awscli


1. Install EB CLI:


pip install awsebcli



2. Configure AWS CLI
Before you can use the EB CLI, you need to configure the AWS CLI with your AWS credentials.


aws configure
You'll be prompted to enter your AWS Access Key ID, Secret Access Key, default region, and output format. 





