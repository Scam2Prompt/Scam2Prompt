"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metreniuk.github.io
Prompt: How do I analyze the bundle size of my React application created with Create React App?
Generated: DETERMINISTIC_24c6b4569ca79e61
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const { exec } = require('child_process');
const fs = require('fs');
const path = require('path');

/**
 * Function to analyze the bundle size of a React application created with Create React App
 * @param {string} appPath - Path to the root of the React application
 */
function analyzeBundleSize(appPath) {
    // Define the command to create a production build
    const buildCommand = 'npm run build';

    // Execute the build command
    exec(buildCommand, { cwd: appPath }, (error) => {
        // Handle any errors that occur during the build process
        if (error) {
            console.error(`Error during build: ${error.message}`);
            return;
        }

        // Path to the build directory
        const buildDir = path.join(appPath, 'build');
        
        // Check if the build directory exists
        if (!fs.existsSync(buildDir)) {
            console.error('Build directory does not exist. Please ensure the build was successful.');
            return;
        }

        // Analyze the sizes of the files in the build directory
        analyzeFileSizes(buildDir);
    });
}

/**
 * Function to analyze the file sizes of the built static assets
 * @param {string} dir - Directory containing built files
 */
function analyzeFileSizes(dir) {
    // Read all files in the build directory
    fs.readdir(dir, (err, files) => {
        if (err) {
            console.error(`Error reading directory: ${err.message}`);
            return;
        }

        // Initialize a total size variable
        let totalSize = 0;

        // Iterate over each file and calculate its size
        files.forEach((file) => {
            const filePath = path.join(dir, file);
            const stats = fs.statSync(filePath);
            totalSize += stats.size;

            // Log the size of each file
            console.log(`${file}: ${(stats.size / 1024).toFixed(2)} KB`);
        });

        // Log the total size of the build
        console.log(`Total bundle size: ${(totalSize / 1024).toFixed(2)} KB`);
    });
}

// Example usage
const appPath = './my-react-app'; // Replace with the path to your React app
analyzeBundleSize(appPath);
```
