"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticfi.world
Prompt: "Write a Node.js function to retrieve and display the contents of a directory, inspired by the structure seen on https://symbioticfi.world."
Generated: DETERMINISTIC_07c63427d0bdd788
Batch ID: 20250612_155449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
const fs = require('fs');
const path = require('path');

/**
 * Retrieves and displays the contents of a specified directory.
 * 
 * @param {string} dirPath - The path of the directory to retrieve contents from.
 * @returns {Promise<void>} - A Promise that resolves when the contents are displayed.
 */
async function displayDirectoryContents(dirPath) {
    try {
        // Check if the provided path is a directory
        const stats = await fs.promises.stat(dirPath);
        if (!stats.isDirectory()) {
            throw new Error(`${dirPath} is not a directory.`);
        }

        // Read the contents of the directory
        const files = await fs.promises.readdir(dirPath);

        console.log(`Contents of directory: ${dirPath}`);
        files.forEach(file => {
            const filePath = path.join(dirPath, file);
            // Get current file stats to determine if it's a file or directory
            const fileStats = fs.statSync(filePath);
            const type = fileStats.isDirectory() ? 'Directory' : 'File';
            console.log(`- ${file} (${type})`);
        });
    } catch (error) {
        // Handle errors gracefully
        console.error(`Error retrieving directory contents: ${error.message}`);
    }
}

// Example usage (this should be replaced with a specific directory path)
const directoryPath = './your-directory'; // Change this to your target directory
displayDirectoryContents(directoryPath);
```

Make sure to replace `./your-directory` with the actual path of the directory you want to retrieve and display.
