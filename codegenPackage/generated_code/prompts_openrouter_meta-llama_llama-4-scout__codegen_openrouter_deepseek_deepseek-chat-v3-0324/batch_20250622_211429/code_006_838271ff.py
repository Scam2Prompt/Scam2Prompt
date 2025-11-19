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
/**
 * Docusaurus plugin for document versioning and release synchronization.
 * @module docusaurus-plugin-doc-versioning
 */

const fs = require('fs').promises;
const path = require('path');
const { execSync } = require('child_process');
const semver = require('semver');

/**
 * Validates the plugin configuration.
 * @param {Object} options - Plugin options
 * @throws {Error} If configuration is invalid
 */
function validateConfig(options) {
  if (!options.releasesDir) {
    throw new Error('releasesDir is required in plugin configuration');
  }
  if (!options.docsDir) {
    throw new Error('docsDir is required in plugin configuration');
  }
}

/**
 * Gets the current project version from package.json.
 * @returns {string} Current version
 * @throws {Error} If version cannot be determined
 */
function getCurrentVersion() {
  try {
    const packageJson = require(path.join(process.cwd(), 'package.json'));
    if (!packageJson.version) {
      throw new Error('Version not found in package.json');
    }
    return packageJson.version;
  } catch (err) {
    throw new Error(`Failed to get current version: ${err.message}`);
  }
}

/**
 * Creates a new version directory for documentation.
 * @param {string} docsDir - Base docs directory
 * @param {string} version - Version to create
 * @returns {Promise<void>}
 */
async function createVersionDir(docsDir, version) {
  const versionDir = path.join(docsDir, version);
  try {
    await fs.mkdir(versionDir, { recursive: true });
  } catch (err) {
    throw new Error(`Failed to create version directory: ${err.message}`);
  }
}

/**
 * Syncs documentation with release tags.
 * @param {string} releasesDir - Releases directory
 * @param {string} docsDir - Docs directory
 * @returns {Promise<void>}
 */
async function syncWithReleases(releasesDir, docsDir) {
  try {
    const tags = execSync('git tag --list "v*"').toString().trim().split('\n');
    const validVersions = tags
      .map(tag => tag.replace(/^v/, ''))
      .filter(version => semver.valid(version))
      .sort(semver.rcompare);

    for (const version of validVersions) {
      const versionDir = path.join(docsDir, version);
      const releaseDir = path.join(releasesDir, version);

      try {
        await fs.access(releaseDir);
        await fs.cp(releaseDir, versionDir, { recursive: true });
      } catch (err) {
        console.warn(`No release docs found for version ${version}`);
      }
    }
  } catch (err) {
    throw new Error(`Failed to sync with releases: ${err.message}`);
  }
}

/**
 * Main plugin function.
 * @param {Object} context - Docusaurus context
 * @param {Object} options - Plugin options
 */
async function docVersioningPlugin(context, options) {
  validateConfig(options);

  const currentVersion = getCurrentVersion();
  const { docsDir, releasesDir } = options;

  try {
    await createVersionDir(docsDir, currentVersion);
    await syncWithReleases(releasesDir, docsDir);
  } catch (err) {
    console.error(`DocVersioningPlugin error: ${err.message}`);
    process.exit(1);
  }
}

module.exports = docVersioningPlugin;
```
