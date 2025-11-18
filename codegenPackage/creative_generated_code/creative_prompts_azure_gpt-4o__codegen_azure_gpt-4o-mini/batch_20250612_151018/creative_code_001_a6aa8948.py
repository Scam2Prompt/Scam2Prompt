"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2614--docusaurus-2.netlify.app
Prompt: How can I use Docusaurus to implement document versioning for multiple releases of my software? Provide code examples.
Generated: DETERMINISTIC_a6aa8948e169188c
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://yourwebsite.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```bash
# First, make sure you have Docusaurus installed
npx create-docusaurus@latest my-website classic
cd my-website

# Install required plugins for versioning
npm install @docusaurus/plugin-content-docs
```

```javascript
// docusaurus.config.js

module.exports = {
  title: 'My Software Documentation',
  tagline: 'Documentation for multiple releases',
  url: 'https://yourwebsite.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  presets: [
    [
      'classic',
      {
        docs: {
          routeBasePath: 'docs', // Set the route base path for docs
          sidebarPath: require.resolve('./sidebars.js'),
          // Enable versioning
          versions: {
            current: {
              label: 'Latest',
              path: 'latest',
              // Documentation for the current version
              lastUpdatedAt: new Date().getTime(),
            },
            '1.0.0': {
              label: 'Version 1.0.0',
              path: '1.0.0',
              // Documentation for version 1.0.0
              lastUpdatedAt: '2023-01-01T00:00:00Z',
            },
            '2.0.0': {
              label: 'Version 2.0.0',
              path: '2.0.0',
              // Documentation for version 2.0.0
              lastUpdatedAt: '2023-06-01T00:00:00Z',
            },
          },
          // Other options...
        },
        blog: false, // Disable blog if not required
        pages: false, // Disable pages if not required
      },
    ],
  ],
};
```

```javascript
// sidebars.js

module.exports = {
  // Define sidebars for different versions
  docs: {
    'Getting Started': ['getting-started'],
    'Version 1.0.0': [
      {
        type: 'category',
        label: 'Version 1.0.0',
        items: ['1.0.0/introduction', '1.0.0/feature1', '1.0.0/feature2'],
      },
    ],
    'Version 2.0.0': [
      {
        type: 'category',
        label: 'Version 2.0.0',
        items: ['2.0.0/introduction', '2.0.0/feature1', '2.0.0/feature2'],
      },
    ],
  },
};
```

```markdown
# Create documentation files for each version

## Directory Structure
# docs/
# ├── 1.0.0/
# │   ├── introduction.md
# │   ├── feature1.md
# │   └── feature2.md
# └── 2.0.0/
#     ├── introduction.md
#     ├── feature1.md
#     └── feature2.md
```

```markdown
<!-- Example content for introduction.md -->

# Introduction

This document provides an overview of the software and its features for version 1.0.0.

## Getting Started

To install the software, use the following command:

```bash
npm install my-software
```
```

```markdown
<!-- Example content for feature1.md -->

# Feature 1

Feature 1 provides the ability to do X. 

## Usage Example

```javascript
const feature1 = require('my-software/feature1');
feature1.doSomething();
```
```

```bash
# Build your Docusaurus site
npm run build

# Serve the site locally
npm run serve
```

### Note:
Ensure that your documentation files are named and structured correctly to align with the versioning defined in the configuration. Each version should have its own dedicated directory within the `docs` folder.
