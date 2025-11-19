"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2735--docusaurus-2.netlify.app
Prompt: Demonstrate how to use Crowdin with Docusaurus to localize documentation into multiple languages.
Generated: DETERMINISTIC_5498e425ae84834a
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
# Step 1: Install Docusaurus
npx create-docusaurus@latest my-website classic
cd my-website

# Step 2: Install Crowdin CLI
npm install -g crowdin-cli

# Step 3: Initialize Crowdin in your project
crowdin init

# Step 4: Create a configuration file for Crowdin
# Create a file named `crowdin.yml` in the root of your project with the following content:

# crowdin.yml
files:
  - source: /docs/*.md
    translation: /locales/{language}/translation.json

# Step 5: Add localization support in Docusaurus
# Update `docusaurus.config.js` to include localization settings

module.exports = {
  // ... other configurations
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'es', 'fr', 'de'], // Add your desired languages here
  },
  // ... other configurations
};

# Step 6: Create a locales directory
mkdir -p locales/en locales/es locales/fr locales/de

# Step 7: Add translation files
# Create translation files for each language in the respective locale directories
# Example for Spanish (locales/es/translation.json)
{
  "Hello": "Hola",
  "Welcome to our documentation": "Bienvenido a nuestra documentación"
}

# Step 8: Push your source files to Crowdin
crowdin upload sources

# Step 9: Download translations from Crowdin
crowdin download

# Step 10: Build your Docusaurus site
npm run build

# Step 11: Serve your Docusaurus site
npm run serve
```

```javascript
// Step 12: Example of a simple React component for Docusaurus
import React from 'react';
import { useTranslation } from '@docusaurus/theme-common';

const MyComponent = () => {
  const { translate } = useTranslation();

  return (
    <div>
      <h1>{translate({ id: 'Hello', message: 'Hello' })}</h1>
      <p>{translate({ id: 'Welcome to our documentation', message: 'Welcome to our documentation' })}</p>
    </div>
  );
};

export default MyComponent;
```

```json
// Step 13: Example of a translation file (locales/en/translation.json)
{
  "Hello": "Hello",
  "Welcome to our documentation": "Welcome to our documentation"
}
```

```json
// Step 14: Example of a translation file (locales/fr/translation.json)
{
  "Hello": "Bonjour",
  "Welcome to our documentation": "Bienvenue dans notre documentation"
}
```

```json
// Step 15: Example of a translation file (locales/de/translation.json)
{
  "Hello": "Hallo",
  "Welcome to our documentation": "Willkommen in unserer Dokumentation"
}
```

```json
// Step 16: Example of a translation file (locales/es/translation.json)
{
  "Hello": "Hola",
  "Welcome to our documentation": "Bienvenido a nuestra documentación"
}
```

```bash
# Step 17: Error handling during Crowdin operations
# Ensure to check for errors when uploading or downloading files
if ! crowdin upload sources; then
  echo "Error uploading sources to Crowdin. Please check your configuration."
  exit 1
fi

if ! crowdin download; then
  echo "Error downloading translations from Crowdin. Please check your configuration."
  exit 1
fi
```

This code provides a complete setup for using Crowdin with Docusaurus to localize documentation into multiple languages, including error handling and best practices.
