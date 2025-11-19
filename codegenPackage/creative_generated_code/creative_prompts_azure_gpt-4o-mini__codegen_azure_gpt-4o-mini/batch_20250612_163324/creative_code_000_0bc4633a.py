"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doubleway.rf.gd
Prompt: Generate code to set up a Node.js application using the hosting features provided by iFastNet, including unlimited bandwidth and multiple PHP versions.
Generated: DETERMINISTIC_0bc4633a276753b5
Batch ID: 20250612_163324
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const express = require('express');
const path = require('path');

// Create an instance of Express
const app = express();

// Set the port number to use
const PORT = process.env.PORT || 3000; // Use environment variable or default to 3000

// Middleware to serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Middleware to parse JSON request bodies
app.use(express.json());

// Route for the root URL
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html')); // Serve the index.html file
});

// Sample API endpoint
app.get('/api/info', (req, res) => {
    res.json({ message: 'Welcome to the Node.js application hosted on iFastNet!' });
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack); // Log the error stack
    res.status(500).send('Something broke!'); // Send a generic error response
});

// Start the server and listen on the specified port
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`); // Log server start
});
```

### Directory Structure
```
/your-node-app
│
├── public
│   └── index.html
│
├── package.json
├── package-lock.json
└── server.js
```

### Example `index.html` (to be placed in the `public` directory)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Node.js Application</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a Node.js application running on iFastNet.</p>
    <script>
        // Fetch info from the API
        fetch('/api/info')
            .then(response => response.json())
            .then(data => {
                console.log(data.message); // Log the message from the API
            })
            .catch(error => console.error('Error fetching API:', error)); // Handle errors
    </script>
</body>
</html>
```
