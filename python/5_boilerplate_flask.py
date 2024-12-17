# Scenario: Start writing a Flask route for a REST API endpoint.
# Goal: Let Copilot suggest the boilerplate code for the route, including error handling.
# In a live demo, start typing out the Flask boilerplate and see what Copilot suggests.

from flask import Flask, request, jsonify

app = Flask(__name__)

# Suppose we start with a comment or partial code, expecting Copilot to fill in:
# "Write a Flask endpoint /items that returns a JSON list of items."
@app.route("/items", methods=["GET", "POST"])
def items():
    if request.method == "GET":
        # Copilot might suggest fetching items from a database or a hardcoded list
        return jsonify(["item1", "item2", "item3"])
    elif request.method == "POST":
        # Copilot could suggest reading JSON data and returning the updated list
        data = request.get_json()
        # Add error handling or validation
        if not data or "name" not in data:
            return jsonify({"error": "Invalid input"}), 400
        # Pretend to add the item
        return jsonify({"message": f"Added {data['name']}"}), 201

if __name__ == "__main__":
    # Run the Flask app for demonstration purposes
    # Copilot might even suggest a debug mode, host, and port
    app.run(debug=True)