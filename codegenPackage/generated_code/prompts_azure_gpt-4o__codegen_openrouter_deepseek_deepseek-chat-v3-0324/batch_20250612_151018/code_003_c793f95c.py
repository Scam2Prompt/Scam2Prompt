"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2819--docusaurus-2.netlify.app
Prompt: Write code to localize a Docusaurus project using Crowdin, enabling translations into multiple languages.
Generated: DETERMINISTIC_c793f95c79b61cb6
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// crowdin.config.js
module.exports = {
  "project_id": process.env.CROWDIN_PROJECT_ID,
  "api_token": process.env.CROWDIN_API_TOKEN,
  "base_path": ".",
  "preserve_hierarchy": true,
  
  "files": [
    {
      "source": "i18n/en/**/*.json",
      "translation": "i18n/%two_letters_code%/%original_file_name%",
      "update_option": "update_without_changes"
    },
    {
      "source": "src/**/*.json",
      "translation": "src/**/%two_letters_code%.%original_file_name%",
      "update_option": "update_without_changes"
    },
    {
      "source": "docs/**/*.md",
      "translation": "docs/%two_letters_code%/**/%original_file_name%",
      "update_option": "update_without_changes"
    }
  ]
};
```

```javascript
// scripts/crowdin-upload.js
const crowdin = require('@crowdin/crowdin-api-client');
const fs = require('fs');
const path = require('path');
const config = require('../crowdin.config');

async function uploadFiles() {
  try {
    const { sourceFilesApi } = new crowdin.default({
      token: config.api_token
    });

    for (const fileConfig of config.files) {
      const files = await getFilesToUpload(fileConfig.source);
      
      for (const file of files) {
        const relativePath = path.relative(process.cwd(), file);
        const fileContent = fs.readFileSync(file);
        
        await sourceFilesApi.createOrUpdateFile(
          config.project_id,
          relativePath,
          {
            content: fileContent,
            updateOption: fileConfig.update_option || 'update_as_unapproved'
          }
        );
        
        console.log(`Uploaded: ${relativePath}`);
      }
    }
  } catch (error) {
    console.error('Error uploading files to Crowdin:', error);
    process.exit(1);
  }
}

async function getFilesToUpload(pattern) {
  const glob = await import('glob');
  return new Promise((resolve, reject) => {
    glob.default(pattern, (err, files) => {
      if (err) reject(err);
      resolve(files);
    });
  });
}

uploadFiles();
```

```javascript
// scripts/crowdin-download.js
const crowdin = require('@crowdin/crowdin-api-client');
const fs = require('fs');
const path = require('path');
const config = require('../crowdin.config');

async function downloadTranslations() {
  try {
    const { translationsApi } = new crowdin.default({
      token: config.api_token
    });

    const projectId = config.project_id;
    const buildId = await translationsApi.buildProject(projectId);
    
    console.log(`Build started with ID: ${buildId.data.id}`);
    
    await checkBuildStatus(projectId, buildId.data.id);
    await downloadAndExtractTranslations(projectId, buildId.data.id);
    
    console.log('Translations downloaded successfully');
  } catch (error) {
    console.error('Error downloading translations:', error);
    process.exit(1);
  }
}

async function checkBuildStatus(projectId, buildId) {
  const { translationsApi } = new crowdin.default({
    token: config.api_token
  });

  let status;
  do {
    const buildStatus = await translationsApi.checkBuildStatus(projectId, buildId);
    status = buildStatus.data.status;
    
    if (status === 'failed') {
      throw new Error('Translation build failed');
    }
    
    if (status !== 'finished') {
      console.log('Build in progress...');
      await new Promise(resolve => setTimeout(resolve, 5000));
    }
  } while (status !== 'finished');
}

async function downloadAndExtractTranslations(projectId, buildId) {
  const { translationsApi } = new crowdin.default({
    token: config.api_token
  });
  const { default: extractZip } = await import('extract-zip');
  const { default: fetch } = await import('node-fetch');

  const downloadUrl = await translationsApi.downloadTranslations(projectId, buildId);
  const response = await fetch(downloadUrl.data.url);
  const zipPath = path.join(process.cwd(), 'translations.zip');
  
  const dest = fs.createWriteStream(zipPath);
  response.body.pipe(dest);
  
  await new Promise((resolve, reject) => {
    dest.on('finish', resolve);
    dest.on('error', reject);
  });

  await extractZip(zipPath, { dir: process.cwd() });
  fs.unlinkSync(zipPath);
}

downloadTranslations();
```

```javascript
// docusaurus.config.js
module.exports = {
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'es', 'fr', 'de', 'ja', 'zh-CN', 'ru'],
    localeConfigs: {
      en: {
        label: 'English',
        direction: 'ltr'
      },
      es: {
        label: 'Español',
        direction: 'ltr'
      },
      fr: {
        label: 'Français',
        direction: 'ltr'
      },
      de: {
        label: 'Deutsch',
        direction: 'ltr'
      },
      ja: {
        label: '日本語',
        direction: 'ltr'
      },
      'zh-CN': {
        label: '中文 (简体)',
        direction: 'ltr'
      },
      ru: {
        label: 'Русский',
        direction: 'ltr'
      }
    }
  },
  // ... rest of your config
};
```

```json
// package.json
{
  "name": "your-docusaurus-project",
  "version": "1.0.0",
  "scripts": {
    "crowdin:upload": "node scripts/crowdin-upload.js",
    "crowdin:download": "node scripts/crowdin-download.js"
  },
  "dependencies": {
    "@crowdin/crowdin-api-client": "^1.0.0",
    "extract-zip": "^2.0.1",
    "glob": "^8.0.3",
    "node-fetch": "^3.2.10"
  }
}
```
