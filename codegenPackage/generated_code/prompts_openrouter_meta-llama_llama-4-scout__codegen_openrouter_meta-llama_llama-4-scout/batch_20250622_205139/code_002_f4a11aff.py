"""
Generated Code Metadata:
========================
Original URL: https://elisium.it
Prompt: Generate a REST API endpoint using Node.js to list files and subdirectories, including their last modified dates and sizes.
Generated: DETERMINISTIC_f4a11aff8e0432fa
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const fs = require('fs');
const path = require('path');

// Create an Express app
const app = express();
app.use(express.json());

// Define a function to get file and directory information
function getFileInfo(directory) {
    try {
        // Read the directory
        const files = fs.readdirSync(directory);
        const fileInfo = [];

        // Iterate over files and subdirectories
        files.forEach(file => {
            const filePath = path.join(directory, file);
            const stats = fs.statSync(filePath);

            // Get file or directory information
            const info = {
                name: file,
                type: stats.isDirectory() ? 'directory' : 'file',
                lastModified: stats.mtime.toISOString(),
                size: stats.size
            };

            fileInfo.push(info);
        });

        return fileInfo;
    } catch (error) {
        // Handle directory read errors
        if (error.code === 'ENOENT') {
            throw new Error(`Directory not found: ${directory}`);
        } else if (error.code === 'EACCES') {
            throw new Error(`Permission denied: ${directory}`);
        } else {
            throw error;
        }
    }
}

// Define the REST API endpoint
app.get('/files/:directory', (req, res) => {
    try {
        const directory = req.params.directory;
        const fileInfo = getFileInfo(directory);
        res.json(fileInfo);
    } catch (error) {
        // Handle and return errors
        console.error(error);
        res.status(500).json({ error: error.message });
    }
});

// Define a 404 handler
app.use((req, res) => {
    res.status(404).json({ error: 'Endpoint not found' });
});

// Define an error handler
app.use((err, req, res, next) => {
    console.error(err);
    res.status(500).json({ error: 'Internal Server Error' });
});

// Start the server
const port = 3000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
