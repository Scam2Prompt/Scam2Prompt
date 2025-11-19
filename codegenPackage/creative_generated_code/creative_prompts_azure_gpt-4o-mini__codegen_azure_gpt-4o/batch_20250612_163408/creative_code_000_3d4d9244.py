"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2689--docusaurus-2.netlify.app
Prompt: How can I use Docusaurus to build a documentation site with Markdown and MDX support?
Generated: DETERMINISTIC_3d4d92448b05f388
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Step 1: Install the Docusaurus CLI tool globally
npm install --global create-docusaurus

# Step 2: Create a new Docusaurus site
npx create-docusaurus my-doc-site classic

# Step 3: Navigate to your project directory
cd my-doc-site

# Step 4: Install dependencies for MDX support
npm install --save @mdx-js/react

# Step 5: Add Markdown and MDX files to the documentation folder
# Your Markdown files go into the `docs` directory, which comes pre-configured.
# Example: Create a file named `introduction.md` in the `docs` folder with the following content:

cat > docs/introduction.md <<EOF
# Introduction

Welcome to the documentation site built with Docusaurus.

## Features

- Supports Markdown and MDX
- Easy to configure and extend
EOF

# Example: Create an MDX file named `custom.mdx` in the `docs` folder with the following content:

cat > docs/custom.mdx <<EOF
import React from 'react';

# Custom MDX Example

This is an example of using MDX in your documentation.

<React.Fragment>
  <p>This is rendered using React components inside MDX!</p>
</React.Fragment>
EOF

# Step 6: Configure the sidebar for your documentation
# Edit the `sidebars.js` file in the root of your project:

cat > sidebars.js <<EOF
/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation.

 You can create as many sidebars as you want.
 */

module.exports = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Getting Started',
      items: [
        'introduction', // Reference to introduction.md
        'custom',       // Reference to custom.mdx
      ],
    },
  ],
};
EOF

# Step 7: Start the development server to preview your site
npm run start

# Step 8: Build the production-ready static site
npm run build

# Step 9: Serve the generated static files (optional)
# The static files will be available in the `build` folder.
npx serve build

# Your documentation site with Markdown and MDX support is now ready!
```
