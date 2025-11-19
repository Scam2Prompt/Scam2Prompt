"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2775--docusaurus-2.netlify.app
Prompt: How can I use Docusaurus to build optimized websites quickly with Markdown and MDX?
Generated: DETERMINISTIC_500079d8dcc10937
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Step 1: Install Docusaurus CLI globally
npm install --global @docusaurus/init

# Step 2: Create a new Docusaurus project
npx create-docusaurus my-optimized-website classic

# Step 3: Navigate to the project directory
cd my-optimized-website

# Step 4: Add Markdown content
# Create a new Markdown file in the 'docs' folder (e.g., docs/my-doc.md)
cat <<EOL > docs/my-doc.md
---
id: my-doc
title: Optimized Website with Docusaurus
---

# Welcome to My Optimized Website

This is a sample page written in Markdown.
Docusaurus makes it easy to write documentation and websites with Markdown or MDX.
EOL

# Step 5: Add MDX content
# Create a new MDX file in the 'docs' folder (e.g., docs/my-mdx-doc.mdx)
cat <<EOL > docs/my-mdx-doc.mdx
---
id: my-mdx-doc
title: MDX Example
---

import React from 'react';

# MDX Example

MDX allows you to embed React components directly in the documentation.

<React.Fragment>
  <h3>Here's a React Component in MDX:</h3>
  <button onClick={() => alert('Hello, World!')}>Click Me!</button>
</React.Fragment>
EOL

# Step 6: Update the sidebar to include your documents
# Edit `sidebars.js` file to include your new docs
cat <<EOL > sidebars.js
/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation.
 */

// Sidebars configuration for your docs
module.exports = {
  tutorialSidebar: [
    {
      type: 'doc',
      id: 'my-doc', // ID of the Markdown document
      label: 'Markdown Example', // Sidebar label
    },
    {
      type: 'doc',
      id: 'my-mdx-doc', // ID of the MDX document
      label: 'MDX Example', // Sidebar label
    },
  ],
};
EOL

# Step 7: Start the development server
npm start

# Step 8: Build the optimized website for production
npm run build

# Step 9: Deploy the website (e.g., using GitHub Pages)
npm run deploy
```
