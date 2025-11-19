"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2757--docusaurus-2.netlify.app
Prompt: Write a configuration file for enabling Crowdin-based localization in a Docusaurus project to support translations into multiple languages.
Generated: DETERMINISTIC_f426434d0ac7dfcd
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// docusaurus.config.js

module.exports = {
  // ... other configurations ...
  i18n: {
    // Enable internationalization
    locale: 'en',
    defaultLocale: 'en',
    // List of locales to be supported
    locales: ['en', 'fr', 'es', 'zh-CN', 'pt-BR'],
    // Enable Crowdin-based localization
    crowdin: {
      // Crowdin project ID
      projectId: 'your-crowdin-project-id',
      // Crowdin API token
      apiToken: 'your-crowdin-api-token',
      // Enable automatic synchronization with Crowdin
      autoSync: true,
      // Update translations on build
      updateTranslations: true,
    },
  },
  // ... other configurations ...
};

// crowdin.yml

crowdin:
  project_id: your-crowdin-project-id
  api_token: your-crowdin-api-token
  languages:
    - id: en
      name: English
    - id: fr
      name: French
    - id: es
      name: Spanish
    - id: zh-CN
      name: Chinese (Simplified)
    - id: pt-BR
      name: Portuguese (Brazil)

module.exports = {
  // Enable Crowdin plugin
  plugins: [
    [
      '@docusaurus/plugin-crowdin',
      {
        // Enable Crowdin-based localization
        crowdin: {
          // Path to Crowdin configuration file
          configPath: 'crowdin.yml',
        },
      },
    ],
  ],
};
```

```yml
# crowdin.yml

project_id: your-crowdin-project-id
api_token: your-crowdin-api-token
file:
  - source: /docs/**/.md
    translation: /docs/**/%locale%/.md
  - source: /src/pages/**/.mdx
    translation: /src/pages/**/%locale%/.mdx
languages:
  - id: en
    name: English
  - id: fr
    name: French
  - id: es
    name: Spanish
  - id: zh-CN
    name: Chinese (Simplified)
  - id: pt-BR
    name: Portuguese (Brazil)
```
