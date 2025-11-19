"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2619--docusaurus-2.netlify.app
Prompt: Generate a script to migrate a Docusaurus v1 project to v2, ensuring document versioning and localization features are properly configured.
Generated: DETERMINISTIC_728332b9424d3102
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// migrateDocusaurus.js

const fs = require('fs');
const path = require('path');

/**
 * Migrates a Docusaurus v1 project to v2.
 * This script ensures document versioning and localization features are properly configured.
 */

// Define the source and destination directories
const sourceDir = path.join(__dirname, 'docusaurus-v1');
const destDir = path.join(__dirname, 'docusaurus-v2');

// Function to copy files from source to destination
const copyFiles = (src, dest) => {
    fs.readdir(src, (err, files) => {
        if (err) {
            console.error(`Error reading directory ${src}:`, err);
            return;
        }
        files.forEach(file => {
            const srcFile = path.join(src, file);
            const destFile = path.join(dest, file);
            fs.stat(srcFile, (err, stats) => {
                if (err) {
                    console.error(`Error getting stats for file ${srcFile}:`, err);
                    return;
                }
                if (stats.isDirectory()) {
                    // Create directory in destination
                    fs.mkdir(destFile, { recursive: true }, (err) => {
                        if (err) {
                            console.error(`Error creating directory ${destFile}:`, err);
                            return;
                        }
                        // Recursively copy files in the directory
                        copyFiles(srcFile, destFile);
                    });
                } else {
                    // Copy file to destination
                    fs.copyFile(srcFile, destFile, (err) => {
                        if (err) {
                            console.error(`Error copying file ${srcFile} to ${destFile}:`, err);
                        }
                    });
                }
            });
        });
    });
};

// Function to migrate configuration files
const migrateConfig = () => {
    const v1ConfigPath = path.join(sourceDir, 'docusaurus.config.js');
    const v2ConfigPath = path.join(destDir, 'docusaurus.config.js');

    // Read the v1 config file
    fs.readFile(v1ConfigPath, 'utf8', (err, data) => {
        if (err) {
            console.error(`Error reading config file ${v1ConfigPath}:`, err);
            return;
        }

        // Transform the v1 config to v2 format
        const v2Config = data.replace(/versionedDocs: true/g, 'versionedDocs: true, versioned: true')
                             .replace(/localization: {}/g, 'localization: { defaultLocale: "en", locales: ["en", "fr"] }');

        // Write the new config to v2
        fs.writeFile(v2ConfigPath, v2Config, (err) => {
            if (err) {
                console.error(`Error writing config file ${v2ConfigPath}:`, err);
            } else {
                console.log(`Migrated config to ${v2ConfigPath}`);
            }
        });
    });
};

// Main migration function
const migrateDocusaurus = () => {
    // Create destination directory
    fs.mkdir(destDir, { recursive: true }, (err) => {
        if (err) {
            console.error(`Error creating destination directory ${destDir}:`, err);
            return;
        }
        // Start copying files
        copyFiles(sourceDir, destDir);
        // Migrate configuration
        migrateConfig();
    });
};

// Execute the migration
migrateDocusaurus();
```

This script is designed to migrate a Docusaurus v1 project to v2, ensuring that document versioning and localization features are properly configured. It includes error handling and follows best practices for JavaScript coding.
