"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2792--docusaurus-2.netlify.app
Prompt: Can you provide a code example for setting up Algolia search in a Docusaurus documentation site?
Generated: DETERMINISTIC_d894add0ee251a3a
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
  "https://twitter.com/your-twitter": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://discord.com/invite/your-community": {
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
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// docusaurus.config.js

module.exports = {
  title: 'My Docusaurus Site', // Your site title
  tagline: 'Dinosaurs are cool', // Your tagline
  url: 'https://your-site.com', // Your site's URL
  baseUrl: '/',
  onBrokenLinks: 'throw', // Throw error on broken links
  onBrokenMarkdownLinks: 'warn', // Warn on broken markdown links
  favicon: 'img/favicon.ico', // Path to the favicon
  organizationName: 'your-org', // Your GitHub organization name
  projectName: 'your-project', // Your GitHub project/repo name

  // Theme configuration
  themeConfig: {
    navbar: {
      title: 'My Site',
      logo: {
        alt: 'My Site Logo',
        src: 'img/logo.svg', // Path to your logo
      },
      items: [
        { to: 'docs/', label: 'Docs', position: 'left' },
        { to: 'blog', label: 'Blog', position: 'left' },
        { 
          href: 'https://github.com/your-org/your-project', 
          label: 'GitHub', 
          position: 'right' 
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            { label: 'Getting Started', to: 'docs/' },
            { label: 'API Reference', to: 'docs/api/' },
          ],
        },
        {
          title: 'Community',
          items: [
            { label: 'Discord', href: 'https://discord.com/invite/your-community' },
            { label: 'Twitter', href: 'https://twitter.com/your-twitter' },
          ],
        },
        {
          title: 'More',
          items: [
            { label: 'Blog', to: 'blog' },
            { label: 'GitHub', href: 'https://github.com/your-org/your-project' },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Docusaurus Site.`,
    },
    // Algolia search configuration
    algolia: {
      appId: 'YOUR_ALGOLIA_APP_ID', // Replace with your Algolia app ID
      apiKey: 'YOUR_ALGOLIA_API_KEY', // Replace with your Algolia search-only API key
      indexName: 'YOUR_INDEX_NAME', // Replace with your Algolia index name
      contextualSearch: true, // Enables contextual search
      searchParameters: {}, // Additional search parameters (optional)
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'), // Path to sidebar configuration
        },
        blog: {
          showReadingTime: true, // Show estimated reading time on blog posts
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'), // Path to custom CSS
        },
      },
    ],
  ],
};
```

This code sets up a Docusaurus site and integrates Algolia search. Replace the placeholders (`YOUR_ALGOLIA_APP_ID`, `YOUR_ALGOLIA_API_KEY`, and `YOUR_INDEX_NAME`) with your actual Algolia credentials and index name.
