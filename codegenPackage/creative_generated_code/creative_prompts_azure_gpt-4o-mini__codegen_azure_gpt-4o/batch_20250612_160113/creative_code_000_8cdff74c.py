"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletsignpage.rf.gd
Prompt: Generate a code snippet to set up a Node.js application on iFastNet Web Hosting with unlimited bandwidth.
Generated: DETERMINISTIC_8cdff74cbd50e01b
Batch ID: 20250612_160113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express'); // Express framework for creating the application
const path = require('path'); // Path module for dealing with file paths
const fs = require('fs'); // File system module for handling file operations

// Initialize the Express app
const app = express();

// Define the port to run the application
// Use the environment variable 'PORT' provided by the hosting service, or default to port 3000
const PORT = process.env.PORT || 3000;

// Middleware to parse incoming JSON data
app.use(express.json());

// Middleware to serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Example route: Home page
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Example API route: Health check
app.get('/api/health', (req, res) => {
  res.json({ status: 'OK', message: 'Application is running successfully' });
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack); // Log the error stack for debugging
  res.status(500).json({ error: 'Internal Server Error' }); // Respond with a generic error message
});

// Start the server and listen on the specified port
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Instructions for deployment:
// 1. Upload the project directory to the iFastNet file manager or FTP client.
// 2. Ensure Node.js is enabled in the hosting settings.
// 3. Run `npm install` in the terminal provided by iFastNet to install dependencies.
// 4. Use the hosting service's configuration panel to start the Node.js application.
```
