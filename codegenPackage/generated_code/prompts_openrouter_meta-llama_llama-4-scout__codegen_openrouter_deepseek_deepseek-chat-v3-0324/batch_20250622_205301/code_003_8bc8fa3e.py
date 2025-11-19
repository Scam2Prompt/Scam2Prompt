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
const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

/**
 * Helper function to get file stats
 * @param {string} filePath - Path to the file/directory
 * @returns {Promise<Object>} File/directory metadata
 */
const getFileStats = (filePath) => {
  return new Promise((resolve, reject) => {
    fs.stat(filePath, (err, stats) => {
      if (err) return reject(err);
      
      resolve({
        name: path.basename(filePath),
        path: filePath,
        size: stats.size,
        isDirectory: stats.isDirectory(),
        isFile: stats.isFile(),
        createdAt: stats.birthtime,
        modifiedAt: stats.mtime,
        accessedAt: stats.atime
      });
    });
  });
};

/**
 * API endpoint to list directory contents
 * @param {string} dirPath - Directory path to list
 * @returns {Promise<Array>} Array of file/directory metadata
 */
const listDirectory = async (dirPath) => {
  try {
    const files = await fs.promises.readdir(dirPath);
    const results = await Promise.all(
      files.map(file => getFileStats(path.join(dirPath, file)))
    );
    return results.sort((a, b) => {
      // Directories first, then files
      if (a.isDirectory && !b.isDirectory) return -1;
      if (!a.isDirectory && b.isDirectory) return 1;
      return a.name.localeCompare(b.name);
    });
  } catch (err) {
    throw err;
  }
};

// API Routes
app.get('/api/list', async (req, res) => {
  try {
    const dirPath = req.query.path || process.cwd();
    const absolutePath = path.resolve(dirPath);
    
    // Security check to prevent directory traversal
    if (!absolutePath.startsWith(process.cwd())) {
      return res.status(403).json({ error: 'Access denied' });
    }

    const contents = await listDirectory(absolutePath);
    res.json({ path: absolutePath, contents });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Failed to list directory contents' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.exports = app;
```
