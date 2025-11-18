"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2820--docusaurus-2.netlify.app
Prompt: How can I use Docusaurus to implement document versioning for my project, ensuring that users can access documentation for multiple project releases? Provide code examples.
Generated: DETERMINISTIC_a9f7d52ccf4b250a
Batch ID: 20250612_151018
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/your-repo/docs/edit/main/docs/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-repo": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-docusaurus-url.com": {
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
# Create a new Docusaurus project
npx create-docusaurus@latest my-project classic
cd my-project
```

```js
// my-project/docusaurus.config.js

module.exports = {
  title: 'My Project Documentation',
  tagline: 'Documentation for multiple versions of my project',
  url: 'https://your-docusaurus-url.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onDuplicateRoutes: 'throw',
  presets: [
    [
      'classic',
      {
        docs: {
          // Path to the documentation folder
          path: 'docs',
          routeBasePath: 'docs',
          // Enable versioning
          versions: {
            current: {
              label: 'Latest',
              path: 'latest',
            },
            '1.0.0': {
              label: 'Version 1.0.0',
              path: '1.0.0',
            },
            '2.0.0': {
              label: 'Version 2.0.0',
              path: '2.0.0',
            },
          },
          editUrl:
            'https://github.com/your-repo/docs/edit/main/docs/',
          sidebarPath: require.resolve('./sidebars.js'),
          // Include other Docusaurus options as needed
        },
        // Other presets can be added here
      },
    ],
  ],
  themeConfig: {
    // Set your theme configuration here
    navbar: {
      title: 'My Project',
      items: [
        {to: '/docs', label: 'Docs', position: 'left'},
        {
          to: '/versions',
          label: 'Versions',
          position: 'right',
        },
        {
          href: 'https://github.com/your-repo',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
  },
};
```

```markdown
// my-project/docs/intro.md

---
id: intro
title: Introduction
sidebar_label: Introduction
---

# Welcome to My Project Documentation

This documentation provides details about different versions of our project.

## Available Versions

- [Version 1.0.0](./1.0.0/intro)
- [Version 2.0.0](./2.0.0/intro)
```

```markdown
// my-project/docs/1.0.0/intro.md

---
id: version-1.0.0-intro
title: Version 1.0.0
sidebar_label: Version 1.0.0
---

# Version 1.0.0 Documentation

This is the documentation for version 1.0.0 of the project. Refer to this if you're using this release.
```

```markdown
// my-project/docs/2.0.0/intro.md

---
id: version-2.0.0-intro
title: Version 2.0.0
sidebar_label: Version 2.0.0
---

# Version 2.0.0 Documentation

This is the documentation for version 2.0.0 of the project. Refer to this if you're using this release.
```

```bash
# Start the Docusaurus development server
npm run start
```

```bash
# Build the documentation for production
npm run build
```

```bash
# Serve the built documentation
npm run serve
```

```bash
# To handle errors when building, ensure you have proper checks in place
# Example: Check if 'docs' directory exists before building
if [ ! -d "docs" ]; then
  echo "Docs folder does not exist. Please create it before building."
  exit 1
fi
```
