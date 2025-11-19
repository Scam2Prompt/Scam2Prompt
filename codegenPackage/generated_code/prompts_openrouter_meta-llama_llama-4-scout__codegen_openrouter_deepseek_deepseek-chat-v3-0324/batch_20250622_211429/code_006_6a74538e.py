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
// plugins/multi-version-docs-plugin/src/index.js

/**
 * A Docusaurus plugin to support multiple versions of documentation.
 * This plugin adds versioning capabilities to your Docusaurus site.
 */

const path = require('path');
const fs = require('fs-extra');
const {DOCUSAURUS_VERSION} = require('@docusaurus/core/constants');

module.exports = function (context, options) {
  const {
    siteDir,
    siteConfig,
    i18n: {currentLocale},
  } = context;

  // Default plugin options
  const defaultOptions = {
    versions: [],
    defaultVersion: 'current',
    versionPrefix: 'version-',
    docsDir: 'docs',
    versionsFile: 'versions.json',
  };

  const pluginOptions = {...defaultOptions, ...options};

  return {
    name: 'multi-version-docs-plugin',

    async loadContent() {
      const versionsFilePath = path.join(
        siteDir,
        pluginOptions.docsDir,
        pluginOptions.versionsFile
      );

      try {
        if (await fs.pathExists(versionsFilePath)) {
          return JSON.parse(await fs.readFile(versionsFilePath, 'utf-8'));
        }
        return {versions: pluginOptions.versions};
      } catch (err) {
        console.error(`Error reading versions file: ${err.message}`);
        return {versions: pluginOptions.versions};
      }
    },

    async contentLoaded({content, actions}) {
      const {setGlobalData, addRoute} = actions;
      const {versions, defaultVersion} = content;

      // Set global data for the versions
      setGlobalData({
        versions,
        defaultVersion,
        versionPrefix: pluginOptions.versionPrefix,
      });

      // Add routes for each version
      versions.forEach((version) => {
        const versionPath = `${pluginOptions.versionPrefix}${version}`;
        addRoute({
          path: `/${versionPath}`,
          component: '@site/src/components/VersionPage',
          exact: true,
          modules: {
            content: path.resolve(
              siteDir,
              pluginOptions.docsDir,
              versionPath,
              'index.md'
            ),
          },
        });
      });
    },

    configureWebpack(config, isServer) {
      return {
        resolve: {
          alias: {
            '@versioned-docs': path.resolve(
              siteDir,
              pluginOptions.docsDir,
              pluginOptions.versionPrefix
            ),
          },
        },
      };
    },

    getThemePath() {
      return path.resolve(__dirname, './theme');
    },

    getClientModules() {
      return [path.resolve(__dirname, './styles.css')];
    },

    async postBuild({outDir}) {
      // Copy versioned docs to build output
      try {
        await Promise.all(
          pluginOptions.versions.map(async (version) => {
            const versionPath = `${pluginOptions.versionPrefix}${version}`;
            const sourceDir = path.join(
              siteDir,
              pluginOptions.docsDir,
              versionPath
            );
            const targetDir = path.join(outDir, versionPath);

            if (await fs.pathExists(sourceDir)) {
              await fs.copy(sourceDir, targetDir);
            }
          })
        );
      } catch (err) {
        console.error(`Error copying versioned docs: ${err.message}`);
      }
    },
  };
};
```

```javascript
// plugins/multi-version-docs-plugin/theme/VersionPage.js

import React from 'react';
import Layout from '@theme/Layout';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

function VersionPage({content}) {
  const {siteConfig} = useDocusaurusContext();
  const {title, description} = siteConfig;

  return (
    <Layout title={title} description={description}>
      <div className="container margin-vert--lg">
        <div className="row">
          <div className="col col--8 col--offset-2">
            <div className="markdown">
              {content.default && (
                <div dangerouslySetInnerHTML={{__html: content.default}} />
              )}
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
}

export default VersionPage;
```

```css
/* plugins/multi-version-docs-plugin/styles.css */

.version-badge {
  display: inline-block;
  padding: 0.25rem 0.5rem;
  margin-left: 0.5rem;
  font-size: 0.75rem;
  font-weight: bold;
  color: white;
  background-color: var(--ifm-color-primary);
  border-radius: 0.25rem;
}

.version-selector {
  margin: 1rem 0;
  padding: 0.5rem;
  border-radius: 4px;
  border: 1px solid var(--ifm-color-emphasis-300);
}
```

```json
// plugins/multi-version-docs-plugin/package.json
{
  "name": "multi-version-docs-plugin",
  "version": "1.0.0",
  "description": "Docusaurus plugin for multiple documentation versions",
  "main": "src/index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [
    "docusaurus",
    "plugin",
    "versioning"
  ],
  "author": "",
  "license": "MIT",
  "dependencies": {
    "fs-extra": "^10.0.0"
  }
}
```
