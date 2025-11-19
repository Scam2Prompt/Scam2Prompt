"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2735--docusaurus-2.netlify.app
Prompt: How can I implement document versioning in Docusaurus to support multiple versions of my project's documentation? Provide code examples.
Generated: DETERMINISTIC_2fb1fa8a04ddb1f1
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
  //...
  versions: {
    // 'current' is the latest version of your docs
    current: {
      label: 'Latest',
      path: 'latest',
    },
    // Add as many versions as you want here
    '1.0': {
      label: 'v1.0',
      path: 'v1.0',
    },
  },
  //...
};

// Create a new file for versioned docs
// docs/v1.0/_category_.json
{
  "label": "Version 1.0",
  "position": 1,
  "items": [
    {
      "type": "category",
      "label": "Getting Started",
      "items": [
        "v1.0/introduction",
        "v1.0/installation"
      ]
    },
    {
      "type": "category",
      "label": "Tutorials",
      "items": [
        "v1.0/tutorial1",
        "v1.0/tutorial2"
      ]
    }
  ]
}

// docs/latest/_category_.json
{
  "label": "Latest",
  "position": 1,
  "items": [
    {
      "type": "category",
      "label": "Getting Started",
      "items": [
        "latest/introduction",
        "latest/installation"
      ]
    },
    {
      "type": "category",
      "label": "Tutorials",
      "items": [
        "latest/tutorial1",
        "latest/tutorial2"
      ]
    }
  ]
}

// Create a script to automate versioning
// scripts/createVersion.js
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

const createVersion = async (version) => {
  try {
    // Create version directory
    const versionDir = path.join('docs', version);
    fs.mkdirSync(versionDir, { recursive: true });

    // Copy latest docs to version directory
    const latestDir = path.join('docs', 'latest');
    const files = fs.readdirSync(latestDir);
    files.forEach((file) => {
      const filePath = path.join(latestDir, file);
      const stat = fs.statSync(filePath);
      if (stat.isDirectory()) {
        fs.cpSync(filePath, path.join(versionDir, file), { recursive: true });
      } else {
        fs.copyFileSync(filePath, path.join(versionDir, file));
      }
    });

    // Update versioned doc links
    const categoryFile = path.join(versionDir, '_category_.json');
    const categoryContent = fs.readFileSync(categoryFile, 'utf8');
    const updatedContent = categoryContent.replace(/latest/g, version);
    fs.writeFileSync(categoryFile, updatedContent);

    // Commit changes
    exec(`git add ${versionDir}`);
    exec(`git commit -m "Added version ${version}"`);
  } catch (error) {
    console.error(error);
  }
};

createVersion('1.0');
```

```bash
// Add a script to package.json to run the createVersion script
"scripts": {
  "create-version": "node scripts/createVersion.js"
}
```

```markdown
// docs/latest/introduction.md
---
sidebar_position: 1
---

# Introduction
This is the introduction to the latest version of our docs.

## Changes in v1.0
For changes in v1.0, see [v1.0 introduction](/v1.0/introduction).
```

```markdown
// docs/v1.0/introduction.md
---
sidebar_position: 1
---

# Introduction (v1.0)
This is the introduction to v1.0 of our docs.
```
