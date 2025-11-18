"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-optimism-airdrop.rf.gd
Prompt: Generate a Node.js server configuration optimized for deployment on a hosting service that includes unlimited disk space and modern cPanel, as described on iFastNet's hosting platform.
Generated: DETERMINISTIC_aeb2ea3c501596d5
Batch ID: 20250612_152954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const express = require('express');
const path = require('path');
const logger = require('morgan');
const bodyParser = require('body-parser');

// Create an instance of the Express application
const app = express();

// Middleware setup
app.use(logger('dev')); // Logs requests to the console
app.use(bodyParser.json()); // Parses incoming JSON requests
app.use(bodyParser.urlencoded({ extended: true })); // Parses URL-encoded requests

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Basic route for the root URL
app.get('/', (req, res) => {
    res.send('Hello, World! This is your Node.js server.');
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack); // Log the error stack trace
    res.status(500).send('Something broke!'); // Send a 500 response
});

// Start the server and listen on the specified PORT
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// Export the app for testing or further use
module.exports = app;
```

### Deployment Instructions
1. Ensure you have Node.js installed on your hosting server.
2. Upload the code to your hosting account (e.g., via cPanel).
3. Install dependencies using the command:
   ```
   npm install express morgan body-parser
   ```
4. Start the server using:
   ```
   node server.js
   ```
5. Set up the necessary environment variables in your hosting service if needed.
