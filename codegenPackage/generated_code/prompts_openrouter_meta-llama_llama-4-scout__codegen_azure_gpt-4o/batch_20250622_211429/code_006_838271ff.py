"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2691--docusaurus-2.netlify.app
Prompt: Develop a Docusaurus plugin that supports document versioning and syncs with project releases.
Generated: DETERMINISTIC_838271ffca9f776f
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Docusaurus Plugin for Document Versioning and Syncing with Project Releases
// This plugin enables versioning of documentation and syncs with project releases.

const fs = require('fs');
const path = require('path');
const semver = require('semver');

module.exports = function versioningPlugin(context, options) {
  // Default options for the plugin
  const defaultOptions = {
    versionsDir: 'versions', // Directory to store versioned docs
    currentVersion: 'current', // Name for the current version
    projectVersionFile: 'project-version.json', // File containing project version info
  };

  // Merge user-provided options with defaults
  const pluginOptions = { ...defaultOptions, ...options };

  return {
    name: 'docusaurus-plugin-versioning',

    async loadContent() {
      // Load the current project version from the specified file
      const projectVersionPath = path.resolve(context.siteDir, pluginOptions.projectVersionFile);
      let projectVersion;

      try {
        const versionData = fs.readFileSync(projectVersionPath, 'utf-8');
        projectVersion = JSON.parse(versionData).version;

        if (!semver.valid(projectVersion)) {
          throw new Error(`Invalid project version: ${projectVersion}`);
        }
      } catch (error) {
        console.error('Error loading project version:', error.message);
        throw error;
      }

      return { projectVersion };
    },

    async contentLoaded({ content, actions }) {
      const { projectVersion } = content;
      const { addRoute, createData } = actions;

      // Path to the versions directory
      const versionsDirPath = path.resolve(context.siteDir, pluginOptions.versionsDir);

      // Ensure the versions directory exists
      if (!fs.existsSync(versionsDirPath)) {
        fs.mkdirSync(versionsDirPath, { recursive: true });
      }

      // Path for the current version docs
      const currentVersionPath = path.join(versionsDirPath, pluginOptions.currentVersion);

      // Sync current docs with the current version
      try {
        if (!fs.existsSync(currentVersionPath)) {
          fs.mkdirSync(currentVersionPath, { recursive: true });
        }

        const docsDir = path.resolve(context.siteDir, 'docs');
        const files = fs.readdirSync(docsDir);

        files.forEach((file) => {
          const srcPath = path.join(docsDir, file);
          const destPath = path.join(currentVersionPath, file);

          fs.copyFileSync(srcPath, destPath);
        });

        console.log(`Synced current docs to version: ${projectVersion}`);
      } catch (error) {
        console.error('Error syncing docs:', error.message);
        throw error;
      }

      // Create a route for versioned documentation
      const versionedDocsData = await createData(
        'versionedDocs.json',
        JSON.stringify({ version: projectVersion })
      );

      addRoute({
        path: '/docs/versioned',
        component: '@site/src/components/VersionedDocs',
        modules: {
          versionedDocs: versionedDocsData,
        },
      });
    },

    async postBuild({ content }) {
      const { projectVersion } = content;

      // Save the current project version to the versions directory
      const versionFilePath = path.join(pluginOptions.versionsDir, `${projectVersion}.json`);

      try {
        fs.writeFileSync(
          versionFilePath,
          JSON.stringify({ version: projectVersion }, null, 2)
        );
        console.log(`Saved version file: ${versionFilePath}`);
      } catch (error) {
        console.error('Error saving version file:', error.message);
        throw error;
      }
    },
  };
};
```
