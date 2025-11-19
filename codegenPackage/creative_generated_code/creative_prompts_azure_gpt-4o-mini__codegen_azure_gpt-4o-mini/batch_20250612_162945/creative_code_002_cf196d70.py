"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://birunoko.art
Prompt: Can you provide code examples for handling HTTP errors, specifically "403 Forbidden", in a web application?
Generated: DETERMINISTIC_cf196d70f7ff5e77
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, abort

app = Flask(__name__)

@app.errorhandler(403)
def forbidden_error(error):
    """Handle 403 Forbidden errors and return a structured JSON response."""
    response = {
        'status': 403,
        'error': 'Forbidden',
        'message': 'You do not have permission to access this resource.'
    }
    return jsonify(response), 403

@app.route('/protected-resource')
def protected_resource():
    """Simulate access to a protected resource."""
    # For demonstration, we're simulating a forbidden access
    abort(403)

if __name__ == '__main__':
    app.run(debug=True)
```

```javascript
// Assuming an Express.js application
const express = require('express');
const app = express();

// Middleware to handle 403 Forbidden errors
app.use((req, res, next) => {
    // Check some condition for forbidden access
    const forbiddenCondition = true; // Replace with actual condition
    if (forbiddenCondition) {
        return res.status(403).json({
            status: 403,
            error: 'Forbidden',
            message: 'You do not have permission to access this resource.'
        });
    }
    next();
});

// Sample route that could trigger a 403 error
app.get('/protected-resource', (req, res) => {
    res.send('This is a protected resource.');
});

// Global error handler for unexpected errors
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({
        status: 500,
        error: 'Internal Server Error',
        message: 'An unexpected error occurred.'
    });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```
