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
// @ts-check
// eslint-disable-next-line @typescript-eslint/no-var-requires
const { plugin } = require('@docusaurus/plugin-common');

// Define the plugin name
const pluginName = 'multi-version-docs';

// Define the plugin
module.exports = async function multiVersionDocsPlugin(context, options) {
  // Validate options
  if (!options.versions) {
    throw new Error(`The option "versions" is required for plugin "${pluginName}".`);
  }

  // Destructure options
  const { versions, defaultVersion } = options;

  // Check if default version is provided
  if (!defaultVersion) {
    throw new Error(`The option "defaultVersion" is required for plugin "${pluginName}".`);
  }

  // Check if default version exists in versions
  if (!versions.includes(defaultVersion)) {
    throw new Error(`The default version "${defaultVersion}" does not exist in versions.`);
  }

  // Return the plugin
  return {
    name: pluginName,

    // Extend the docs plugin
    extendDocsPlugin: (docsPlugin) => {
      // Get the versioned docs
      const versionedDocs = {};

      // Loop through each version
      versions.forEach((version) => {
        // Initialize versioned docs
        versionedDocs[version] = {};

        // Loop through each doc
        docsPlugin.docs.forEach((doc) => {
          // Check if doc has a version
          if (doc.versions) {
            // Check if doc is available in current version
            if (doc.versions.includes(version)) {
              // Add doc to versioned docs
              versionedDocs[version][doc.id] = doc;
            }
          } else {
            // Add doc to versioned docs if no version is specified
            versionedDocs[version][doc.id] = doc;
          }
        });
      });

      // Return the extended plugin
      return {
        ...docsPlugin,

        // Get versioned docs
        getVersionedDocs: (version) => {
          // Check if version exists
          if (!versionedDocs[version]) {
            throw new Error(`Version "${version}" does not exist.`);
          }

          // Return versioned docs
          return versionedDocs[version];
        },

        // Get the active version
        getActiveVersion: () => {
          // Get the active version from context
          return context.siteConfig.customFields.activeVersion || defaultVersion;
        },
      };
    },

    // Add a custom route for versioned docs
    async routes(page) {
      // Get the active version
      const activeVersion = page.route.context.getActiveVersion();

      // Get the versioned docs
      const versionedDocs = page.route.context.getVersionedDocs(activeVersion);

      // Loop through each doc
      Object.values(versionedDocs).forEach((doc) => {
        // Add a custom route for the doc
        page.route.routes.push({
          path: `${activeVersion}/${doc.path}`,
          component: '@docusaurus/DocPage',
          exact: true,
          modules: {
            content: doc.content,
          },
        });
      });
    },
  };
};

// Define the plugin options type
/** @typedef {object} MultiVersionDocsPluginOptions */
/** @typedef {string[]} MultiVersionDocsPluginOptions.versions */
/** @typedef {string} MultiVersionDocsPluginOptions.defaultVersion */

// Define the plugin type
/** @typedef {import('@docusaurus/types').Plugin} MultiVersionDocsPlugin */
/** @typedef {import('@docusaurus/types').PluginModule} MultiVersionDocsPluginModule */
```
