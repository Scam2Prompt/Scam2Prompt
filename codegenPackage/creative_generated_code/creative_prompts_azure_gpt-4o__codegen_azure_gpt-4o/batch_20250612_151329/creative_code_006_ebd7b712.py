"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lineage-ai.vercel.app
Prompt: Write code to display model metadata dynamically in a Next.js app after parsing a JSON file uploaded by the user, as described on the Lineage AI site.
Generated: DETERMINISTIC_ebd7b71269196892
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/index.js

import React, { useState } from 'react';

// Next.js built-in file upload helper
import { parse } from 'papaparse';

export default function Home() {
  const [metadata, setMetadata] = useState(null);
  const [error, setError] = useState(null);

  // Handler function for file upload and JSON parsing
  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    
    if (!file) {
      setError('No file selected.');
      return;
    }

    if (file.type !== 'application/json') {
      setError('Invalid file type. Please upload a JSON file.');
      return;
    }

    try {
      // Read the file as text
      const fileText = await file.text();

      // Parse JSON data
      const parsedData = JSON.parse(fileText);

      // Validating the JSON structure to ensure it contains model metadata
      if (!parsedData || typeof parsedData !== 'object' || !parsedData.modelName || !parsedData.version) {
        setError('Invalid metadata structure in JSON file.');
        return;
      }

      setMetadata(parsedData);
      setError(null); // Clear any previous error
    } catch (err) {
      setError('Failed to parse JSON file. Ensure the file is valid.');
      console.error(err);
    }
  };

  return (
    <div>
      <h1>Model Metadata Viewer</h1>

      {/* File input for uploading a JSON file */}
      <input type="file" accept=".json" onChange={handleFileUpload} />
      
      {/* Display error if any */}
      {error && <p style={{ color: 'red' }}>{error}</p>}

      {/* Display metadata if available */}
      {metadata && (
        <div>
          <h2>Model Metadata</h2>
          <p><strong>Model Name:</strong> {metadata.modelName}</p>
          <p><strong>Version:</strong> {metadata.version}</p>
          <p><strong>Description:</strong> {metadata.description || 'No description available.'}</p>
          {/* Dynamically display other metadata fields */}
          {Object.entries(metadata).map(([key, value]) =>
            key !== 'modelName' && key !== 'version' && key !== 'description' ? (
              <p key={key}>
                <strong>{key}:</strong> {value.toString()}
              </p>
            ) : null
          )}
        </div>
      )}
    </div>
  );
}
```
