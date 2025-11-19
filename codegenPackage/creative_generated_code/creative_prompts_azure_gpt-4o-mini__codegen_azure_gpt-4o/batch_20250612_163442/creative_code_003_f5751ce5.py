"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimeth.epizy.com
Prompt: Create a Node.js application that can be deployed on iFastNet's hosting platform, considering their support for Python apps as well.
Generated: DETERMINISTIC_f5751ce554c535c3
Batch ID: 20250612_163442
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
const fs = require('fs');
const { spawn } = require('child_process');

// Create an instance of Express
const app = express();

// Define the port on which the application will run
const PORT = process.env.PORT || 3000;

// Middleware for JSON parsing
app.use(express.json());

// Serve static files from the public directory
app.use(express.static(path.join(__dirname, 'public')));

// Home route
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Route to run a Python script
app.post('/run-python', (req, res) => {
  try {
    // Get the script name and arguments from the request body
    const { scriptName, args } = req.body;

    if (!scriptName) {
      return res.status(400).json({ error: 'Script name is required' });
    }

    const scriptPath = path.join(__dirname, 'scripts', scriptName);

    // Check if the script exists
    if (!fs.existsSync(scriptPath)) {
      return res.status(404).json({ error: 'Python script not found' });
    }

    // Spawn a child process to execute the Python script
    const pythonProcess = spawn('python', [scriptPath, ...(args || [])]);

    let output = '';
    let errorOutput = '';

    // Collect data from the script's stdout
    pythonProcess.stdout.on('data', (data) => {
      output += data.toString();
    });

    // Collect data from the script's stderr
    pythonProcess.stderr.on('data', (data) => {
      errorOutput += data.toString();
    });

    // Handle process close event
    pythonProcess.on('close', (code) => {
      if (code === 0) {
        res.json({ output });
      } else {
        res.status(500).json({
          error: 'Error executing Python script',
          details: errorOutput,
        });
      }
    });
  } catch (error) {
    // Handle unexpected errors
    res.status(500).json({ error: 'Internal Server Error', details: error.message });
  }
});

// Error handler middleware for invalid routes
app.use((req, res, next) => {
  res.status(404).json({ error: 'Route not found' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

/**
 * Directory Structure:
 * - public/
 *   - index.html (Your HTML front-end to interact with the API)
 * - scripts/
 *   - Your Python script files (e.g., example.py)
 *
 * Deployment Notes:
 * - Place the Node.js app files at the root of your project.
 * - Ensure the `scripts` directory contains the Python files.
 * - Install necessary dependencies (`npm install express`).
 */
```
