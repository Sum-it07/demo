# Import the Flask class from the flask module
from flask import Flask, jsonify

# Create an instance of the Flask class. This is your web application.
app = Flask(__name__)

# Define the root route ('/') using the @app.route decorator.
# When a user visits the homepage, this function will run.
@app.route('/')
def home():
    # Return a simple string to be displayed in the browser.
    return "Hello, World! This is my first backend."

# Define a new route for '/users'.
@app.route('/users')
def get_users():
    # Create a list of dictionaries to represent user data.
    users = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"}
    ]
    # Use jsonify to convert the Python list to a JSON response.
    return jsonify(users)

# This block ensures the application runs only when the script is executed directly.
if __name__ == '__main__':
    # Run the application in debug mode.
    # Debug mode provides helpful error messages in the browser.
    app.run(debug=True)