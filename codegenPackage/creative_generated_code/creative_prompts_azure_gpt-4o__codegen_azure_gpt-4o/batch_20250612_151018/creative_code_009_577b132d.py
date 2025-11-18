"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2819--docusaurus-2.netlify.app
Prompt: Generate a Docusaurus plugin to add custom functionality for managing document versioning across multiple project releases.
Generated: DETERMINISTIC_577b132df59b2902
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Docusaurus Plugin: Document Versioning Management
// This plugin adds custom functionality for managing document versioning
// across multiple project releases in a Docusaurus site.

const fs = require('fs');
const path = require('path');

module.exports = function documentVersioningPlugin(context, options) {
  return {
    name: 'docusaurus-plugin-document-versioning',

    /**
     * Extend the Docusaurus CLI commands with a custom command
     * to handle document versioning tasks.
     */
    extendCli(cli) {
      cli
        .command('create-version <version>', 'Create a new document version')
        .action(async (version) => {
          try {
            const docsDir = path.resolve(__dirname, '../docs');
            const versionedDir = path.resolve(__dirname, '../versioned_docs');
            const versionFolder = path.join(versionedDir, `version-${version}`);

            // Ensure 'versioned_docs' directory exists
            if (!fs.existsSync(versionedDir)) {
              fs.mkdirSync(versionedDir);
            }

            // Check if the version already exists
            if (fs.existsSync(versionFolder)) {
              console.error(`Error: Version ${version} already exists.`);
              return;
            }

            // Copy documents from 'docs' to the versioned folder
            copyDirectoryContents(docsDir, versionFolder);
            console.log(`Successfully created version: ${version}`);
          } catch (error) {
            console.error(`Failed to create version: ${error.message}`);
          }
        });
    },

    /**
     * Inject custom configuration into Docusaurus.
     * Adds versioned docs path to the site configuration.
     */
    async configureWebpack(config, isServer, utils) {
      // No specific modifications to Webpack for this plugin
      return config;
    },

    /**
     * Additional lifecycle hooks can be implemented here
     * if needed for further customization.
     */
  };
};

/**
 * Recursively copy the contents of one directory to another.
 * @param {string} source - The source directory path.
 * @param {string} destination - The destination directory path.
 */
function copyDirectoryContents(source, destination) {
  // Ensure the destination directory exists
  if (!fs.existsSync(destination)) {
    fs.mkdirSync(destination, { recursive: true });
  }

  // Read contents of the source directory
  const entries = fs.readdirSync(source);

  for (const entry of entries) {
    const sourcePath = path.join(source, entry);
    const destinationPath = path.join(destination, entry);
    const stats = fs.statSync(sourcePath);

    if (stats.isDirectory()) {
      // Recursively copy subdirectory
      copyDirectoryContents(sourcePath, destinationPath);
    } else {
      // Copy file
      fs.copyFileSync(sourcePath, destinationPath);
    }
  }
}
```

To use this plugin, save the code in a JavaScript file (e.g., `documentVersioningPlugin.js`) within your Docusaurus project. Register this plugin in the `docusaurus.config.js` file, and run the custom CLI command `yarn docusaurus create-version <version>` to create a new document version.
