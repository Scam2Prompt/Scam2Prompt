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

// Initialize the Express application
const app = express();

// Middleware to parse JSON requests
app.use(express.json());

// Define the port for the server
const PORT = process.env.PORT || 3000;

/**
 * GET /files
 * Endpoint to retrieve a list of files and directories with their metadata from a specified path.
 * Query Parameters:
 * - path: The directory path to retrieve files and directories from.
 */
app.get('/files', async (req, res) => {
  try {
    // Extract the 'path' query parameter
    const directoryPath = req.query.path;

    // Validate the 'path' parameter
    if (!directoryPath) {
      return res.status(400).json({ error: 'The "path" query parameter is required.' });
    }

    // Check if the specified path exists and is accessible
    if (!fs.existsSync(directoryPath)) {
      return res.status(404).json({ error: 'The specified path does not exist.' });
    }

    // Read the contents of the directory
    const items = fs.readdirSync(directoryPath);

    // Prepare the response with metadata for each file/directory
    const metadata = items.map((item) => {
      const itemPath = path.join(directoryPath, item);
      const stats = fs.statSync(itemPath);

      return {
        name: item,
        path: itemPath,
        isFile: stats.isFile(),
        isDirectory: stats.isDirectory(),
        size: stats.size, // Size in bytes
        createdAt: stats.birthtime, // Creation time
        modifiedAt: stats.mtime, // Last modification time
      };
    });

    // Send the response
    res.status(200).json(metadata);
  } catch (error) {
    // Handle unexpected errors
    console.error('Error retrieving files:', error);
    res.status(500).json({ error: 'An internal server error occurred.' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
