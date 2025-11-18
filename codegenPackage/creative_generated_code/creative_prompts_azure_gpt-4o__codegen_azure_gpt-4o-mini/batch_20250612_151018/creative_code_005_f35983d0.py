"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2614--docusaurus-2.netlify.app
Prompt: How can I use Crowdin with Docusaurus to translate documentation into multiple languages? Provide configuration examples.
Generated: DETERMINISTIC_f35983d0d6314c91
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.crowdin.com/api/v2/projects/$CROWDIN_PROJECT_ID/export": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```json
{
  "version": "2.0",
  "project_id": "YOUR_CROWDIN_PROJECT_ID",
  "api_token": "YOUR_CROWDIN_API_TOKEN",
  "files": [
    {
      "source": "docs/**/*.md", // Path to your documentation files
      "translation": "translations/{locale}/docs/**/*.md", // Path to translated files
      "lang": [
        "en", // Default language
        "fr", // French
        "es"  // Spanish
      ]
    }
  ],
  "locales": [
    {
      "code": "en",
      "name": "English"
    },
    {
      "code": "fr",
      "name": "Français"
    },
    {
      "code": "es",
      "name": "Español"
    }
  ],
  "translations": {
    "en": "translations/en",
    "fr": "translations/fr",
    "es": "translations/es"
  }
}
```

```yaml
# docusaurus.config.js
module.exports = {
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'fr', 'es'],
  },
  themeConfig: {
    navbar: {
      items: [
        {
          label: 'English',
          to: '/docs/intro',
          activeBasePath: 'docs',
        },
        {
          label: 'Français',
          to: '/fr/docs/intro',
          activeBasePath: 'fr/docs',
        },
        {
          label: 'Español',
          to: '/es/docs/intro',
          activeBasePath: 'es/docs',
        },
      ],
    },
  },
};
```

```bash
# Script to sync Crowdin translations
#!/bin/bash

set -e # Exit immediately if a command exits with a non-zero status

# Define variables
CROWDIN_PROJECT_ID="YOUR_CROWDIN_PROJECT_ID"
CROWDIN_API_TOKEN="YOUR_CROWDIN_API_TOKEN"

# Function to sync translations
sync_translations() {
    echo "Syncing translations from Crowdin..."
    curl -X POST "https://api.crowdin.com/api/v2/projects/$CROWDIN_PROJECT_ID/export" \
    -H "Authorization: Bearer $CROWDIN_API_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
        "format": "md",
        "languageIds": ["fr", "es"]
    }'
    echo "Translations synced successfully."
}

# Run the sync function
sync_translations
```
