"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2785--docusaurus-2.netlify.app
Prompt: What are the steps to migrate from Docusaurus v1 to v2, and how does it improve documentation management?
Generated: DETERMINISTIC_aa70fb0a74c31c5b
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Migrating from Docusaurus v1 to v2 involves various steps, primarily centered on upgrading dependencies, restructuring the project, and ensuring compatibility with the new version. Below is a clean, well-documented, and runnable Node.js script that outlines the migration process programmatically:

```javascript
// migration.js

/**
 * Script to migrate a Docusaurus v1 project to v2.
 * This script automates key steps in the migration process.
 * 
 * Prerequisites:
 * 1. Node.js and npm must be installed.
 * 2. Run this script inside the Docusaurus project directory.
 * 
 * Usage:
 *   node migration.js
 */

const fs = require('fs');
const { exec } = require('child_process'); // For running shell commands

/**
 * Execute a shell command asynchronously and return the result.
 * @param {string} command - The shell command to execute.
 * @returns {Promise<void>}
 */
const runCommand = (command) => {
  return new Promise((resolve, reject) => {
    exec(command, (error, stdout, stderr) => {
      if (error) {
        console.error(`Error executing command: ${command}\nDetails: ${error.message}`);
        reject(error);
      } else {
        console.log(stdout || stderr);
        resolve();
      }
    });
  });
};

/**
 * Check if a file or directory exists.
 * @param {string} path - Path to the file or directory.
 * @returns {boolean} - True if the path exists, else false.
 */
const pathExists = (path) => {
  return fs.existsSync(path);
};

/**
 * Clean up Docusaurus v1 files no longer supported in v2.
 * @returns {void}
 */
const cleanUpLegacyFiles = () => {
  console.log("\nCleaning up legacy files...");
  const filesToDelete = ['siteConfig.js', 'core', 'static', 'pages'];
  
  filesToDelete.forEach((file) => {
    if (pathExists(file)) {
      fs.rmSync(file, { recursive: true, force: true });
      console.log(`Deleted: ${file}`);
    } else {
      console.log(`File not found, skipping: ${file}`);
    }
  });

  console.log("Legacy cleanup complete.\n");
};

/**
 * Start the migration process.
 */
const migrateDocusaurus = async () => {
  console.log("Starting migration from Docusaurus v1 to v2...\n");

  try {
    // Step 1: Install Docusaurus v2
    console.log("Installing Docusaurus v2...");
    await runCommand('npm install @docusaurus/core @docusaurus/preset-classic');

    // Step 2: Create a new Docusaurus v2 site structure
    console.log("\nCreating new site structure...");
    await runCommand('npx create-docusaurus@latest docs-site classic');

    // Step 3: Move existing content to the new structure
    console.log("\nMigrating content...");
    if (pathExists('docs')) {
      fs.renameSync('docs', 'docs-site/docs');
      console.log("Moved: docs -> docs-site/docs");
    } else {
      console.log("No 'docs' directory found in the v1 project.");
    }

    // Step 4: Migrate blog content (if any)
    if (pathExists('blog')) {
      fs.renameSync('blog', 'docs-site/blog');
      console.log("Moved: blog -> docs-site/blog");
    } else {
      console.log("No 'blog' directory found in the v1 project.");
    }

    // Step 5: Clean up legacy files
    cleanUpLegacyFiles();

    console.log("\nMigration complete!");
    console.log("Navigate to 'docs-site' and run 'npm start' to preview your new Docusaurus v2 site.\n");
  } catch (error) {
    console.error("Migration failed. Please review the error details:", error);
  }
};

// Execute the migration script
migrateDocusaurus();
```

**Final Notes**:
- Save this script as `migration.js` in your project directory.
- Run it in the terminal with `node migration.js`.
- Modify paths as needed based on your existing v1 project structure.
