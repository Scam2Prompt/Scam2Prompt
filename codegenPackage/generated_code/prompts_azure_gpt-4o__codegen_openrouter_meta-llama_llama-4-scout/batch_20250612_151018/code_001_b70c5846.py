"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2792--docusaurus-2.netlify.app
Prompt: Generate code to implement document versioning in a Docusaurus project to support multiple versions of documentation.
Generated: DETERMINISTIC_b70c584688ac7383
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
  versions: {
    current: '1.0.0',
    archived: ['0.1.0', '0.2.0'],
  },
  // ... other configurations ...
};

// versioned_docs/version-0.1.0/** 
// versioned_docs/version-0.2.0/** 
// versioned_docs/version-1.0.0/** 

// utils/versioning.js
const fs = require('fs');
const path = require('path');

const getVersionedDocs = (version) => {
  try {
    const versionedDocsPath = path.join(process.cwd(), 'versioned_docs', `version-${version}`);
    return fs.readdirSync(versionedDocsPath);
  } catch (error) {
    if (error.code === 'ENOENT') {
      console.error(`Version ${version} not found.`);
    } else {
      console.error(`Error reading versioned docs: ${error.message}`);
    }
    return [];
  }
};

const getCurrentVersion = () => {
  const docusaurusConfig = require(path.join(process.cwd(), 'docusaurus.config.js'));
  return docusaurusConfig.versions.current;
};

const getArchivedVersions = () => {
  const docusaurusConfig = require(path.join(process.cwd(), 'docusaurus.config.js'));
  return docusaurusConfig.versions.archived;
};

// components/VersionedDoc.js
import React from 'react';
import { getVersionedDocs } from '../utils/versioning';

const VersionedDoc = ({ version, docId }) => {
  const versionedDocs = getVersionedDocs(version);
  const doc = versionedDocs.find((doc) => doc === `${docId}.md`);

  if (!doc) {
    return <div>Document not found.</div>;
  }

  return (
    <div>
      <h1>{doc.replace('.md', '')}</h1>
      {/* render the markdown document */}
    </div>
  );
};

export default VersionedDoc;

// pages/versions.js
import React from 'react';
import { getCurrentVersion, getArchivedVersions } from '../utils/versioning';

const VersionsPage = () => {
  const currentVersion = getCurrentVersion();
  const archivedVersions = getArchivedVersions();

  return (
    <div>
      <h1>Versions</h1>
      <ul>
        <li>
          <a href={`/docs/${currentVersion}/`}>Current Version ({currentVersion})</a>
        </li>
        {archivedVersions.map((version) => (
          <li key={version}>
            <a href={`/docs/version-${version}/`}>{version}</a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default VersionsPage;

// pages/_app.js
import React from 'react';
import VersionedDoc from '../components/VersionedDoc';

const App = () => {
  return (
    <div>
      <VersionedDoc version="1.0.0" docId="getting-started" />
    </div>
  );
};

export default App;
```
