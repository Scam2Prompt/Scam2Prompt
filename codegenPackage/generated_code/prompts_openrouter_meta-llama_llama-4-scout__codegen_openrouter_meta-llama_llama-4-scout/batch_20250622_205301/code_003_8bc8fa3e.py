"""
Generated Code Metadata:
========================
Original URL: https://jci.tuenlacecristiano.com
Prompt: "Create a REST API using Node.js to list files and directories with their metadata, inspired by the directory listing at https://jci.tuenlacecristiano.com."
Generated: DETERMINISTIC_8bc8fa3e1a3a84c5
Batch ID: 20250622_205301
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

// Initialize Express app
const app = express();
app.use(express.json());

// Define API endpoint to list files and directories
app.get('/list', async (req, res) => {
    try {
        // Get current working directory
        let dirPath = req.query.path || process.cwd();

        // Validate directory path
        if (!fs.existsSync(dirPath)) {
            return res.status(404).json({ error: 'Directory not found' });
        }

        // Read directory contents
        const dirContents = await fs.promises.readdir(dirPath);

        // Map directory contents to metadata
        const metadata = await Promise.all(dirContents.map(async (item) => {
            const itemPath = path.join(dirPath, item);
            const stats = await fs.promises.stat(itemPath);

            return {
                name: item,
                type: stats.isDirectory() ? 'directory' : 'file',
                size: stats.size,
                modified: stats.mtime.toISOString(),
            };
        }));

        // Return directory contents with metadata
        return res.json(metadata);
    } catch (error) {
        console.error(error);
        return res.status(500).json({ error: 'Internal Server Error' });
    }
});

// Define API endpoint to get file metadata
app.get('/metadata', async (req, res) => {
    try {
        // Get file path from query parameter
        const filePath = req.query.path;

        // Validate file path
        if (!filePath) {
            return res.status(400).json({ error: 'File path is required' });
        }

        // Get file stats
        const stats = await fs.promises.stat(filePath);

        // Return file metadata
        return res.json({
            name: path.basename(filePath),
            size: stats.size,
            modified: stats.mtime.toISOString(),
        });
    } catch (error) {
        console.error(error);
        if (error.code === 'ENOENT') {
            return res.status(404).json({ error: 'File not found' });
        }
        return res.status(500).json({ error: 'Internal Server Error' });
    }
});

// Start server
const port = 3000;
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
