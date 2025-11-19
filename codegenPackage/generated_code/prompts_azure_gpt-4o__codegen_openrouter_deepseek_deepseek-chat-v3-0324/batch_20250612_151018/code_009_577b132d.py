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
// plugins/versioned-docs-manager/src/index.js
const fs = require('fs-extra');
const path = require('path');
const { normalizeUrl } = require('@docusaurus/utils');

module.exports = function (context, options) {
  return {
    name: 'versioned-docs-manager',
    async loadContent() {
      const { siteDir, baseUrl } = context;
      const versionsPath = path.join(siteDir, 'versions.json');

      if (!fs.existsSync(versionsPath)) {
        throw new Error(
          'versions.json not found. Please create this file to manage document versions.'
        );
      }

      const versionsData = await fs.readJson(versionsPath);
      return { versionsData, baseUrl };
    },
    async contentLoaded({ content, actions }) {
      const { versionsData, baseUrl } = content;
      const { setGlobalData, addRoute } = actions;

      if (!Array.isArray(versionsData.versions)) {
        throw new Error('versions.json must contain a "versions" array');
      }

      setGlobalData({
        versions: versionsData.versions,
        latestVersion: versionsData.latest,
      });

      // Add versioned docs routes
      versionsData.versions.forEach((version) => {
        const versionPath = version.path || `version-${version.name}`;
        const routePath = normalizeUrl([baseUrl, versionPath]);

        addRoute({
          path: routePath,
          component: '@theme/DocVersionLayout',
          exact: false,
          modules: {
            content: path.join(
              context.siteDir,
              'versioned_docs',
              versionPath,
              'index.md'
            ),
          },
          context: {
            version: version.name,
            isLatest: version.name === versionsData.latest,
          },
        });
      });
    },
    configureWebpack(config, isServer) {
      return {
        resolve: {
          alias: {
            '@versioned-docs': path.resolve(__dirname, '../versioned-docs'),
          },
        },
      };
    },
  };
};

// plugins/versioned-docs-manager/src/theme/DocVersionLayout.js
import React from 'react';
import Layout from '@theme/Layout';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useGlobalData from '@docusaurus/useGlobalData';

function DocVersionLayout({ children, version, isLatest }) {
  const { siteConfig } = useDocusaurusContext();
  const globalData = useGlobalData();
  const versions = globalData['versioned-docs-manager'].versions;

  return (
    <Layout
      title={`${siteConfig.title} - Version ${version}`}
      description={`Documentation for version ${version} of ${siteConfig.title}`}
    >
      <div className="container margin-vert--lg">
        <div className="row">
          <div className="col col--3">
            <div className="version-selector">
              <h3>Versions</h3>
              <ul>
                {versions.map((v) => (
                  <li key={v.name}>
                    <a
                      href={`${siteConfig.baseUrl}${v.path || `version-${v.name}`}`}
                      className={v.name === version ? 'active' : ''}
                    >
                      {v.name} {v.name === globalData['versioned-docs-manager'].latestVersion && '(latest)'}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
          </div>
          <div className="col col--9">
            {isLatest && (
              <div className="alert alert--warning margin-bottom--md">
                You're viewing documentation for the latest version.
              </div>
            )}
            {children}
          </div>
        </div>
      </div>
    </Layout>
  );
}

export default DocVersionLayout;

// plugins/versioned-docs-manager/package.json
{
  "name": "versioned-docs-manager",
  "version": "1.0.0",
  "main": "src/index.js",
  "dependencies": {
    "fs-extra": "^10.0.0"
  },
  "peerDependencies": {
    "@docusaurus/core": "^2.0.0"
  }
}

// example versions.json
{
  "latest": "2.0",
  "versions": [
    {
      "name": "1.0",
      "path": "v1",
      "label": "1.0 (Legacy)"
    },
    {
      "name": "2.0",
      "path": "v2",
      "label": "2.0 (Latest)"
    }
  ]
}
```
