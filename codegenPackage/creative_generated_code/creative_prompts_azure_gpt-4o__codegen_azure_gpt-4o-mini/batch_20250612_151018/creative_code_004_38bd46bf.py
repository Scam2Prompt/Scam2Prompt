"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2803--docusaurus-2.netlify.app
Prompt: How can I use Crowdin with Docusaurus to translate documentation into multiple languages? Provide an example setup.
Generated: DETERMINISTIC_38bd46bfcd664bd2
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Create a new Docusaurus project
npx create-docusaurus@latest my-website classic
cd my-website
```

```bash
# Install necessary dependencies for Crowdin integration
npm install --save @crowdin/crowdin-cli
```

```bash
# Create a configuration file for Crowdin (crowdin.yml)
touch crowdin.yml
```

```yaml
# crowdin.yml
# Crowdin configuration file for managing translations

# Define project settings
project_id: your_project_id_here
api_token: your_api_token_here

# Specify the files for translation
files:
  - source: "/docs/**/*.md"
    translation: "/i18n/{LANG}/docusaurus-plugin-content-docs/*"
    type: "md"

# Define the languages for translation
languages:
  - name: "en"
    code: "en"
  - name: "fr"
    code: "fr"
  - name: "de"
    code: "de"
```

```bash
# Add Crowdin CLI commands to package.json for easy access
# Modify package.json to add scripts

{
  "scripts": {
    "crowdin:upload": "crowdin upload",
    "crowdin:download": "crowdin download"
  }
}
```

```bash
# Create a .crowdin.yaml file for the Crowdin CLI setup
touch .crowdin.yaml
```

```yaml
# .crowdin.yaml
# Configuration for Crowdin CLI

# Specify the project type
project_type: "docusaurus"

# Define the source language
source_language: "en"

# Define file mapping
files:
  - source: "/docs/**/*.md"
    translation: "/i18n/{LANG}/docusaurus-plugin-content-docs/*"
```

```bash
# Setup local environment variables for Crowdin access
# Ensure you have .env file to store sensitive information
touch .env
```

```env
# .env
# Environment variables for Crowdin

CROWDIN_API_TOKEN=your_api_token_here
```

```javascript
// Example of a simple script to manage the translation process

const { exec } = require('child_process');
require('dotenv').config();

const uploadToCrowdin = () => {
  exec('npm run crowdin:upload', (err, stdout, stderr) => {
    if (err) {
      console.error(`Upload failed: ${stderr}`);
      return;
    }
    console.log(`Upload successful: ${stdout}`);
  });
};

const downloadFromCrowdin = () => {
  exec('npm run crowdin:download', (err, stdout, stderr) => {
    if (err) {
      console.error(`Download failed: ${stderr}`);
      return;
    }
    console.log(`Download successful: ${stdout}`);
  });
};

// Execute the upload and download functions
uploadToCrowdin();
downloadFromCrowdin();
```

```bash
# To run the translations, execute the following commands in your terminal
npm run crowdin:upload
npm run crowdin:download
```

```bash
# Finally, build your Docusaurus site
npm run build
```

```bash
# Start the Docusaurus development server to view the translations
npm run start
```
