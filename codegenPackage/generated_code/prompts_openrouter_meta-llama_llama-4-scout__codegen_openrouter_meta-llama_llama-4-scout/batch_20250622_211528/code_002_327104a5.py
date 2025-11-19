"""
Generated Code Metadata:
========================
Original URL: https://bryantroll.com
Prompt: "Generate a REST API endpoint using Node.js to retrieve a list of files and directories with their metadata from a specified path."
Generated: DETERMINISTIC_327104a5c7ba72b0
Batch ID: 20250622_211528
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

// Define a function to get file metadata
function getFileMetadata(filePath) {
  try {
    // Get file stats
    const stats = fs.statSync(filePath);

    // Create metadata object
    const metadata = {
      name: path.basename(filePath),
      path: filePath,
      size: stats.size,
      type: stats.isDirectory() ? 'directory' : 'file',
      modified: stats.mtime.toISOString(),
    };

    return metadata;
  } catch (error) {
    // Handle file not found or permission denied errors
    if (error.code === 'ENOENT' || error.code === 'EACCES') {
      return null;
    }
    throw error;
  }
}

// Define the API endpoint
app.get('/files/:path', (req, res) => {
  try {
    // Get the specified path from the request
    const filePath = req.params.path;

    // Check if the path exists
    if (!fs.existsSync(filePath)) {
      res.status(404).send({ error: 'Path not found' });
      return;
    }

    // Read the directory contents
    const files = fs.readdirSync(filePath);

    // Create a list to store file metadata
    const fileMetadataList = [];

    // Iterate over the files and get their metadata
    files.forEach((file) => {
      const filePathWithName = path.join(filePath, file);
      const metadata = getFileMetadata(filePathWithName);
      if (metadata) {
        fileMetadataList.push(metadata);
      }
    });

    // Return the list of file metadata
    res.send(fileMetadataList);
  } catch (error) {
    // Handle internal server errors
    console.error(error);
    res.status(500).send({ error: 'Internal server error' });
  }
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
