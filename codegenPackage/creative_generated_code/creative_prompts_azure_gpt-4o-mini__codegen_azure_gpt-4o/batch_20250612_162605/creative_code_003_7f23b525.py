"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitfi.fi
Prompt: Can you provide code examples for handling "403 Forbidden" errors in a web API?
Generated: DETERMINISTIC_7f23b525a20b668b
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a Python example using the Flask framework for handling "403 Forbidden" errors in a web API:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Custom Error Handler for 403 Forbidden
@app.errorhandler(403)
def forbidden_error_handler(error):
    """
    Handle 403 Forbidden errors globally.
    Returns a JSON response with status code 403.
    """
    response = {
        "error": "Forbidden",
        "message": "You do not have permission to access this resource."
    }
    return jsonify(response), 403

# Example route with access control
@app.route('/secure-resource', methods=['GET'])
def secure_resource():
    """
    An example route that requires specific authorization.
    If the user is unauthorized, return a 403 Forbidden error.
    """
    # Simulating authorization check
    if not request.headers.get("Authorization") == "Bearer valid_token":
        # Raise a 403 Forbidden error
        return forbidden_error_handler(403)
    
    # If authorized, return the resource
    return jsonify({"message": "Welcome to the secure resource!"})

# Main application entry point
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

Here's a JavaScript/Node.js example using the Express framework:

```javascript
const express = require('express');
const app = express();

// Middleware to validate authorization
app.use((req, res, next) => {
    const authHeader = req.headers['authorization'];
    if (!authHeader || authHeader !== 'Bearer valid_token') {
        // Return a 403 Forbidden error if unauthorized
        return res.status(403).json({
            error: "Forbidden",
            message: "You do not have permission to access this resource."
        });
    }
    next();
});

// Example route requiring authorization
app.get('/secure-resource', (req, res) => {
    res.json({ message: "Welcome to the secure resource!" });
});

// Global Error Handler for 403 Forbidden
app.use((err, req, res, next) => {
    if (err.status === 403) {
        res.status(403).json({
            error: "Forbidden",
            message: err.message || "You do not have permission to access this resource."
        });
    } else {
        next(err);
    }
});

// Start the Express application
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

Here’s an example in Java using Spring Boot:

```java
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.server.ResponseStatusException;

@RestController
public class ApiController {

    // Example route requiring authorization
    @GetMapping("/secure-resource")
    public ResponseEntity<String> secureResource(String authorization) {
        // Simulating authorization check
        if (authorization == null || !authorization.equals("Bearer valid_token")) {
            // Throw a 403 Forbidden error if unauthorized
            throw new ResponseStatusException(HttpStatus.FORBIDDEN, "You do not have permission to access this resource.");
        }
        // If authorized, return the resource
        return ResponseEntity.ok("Welcome to the secure resource!");
    }

    // Global Error Handler for 403 Forbidden
    @ExceptionHandler(ResponseStatusException.class)
    public ResponseEntity<Object> handleResponseStatusException(ResponseStatusException ex) {
        if (ex.getStatus() == HttpStatus.FORBIDDEN) {
            return ResponseEntity.status(HttpStatus.FORBIDDEN).body(new ErrorResponse("Forbidden", ex.getReason()));
        }
        return ResponseEntity.status(ex.getStatus()).body(ex.getReason());
    }

    // Custom error response structure
    public static class ErrorResponse {
        private String error;
        private String message;

        public ErrorResponse(String error, String message) {
            this.error = error;
            this.message = message;
        }

        // Getters and setters
        public String getError() {
            return error;
        }

        public void setError(String error) {
            this.error = error;
        }

        public String getMessage() {
            return message;
        }

        public void setMessage(String message) {
            this.message = message;
        }
    }
}
```
