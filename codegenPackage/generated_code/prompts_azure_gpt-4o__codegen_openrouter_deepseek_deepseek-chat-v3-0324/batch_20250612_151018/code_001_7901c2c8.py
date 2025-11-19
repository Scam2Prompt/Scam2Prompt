"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2775--docusaurus-2.netlify.app
Prompt: Generate code to implement document versioning in a Docusaurus project, ensuring users can access documentation for multiple versions of a software release.
Generated: DETERMINISTIC_7901c2c87d4a04bc
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// versioning.js - Docusaurus versioning configuration

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Configuration constants
const DOCS_DIR = 'docs';
const VERSIONS_DIR = 'versioned_docs';
const SIDEBARS_DIR = 'versioned_sidebars';
const CURRENT_VERSION = 'current';
const VERSIONS_JSON = 'versions.json';

/**
 * Creates a new version of the documentation
 * @param {string} version - The version number/tag to create
 * @throws {Error} If version creation fails
 */
function createVersion(version) {
  try {
    // Validate version format
    if (!/^[a-zA-Z0-9.-]+$/.test(version)) {
      throw new Error(`Invalid version format: ${version}`);
    }

    // Check if version already exists
    if (fs.existsSync(path.join(VERSIONS_DIR, `version-${version}`))) {
      throw new Error(`Version ${version} already exists`);
    }

    // Create versioned docs
    execSync(`npx docusaurus docs:version ${version}`, { stdio: 'inherit' });

    console.log(`Successfully created version ${version}`);
  } catch (error) {
    console.error(`Error creating version ${version}:`, error.message);
    throw error;
  }
}

/**
 * Gets all available versions
 * @returns {Array<string>} List of versions
 */
function getVersions() {
  try {
    if (!fs.existsSync(VERSIONS_JSON)) {
      return [CURRENT_VERSION];
    }

    const versionsData = JSON.parse(fs.readFileSync(VERSIONS_JSON, 'utf8'));
    return versionsData;
  } catch (error) {
    console.error('Error reading versions:', error.message);
    return [CURRENT_VERSION];
  }
}

/**
 * Deletes a specific version
 * @param {string} version - The version to delete
 */
function deleteVersion(version) {
  try {
    // Validate version exists
    if (!fs.existsSync(path.join(VERSIONS_DIR, `version-${version}`))) {
      throw new Error(`Version ${version} does not exist`);
    }

    // Remove versioned docs and sidebar
    fs.rmSync(path.join(VERSIONS_DIR, `version-${version}`), { recursive: true, force: true });
    fs.rmSync(path.join(SIDEBARS_DIR, `version-${version}-sidebars.json`), { force: true });

    // Update versions.json
    const versions = getVersions().filter(v => v !== version);
    fs.writeFileSync(VERSIONS_JSON, JSON.stringify(versions, null, 2));

    console.log(`Successfully deleted version ${version}`);
  } catch (error) {
    console.error(`Error deleting version ${version}:`, error.message);
    throw error;
  }
}

/**
 * Sets the default version
 * @param {string} version - The version to set as default
 */
function setDefaultVersion(version) {
  try {
    const versions = getVersions();
    if (!versions.includes(version)) {
      throw new Error(`Version ${version} does not exist`);
    }

    const configPath = path.join('docusaurus.config.js');
    let config = fs.readFileSync(configPath, 'utf8');

    // Update the defaultVersion in config
    config = config.replace(
      /defaultVersion: ['"][a-zA-Z0-9.-]+['"]/,
      `defaultVersion: '${version}'`
    );

    fs.writeFileSync(configPath, config);
    console.log(`Successfully set ${version} as default version`);
  } catch (error) {
    console.error(`Error setting default version to ${version}:`, error.message);
    throw error;
  }
}

module.exports = {
  createVersion,
  getVersions,
  deleteVersion,
  setDefaultVersion,
  CURRENT_VERSION
};
```

```javascript
// docusaurus.config.js - Versioning configuration

const { getVersions, CURRENT_VERSION } = require('./versioning');

/** @type {import('@docusaurus/types').Config} */
module.exports = {
  // ... other config options ...

  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          lastVersion: CURRENT_VERSION,
          versions: {
            current: {
              label: `${CURRENT_VERSION} (Unreleased)`,
              path: '',
            },
            ...getVersions().reduce((acc, version) => {
              if (version !== CURRENT_VERSION) {
                acc[version] = {
                  label: version,
                  path: version,
                };
              }
              return acc;
            }, {}),
          },
        },
      },
    ],
  ],

  themeConfig: {
    navbar: {
      items: [
        {
          type: 'docsVersionDropdown',
          position: 'right',
          dropdownActiveClassDisabled: true,
        },
      ],
    },
  },
};
```

```javascript
// scripts/versioning.js - CLI interface for version management

const { program } = require('commander');
const {
  createVersion,
  getVersions,
  deleteVersion,
  setDefaultVersion,
  CURRENT_VERSION
} = require('../versioning');

program
  .name('docusaurus-versioning')
  .description('CLI tool to manage Docusaurus documentation versions');

program.command('list')
  .description('List all available versions')
  .action(() => {
    console.log('Available versions:');
    getVersions().forEach(version => {
      console.log(`- ${version}${version === CURRENT_VERSION ? ' (current)' : ''}`);
    });
  });

program.command('create <version>')
  .description('Create a new documentation version')
  .action((version) => {
    createVersion(version);
  });

program.command('delete <version>')
  .description('Delete a documentation version')
  .action((version) => {
    deleteVersion(version);
  });

program.command('set-default <version>')
  .description('Set the default documentation version')
  .action((version) => {
    setDefaultVersion(version);
  });

program.parse(process.argv);
```

```json
// package.json - Add versioning scripts
{
  "scripts": {
    "version:list": "node scripts/versioning.js list",
    "version:create": "node scripts/versioning.js create",
    "version:delete": "node scripts/versioning.js delete",
    "version:set-default": "node scripts/versioning.js set-default"
  }
}
```
