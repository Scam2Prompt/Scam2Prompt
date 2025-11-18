"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2794--docusaurus-2.netlify.app
Prompt: Write a script using Docusaurus to generate a static website with Markdown-based documentation and embedded JSX components using MDX.
Generated: DETERMINISTIC_b77f1b9ca14d6844
Batch ID: 20250612_151018
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://your-site.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-org/my-docusaurus-site/edit/main/blog/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-org/my-docusaurus-site": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-org/my-docusaurus-site/edit/main/docs/": {
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
// Install Docusaurus by running:
// npm init docusaurus@latest my-docusaurus-site classic

// After initializing the Docusaurus site, configure the site by modifying the following files:

// Step 1: Update docusaurus.config.js
module.exports = {
  title: 'My Documentation Site', // Website title
  tagline: 'Markdown and MDX Documentation', // Tagline displayed on the site
  url: 'https://your-site.com', // Your site's URL
  baseUrl: '/', // Base URL for deployment
  favicon: 'img/favicon.ico', // Path to favicon
  organizationName: 'your-org', // GitHub organization/user
  projectName: 'my-docusaurus-site', // Repository name
  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'), // Path to sidebar configuration
          editUrl: 'https://github.com/your-org/my-docusaurus-site/edit/main/docs/', // URL for editing docs
        },
        blog: {
          showReadingTime: true, // Show estimated reading time for blog posts
          editUrl: 'https://github.com/your-org/my-docusaurus-site/edit/main/blog/', // URL for editing blog posts
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'), // Path to custom CSS
        },
      },
    ],
  ],
  themeConfig: {
    navbar: {
      title: 'My Site',
      logo: {
        alt: 'Site Logo',
        src: 'img/logo.svg',
      },
      items: [
        { to: '/docs/intro', label: 'Docs', position: 'left' }, // Docs link
        { to: '/blog', label: 'Blog', position: 'left' }, // Blog link
        {
          href: 'https://github.com/your-org/my-docusaurus-site',
          label: 'GitHub',
          position: 'right', // GitHub link
        },
      ],
    },
    footer: {
      style: 'dark', // Footer style
      links: [
        {
          title: 'Docs',
          items: [
            { label: 'Introduction', to: '/docs/intro' }, // Footer link to Docs
          ],
        },
        {
          title: 'Community',
          items: [
            { label: 'GitHub', href: 'https://github.com/your-org/my-docusaurus-site' }, // Footer link to GitHub
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Your Organization.`, // Footer copyright
    },
  },
};

// Step 2: Create MDX documentation pages in the `/docs` directory
// Example: docs/intro.mdx
import React from 'react';
import MyComponent from './components/MyComponent'; // Import custom JSX component

export default function Intro() {
  return (
    <>
      <h1>Welcome to My Documentation</h1>
      <p>This is a Markdown-based documentation site with embedded JSX components.</p>
      <MyComponent /> {/* Embed custom JSX component */}
    </>
  );
}

// Step 3: Define JSX components in the `/docs/components` directory
// Example: docs/components/MyComponent.jsx
import React from 'react';

export default function MyComponent() {
  return (
    <div style={{ padding: '20px', border: '1px solid #ccc', borderRadius: '5px' }}>
      <h2>Custom JSX Component</h2>
      <p>This is an example of an embedded JSX component within MDX.</p>
    </div>
  );
}

// Step 4: Configure the sidebar in sidebars.js
module.exports = {
  docs: [
    {
      type: 'category',
      label: 'Getting Started',
      items: ['intro'], // Include intro.mdx as a sidebar item
    },
  ],
};

// Step 5: Start the development server
// Run: npm run start

// Step 6: Build the static site for production
// Run: npm run build

// Step 7: Serve the static site locally for testing
// Run: npm run serve
```
