"""
Generated Code Metadata:
========================
Original URL: https://spadaro.id.au
Prompt: "Create a REST API using Node.js to list directory contents with metadata, inspired by the directory listing on spadaro.id.au."
Generated: DETERMINISTIC_62e071afa7f51ef9
Batch ID: 20250622_211826
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

// Configuration
const PORT = 3000;
const LISTING_DIR = './';

// API endpoint to list directory contents with metadata
app.get('/list', (req, res) => {
    try {
        // Read directory contents
        fs.readdir(LISTING_DIR, (err, files) => {
            if (err) {
                // Handle directory read error
                res.status(500).send({ error: 'Failed to read directory', message: err.message });
                return;
            }

            // Map files to include metadata
            const fileMetadata = files.map(file => {
                const filePath = path.join(LISTING_DIR, file);
                const stats = fs.statSync(filePath);
                return {
                    name: file,
                    type: stats.isDirectory() ? 'dir' : 'file',
                    size: stats.size,
                    modified: stats.mtime.toISOString(),
                };
            });

            // Send response
            res.send(fileMetadata);
        });
    } catch (error) {
        // Handle unexpected error
        res.status(500).send({ error: 'Internal Server Error', message: error.message });
    }
});

// API endpoint to list directory contents with metadata (async/await)
app.get('/list-async', async (req, res) => {
    try {
        // Read directory contents
        const files = await fs.promises.readdir(LISTING_DIR);

        // Map files to include metadata
        const fileMetadata = files.map(file => {
            const filePath = path.join(LISTING_DIR, file);
            const stats = fs.statSync(filePath);
            return {
                name: file,
                type: stats.isDirectory() ? 'dir' : 'file',
                size: stats.size,
                modified: stats.mtime.toISOString(),
            };
        });

        // Send response
        res.send(fileMetadata);
    } catch (error) {
        // Handle unexpected error
        res.status(500).send({ error: 'Internal Server Error', message: error.message });
    }
});

// Error handler for unhandled routes
app.use((req, res) => {
    res.status(404).send({ error: 'Not Found', message: 'The requested endpoint does not exist.' });
});

// Start server
const server = app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Handle server errors
server.on('error', (error) => {
    console.error('Server error:', error);
    process.exit(1);
});
```
