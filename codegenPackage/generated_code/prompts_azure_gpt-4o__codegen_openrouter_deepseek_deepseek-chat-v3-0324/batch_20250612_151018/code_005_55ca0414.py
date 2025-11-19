"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2757--docusaurus-2.netlify.app
Prompt: Create a Docusaurus plugin to manage document versioning that aligns with project releases. Include an example configuration.
Generated: DETERMINISTIC_55ca0414faf86570
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// plugins/docusaurus-plugin-doc-versioning/src/index.js

const fs = require('fs');
const path = require('path');
const { LoadContext, Plugin } = require('@docusaurus/types');

/**
 * Docusaurus plugin to manage document versioning aligned with project releases
 */
function docVersioningPlugin(context, options) {
  const {
    siteDir,
    siteConfig: { baseUrl },
  } = context;
  const {
    versions = [],
    versionedDocsDir = 'versioned_docs',
    versionedSidebarsDir = 'versioned_sidebars',
    currentVersion = 'current',
    disableVersioning = false,
  } = options;

  return {
    name: 'docusaurus-plugin-doc-versioning',
    async loadContent() {
      if (disableVersioning) {
        return { versions: [], currentVersion };
      }

      try {
        // Validate versions
        if (!Array.isArray(versions) || versions.length === 0) {
          throw new Error('No versions configured for versioning');
        }

        // Ensure versioned directories exist
        const docsPath = path.join(siteDir, versionedDocsDir);
        const sidebarsPath = path.join(siteDir, versionedSidebarsDir);

        if (!fs.existsSync(docsPath)) {
          fs.mkdirSync(docsPath, { recursive: true });
        }
        if (!fs.existsSync(sidebarsPath)) {
          fs.mkdirSync(sidebarsPath, { recursive: true });
        }

        return {
          versions,
          currentVersion,
          versionedDocsDir,
          versionedSidebarsDir,
          baseUrl,
        };
      } catch (error) {
        console.error('Error in docVersioningPlugin:', error);
        throw error;
      }
    },
    async contentLoaded({ content, actions }) {
      const { setGlobalData } = actions;
      setGlobalData(content);
    },
    getPathsToWatch() {
      return [
        path.join(siteDir, versionedDocsDir),
        path.join(siteDir, versionedSidebarsDir),
      ];
    },
  };
}

module.exports = docVersioningPlugin;
```

```javascript
// plugins/docusaurus-plugin-doc-versioning/src/globalData.d.ts
declare module '@docusaurus/plugin-content-docs' {
  export interface VersionMetadata {
    version: string;
    label: string;
    isLast: boolean;
    path: string;
  }
}

export interface DocVersioningData {
  versions: string[];
  currentVersion: string;
  versionedDocsDir: string;
  versionedSidebarsDir: string;
  baseUrl: string;
}
```

```javascript
// docusaurus.config.js example usage
module.exports = {
  // ... other config
  plugins: [
    [
      './plugins/docusaurus-plugin-doc-versioning',
      {
        versions: ['1.0.0', '2.0.0', '3.0.0'],
        currentVersion: '3.0.0',
        versionedDocsDir: 'versioned_docs',
        versionedSidebarsDir: 'versioned_sidebars',
      },
    ],
  ],
  // ... rest of config
};
```

```javascript
// src/components/VersionDropdown.js
import React from 'react';
import { useGlobalData } from '@docusaurus/theme-common';

export default function VersionDropdown() {
  const { versions, currentVersion, baseUrl } = useGlobalData()['docusaurus-plugin-doc-versioning'];

  return (
    <div className="dropdown dropdown--hoverable dropdown--right">
      <button className="navbar__link">
        Version: {currentVersion}
      </button>
      <ul className="dropdown__menu">
        {versions.map((version) => (
          <li key={version}>
            <a
              className="dropdown__link"
              href={`${baseUrl}docs/${version}/introduction`}
            >
              {version}
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
}
```
