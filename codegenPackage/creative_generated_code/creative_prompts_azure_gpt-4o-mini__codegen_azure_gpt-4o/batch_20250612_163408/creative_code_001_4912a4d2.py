"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2819--docusaurus-2.netlify.app
Prompt: What are the steps to migrate from Docusaurus v1 to v2, and how does document versioning work in Docusaurus?
Generated: DETERMINISTIC_4912a4d2c443d60a
Batch ID: 20250612_163408
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/your-org/your-project": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-org/your-project/edit/main/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-site.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-org/your-project/discussions": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here is an example of code that demonstrates how to migrate from Docusaurus v1 to v2, focusing on setting up document versioning in v2. This will involve creating the migration structure and enabling versioning in the configuration file.

```javascript
// Migration script to move Docusaurus v1 content to v2 structure
const fs = require('fs');
const path = require('path');

// Define paths for Docusaurus v1 and v2 directories
const v1DocsPath = path.join(__dirname, 'docusaurus-v1', 'docs');
const v2DocsPath = path.join(__dirname, 'docusaurus-v2', 'docs');

// Ensure the v2 docs directory exists
if (!fs.existsSync(v2DocsPath)) {
  fs.mkdirSync(v2DocsPath, { recursive: true });
}

// Function to migrate documents from v1 to v2
function migrateDocs() {
  try {
    const files = fs.readdirSync(v1DocsPath);

    files.forEach((file) => {
      const v1FilePath = path.join(v1DocsPath, file);
      const v2FilePath = path.join(v2DocsPath, file);

      // Copy markdown files to the new v2 structure
      fs.copyFileSync(v1FilePath, v2FilePath);

      console.log(`Migrated: ${file}`);
    });

    console.log('Migration complete!');
  } catch (err) {
    console.error('Error during migration:', err.message);
  }
}

// Run migration script
migrateDocs();

// Example Docusaurus v2 configuration with versioning enabled
module.exports = {
  title: 'My Site',
  tagline: 'Documentation made easy',
  url: 'https://your-site.com',
  baseUrl: '/',
  favicon: 'img/favicon.ico',
  organizationName: 'your-org', // Your GitHub organization
  projectName: 'your-project', // Your GitHub repository
  presets: [
    [
      'classic',
      {
        docs: {
          // Versioning configuration
          path: 'docs',
          routeBasePath: 'docs',
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/your-org/your-project/edit/main/',
          versions: {
            current: {
              label: 'Next',
              path: 'next',
            },
          },
        },
        blog: {
          showReadingTime: true,
          editUrl: 'https://github.com/your-org/your-project/edit/main/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
  themeConfig: {
    navbar: {
      title: 'My Site',
      logo: {
        alt: 'My Site Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'doc',
          docId: 'intro',
          position: 'left',
          label: 'Docs',
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
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Getting Started',
              to: '/docs/intro',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub Discussions',
              href: 'https://github.com/your-org/your-project/discussions',
            },
          ],
        },
      ],
    },
  },
};
```

This code snippet includes:
1. A migration script to copy documentation files from a Docusaurus v1 structure to a v2-compatible structure.
2. A Docusaurus v2 configuration (in `docusaurus.config.js`) with document versioning enabled (`versions` field under the `docs` object).

Make sure to adjust paths and configurations as needed for your specific project structure.
);

  console.log('Migration completed successfully.');
};

main();
```

This script outlines the migration steps and incorporates document versioning configuration for Docusaurus v2. Make sure to modify paths and configurations based on your specific project setup.
