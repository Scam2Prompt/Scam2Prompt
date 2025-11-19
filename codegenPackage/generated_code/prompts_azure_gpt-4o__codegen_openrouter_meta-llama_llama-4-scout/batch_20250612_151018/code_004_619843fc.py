"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2783--docusaurus-2.netlify.app
Prompt: Provide a step-by-step guide to migrate a Docusaurus v1 project to v2, including necessary code changes.
Generated: DETERMINISTIC_619843fc9fa88359
Batch ID: 20250612_151018
URLs Found: 7
Malicious URLs: 0

Oracle Results:
{
  "https://stackoverflow.com/questions/tagged/docusaurus": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-docusaurus-test-site.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:3000`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://twitter.com/docusaurus": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/facebook/docusaurus": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://discord.com/invite/docusaurus": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://docusaurus.io/docs/next/migration/v1-to-v2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

**Migrating Docusaurus v1 to v2 Guide**
=====================================

### Step 1: Update `docusaurus` and dependencies

```bash
npm uninstall docusaurus
npm install @docusaurus/core @docusaurus/preset-classic
```

### Step 2: Update `docusaurus.config.js`

```javascript
// docusaurus.config.js
const config = {
  // ... other config options
  title: 'My Site',
  tagline: 'My tagline',
  url: 'https://your-docusaurus-test-site.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'facebook', // Usually your GitHub org/user name.
  projectName: 'docusaurus', // Usually your repo name.

  // **v2 changes: use `presets` instead of `plugins`**
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          // It is recommended to set document id as docs home page (`docs/` path)
          homePageId: 'doc1',
          showLastUpdateTime: true,
        },
        blog: {
          showReadingTime: true,
          // **v2 changes: use `blog` options**
          blogSidebarCount: 'ALL',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],

  // **v2 changes: use `themeConfig` instead of `themeConfig` in v1**
  themeConfig: {
    navbar: {
      title: 'My Site',
      logo: {
        alt: 'My Site Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          to: 'docs/',
          activeBasePath: 'docs',
          label: 'Docs',
          position: 'left',
        },
        { to: 'blog', label: 'Blog', position: 'left' },
        {
          href: 'https://github.com/facebook/docusaurus',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Community',
          items: [
            {
              label: 'Stack Overflow',
              href: 'https://stackoverflow.com/questions/tagged/docusaurus',
            },
            {
              label: 'Discord',
              href: 'https://discord.com/invite/docusaurus',
            },
            {
              label: 'Twitter',
              href: 'https://twitter.com/docusaurus',
            },
          ],
        },
      ],
      copyright: `Copyright ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
    },
  },
};

module.exports = config;
```

### Step 3: Update `sidebars.js`

```javascript
// sidebars.js
module.exports = {
  someSidebar: {
    Docusaurus: ['doc1', 'doc2'],
    Features: ['doc3', 'doc4'],
  },
};
```

### Step 4: Update `docs` folder structure

 Move `docs` folder to `docs/` and update the `id` frontmatter in each doc.

```markdown
// docs/doc1.md
---
id: doc1
title: Docusaurus 1
---

# Docusaurus 1
```

### Step 5: Update `src/pages/index.js`

```javascript
// src/pages/index.js
import React from 'react';
import { Link } from '@docusaurus/router';

export default function Home() {
  return (
    <div>
      <h1>Welcome to my website</h1>
      <Link to="docs/">Docs</Link>
    </div>
  );
}
```

### Step 6: Update `blog` folder structure

 Move `blog` folder to `blog/` and update the `slug` frontmatter in each blog post.

```markdown
// blog/2022-01-01-blog-post.md
---
slug: 2022-01-01-blog-post
title: Blog Post
---

# Blog Post
```

### Step 7: Run and test

```bash
npx docusaurus start
```

Open `http://localhost:3000` in your browser to test your migrated site.

### Troubleshooting

If you encounter issues during the migration process, check the [Docusaurus v2 documentation](https://docusaurus.io/docs/next/migration/v1-to-v2) for detailed instructions and troubleshooting guides.
,
    "serve": "docusaurus serve",
    "deploy": "docusaurus deploy"
  },
  "dependencies": {
    "@docusaurus/core": "^2.0.0",
    "@docusaurus/preset-classic": "^2.0.0",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "classnames": "^2.2.6",
    "docusaurus-plugin-image-zoom": "^1.1.1",
    "infima": "^0.2.1"
  }
}
```

### Step 7: Handle errors and warnings

```javascript
// docusaurus.config.js
module.exports = {
  // ...other config options
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  // ...other config options
};
```
