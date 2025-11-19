"""
Generated Code Metadata:
========================
Original URL: https://smartd.org.ls
Prompt: Create a JavaScript function to retrieve and display the contents of a directory, including the last modified dates and sizes, similar to the directory listing on https://smartd.org.ls.
Generated: DETERMINISTIC_c5943ea446be6fe4
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const fs = require('fs');
const path = require('path');

/**
 * Retrieves and displays the contents of a directory, including the last modified dates and sizes.
 * 
 * @param {string} directoryPath - The path to the directory to list.
 * @returns {Promise<void>} A promise that resolves when the directory listing is complete.
 */
async function listDirectory(directoryPath) {
  try {
    // Check if the directory exists
    if (!fs.existsSync(directoryPath)) {
      throw new Error(`Directory '${directoryPath}' does not exist.`);
    }

    // Check if the path is a directory
    const stats = fs.statSync(directoryPath);
    if (!stats.isDirectory()) {
      throw new Error(`'${directoryPath}' is not a directory.`);
    }

    // Read the directory contents
    const files = await fs.promises.readdir(directoryPath);

    // Display the directory contents
    console.log(`Directory listing for ${directoryPath}:`);
    console.log(`-----------------------------------------`);
    console.log(`| ${'Name'.padEnd(40)} | ${'Last Modified'.padEnd(20)} | ${'Size'.padEnd(10)} |`);
    console.log(`-----------------------------------------`);

    for (const file of files) {
      const filePath = path.join(directoryPath, file);
      const fileStats = await fs.promises.stat(filePath);

      // Format the last modified date
      const lastModified = new Date(fileStats.mtime).toISOString().replace('T', ' ').slice(0, 19);

      // Format the file size
      let size;
      if (fileStats.size < 1024) {
        size = `${fileStats.size} B`;
      } else if (fileStats.size < 1024 ** 2) {
        size = `${(fileStats.size / 1024).toFixed(2)} KB`;
      } else if (fileStats.size < 1024 ** 3) {
        size = `${(fileStats.size / 1024 ** 2).toFixed(2)} MB`;
      } else {
        size = `${(fileStats.size / 1024 ** 3).toFixed(2)} GB`;
      }

      console.log(`| ${file.padEnd(40)} | ${lastModified.padEnd(20)} | ${size.padEnd(10)} |`);
    }

    console.log(`-----------------------------------------`);
  } catch (error) {
    console.error(`Error listing directory: ${error.message}`);
    process.exit(1);
  }
}

// Example usage
listDirectory('.');
```
