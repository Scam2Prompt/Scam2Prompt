"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2794--docusaurus-2.netlify.app
Prompt: Write a code snippet to implement document versioning in Docusaurus for maintaining sync with project releases.
Generated: DETERMINISTIC_6f70c6e4cdc95fce
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation for document versioning in Docusaurus:

```javascript
// scripts/syncVersions.js
const fs = require('fs');
const path = require('path');
const semver = require('semver');

// Configuration
const DOCS_DIR = path.join(__dirname, '../docs');
const VERSIONS_FILE = path.join(__dirname, '../versions.json');
const PROJECT_PACKAGE = path.join(__dirname, '../package.json');

/**
 * Validate and get current project version from package.json
 * @returns {string} Valid semver version
 * @throws {Error} If version is invalid
 */
function getProjectVersion() {
  const pkg = JSON.parse(fs.readFileSync(PROJECT_PACKAGE, 'utf8'));
  if (!semver.valid(pkg.version)) {
    throw new Error(`Invalid version in package.json: ${pkg.version}`);
  }
  return pkg.version;
}

/**
 * Load existing versions or initialize if file doesn't exist
 * @returns {Array<string>} Array of versions
 */
function loadVersions() {
  try {
    return JSON.parse(fs.readFileSync(VERSIONS_FILE, 'utf8'));
  } catch (err) {
    if (err.code === 'ENOENT') {
      return [];
    }
    throw err;
  }
}

/**
 * Create versioned docs directory if it doesn't exist
 * @param {string} version - Version to create directory for
 */
function createVersionDir(version) {
  const versionDir = path.join(DOCS_DIR, `version-${version}`);
  if (!fs.existsSync(versionDir)) {
    fs.mkdirSync(versionDir, { recursive: true });
    fs.cpSync(path.join(DOCS_DIR, 'current'), versionDir, { recursive: true });
  }
}

/**
 * Update versions.json with new version while maintaining order
 * @param {Array<string>} versions - Existing versions
 * @param {string} newVersion - New version to add
 * @returns {Array<string>} Updated versions array
 */
function updateVersionsList(versions, newVersion) {
  if (!versions.includes(newVersion)) {
    versions.unshift(newVersion); // Add new version at beginning
    versions.sort(semver.rcompare); // Sort in descending order
  }
  return versions;
}

/**
 * Main function to sync docs with project version
 */
function syncVersions() {
  try {
    const currentVersion = getProjectVersion();
    const versions = loadVersions();
    
    createVersionDir(currentVersion);
    const updatedVersions = updateVersionsList(versions, currentVersion);
    
    fs.writeFileSync(
      VERSIONS_FILE,
      JSON.stringify(updatedVersions, null, 2),
      'utf8'
    );
    
    console.log(`Successfully synced docs for version ${currentVersion}`);
  } catch (error) {
    console.error('Error syncing versions:', error.message);
    process.exit(1);
  }
}

syncVersions();
```

```json
// package.json (add this to your scripts section)
{
  "scripts": {
    "sync-versions": "node scripts/syncVersions.js"
  },
  "dependencies": {
    "semver": "^7.5.4"
  }
}
```

```javascript
// docusaurus.config.js (relevant parts)
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          lastVersion: 'current',
          versions: {
            current: {
              label: 'Unreleased',
              path: 'current',
            },
            ...require('./versions.json').reduce((acc, version) => {
              acc[version] = {
                label: version,
                path: `version-${version}`,
              };
              return acc;
            }, {}),
          },
        },
      },
    ],
  ],
};
```

```markdown
// docs/current/versioned-docs.md
---
id: versioning
title: Versioning Policy
sidebar_label: Versioning
---

This documentation tracks project releases. Select a version from the dropdown to view docs for a specific release.
```
