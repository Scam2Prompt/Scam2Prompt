"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2747--docusaurus-2.netlify.app
Prompt: Provide a guide on setting up localization in Docusaurus using Crowdin for a multi-language documentation site.
Generated: DETERMINISTIC_d19da8999177ef48
Batch ID: 20250612_163408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://myproject.github.io": {
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

// Import necessary modules
const path = require('path');

/**
 * @type {import('@docusaurus/types').Config}
 * Config for Docusaurus documentation site
 */
const config = {
  title: 'My Project Documentation',  // Title of the documentation site
  tagline: 'Documentation for my project',  // Tagline for the site
  url: 'https://myproject.github.io',  // Your website URL
  baseUrl: '/',  // Base URL for your project
  favicon: 'img/favicon.ico',  // Path to favicon
  organizationName: 'myproject',  // GitHub organization/user name
  projectName: 'myproject',  // Repository name
  plugins: [
    // Configuration for the internationalization (i18n) plugin
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'docs',  // ID for this documentation
        path: 'docs',  // Path to your documentation folder
        routeBasePath: 'docs',  // Base path for serving docs
        sidebarPath: require.resolve('./sidebars.js'),  // Path to sidebar configuration
        // Configure localization
        i18n: {
          defaultLocale: 'en',  // Default language
          locales: ['en', 'fr', 'es'],  // Supported languages
        },
      },
    ],
  ],
  themeConfig: {
    // Configure the localization options for the website
    navbar: {
      title: 'My Project',
      items: [
        { to: 'docs/', label: 'Docs', position: 'left' },
        {
          type: 'localeDropdown',  // Dropdown for language selection
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
              label: 'Getting Started',
              to: 'docs/',
            },
            {
              label: 'API Reference',
              to: 'docs/api',
            },
          ],
        },
      ],
    },
  },
};

// Export the configuration object
module.exports = config;

// Crowdin integration setup
/**
 * Crowdin configuration for localization
 * Make sure to set your Crowdin project and API key in the environment variables
 */
const { execSync } = require('child_process');

try {
  execSync('crowdin upload', { stdio: 'inherit' });  // Upload translations to Crowdin
  execSync('crowdin download', { stdio: 'inherit' }); // Download translations from Crowdin
} catch (error) {
  console.error('Error during Crowdin synchronization:', error.message);
  process.exit(1);  // Exit the process with an error code
}
```

```bash
# .env

# Environment variables for Crowdin
CROWDIN_API_KEY=your_crowdin_api_key
CROWDIN_PROJECT_ID=your_crowdin_project_id
```

```json
// crowdin.yml
"project_id": "your_crowdin_project_id",  // Replace with your Crowdin project ID
"api_key": "your_crowdin_api_key",  // Replace with your Crowdin API key
"files": [
  {
    "source": "docs/**/*.md",  // Source files to be localized
    "translation": "/locales/{locale}/",  // Output path for translated files
  }
],
"locales": [
  "en",  // English
  "fr",  // French
  "es"   // Spanish
]
```

Make sure to replace `your_crowdin_api_key` and `your_crowdin_project_id` with your actual Crowdin credentials. 

This setup will allow you to manage localization using Crowdin effectively in your Docusaurus project.
