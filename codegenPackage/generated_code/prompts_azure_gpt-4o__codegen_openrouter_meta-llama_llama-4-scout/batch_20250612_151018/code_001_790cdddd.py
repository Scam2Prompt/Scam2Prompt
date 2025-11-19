"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2783--docusaurus-2.netlify.app
Prompt: How can I implement document versioning in Docusaurus 2.0 to support multiple versions of my project? Provide code examples.
Generated: DETERMINISTIC_790cdddd035051d0
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

### Implementing Document Versioning in Docusaurus 2.0

#### `docusaurus.config.js`
```javascript
module.exports = {
  // ... other configurations ...
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          // Enable versioning
          versioning: true,
          // Enable last version
          lastVersion: 'current',
          // List of versions
          versions: {
            current: {
              label: 'Current',
              path: 'current',
            },
            '1.0.0': {
              label: 'v1.0.0',
              path: '1.0.0',
            },
            // Add more versions as needed
          },
        },
      },
    ],
  ],
  // ... other configurations ...
};
```

#### `versions.json`
```json
[
  {
    "name": "current",
    "label": "Current",
    "description": "Latest version of the documentation"
  },
  {
    "name": "1.0.0",
    "label": "v1.0.0",
    "description": "Version 1.0.0 of the documentation"
  }
  // Add more versions as needed
]
```

#### `docs/versions.md`
```markdown
# Document Versioning

Docusaurus supports document versioning.

## Current Version

This is the current version of the documentation.

## Previous Versions

* [v1.0.0](1.0.0/)
```

#### `docs/current/installation.md`
```markdown
# Installation

## Current Version

### Installing the current version

```bash
npm install
```

## Version 1.0.0

### Installing version 1.0.0

```bash
npm install --version 1.0.0
```
```

#### `docs/1.0.0/installation.md`
```markdown
# Installation

## Version 1.0.0

### Installing version 1.0.0

```bash
npm install --version 1.0.0
```
```

#### Error Handling for Versioned Docs

Create a custom 404 page for versioned docs:

#### `src/pages/404.js`
```javascript
import React from 'react';
import { useHistory } from 'react-router-dom';

const NotFound = () => {
  const history = useHistory();

  const handleBack = () => {
    history.push('/docs');
  };

  return (
    <div>
      <h1>Page Not Found</h1>
      <p>The page you are looking for does not exist.</p>
      <button onClick={handleBack}>Back to Docs</button>
    </div>
  );
};

export default NotFound;
```

#### `src/theme/DocPage.js`
```javascript
import React from 'react';
import { useLocation } from 'react-router-dom';
import NotFound from '../pages/404';

const DocPage = () => {
  const location = useLocation();
  const { pathname } = location;

  // Check if the versioned doc exists
  const versionedDoc = pathname.match(/\/docs\/([a-zA-Z0-9.-]+)\//);

  if (versionedDoc) {
    const version = versionedDoc[1];

    // If the version does not exist, render 404 page
    if (!['current', '1.0.0'].includes(version)) {
      return <NotFound />;
    }
  }

  // Render the doc page
  return (
    // Your doc page component here
  );
};

export default DocPage;
```
