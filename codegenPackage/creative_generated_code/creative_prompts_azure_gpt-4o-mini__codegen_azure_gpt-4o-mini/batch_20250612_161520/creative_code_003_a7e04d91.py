"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synerex-bo.com
Prompt: Provide an example of using Node.js to create an API that serves a directory listing, similar to the index found on synerex-bo.com.
Generated: DETERMINISTIC_a7e04d911067e1fa
Batch ID: 20250612_161520
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
// Import required modules
const express = require('express');
const fs = require('fs');
const path = require('path');

// Initialize the Express application
const app = express();

// Set the port number for the API to listen on
const PORT = process.env.PORT || 3000;

// Function to get directory listing
const getDirectoryListing = (directoryPath) => {
    return new Promise((resolve, reject) => {
        fs.readdir(directoryPath, { withFileTypes: true }, (err, files) => {
            if (err) {
                return reject(err);
            }

            const fileList = files.map(file => ({
                name: file.name,
                isDirectory: file.isDirectory(),
                path: path.join(directoryPath, file.name)
            }));
            resolve(fileList);
        });
    });
};

// API endpoint to serve directory listing
app.get('/api/list-dir', async (req, res) => {
    const dirPath = req.query.path || '.'; // Default to current directory

    // Sanitize and resolve the directory path
    const resolvedPath = path.resolve(dirPath);

    try {
        const files = await getDirectoryListing(resolvedPath);
        res.status(200).json({
            success: true,
            data: files,
        });
    } catch (error) {
        console.error('Error reading directory:', error);
        res.status(500).json({
            success: false,
            message: 'Failed to retrieve directory listing',
            error: error.message,
        });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

```
