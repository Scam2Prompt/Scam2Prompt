"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2775--docusaurus-2.netlify.app
Prompt: What are the steps to implement document versioning in Docusaurus for my project?
Generated: DETERMINISTIC_96e8db992a842413
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
          routeBasePath: '/',
          sidebarPath: require.resolve('./sidebars.js'),
          // Enable versioning
          lastVersion: 'current',
          versions: {
            current: {
              label: '2.0.0',
              path: '2.0.0',
            },
            '1.0.0': {
              label: '1.0.0',
              path: '1.0.0',
              banner: 'none'
            }
          },
        },
      },
    ],
  ],
};

// versions.json (in root directory)
["1.0.0"]

// package.json (add scripts)
{
  "scripts": {
    "docusaurus": "docusaurus",
    "start": "docusaurus start",
    "build": "docusaurus build",
    "swizzle": "docusaurus swizzle",
    "deploy": "docusaurus deploy",
    "clear": "docusaurus clear",
    "serve": "docusaurus serve",
    "write-translations": "docusaurus write-translations",
    "write-heading-ids": "docusaurus write-heading-ids",
    "version": "docusaurus docs:version 1.0.0"
  }
}

// docs/.current/ (your current version docs)
// docs/1.0.0/ (previous version docs)

// sidebars.js (example)
module.exports = {
  someSidebar: {
    'Version 2.0.0': [
      'intro',
      'getting-started',
    ],
    'Version 1.0.0': [
      '1.0.0/intro',
      '1.0.0/getting-started',
    ],
  },
};
```
lse {
      throw new Error('Current docs directory not found');
    }
  } catch (error) {
    console.error(`Error creating new version: ${error.message}`);
    process.exit(1);
  }
}

module.exports = createNewVersion;

// package.json (partial)
{
  "scripts": {
    "version": "node ./scripts/version.js",
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

// To create a new version:
// 1. Update docusaurus.config.js
// 2. Run: npm run version -- 2.1.0
// 3. Update current symlink: cd docs && rm current && ln -s 2.1.0 current
// 4. Commit changes
```

This implementation includes:
1. Docusaurus versioning configuration
2. Directory structure for versioned docs
3. Script to automate version creation
4. Package.json integration
5. Error handling for the version creation process
