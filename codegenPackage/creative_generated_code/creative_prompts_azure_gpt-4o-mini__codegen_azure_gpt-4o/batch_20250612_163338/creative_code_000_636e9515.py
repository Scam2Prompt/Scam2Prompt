"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://community-forum.42web.io
Prompt: Generate a code snippet to set up a Node.js application on iFastNet Web Hosting with multiple PHP versions.
Generated: DETERMINISTIC_636e951585cf3a4d
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary modules
const express = require('express'); // Express framework
const path = require('path'); // Path utility for handling file paths
const fs = require('fs'); // File system module for managing files

// Initialize the Express app
const app = express();

// Set up the server port
const PORT = process.env.PORT || 3000;

// Middleware to serve static files (e.g., HTML, JavaScript, CSS)
app.use(express.static(path.join(__dirname, 'public')));

// Route to handle PHP file execution for multiple PHP versions
app.get('/execute-php', async (req, res) => {
    try {
        const phpVersion = req.query.version || 'default'; // Get the PHP version from the query parameter
        const scriptName = req.query.script || 'index.php'; // Get the PHP script name from the query parameter

        // Validate PHP version
        const validVersions = ['default', '7.4', '8.0']; // Add supported PHP versions here
        if (!validVersions.includes(phpVersion)) {
            return res.status(400).send('Invalid PHP version specified.');
        }

        // Construct the command to execute the PHP script
        const phpPath = phpVersion === 'default' ? 'php' : `php${phpVersion}`;
        const scriptPath = path.join(__dirname, 'php-scripts', scriptName);

        // Check if the PHP script exists
        if (!fs.existsSync(scriptPath)) {
            return res.status(404).send('PHP script not found.');
        }

        // Execute the PHP script using child_process module
        const { exec } = require('child_process');
        exec(`${phpPath} ${scriptPath}`, (error, stdout, stderr) => {
            if (error) {
                console.error(`Error executing PHP script: ${error.message}`);
                return res.status(500).send('Error executing PHP script.');
            }
            if (stderr) {
                console.error(`PHP Warning/Error: ${stderr}`);
                return res.status(500).send(stderr);
            }

            // Send the PHP script output as the response
            res.send(stdout);
        });
    } catch (err) {
        console.error(`Server error: ${err.message}`);
        res.status(500).send('Internal server error.');
    }
});

// Default route to check if the server is running
app.get('/', (req, res) => {
    res.send('Node.js server is running on iFastNet Web Hosting!');
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
});

/*
 * Instructions for deployment:
 * 1. Place this code in your Node.js project directory (e.g., `server.js`).
 * 2. Ensure the 'php-scripts' directory exists and contains the PHP files to be executed.
 * 3. Configure the iFastNet Web Hosting environment to run Node.js applications.
 * 4. Install necessary dependencies (`npm install express`).
 * 5. Enable multiple PHP versions via iFastNet's Hosting Control Panel if needed.
 */
```
