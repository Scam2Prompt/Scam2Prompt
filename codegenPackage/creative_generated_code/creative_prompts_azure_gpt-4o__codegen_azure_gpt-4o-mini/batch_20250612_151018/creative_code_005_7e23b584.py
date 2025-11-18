"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2619--docusaurus-2.netlify.app
Prompt: Provide code examples for setting up document versioning in Docusaurus to support multiple versions of a project’s documentation.
Generated: DETERMINISTIC_7e23b584f1848903
Batch ID: 20250612_151018
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/<USERNAME>/<REPO>/edit/main/website/docs/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/<USERNAME>/<REPO>": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://stackoverflow.com/questions/tagged/docusaurus": {
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
  },
  "https://discordapp.com/invite/docusaurus": {
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
  // Basic site configuration
  title: 'My Project Documentation',
  tagline: 'Documentation for my project',
  url: 'https://example.com', // Your website URL
  baseUrl: '/', // Base URL for your project
  onBrokenLinks: 'throw', // Throw an error on broken links
  onDuplicateRoutes: 'warn', // Warn on duplicate routes
  favicon: 'img/favicon.ico', // Path to favicon for your site

  // Preset configurations
  presets: [
    [
      'classic',
      {
        // Configuration for the docs plugin
        docs: {
          routeBasePath: '/', // Set the base path for the documentation
          sidebarPath: require.resolve('./sidebars.js'), // Path to sidebar configuration
          // Enable versioning
          editUrl: 'https://github.com/<USERNAME>/<REPO>/edit/main/website/docs/',
          showLastUpdateTime: true, // Show last update time
          lastVersion: 'current', // Specify the last version of documentation
          versions: {
            current: {
              label: 'Current',
              path: 'current', // Path for the current version
              // Enable versioning for documents
              banner: 'unreleased', // Show banner for unreleased version
            },
            '1.0.0': {
              label: '1.0.0',
              path: '1.0.0', // Path for version 1.0.0
            },
            '2.0.0': {
              label: '2.0.0',
              path: '2.0.0', // Path for version 2.0.0
            },
          },
        },
        // Configuration for the blog plugin
        blog: {
          showReadingTime: true, // Show reading time for blog posts
          // Add other blog configuration options as needed
        },
        // Configuration for the pages plugin
        pages: {},
      },
    ],
  ],

  // Theme configuration
  themes: ['@docusaurus/theme-classic'],

  // Custom scripts or styles
  scripts: [],
  stylesheets: [],

  // Additional configurations
  plugins: [
    // Load a plugin for additional functionality (if needed)
    '@docusaurus/plugin-ideal-image',
  ],

  // Custom theme configurations
  themeConfig: {
    // Navbar configuration
    navbar: {
      title: 'Documentation',
      items: [
        { to: '/', label: 'Home', position: 'left' },
        { to: '/docs/', label: 'Docs', position: 'left' },
        { to: '/blog', label: 'Blog', position: 'left' },
        {
          to: 'https://github.com/<USERNAME>/<REPO>',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    // Footer configuration
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Getting Started',
              to: '/docs/intro',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Stack Overflow',
              href: 'https://stackoverflow.com/questions/tagged/docusaurus',
            },
            {
              label: 'Discord',
              href: 'https://discordapp.com/invite/docusaurus',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
    },
  },

  // Error handling
  errorHandling: {
    // Custom error handling logic can be added here
  },
};
```

```javascript
// sidebars.js

module.exports = {
  // Define the sidebar structure for the documentation
  mySidebar: [
    {
      type: 'category',
      label: 'Getting Started',
      items: [
        'intro', // Path to the introduction document
        'installation', // Path to installation guide
      ],
    },
    {
      type: 'category',
      label: 'API Reference',
      items: [
        'api/overview', // Path to API overview
        'api/endpoints', // Path to API endpoints
      ],
    },
  ],
};
```

```bash
# Example folder structure for versioning
my-project-docs/
├── docusaurus.config.js
├── sidebars.js
└── docs/
    ├── current/
    │   ├── intro.md
    │   ├── installation.md
    │   └── api/
    │       ├── overview.md
    │       └── endpoints.md
    ├── 1.0.0/
    │   ├── intro.md
    │   ├── installation.md
    │   └── api/
    │       ├── overview.md
    │       └── endpoints.md
    └── 2.0.0/
        ├── intro.md
        ├── installation.md
        └── api/
            ├── overview.md
            └── endpoints.md
```

This code sets up a Docusaurus project with versioning capability, proper error handling, and organized sidebar structure for easy navigation.
