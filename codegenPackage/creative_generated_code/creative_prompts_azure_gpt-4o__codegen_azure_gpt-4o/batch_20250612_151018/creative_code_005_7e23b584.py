"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2619--docusaurus-2.netlify.app
Prompt: Provide code examples for setting up document versioning in Docusaurus to support multiple versions of a project’s documentation.
Generated: DETERMINISTIC_7e23b584f1848903
Batch ID: 20250612_151018
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/your-org/your-project/edit/main/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// File: docusaurus.config.js
// This is the Docusaurus configuration file where we set up versioning for the documentation.

module.exports = {
  title: 'My Project',
  tagline: 'Documentation for My Project',
  url: 'https://example.com', // Replace with your documentation website URL
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'your-org', // Replace with your GitHub org/user name
  projectName: 'your-project', // Replace with your repo name

  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          // Enable versioning for the documentation
          path: 'docs',
          routeBasePath: 'docs',
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/your-org/your-project/edit/main/',
          lastVersion: 'current', // Define the default version
          versions: {
            current: {
              label: 'Next 🚀', // Custom label for the default version
              path: 'next', // Route path for the current version
            },
            '1.0.0': {
              label: 'v1.0.0',
              path: 'v1.0.0', // Route path for version 1.0.0
            },
          },
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
```

```bash
# Create initial versioning setup
# Run this command in your terminal to create the first version of the documentation.
npx docusaurus docs:version 1.0.0
```

```javascript
// File: sidebars.js
// The sidebar configuration for the documentation.

module.exports = {
  // Define the sidebar items for each version
  docs: {
    'Getting Started': ['introduction', 'setup'],
    'Features': ['feature1', 'feature2'],
  },
};
```

```json
// File: package.json
// Ensure you have the necessary dependencies for Docusaurus.

{
  "name": "my-project-docs",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "start": "docusaurus start",
    "build": "docusaurus build",
    "serve": "docusaurus serve",
    "deploy": "docusaurus deploy",
    "clear": "docusaurus clear",
    "docs:version": "docusaurus docs:version"
  },
  "dependencies": {
    "@docusaurus/core": "^2.4.0",
    "@docusaurus/preset-classic": "^2.4.0"
  }
}
```

```bash
# After setting up versioning, test your setup locally
# Start the development server and check routes for different versions.
npm run start
```

```plaintext
# Directory structure after versioning command (docs:version)
# Automatically created by Docusaurus for versioning.

.
├── docs/
│   ├── introduction.md
│   ├── setup.md
│   ├── feature1.md
│   ├── feature2.md
├── versioned_docs/
│   ├── version-1.0.0/
│       ├── introduction.md
│       ├── setup.md
│       ├── feature1.md
│       ├── feature2.md
├── versions.json
```

```json
// File: versions.json
// Tracks the available versions of your documentation.

[
  "1.0.0", // Older version
  "current" // Current version
]
```
