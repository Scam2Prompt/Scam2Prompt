"""
Generated Code Metadata:
========================
Original URL: https://tkshop6.shop
Prompt: "Write a code snippet in Python/Node.js for routing a request and returning a JSON error response with code 10005 for unregistered paths."
Generated: DETERMINISTIC_dcc33f1ae888d1f3
Batch ID: 20250622_212110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

### Python Solution (using Flask)

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a custom error class for unregistered paths
class UnregisteredPathError(Exception):
    pass

# Define a function to handle unregistered paths
@app.errorhandler(404)
def handle_unregistered_path(e):
    # Return a JSON error response with code 10005
    return jsonify({
        "code": 10005,
        "message": "Unregistered path",
        "data": None
    }), 404

# Define a catch-all route to handle unregistered paths
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def catch_all(path):
    # Raise an exception to trigger the error handler
    raise UnregisteredPathError("Unregistered path")

if __name__ == '__main__':
    app.run(debug=True)
```

### Node.js Solution (using Express)

```javascript
// Import required modules
const express = require('express');

// Create an Express app
const app = express();

// Define a middleware to handle JSON responses
app.use(express.json());

// Define a custom error handler for unregistered paths
const errorHandler = (err, req, res, next) => {
    if (err.status === 404) {
        // Return a JSON error response with code 10005
        res.status(404).json({
            code: 10005,
            message: "Unregistered path",
            data: null
        });
    } else {
        next(err);
    }
};

// Register the error handler
app.use(errorHandler);

// Define a catch-all route to handle unregistered paths
app.use('*', (req, res, next) => {
    const err = new Error('Unregistered path');
    err.status = 404;
    next(err);
});

// Start the server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
