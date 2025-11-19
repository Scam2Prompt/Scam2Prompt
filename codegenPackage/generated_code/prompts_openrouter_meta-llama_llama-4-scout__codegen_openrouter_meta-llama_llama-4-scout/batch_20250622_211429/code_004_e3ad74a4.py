"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2619--docusaurus-2.netlify.app
Prompt: Develop a localization configuration for a Docusaurus site using Crowdin, and translate a documentation page into multiple languages.
Generated: DETERMINISTIC_e3ad74a452b0026c
Batch ID: 20250622_211429
URLs Found: 7
Malicious URLs: 0

Oracle Results:
{
  "https://api.crowdin.com/api/v2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-github-username/your-project-name/edit/master/website/blog/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your-site-url.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-github-username/your-project-name": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-github-username/your-project-name/edit/master/website/docs/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://twitter.com/your-twitter-handle": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://discord.com/invite/your-discord-invite": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// docusaurus.config.js
module.exports = {
  title: 'My Docusaurus Site',
  tagline: 'A tagline for my site',
  url: 'https://your-site-url.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'your-github-username', // Usually your GitHub org/user name.
  projectName: 'your-project-name', // Usually your repo name.

  // Crowdin configuration
  crowdin: {
    username: 'your-crowdin-username',
    token: 'your-crowdin-token',
    projectId: 'your-crowdin-project-id',
    branch: 'main',
    basePath: 'docs/',
    files: [
      {
        source: 'docs/intro.md',
        translation: [
          {
            locale: 'en',
            file: 'intro.md',
          },
          {
            locale: 'fr',
            file: 'intro.fr.md',
          },
          {
            locale: 'es',
            file: 'intro.es.md',
          },
        ],
      },
    ],
  },

  // i18n configuration
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'fr', 'es'],
  },

  // Theme configuration
  themeConfig: {
    navbar: {
      title: 'My Docusaurus Site',
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
        {
          href: 'https://github.com/your-github-username/your-project-name',
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
              label: 'Discord',
              href: 'https://discord.com/invite/your-discord-invite',
            },
            {
              label: 'Twitter',
              href: 'https://twitter.com/your-twitter-handle',
            },
          ],
        },
      ],
      copyright: `Copyright ${new Date().getFullYear()} My Docusaurus Site, Inc. Built with Docusaurus.`,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          // It is recommended to set document id as strings to support
          // hot reloading without losing your documents' order.
          homePageId: 'doc1',
          showLastUpdateTime: true,
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl: 'https://github.com/your-github-username/your-project-name/edit/master/website/blog/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'docs',
        path: 'docs',
        routeBasePath: '/docs/',
        homePageId: 'doc1',
        sidebarPath: require.resolve('./sidebars.js'),
        // Please change this to your repo.
        editUrl: 'https://github.com/your-github-username/your-project-name/edit/master/website/docs/',
      },
    ],
    [
      '@docusaurus/plugin-crowdin',
      {
        username: 'your-crowdin-username',
        token: 'your-crowdin-token',
        projectId: 'your-crowdin-project-id',
      },
    ],
  ],
};

// scripts/crowdin-sync.js
const axios = require('axios');
const FormData = require('form-data');

const crowdinApiUrl = 'https://api.crowdin.com/api/v2';
const projectId = 'your-crowdin-project-id';
const token = 'your-crowdin-token';

async function uploadFile(file, fileName) {
  try {
    const response = await axios.post(`${crowdinApiUrl}/projects/${projectId}/files`, {
      file: file,
      name: fileName,
    }, {
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
    });
    console.log(`File ${fileName} uploaded successfully`);
  } catch (error) {
    console.error(`Error uploading file ${fileName}: ${error.message}`);
  }
}

async function downloadTranslations(locale) {
  try {
    const response = await axios.get(`${crowdinApiUrl}/projects/${projectId}/translations`, {
      params: {
        localeId: locale,
      },
      headers: {
        'Authorization': `Bearer ${token}`,
      },
    });
    const translations = response.data;
    // Process translations here
    console.log(`Translations downloaded for locale ${locale}`);
  } catch (error) {
    console.error(`Error downloading translations for locale ${locale}: ${error.message}`);
  }
}

// Call the functions
uploadFile('docs/intro.md', 'intro.md');
downloadTranslations('fr');
```

```markdown
// docs/intro.md
---
id: intro
title: Introduction
---

Welcome to my Docusaurus site!
```

```markdown
// docs/intro.fr.md
---
id: intro
title: Introduction
---

Bienvenue sur mon site Docusaurus !
```

```markdown
// docs/intro.es.md
---
id: intro
title: Introducción
---

¡Bienvenido a mi sitio de Docusaurus!
```

```javascript
// sidebars.js
module.exports = {
  someSidebar: {
    Docusaurus: ['doc1', 'doc2'],
    Features: ['doc3', 'doc4'],
  },
};
```
