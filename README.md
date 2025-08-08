# User Data Management API

This project is a RESTful API built with Flask to manage user data. The API supports versioning (`/api/v1` and `/api/v2`) and uses SQLAlchemy for interacting with a SQLite database. You can perform CRUD (Create, Read, Update, Delete) operations on users via the API.

## Features

- Versioned API endpoints (`v1` and `v2`).
- Basic user management (name, email, age).
- Database integration with SQLite.
- CRUD operations for user data:
  - **GET**: Retrieve all users.
  - **POST**: Add a new user.
  - **PUT**: Update an existing user by ID.
  - **DELETE**: Delete a user by ID.

## Setup and Installation (One Shell Session)

Run the following commands in **one shell session** to set up the project, install dependencies, configure the database, and run the app:

```bash
# Clone the repository
# Clone the repository and navigate to the project directory
git clone https://github.com/your-username/user-data-management-api.git && cd user-data-management-api

# Set up the virtual environment
python3 -m venv venv && source venv/bin/activate  # For Windows: venv\Scripts\activate

# Install the dependencies
pip install -r requirements.txt

# Initialize the migrations folder (if not already done)
flask db init

# Generate migration files
flask db migrate -m "Initial migration"

# Apply the migration to create the database
flask db upgrade

# Run the Flask application
flask run

# API Endpoints for testing

## GET all users in version 1
curl -X GET http://127.0.0.1:5000/api/v1/users

## Add a new user in version 1
curl -X POST http://127.0.0.1:5000/api/v1/users -H "Content-Type: application/json" -d '{"name": "Alice Green", "email": "alice.green@example.com", "age": 22}'

## GET all users in version 2
curl -X GET http://127.0.0.1:5000/api/v2/users

## Add a new user in version 2
curl -X POST http://127.0.0.1:5000/api/v2/users -H "Content-Type: application/json" -d '{"name": "Bob Brown", "email": "bob.brown@example.com", "age": 35}'

## DELETE a user by ID in version 2
curl -X DELETE http://127.0.0.1:5000/api/v2/users/1

## Update a user by ID in version 2
curl -X PUT http://127.0.0.1:5000/api/v2/users/1 -H "Content-Type: application/json" -d '{"name": "John Doe Updated", "email": "john.doe.updated@example.com", "age": 31}'

# The application uses SQLite as the database backend. 
# The database file will be created automatically as `users.db` in the root directory. 
# You can inspect the database using the SQLite CLI or tools like DB Browser for SQLite.

# Explanation:
- This **single shell session** includes all the necessary steps to **clone the repo, set up the environment, install dependencies,     initialize the database**, and **run the Flask app**.
- It also provides all the **API endpoints and example `cURL` commands** for testing the API.
- The **Database section** mentions that SQLite is used and explains the database setup.
- The **License section** points to the MIT License.









