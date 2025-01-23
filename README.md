# Simple_Flask_API - Add Two Numbers

This is a simple Flask application that exposes an API endpoint to add two numbers.


## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Use an API client (like Postman) or curl to send a POST request to the `/add` endpoint:
    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"x": 5, "y": 3}' http://localhost:5000/add
    ```

3. The server will respond with a JSON object containing the sum of the two numbers:
    ```json
    {
        "z": 8
    }
    ```

1. Imports: The code imports the Flask, jsonify, and request modules from the flask package.

2. App Initialization: A new Flask application is created and assigned to the app variable.

3. Route Definition: The /add endpoint is defined, which accepts POST requests. The add function is associated with this endpoint.

4. Request Handling: The add function retrieves JSON data from the request, extracts the values of x and y, computes their sum, and returns the result as a JSON object with a status code of 200.

5. App Execution: If the script is run directly, the Flask application will start in debug mode.


