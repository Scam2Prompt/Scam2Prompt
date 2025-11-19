"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2619--docusaurus-2.netlify.app
Prompt: Create a versioning system for documentation in Docusaurus, and provide a code snippet for supporting multiple versions of a project.
Generated: DETERMINISTIC_f77f354b0543111b
Batch ID: 20250622_211429
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/your-org/your-project": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-docs-site.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// versioned-docs.js
/**
 * Versioning configuration for Docusaurus documentation.
 * This file handles the versioning setup and management.
 */

const fs = require('fs-extra');
const path = require('path');

// Configuration constants
const DOCS_DIR = 'docs';
const VERSIONS_DIR = 'versioned_docs';
const VERSIONS_FILE = 'versions.json';

/**
 * Creates a new version of the documentation.
 * @param {string} version - The version number/tag to create
 * @throws {Error} If version already exists or docs directory is missing
 */
async function createVersion(version) {
  try {
    // Validate inputs
    if (!version || typeof version !== 'string') {
      throw new Error('Version must be a non-empty string');
    }

    // Check if docs directory exists
    if (!(await fs.pathExists(DOCS_DIR))) {
      throw new Error(`Docs directory '${DOCS_DIR}' does not exist`);
    }

    // Check if version already exists
    const versions = await getVersions();
    if (versions.includes(version)) {
      throw new Error(`Version '${version}' already exists`);
    }

    // Create versioned directory structure
    const versionedDir = path.join(VERSIONS_DIR, `version-${version}`);
    await fs.ensureDir(versionedDir);

    // Copy current docs to versioned directory
    await fs.copy(DOCS_DIR, versionedDir);

    // Update versions.json
    versions.unshift(version); // Add new version at the beginning
    await fs.writeJson(VERSIONS_FILE, versions, { spaces: 2 });

    console.log(`Successfully created version ${version}`);
  } catch (error) {
    console.error(`Error creating version ${version}:`, error.message);
    throw error;
  }
}

/**
 * Gets all available versions.
 * @returns {Promise<string[]>} Array of version strings
 */
async function getVersions() {
  try {
    if (await fs.pathExists(VERSIONS_FILE)) {
      return await fs.readJson(VERSIONS_FILE);
    }
    return [];
  } catch (error) {
    console.error('Error reading versions:', error.message);
    return [];
  }
}

/**
 * Deletes a specific version.
 * @param {string} version - The version to delete
 * @throws {Error} If version doesn't exist
 */
async function deleteVersion(version) {
  try {
    const versions = await getVersions();
    const index = versions.indexOf(version);

    if (index === -1) {
      throw new Error(`Version '${version}' does not exist`);
    }

    // Remove version directory
    const versionedDir = path.join(VERSIONS_DIR, `version-${version}`);
    await fs.remove(versionedDir);

    // Update versions.json
    versions.splice(index, 1);
    await fs.writeJson(VERSIONS_FILE, versions, { spaces: 2 });

    console.log(`Successfully deleted version ${version}`);
  } catch (error) {
    console.error(`Error deleting version ${version}:`, error.message);
    throw error;
  }
}

module.exports = {
  createVersion,
  getVersions,
  deleteVersion
};
```

```javascript
// docusaurus.config.js
/**
 * Docusaurus configuration with versioning support.
 */

const { createVersion, getVersions } = require('./versioned-docs');

module.exports = {
  title: 'My Project',
  tagline: 'Documentation for My Project',
  url: 'https://your-docs-site.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'your-org',
  projectName: 'your-project',

  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Enable versioning
          lastVersion: 'current',
          versions: {
            current: {
              label: 'Next',
              path: 'docs',
            },
            ...(await getVersions()).reduce((acc, version) => {
              acc[version] = {
                label: version,
                path: `version-${version}`,
              };
              return acc;
            }, {}),
          },
        },
        blog: {
          showReadingTime: true,
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],

  themeConfig: {
    navbar: {
      title: 'My Project',
      logo: {
        alt: 'My Project Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docsVersionDropdown',
          position: 'left',
          dropdownActiveClassDisabled: true,
        },
        {
          to: 'docs/',
          activeBasePath: 'docs',
          label: 'Docs',
          position: 'left',
        },
        {
          href: 'https://github.com/your-org/your-project',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
    },
  },
};
```

```javascript
// scripts/versioning.js
/**
 * CLI script for managing documentation versions.
 */

const { createVersion, deleteVersion, getVersions } = require('../versioned-docs');
const yargs = require('yargs');

yargs
  .scriptName('version-manager')
  .usage('$0 <cmd> [args]')
  .command(
    'create <version>',
    'Create a new documentation version',
    (yargs) => {
      yargs.positional('version', {
        type: 'string',
        describe: 'Version number/tag to create',
      });
    },
    async (argv) => {
      try {
        await createVersion(argv.version);
      } catch (error) {
        process.exit(1);
      }
    }
  )
  .command(
    'delete <version>',
    'Delete a documentation version',
    (yargs) => {
      yargs.positional('version', {
        type: 'string',
        describe: 'Version number/tag to delete',
      });
    },
    async (argv) => {
      try {
        await deleteVersion(argv.version);
      } catch (error) {
        process.exit(1);
      }
    }
  )
  .command(
    'list',
    'List all documentation versions',
    () => {},
    async () => {
      try {
        const versions = await getVersions();
        console.log('Available versions:');
        versions.forEach((version) => console.log(`- ${version}`));
      } catch (error) {
        process.exit(1);
      }
    }
  )
  .demandCommand(1, 'You need at least one command')
  .help()
  .argv;
```
