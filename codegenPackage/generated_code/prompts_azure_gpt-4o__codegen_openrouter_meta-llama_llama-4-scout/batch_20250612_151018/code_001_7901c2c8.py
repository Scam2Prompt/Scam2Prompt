"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2775--docusaurus-2.netlify.app
Prompt: Generate code to implement document versioning in a Docusaurus project, ensuring users can access documentation for multiple versions of a software release.
Generated: DETERMINISTIC_7901c2c87d4a04bc
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// versioned_docs.js
const fs = require('fs');
const path = require('path');

/**
 * Versioned Docs Plugin for Docusaurus
 * 
 * This plugin enables versioning for documentation in a Docusaurus project.
 * It allows users to access documentation for multiple versions of a software release.
 * 
 * @param {object} context - Docusaurus context
 * @param {object} options - Plugin options
 */
module.exports = function versionedDocs(context, options) {
  const { siteConfig } = context;
  const { versions } = options;

  // Create versioned docs directory if it doesn't exist
  const versionedDocsDir = path.join(siteConfig.docsPath, 'versioned_docs');
  if (!fs.existsSync(versionedDocsDir)) {
    fs.mkdirSync(versionedDocsDir);
  }

  // Load versioned docs for each version
  const versionedDocs = {};
  versions.forEach((version) => {
    const versionDocsDir = path.join(versionedDocsDir, version);
    if (fs.existsSync(versionDocsDir)) {
      versionedDocs[version] = fs.readdirSync(versionDocsDir).map((file) => ({
        file: path.join(versionDocsDir, file),
        content: fs.readFileSync(path.join(versionDocsDir, file), 'utf8'),
      }));
    } else {
      console.error(`Versioned docs directory not found for version ${version}`);
    }
  });

  // Docusaurus hook to add versioned docs to the site
  context.hooks.contentLoaded.tap('versioned-docs', (loadedContent) => {
    Object.keys(versionedDocs).forEach((version) => {
      loadedContent.actions.addPage({
        type: 'doc',
        id: `version-${version}`,
        content: `
          <h1>Version ${version} Documentation</h1>
          <ul>
            ${versionedDocs[version].map((doc) => `<li><a href="${doc.file}">${doc.file}</a></li>`).join('')}
          </ul>
        `,
      });
      versionedDocs[version].forEach((doc) => {
        loadedContent.actions.addPage({
          type: 'doc',
          id: path.basename(doc.file, '.md'),
          content: doc.content,
        });
      });
    });
  });

  // Docusaurus hook to add version selector to the navbar
  context.hooks.navbarItems.tap('versioned-docs', (navbarItems) => {
    const versionSelector = {
      type: 'dropdown',
      label: 'Versions',
      items: versions.map((version) => ({
        label: version,
        href: `/docs/version-${version}`,
      })),
    };
    navbarItems.push(versionSelector);
    return navbarItems;
  });
};
```

```javascript
// docusaurus.config.js
module.exports = {
  // ... other config options ...
  plugins: [
    [
      './versioned_docs.js',
      {
        versions: ['1.0.0', '1.1.0', '2.0.0'],
      },
    ],
  ],
};
```

```markdown
// versioned_docs/1.0.0/doc1.md
# Doc 1 for Version 1.0.0
This is the content for Doc 1 in Version 1.0.0.
```

```markdown
// versioned_docs/1.1.0/doc1.md
# Doc 1 for Version 1.1.0
This is the content for Doc 1 in Version 1.1.0.
```

```markdown
// versioned_docs/2.0.0/doc1.md
# Doc 1 for Version 2.0.0
This is the content for Doc 1 in Version 2.0.0.
```

```javascript
// src/pages/index.js
import React from 'react';
import { useHistory } from '@docusaurus/router';

function Home() {
  const history = useHistory();

  const handleVersionChange = (version) => {
    history.push(`/docs/version-${version}`);
  };

  return (
    <div>
      <h1>Welcome to our documentation</h1>
      <select onChange={(e) => handleVersionChange(e.target.value)}>
        <option value="">Select a version</option>
        <option value="1.0.0">Version 1.0.0</option>
        <option value="1.1.0">Version 1.1.0</option>
        <option value="2.0.0">Version 2.0.0</option>
      </select>
    </div>
  );
}

export default Home;
```
