"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2758--docusaurus-2.netlify.app
Prompt: How can I implement document versioning in Docusaurus to support multiple versions of my project's documentation?
Generated: DETERMINISTIC_a45433724d149213
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
  // ... other config options
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          // Path to your docs
          path: 'docs',
          // Enable versioning
          showLastUpdateTime: true,
          showLastUpdateAuthor: true,
          // Versioning configuration
          versions: {
            current: {
              label: 'Next 🚧',
              path: 'next',
              banner: 'unreleased',
            },
          },
          lastVersion: 'current',
          // Only include in versioned docs
          includeCurrentVersion: true,
          // Disable version dropdown if only one version exists
          disableVersioning: false,
        },
      },
    ],
  ],
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'api',
        path: 'api',
        routeBasePath: 'api',
        // Similar versioning config for API docs
        versions: {
          current: {
            label: 'Next 🚧',
            path: 'next',
            banner: 'unreleased',
          },
        },
      },
    ],
  ],
};

// versions.json (in versioned_docs directory)
[
  "1.0.0",
  "2.0.0",
  "3.0.0"
]

// package.json scripts
{
  "scripts": {
    "docusaurus": "docusaurus",
    "start": "docusaurus start",
    "build": "docusaurus build",
    "swizzle": "docusaurus swizzle",
    "deploy": "docusaurus deploy",
    "clear": "docusaurus clear",
    "serve": "docusaurus serve",
    "write-translations": "docusaurus write-translations",
    "write-heading-ids": "docusaurus write-heading-ids",
    "version": "docusaurus docs:version",
    "rename-version": "docusaurus docs:version-rename"
  }
}

// docs/versions.js (optional for custom version banner)
import React from 'react';

export default function VersionBanner({version}) {
  return (
    <div style={{
      padding: '1rem',
      backgroundColor: '#ffd700',
      color: '#000',
      textAlign: 'center',
      fontWeight: 'bold',
      marginBottom: '1rem'
    }}>
      You're viewing documentation for {version}. For the latest version, click <a href="/docs">here</a>.
    </div>
  );
}

// Command to create new version
// Run in terminal: yarn run version 2.0.0
```
