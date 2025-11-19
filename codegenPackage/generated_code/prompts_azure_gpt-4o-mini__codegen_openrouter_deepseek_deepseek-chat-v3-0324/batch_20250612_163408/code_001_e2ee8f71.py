"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2758--docusaurus-2.netlify.app
Prompt: Write a code snippet to implement document versioning in Docusaurus for maintaining documentation across project releases.
Generated: DETERMINISTIC_e2ee8f71e6715e5e
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// DocumentVersioning.js
const fs = require('fs-extra');
const path = require('path');

/**
 * Implements document versioning for Docusaurus documentation.
 */
class DocumentVersioning {
  /**
   * @param {string} docsDir - Path to the docs directory
   * @param {string} versionsDir - Path to the versions directory
   * @param {string} currentVersion - Current version to be documented
   */
  constructor(docsDir, versionsDir, currentVersion) {
    this.docsDir = docsDir;
    this.versionsDir = versionsDir;
    this.currentVersion = currentVersion;
  }

  /**
   * Creates a new versioned copy of documentation
   * @throws {Error} If versioning operation fails
   */
  async createVersionedDocs() {
    try {
      // Ensure versions directory exists
      await fs.ensureDir(this.versionsDir);

      const versionedDir = path.join(this.versionsDir, this.currentVersion);
      
      // Remove existing version if it exists
      if (await fs.pathExists(versionedDir)) {
        await fs.remove(versionedDir);
      }

      // Copy current docs to versioned directory
      await fs.copy(this.docsDir, versionedDir);
      
      console.log(`Successfully created versioned docs for ${this.currentVersion}`);
    } catch (error) {
      console.error('Error creating versioned docs:', error);
      throw new Error(`Versioning failed: ${error.message}`);
    }
  }

  /**
   * Updates the current version symlink
   * @throws {Error} If symlink operation fails
   */
  async updateCurrentVersionSymlink() {
    try {
      const symlinkPath = path.join(this.versionsDir, 'current');
      const targetPath = path.join(this.versionsDir, this.currentVersion);

      // Remove existing symlink if it exists
      if (await fs.pathExists(symlinkPath)) {
        await fs.remove(symlinkPath);
      }

      // Create new symlink
      await fs.symlink(targetPath, symlinkPath, 'dir');
      
      console.log(`Updated current version symlink to ${this.currentVersion}`);
    } catch (error) {
      console.error('Error updating symlink:', error);
      throw new Error(`Symlink update failed: ${error.message}`);
    }
  }
}

// Example usage:
// const versioning = new DocumentVersioning(
//   './docs',
//   './versioned_docs',
//   '2.0.0'
// );
// versioning.createVersionedDocs()
//   .then(() => versioning.updateCurrentVersionSymlink())
//   .catch(err => console.error(err));
```

```json
// versions.json (Docusaurus config example)
{
  "versions": {
    "1.0.0": {
      "label": "1.0.0",
      "path": "1.0.0"
    },
    "2.0.0": {
      "label": "2.0.0 (Latest)",
      "path": "2.0.0"
    }
  }
}
```

```javascript
// docusaurus.config.js (relevant parts)
module.exports = {
  themeConfig: {
    navbar: {
      items: [
        {
          type: 'docsVersionDropdown',
          position: 'left',
          dropdownActiveClassDisabled: true,
          dropdownItemsAfter: [
            {
              to: '/versions',
              label: 'All versions'
            }
          ]
        }
      ]
    }
  },
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        lastVersion: 'current',
        versions: {
          current: {
            label: 'Next',
            path: 'docs'
          }
        }
      }
    ]
  ]
};
```
