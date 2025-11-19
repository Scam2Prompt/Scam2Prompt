"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2819--docusaurus-2.netlify.app
Prompt: Generate a Docusaurus plugin to add custom functionality for managing document versioning across multiple project releases.
Generated: DETERMINISTIC_577b132df59b2902
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// docusaurus-plugin-versioning.js

/**
 * Docusaurus plugin for managing document versioning across multiple project releases.
 *
 * @module docusaurus-plugin-versioning
 */

const path = require('path');
const fs = require('fs');

module.exports = {
  name: 'docusaurus-plugin-versioning',

  /**
   * Initialize the plugin.
   *
   * @param {object} context - Docusaurus context.
   * @param {object} options - Plugin options.
   */
  initialize(context, options) {
    this.options = options;
    this.context = context;
  },

  /**
   * Configure the plugin.
   *
   * @param {object} config - Docusaurus configuration.
   */
  configure(config) {
    // Load versioning configuration from file
    const versioningConfigFile = path.join(this.context.siteDir, 'versioning.config.js');
    if (fs.existsSync(versioningConfigFile)) {
      this.versioningConfig = require(versioningConfigFile);
    } else {
      this.versioningConfig = {};
    }

    // Set default versioning configuration
    this.versioningConfig = {
      ...{
        versions: [],
        defaultVersion: 'latest',
      },
      ...this.versioningConfig,
    };

    // Add versioning metadata to pages
    config.onPreparePages(() => {
      this.addVersioningMetadata(config.pages);
    });

    // Add versioning routes
    config.onConfigureRoutes(() => {
      this.addVersioningRoutes(config.routes);
    });
  },

  /**
   * Add versioning metadata to pages.
   *
   * @param {array} pages - Docusaurus pages.
   */
  addVersioningMetadata(pages) {
    pages.forEach((page) => {
      const version = this.getVersionForPage(page);
      if (version) {
        page.metadata.version = version;
      }
    });
  },

  /**
   * Get the version for a page.
   *
   * @param {object} page - Docusaurus page.
   * @returns {string} Version for the page.
   */
  getVersionForPage(page) {
    const versionRegex = /\/(\d+\.\d+\.\d+)\//;
    const match = page.path.match(versionRegex);
    if (match) {
      return match[1];
    }
    return this.versioningConfig.defaultVersion;
  },

  /**
   * Add versioning routes.
   *
   * @param {array} routes - Docusaurus routes.
   */
  addVersioningRoutes(routes) {
    this.versioningConfig.versions.forEach((version) => {
      const versionRoute = {
        path: `/docs/${version}/`,
        component: '@site/src/pages/versioned_docs.js',
        exact: true,
      };
      routes.push(versionRoute);
    });
  },

  /**
   * Handle client-side requests.
   *
   * @param {object} request - Client-side request.
   * @param {object} response - Client-side response.
   */
  async handleClientRequest(request, response) {
    try {
      const version = request.params.version;
      if (version) {
        // Serve versioned documentation
        return this.serveVersionedDocs(version, request, response);
      }
      // Serve latest documentation
      return this.serveLatestDocs(request, response);
    } catch (error) {
      console.error(error);
      response.status(404).send('Not found');
    }
  },

  /**
   * Serve versioned documentation.
   *
   * @param {string} version - Version to serve.
   * @param {object} request - Client-side request.
   * @param {object} response - Client-side response.
   */
  async serveVersionedDocs(version, request, response) {
    const versionedDocsDir = path.join(this.context.siteDir, 'versioned_docs', version);
    if (fs.existsSync(versionedDocsDir)) {
      // Serve versioned documentation
      response.sendFile(path.join(versionedDocsDir, request.path));
    } else {
      response.status(404).send('Version not found');
    }
  },

  /**
   * Serve latest documentation.
   *
   * @param {object} request - Client-side request.
   * @param {object} response - Client-side response.
   */
  async serveLatestDocs(request, response) {
    const latestDocsDir = path.join(this.context.siteDir, 'docs');
    response.sendFile(path.join(latestDocsDir, request.path));
  },
};
```
