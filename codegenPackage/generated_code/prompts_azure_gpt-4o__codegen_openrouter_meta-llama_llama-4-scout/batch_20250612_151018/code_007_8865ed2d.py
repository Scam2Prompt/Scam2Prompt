"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2809--docusaurus-2.netlify.app
Prompt: Write a script to implement document versioning in a Docusaurus project to support multiple project releases.
Generated: DETERMINISTIC_8865ed2dc5ce20e8
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
const path = require('path');
const fs = require('fs');
const { createPlugin } = require('@docusaurus/core');

const VERSIONED_DOCS_FOLDER = 'versioned_docs';
const VERSIONS_JSON_FILE = 'versions.json';

const createVersionedDocPath = (version, docPath) => {
  return path.join(VERSIONED_DOCS_FOLDER, version, docPath);
};

const getVersionedDocs = (context, version) => {
  const { siteDir } = context;
  const versionedDocsPath = path.join(siteDir, VERSIONED_DOCS_FOLDER, version);
  return fs.readdirSync(versionedDocsPath).map((file) => {
    return createVersionedDocPath(version, file);
  });
};

const getVersions = (context) => {
  const { siteDir } = context;
  const versionsJsonPath = path.join(siteDir, VERSIONS_JSON_FILE);
  try {
    return JSON.parse(fs.readFileSync(versionsJsonPath, 'utf8'));
  } catch (error) {
    if (error.code === 'ENOENT') {
      return [];
    }
    throw error;
  }
};

const VersioningPlugin = createPlugin({
  name: 'docusaurus-plugin-versioning',
  async contentLoaded({ content, actions }) {
    const { createData, setGlobalData } = actions;
    const { siteDir } = content;
    const versions = getVersions(content);

    const versionedDocs = {};
    versions.forEach((version) => {
      versionedDocs[version] = getVersionedDocs(content, version);
    });

    setGlobalData({ versionedDocs });

    // Create versioned doc data
    Object.keys(versionedDocs).forEach((version) => {
      const docs = versionedDocs[version];
      createData(
        `versioned-docs-${version}.json`,
        JSON.stringify({ docs })
      );
    });
  },
});

module.exports = VersioningPlugin;
```

```javascript
// versions.json
[
  "1.0.0",
  "1.1.0",
  "2.0.0"
]
```

```javascript
// docusaurus.config.js
const VersioningPlugin = require('./docusaurus-plugin-versioning');

module.exports = {
  // ... other config options ...
  plugins: [
    VersioningPlugin,
  ],
};
```

```javascript
// versioned_docs/1.0.0/doc1.md
---
id: doc1
title: Doc 1
version: 1.0.0
---

This is doc 1 in version 1.0.0.
```

```javascript
// versioned_docs/1.1.0/doc1.md
---
id: doc1
title: Doc 1
version: 1.1.0
---

This is doc 1 in version 1.1.0.
```

```javascript
// versioned_docs/2.0.0/doc1.md
---
id: doc1
title: Doc 1
version: 2.0.0
---

This is doc 1 in version 2.0.0.
```

```javascript
// src/pages/index.js
import React from 'react';
import { useGlobalData } from '@docusaurus/core';

const Home = () => {
  const globalData = useGlobalData();
  const versionedDocs = globalData.versionedDocs;

  return (
    <div>
      <h1>Versioned Docs</h1>
      <ul>
        {Object.keys(versionedDocs).map((version) => (
          <li key={version}>
            <a href={`docs/${version}/doc1`}>{version}</a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Home;
```
