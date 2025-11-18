"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2735--docusaurus-2.netlify.app
Prompt: Create a Docusaurus configuration file that integrates Algolia for documentation search functionality.
Generated: DETERMINISTIC_d426fa9d8c0e146f
Batch ID: 20250612_151018
URLs Found: 3
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
  "https://your-domain.com": {
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
// @ts-check

// This is a Docusaurus configuration file that integrates Algolia for documentation search functionality.
// Ensure you have the correct Algolia App ID and API Key before deployment.

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Your Project Title',
  tagline: 'Your Project Tagline',
  url: 'https://your-domain.com', // Your site's domain
  baseUrl: '/', // Base URL for your site
  onBrokenLinks: 'throw', // Throw error on broken links
  onBrokenMarkdownLinks: 'warn', // Warn about broken markdown links
  favicon: 'img/favicon.ico', // Path to your site's favicon

  // Project information
  organizationName: 'your-org', // Your GitHub organization or user name
  projectName: 'your-project', // Repository name for your project

  // Internationalization settings
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  // Presets
  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'), // Path to your sidebar configuration
          editUrl: 'https://github.com/your-org/your-project/edit/main/', // URL for editing docs
        },
        blog: {
          showReadingTime: true, // Display reading time in blog posts
          editUrl: 'https://github.com/your-org/your-project/edit/main/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'), // Path to your custom CSS
        },
      }),
    ],
  ],

  // Theme configuration
  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'Your Project',
        logo: {
          alt: 'Your Logo Alt Text',
          src: 'img/logo.svg', // Path to your logo
        },
        items: [
          { to: 'docs/', label: 'Docs', position: 'left' },
          { to: 'blog', label: 'Blog', position: 'left' },
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
                label: 'Documentation',
                to: '/docs/',
              },
            ],
          },
          {
            title: 'Community',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/your-org/your-project',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'Blog',
                to: '/blog',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Your Project Name.`,
      },
      prism: {
        theme: require('prism-react-renderer/themes/github'),
        darkTheme: require('prism-react-renderer/themes/dracula'),
      },
      // Algolia search configuration
      algolia: {
        appId: 'YOUR_ALGOLIA_APP_ID', // Replace with your Algolia App ID
        apiKey: 'YOUR_ALGOLIA_API_KEY', // Replace with your Algolia API Key
        indexName: 'YOUR_INDEX_NAME', // Replace with your Algolia index name
        contextualSearch: true, // Enable contextual search
        searchParameters: {}, // Additional search parameters (if needed)
      },
    }),
};

module.exports = config;
```
iKey: 'YOUR_ALGOLIA_SEARCH_API_KEY',

      // Index name for your documentation
      indexName: 'YOUR_ALGOLIA_INDEX_NAME',

      // Optional: see https://www.algolia.com/doc/api-reference/widgets/search-box/js/#widget-options
      contextualSearch: true,

      // Optional: Algolia search parameters
      searchParameters: {},

      // Optional: path for search page
      searchPagePath: 'search',
    },
  },

  // Plugins configuration
  plugins: [
    // Add any additional Docusaurus plugins here
  ],
};

module.exports = config;
```
```
