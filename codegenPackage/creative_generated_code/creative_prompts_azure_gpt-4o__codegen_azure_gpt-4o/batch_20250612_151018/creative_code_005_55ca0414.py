"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2757--docusaurus-2.netlify.app
Prompt: Create a Docusaurus plugin to manage document versioning that aligns with project releases. Include an example configuration.
Generated: DETERMINISTIC_55ca0414faf86570
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Docusaurus Plugin: Document Versioning Aligned with Project Releases
// File: docusaurus-plugin-versioning.js

const fs = require('fs');
const path = require('path');

module.exports = function pluginVersioning(context, options) {
  // Ensure required options are provided
  if (!options.versionFile || !options.docsDir || !options.defaultVersion) {
    throw new Error(
      'Missing required options for versioning plugin: versionFile, docsDir, defaultVersion'
    );
  }

  const versionFilePath = path.resolve(context.siteDir, options.versionFile);
  const docsDirPath = path.resolve(context.siteDir, options.docsDir);

  return {
    name: 'docusaurus-plugin-versioning',

    // Generate versioned documents during the build process
    async loadContent() {
      let versions;

      try {
        // Read the version file
        const versionData = fs.readFileSync(versionFilePath, 'utf-8');
        versions = JSON.parse(versionData);

        if (!Array.isArray(versions)) {
          throw new Error('Version file must contain an array of versions.');
        }
      } catch (error) {
        console.error(`Error reading version file: ${versionFilePath}`);
        throw error;
      }

      return versions;
    },

    async contentLoaded({ content, actions }) {
      const { createData, addRoute } = actions;

      // Create versioned routes for each version
      for (const version of content) {
        const versionDir = path.join(docsDirPath, version);

        if (!fs.existsSync(versionDir)) {
          console.warn(`Version directory not found: ${versionDir}`);
          continue;
        }

        const dataPath = await createData(
          `version-${version}.json`,
          JSON.stringify({ version })
        );

        addRoute({
          path: `/docs/${version}`,
          component: '@site/src/components/VersionDocsPage',
          modules: { version: dataPath },
          exact: true,
        });
      }

      // Handle default version routing
      addRoute({
        path: '/docs',
        component: '@site/src/components/DefaultDocsPage',
        modules: { version: options.defaultVersion },
        exact: true,
      });
    },

    // Extend the Docusaurus config if needed
    configureWebpack(config, isServer, utils) {
      // No specific webpack configuration for this plugin
      return config;
    },
  };
};

// Example Configuration (Include in docusaurus.config.js)
const config = {
  plugins: [
    [
      path.resolve(__dirname, 'docusaurus-plugin-versioning.js'),
      {
        versionFile: 'versions.json', // JSON file containing version array (e.g., ["v1.0", "v1.1", "v2.0"])
        docsDir: 'docs', // Directory where documentation resides
        defaultVersion: 'v2.0', // Default version to serve
      },
    ],
  ],
};

module.exports = config;
```
