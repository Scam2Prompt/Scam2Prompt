"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-v2.org
Prompt: Generate a script using Node.js and Express to set up a web server that responds with "Success! Your new web server is ready to use." on the homepage.
Generated: DETERMINISTIC_ffe5d624579b3c99
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Express framework for building web servers
const http = require('http'); // Node.js HTTP module

// Initialize the Express application
const app = express();

// Define the port the server will use
const PORT = process.env.PORT || 3000; // Use the environment variable or default to port 3000

// Define the route for the homepage
app.get('/', (req, res) => {
  // Send a success message as a response
  res.status(200).send('Success! Your new web server is ready to use.');
});

// Handle undefined routes (404 error)
app.use((req, res) => {
  res.status(404).send('404 Not Found: The requested resource could not be found.');
});

// Handle server-level errors (500 error)
app.use((err, req, res, next) => {
  console.error('Server Error:', err); // Log the error for debugging purposes
  res.status(500).send('500 Internal Server Error: Something went wrong on the server.');
});

// Start the server
const server = http.createServer(app);
server.listen(PORT, () => {
  console.log(`Server is running and listening on port ${PORT}`);
});

// Graceful shutdown on termination signals
process.on('SIGINT', () => {
  console.log('Shutting down the server...');
  server.close(() => {
    console.log('Server has been shut down.');
    process.exit(0);
  });
});

process.on('SIGTERM', () => {
  console.log('Shutting down the server...');
  server.close(() => {
    console.log('Server has been shut down.');
    process.exit(0);
  });
});
```
