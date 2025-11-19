"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2785--docusaurus-2.netlify.app
Prompt: Write a Docusaurus plugin that adds a custom feature to support multiple versions of documentation.
Generated: DETERMINISTIC_6a74538e743d0668
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Docusaurus plugin to support multiple versions of documentation
// This plugin allows users to define and manage multiple versions of their documentation
// in a Docusaurus site.

const path = require('path');
const fs = require('fs');

module.exports = function multiVersionPlugin(context, options) {
  // Validate options
  if (!options || !options.versions || !Array.isArray(options.versions)) {
    throw new Error(
      'multiVersionPlugin requires a "versions" array in its options.'
    );
  }

  return {
    name: 'docusaurus-plugin-multi-version',

    // Extend the content of the site
    async contentLoaded({ actions }) {
      const { setGlobalData } = actions;

      // Set global data for versions
      setGlobalData({
        versions: options.versions,
      });
    },

    // Extend the webpack configuration
    configureWebpack(config, isServer, utils) {
      return {
        resolve: {
          alias: {
            // Create aliases for each version's documentation folder
            ...options.versions.reduce((aliases, version) => {
              const versionPath = path.resolve(
                context.siteDir,
                `docs/${version}`
              );
              if (!fs.existsSync(versionPath)) {
                throw new Error(
                  `Documentation folder for version "${version}" does not exist at path: ${versionPath}`
                );
              }
              aliases[`@docs/${version}`] = versionPath;
              return aliases;
            }, {}),
          },
        },
      };
    },

    // Inject routes for each version
    async postBuild({ outDir }) {
      const versionsFilePath = path.join(outDir, 'versions.json');
      try {
        // Write the versions to a JSON file for client-side use
        fs.writeFileSync(
          versionsFilePath,
          JSON.stringify({ versions: options.versions }, null, 2)
        );
      } catch (error) {
        console.error('Error writing versions.json:', error);
        throw error;
      }
    },
  };
};

// Example usage in docusaurus.config.js:
// const multiVersionPlugin = require('./path/to/multiVersionPlugin');
// module.exports = {
//   plugins: [
//     [
//       multiVersionPlugin,
//       {
//         versions: ['v1', 'v2', 'v3'], // Define your documentation versions here
//       },
//     ],
//   ],
// };
```
