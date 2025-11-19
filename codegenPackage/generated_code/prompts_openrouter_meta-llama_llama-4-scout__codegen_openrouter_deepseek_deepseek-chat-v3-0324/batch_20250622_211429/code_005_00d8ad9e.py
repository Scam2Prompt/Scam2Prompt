"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2809--docusaurus-2.netlify.app
Prompt: Write a Docusaurus migration guide from version 1 to version 2, highlighting key changes and updates.
Generated: DETERMINISTIC_00d8ad9e57ad33b4
Batch ID: 20250622_211429
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://docusaurus.io/docs/migration": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/facebook/docusaurus/discussions": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://docusaurus.io/docs": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```markdown
---
title: Docusaurus Migration Guide (v1 to v2)
description: Step-by-step guide to migrate from Docusaurus v1 to v2
---

# Docusaurus Migration Guide (v1 to v2)

## Prerequisites

- Node.js v16.14 or later
- Existing Docusaurus v1 project
- Backup of your current project

## Step 1: Update Dependencies

```bash
# Remove old Docusaurus packages
npm uninstall docusaurus --save

# Install new Docusaurus v2 packages
npm install --save @docusaurus/core@latest @docusaurus/preset-classic@latest
```

## Step 2: Update Configuration

### Old `siteConfig.js` (v1) to `docusaurus.config.js` (v2)

```javascript
// v1: siteConfig.js
module.exports = {
  title: 'My Site',
  tagline: 'The tagline of my site',
  // ... other config
};

// v2: docusaurus.config.js
module.exports = {
  title: 'My Site',
  tagline: 'The tagline of my site',
  themeConfig: {
    // Moved navbar, footer, etc. here
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          // Docs plugin options
        },
        blog: {
          // Blog plugin options
        },
      },
    ],
  ],
};
```

## Step 3: Migrate Docs Structure

### v1 Structure
```
docs/
  doc1.md
  doc2.md
  subdir/
    doc3.md
```

### v2 Structure
```
docs/
  intro.md          # Homepage for docs
  getting-started/  # Subfolder becomes a category
    installation.md
    configuration.md
  advanced/
    api.md
```

## Step 4: Update Front Matter

```markdown
# v1 front matter
---
id: my-doc
title: My Document
---

# v2 front matter
---
id: my-doc
title: My Document
sidebar_label: Custom Label
slug: /custom-path
---
```

## Step 5: Migrate Blog

### v1 Blog
```
blog/
  2019-05-28-first-blog-post.md
```

### v2 Blog
```
blog/
  2021-01-01-new-blog-post.md
  first-blog-post.md    # No date prefix needed
```

## Step 6: Update Custom Styles

```javascript
// v1: siteConfig.js
stylesheets: [
  '/css/custom.css'
]

// v2: docusaurus.config.js
stylesheets: [
  '/css/custom.css'
]
```

## Step 7: Run Migration Checks

```bash
# Start the development server to verify
npx docusaurus start

# Build the project
npx docusaurus build
```

## Common Issues

1. **Broken Links**: Use `yarn build --broken-links` to check
2. **Deprecated APIs**: Check console warnings during build
3. **CSS Conflicts**: Isolate v1 styles and migrate gradually

## Final Steps

1. Update deployment configuration if needed
2. Test all documentation pages
3. Verify search functionality
4. Check mobile responsiveness

## Additional Resources

- [Official Migration Guide](https://docusaurus.io/docs/migration)
- [v2 Documentation](https://docusaurus.io/docs)
- [GitHub Discussions](https://github.com/facebook/docusaurus/discussions)
```
