"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ppl-metamask.42web.io
Prompt: Create a Node.js application that can be deployed on iFastNet hosting, highlighting the benefits of their free SSL and multiple email accounts.
Generated: DETERMINISTIC_4340eb91debcd057
Batch ID: 20250612_163438
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
const helmet = require('helmet'); // For setting secure HTTP headers
const morgan = require('morgan'); // For logging requests
const path = require('path');

// Initialize the Express application
const app = express();

// Middleware setup
app.use(helmet()); // Security middleware
app.use(morgan('combined')); // Logging middleware for HTTP requests
app.use(express.json()); // To parse JSON request bodies
app.use(express.static(path.join(__dirname, 'public'))); // Serve static files from 'public' directory

// Basic route for the home page
app.get('/', (req, res) => {
    res.send(`
        <h1>Welcome to Our Node.js Application!</h1>
        <p>Enjoy the benefits of free SSL and multiple email accounts with iFastNet hosting.</p>
        <h2>Benefits of iFastNet Hosting:</h2>
        <ul>
            <li><strong>Free SSL:</strong> All your data is encrypted with a free SSL certificate, enhancing security.</li>
            <li><strong>Multiple Email Accounts:</strong> Create as many email accounts as you need for your domains.</li>
            <li><strong>Reliable Performance:</strong> Experience high uptime and speedy load times.</li>
        </ul>
    `);
});

// 404 error handling
app.use((req, res, next) => {
    res.status(404).send('Sorry, page not found!');
});

// General error handling
app.use((err, req, res, next) => {
    console.error(err.stack); // Log the error stack trace
    res.status(500).send('Something broke! Please try again later.'); // Send a generic error response
});

// Set the application to listen on the specified port
const PORT = process.env.PORT || 3000; // Default to port 3000 if not set
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### Instructions for Deployment on iFastNet Hosting
1. Create a new Node.js application (if not already created).
2. Include the above code in your `server.js` or similar main file.
3. Ensure you have `express`, `helmet`, and `morgan` installed by running:
   ```bash
   npm install express helmet morgan
   ```
4. Deploy your application according to iFastNet's hosting guidelines.
5. Ensure your domain has a free SSL certificate configured through the iFastNet dashboard.
