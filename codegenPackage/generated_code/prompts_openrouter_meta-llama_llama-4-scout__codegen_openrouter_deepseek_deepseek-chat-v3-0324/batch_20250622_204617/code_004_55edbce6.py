"""
Generated Code Metadata:
========================
Original URL: https://binance.bey-dev.mixh.jp
Prompt: "Create a simple API using Node.js to update the 'Last Modified' date and 'Size' of files on a LiteSpeed Web Server, inspired by the details shown on binance.bey-dev.mixh.jp."
Generated: DETERMINISTIC_55edbce62c027623
Batch ID: 20250622_204617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const express = require('express');
const fs = require('fs');
const path = require('path');
const { promisify } = require('util');

const app = express();
const port = process.env.PORT || 3000;

// Promisify fs functions for async/await usage
const statAsync = promisify(fs.stat);
const readdirAsync = promisify(fs.readdir);

// Middleware to parse JSON requests
app.use(express.json());

/**
 * Helper function to get file details
 * @param {string} filePath - Path to the file
 * @returns {Promise<Object>} File details including size and last modified date
 */
async function getFileDetails(filePath) {
  try {
    const stats = await statAsync(filePath);
    return {
      size: stats.size,
      lastModified: stats.mtime
    };
  } catch (error) {
    throw new Error(`Error getting file details: ${error.message}`);
  }
}

/**
 * API endpoint to update file details
 * @param {string} directory - Directory path to scan
 * @returns {Object} List of files with updated details
 */
app.get('/api/files/update', async (req, res) => {
  try {
    const directory = req.query.directory || '/var/www/html'; // Default LiteSpeed web directory
    const files = await readdirAsync(directory);
    
    const fileDetails = await Promise.all(
      files.map(async (file) => {
        const filePath = path.join(directory, file);
        const details = await getFileDetails(filePath);
        return {
          name: file,
          ...details
        };
      })
    );

    res.json({
      success: true,
      data: fileDetails
    });
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({
      success: false,
      message: error.message
    });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    success: false,
    message: 'Internal server error'
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

// Export the app for testing
module.exports = app;
```
