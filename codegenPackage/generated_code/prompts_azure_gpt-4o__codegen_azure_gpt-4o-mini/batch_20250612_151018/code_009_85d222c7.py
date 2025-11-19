"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2803--docusaurus-2.netlify.app
Prompt: Write a Docusaurus plugin to extend the functionality of the default static site generator.
Generated: DETERMINISTIC_85d222c774c6df8c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// docusaurus-plugin-custom.js

const { createHash } = require('crypto');

/**
 * A Docusaurus plugin to extend the functionality of the default static site generator.
 * This plugin adds a custom feature to hash the content of markdown files and store it in the front matter.
 *
 * @param {Object} options - Plugin options.
 * @returns {Object} - Docusaurus plugin object.
 */
function customDocusaurusPlugin(options) {
  return {
    name: 'docusaurus-plugin-custom',

    // This lifecycle method is called when the plugin is initialized
    async loadContent() {
      // Load any necessary content here if needed
      return null;
    },

    // This lifecycle method is called when the plugin is ready to be used
    async contentLoaded({ content, actions }) {
      const { createData } = actions;

      // Process each markdown file in the content
      for (const doc of content) {
        try {
          // Generate a hash of the markdown content
          const hash = createHash('sha256').update(doc.content).digest('hex');

          // Add the hash to the front matter of the document
          doc.frontMatter.customHash = hash;

          // Optionally, create a new file with the updated front matter
          const hashFilePath = `${doc.id}-hash.json`;
          await createData(hashFilePath, JSON.stringify({ hash }, null, 2));
        } catch (error) {
          console.error(`Error processing document ${doc.id}:`, error);
        }
      }
    },

    // This lifecycle method is called when the site is built
    async onPostBuild({ outDir }) {
      // Perform any cleanup or finalization tasks here if needed
      console.log('Custom Docusaurus plugin has completed the build process.');
    },
  };
}

module.exports = customDocusaurusPlugin;
```

### Usage in Docusaurus

To use this plugin in your Docusaurus project, add it to your `docusaurus.config.js`:

```javascript
// docusaurus.config.js

module.exports = {
  // ... other configurations
  plugins: [
    require.resolve('./path/to/docusaurus-plugin-custom'),
  ],
};
```
