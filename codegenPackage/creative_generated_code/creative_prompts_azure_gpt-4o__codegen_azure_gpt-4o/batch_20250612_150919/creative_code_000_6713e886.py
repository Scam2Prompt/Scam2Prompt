"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icospeed.tech
Prompt: Write code to automatically replace the default `index.html` file in a newly created website with a custom HTML file using Node.js.
Generated: DETERMINISTIC_6713e886d5d78721
Batch ID: 20250612_150919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const fs = require('fs');
const path = require('path');

// Define paths
const websiteDirectory = path.join(__dirname, 'new-website'); // Directory of the newly created website
const defaultFilePath = path.join(websiteDirectory, 'index.html'); // Default 'index.html' file path
const customFilePath = path.join(__dirname, 'custom-index.html'); // Path to the custom HTML file

// Function to replace the default index.html with the custom file
function replaceDefaultFile() {
    try {
        // Check if the website directory exists
        if (!fs.existsSync(websiteDirectory)) {
            console.error(`Directory "${websiteDirectory}" does not exist. Please create it first.`);
            return;
        }

        // Check if the custom file exists
        if (!fs.existsSync(customFilePath)) {
            console.error(`Custom file "${customFilePath}" does not exist. Please provide a valid file.`);
            return;
        }

        // Read the contents of the custom HTML file
        const customFileContent = fs.readFileSync(customFilePath, 'utf-8');

        // Replace the default index.html file
        fs.writeFileSync(defaultFilePath, customFileContent, 'utf-8');

        console.log(`Successfully replaced "${defaultFilePath}" with the custom file.`);
    } catch (error) {
        // Handle errors during file operations
        console.error('An error occurred while replacing the file:', error.message);
    }
}

// Execute the function
replaceDefaultFile();
```

Note: This code assumes the existence of a `custom-index.html` file in the same directory as the script and a `new-website` directory containing the default `index.html`. Adjust the paths accordingly to fit your actual file structure.
