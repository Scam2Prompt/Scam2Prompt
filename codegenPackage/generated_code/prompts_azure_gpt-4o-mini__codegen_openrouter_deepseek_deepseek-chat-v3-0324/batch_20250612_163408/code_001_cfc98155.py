"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2792--docusaurus-2.netlify.app
Prompt: What are the steps to implement document versioning in Docusaurus for maintaining documentation across multiple project releases?
Generated: DETERMINISTIC_cfc98155385f3c21
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean implementation for document versioning in Docusaurus:

```javascript
// docusaurus.config.js
module.exports = {
  // ... other configs
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          lastVersion: 'current',
          versions: {
            current: {
              label: '2.0.0',
              path: '2.0.0',
            },
            '1.0.0': {
              label: '1.0.0',
              path: '1.0.0',
              banner: 'none',
            },
          },
        },
      },
    ],
  ],
};

// versions.json (in versioned_docs directory)
["1.0.0"]

// scripts/version.js
const fs = require('fs-extra');
const path = require('path');

async function createVersion(version) {
  try {
    const docsDir = path.join(__dirname, '..', 'docs');
    const versionedDir = path.join(__dirname, '..', 'versioned_docs');
    const versionedSidebarsDir = path.join(__dirname, '..', 'versioned_sidebars');
    
    // Create versioned docs directory
    await fs.copy(
      docsDir,
      path.join(versionedDir, `version-${version}`)
    );

    // Create versioned sidebar
    const sidebarPath = path.join(__dirname, '..', 'sidebars.js');
    if (await fs.pathExists(sidebarPath)) {
      await fs.copy(
        sidebarPath,
        path.join(versionedSidebarsDir, `version-${version}-sidebars.json`)
      );
    }

    // Update versions.json
    const versionsPath = path.join(versionedDir, 'versions.json');
    let versions = [];
    if (await fs.pathExists(versionsPath)) {
      versions = JSON.parse(await fs.readFile(versionsPath));
    }
    versions.unshift(version);
    await fs.writeFile(versionsPath, JSON.stringify(versions, null, 2));

    console.log(`Version ${version} created successfully!`);
  } catch (error) {
    console.error(`Error creating version ${version}:`, error);
    process.exit(1);
  }
}

const version = process.argv[2];
if (!version) {
  console.error('Please specify a version number');
  process.exit(1);
}

createVersion(version);
```

```json
// package.json (partial)
{
  "scripts": {
    "version": "node scripts/version.js",
    "docusaurus": "docusaurus",
    "start": "docusaurus start",
    "build": "docusaurus build",
    "swizzle": "docusaurus swizzle",
    "deploy": "docusaurus deploy",
    "clear": "docusaurus clear",
    "serve": "docusaurus serve",
    "write-translations": "docusaurus write-translations",
    "write-heading-ids": "docusaurus write-heading-ids"
  }
}
```

```javascript
// docs/versions.js (if using TypeScript)
export const versions = {
  current: {
    label: 'Next',
    path: 'next',
  },
  '2.0.0': {
    label: '2.0.0',
    path: '2.0.0',
  },
  '1.0.0': {
    label: '1.0.0',
    path: '1.0.0',
  },
};
```
