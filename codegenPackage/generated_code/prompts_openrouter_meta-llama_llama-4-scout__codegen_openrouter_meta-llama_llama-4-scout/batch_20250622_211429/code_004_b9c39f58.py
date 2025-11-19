"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2820--docusaurus-2.netlify.app
Prompt: Provide a step-by-step guide on migrating a Docusaurus site from version 1 to version 2.
Generated: DETERMINISTIC_b9c39f58d33a814b
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Migrating Docusaurus Site from v1 to v2**
=============================================

### Step 1: Update `docusaurus` and `@docusaurus/core` packages

```bash
npm install docusaurus@latest @docusaurus/core@latest
```

### Step 2: Update `docusaurus.config.js` file

```javascript
// docusaurus.config.js (v2)
module.exports = {
  // ... other config options ...
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        // ... preset options ...
      },
    ],
  ],
  themeConfig: {
    // ... theme config options ...
  },
};
```

### Step 3: Update `sidebars.js` file (if using)

```javascript
// sidebars.js (v2)
module.exports = {
  someSidebar: {
    // ... sidebar items ...
  },
};
```

### Step 4: Update Markdown files to use `MDX` syntax (if using)

```markdown
// example.md (v2)
import React from 'react';

## Example Heading

This is an example paragraph.

### Code block example

```jsx
import React from 'react';

function ExampleCode() {
  return <div>Hello World!</div>;
}
```

### Step 5: Update `docs` directory structure (if necessary)

 Move files to a new directory structure if necessary.

### Step 6: Run the Docusaurus site

```bash
npx docusaurus start
```

### Automated Migration Script

```javascript
// migrate-docusaurus.js
const fs = require('fs');
const path = require('path');

const migrateDocusaurus = async () => {
  try {
    // Update docusaurus and @docusaurus/core packages
    console.log('Updating packages...');
    await execCommand('npm', ['install', 'docusaurus@latest', '@docusaurus/core@latest']);

    // Update docusaurus.config.js file
    console.log('Updating docusaurus.config.js...');
    const configFile = path.join(process.cwd(), 'docusaurus.config.js');
    const configContent = fs.readFileSync(configFile, 'utf8');
    const updatedConfigContent = configContent.replace(
      /module\.exports\s*=\s*{/,
      'module.exports = {\n  presets: [\n    ["@docusaurus/preset-classic"],\n  ],\n  themeConfig: {\n    // ... theme config options ...\n  },'
    );
    fs.writeFileSync(configFile, updatedConfigContent);

    // Update sidebars.js file (if using)
    const sidebarsFile = path.join(process.cwd(), 'sidebars.js');
    if (fs.existsSync(sidebarsFile)) {
      console.log('Updating sidebars.js...');
      const sidebarsContent = fs.readFileSync(sidebarsFile, 'utf8');
      const updatedSidebarsContent = sidebarsContent.replace(
        /module\.exports\s*=\s*{/,
        'module.exports = {\n  someSidebar: {\n    // ... sidebar items ...\n  },'
      );
      fs.writeFileSync(sidebarsFile, updatedSidebarsContent);
    }

    console.log('Migration completed successfully!');
  } catch (error) {
    console.error('Error during migration:', error);
  }
};

const execCommand = (command, args) => {
  return new Promise((resolve, reject) => {
    const childProcess = require('child_process').spawn(command, args);
    childProcess.stdout.on('data', (data) => {
      console.log(`stdout: ${data}`);
    });
    childProcess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
    });
    childProcess.on('close', (code) => {
      if (code === 0) {
        resolve();
      } else {
        reject(new Error(`Command failed with code ${code}`));
      }
    });
  });
};

migrateDocusaurus();
```

### Usage

```bash
node migrate-docusaurus.js
```
