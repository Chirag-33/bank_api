# bank_api

A RESTful API for accessing bank and branch data using Django and Django REST Framework. This project is part of an evaluation assignment and follows best practices including filtering, testing, and deployment.

📌 Features
REST API endpoints to list banks and their branches

Filtering support using django-filter

Read-only access via ReadOnlyModelViewSet

PostgreSQL database support with dj-database-url

Test cases included

Hosted live on Render

🚀 Hosted API
The project is deployed on Render:
👉 https://bank-api-3hp4.onrender.com

Note: Render takes ~1 minute to wake up the server due to cold start.

🔧 Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Install Dependencies
We use Pipenv for environment management:

bash
Copy
Edit
pipenv install
3. Activate the Environment
bash
Copy
Edit
pipenv shell
4. Set Up the Database
Ensure you have a PostgreSQL instance running. Configure your database URL in .env (or through Render environment variables):

bash
Copy
Edit
DATABASE_URL=postgres://user:password@host:port/dbname
Run migrations:

bash
Copy
Edit
python manage.py migrate
5. Load Data (If applicable)
If you're provided with fixtures or a dump, load it via:

bash
Copy
Edit
python manage.py loaddata <data_file.json>
🧪 Running Tests
Test cases are included in test.py. To run them:

bash
Copy
Edit
python manage.py test
Note: Ensure the test database is properly configured and accessible.

🧠 Key Design Choices
ReadOnlyModelViewSet: Enforces a safe, read-only API without requiring explicit permission classes.

Django Filters: Enables filtering branches by bank name and city using query parameters like:

perl
Copy
Edit
/api/branches/?bank__name=STATE%20BANK%20OF%20INDIA&city=MUMBAI
Nested Serializers: BranchSerializer includes a nested BankSerializer for richer API output.

📁 Endpoints Overview
Endpoint	Description
/api/banks/	List all banks
/api/branches/	List all branches with filters

Example Filters
http
Copy
Edit
GET /api/branches/?bank__name=ICICI&city=delhi

Time Taken
2 Days
