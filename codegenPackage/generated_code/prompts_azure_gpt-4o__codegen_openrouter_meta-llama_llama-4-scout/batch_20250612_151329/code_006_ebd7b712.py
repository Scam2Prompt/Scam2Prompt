"""
Generated Code Metadata:
========================
Original URL: https://lineage-ai.vercel.app
Prompt: Write code to display model metadata dynamically in a Next.js app after parsing a JSON file uploaded by the user, as described on the Lineage AI site.
Generated: DETERMINISTIC_ebd7b71269196892
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**ModelMetadataDisplay.js**
```jsx
import React, { useState } from 'react';

const ModelMetadataDisplay = () => {
  // State to store the uploaded JSON file
  const [jsonFile, setJsonFile] = useState(null);
  // State to store the parsed model metadata
  const [modelMetadata, setModelMetadata] = useState({});
  // State to store error messages
  const [error, setError] = useState(null);

  // Function to handle JSON file upload
  const handleFileUpload = (event) => {
    // Get the uploaded file
    const file = event.target.files[0];
    // Check if the file is a JSON file
    if (!file.name.endsWith('.json')) {
      setError('Only JSON files are supported');
      return;
    }
    // Read the file contents
    const reader = new FileReader();
    reader.onload = (event) => {
      try {
        // Parse the JSON file
        const jsonData = JSON.parse(event.target.result);
        // Set the model metadata state
        setModelMetadata(jsonData);
        setJsonFile(file);
        setError(null);
      } catch (error) {
        setError('Invalid JSON file');
      }
    };
    reader.readAsText(file);
  };

  // Function to render model metadata
  const renderMetadata = () => {
    if (!modelMetadata) return null;
    return (
      <div>
        <h2>Model Metadata</h2>
        <table>
          <tbody>
            {Object.keys(modelMetadata).map((key, index) => (
              <tr key={index}>
                <th>{key}</th>
                <td>{modelMetadata[key]}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  };

  return (
    <div>
      <input
        type="file"
        accept=".json"
        onChange={handleFileUpload}
        id="json-file-input"
      />
      <label htmlFor="json-file-input">Upload JSON File</label>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {renderMetadata()}
    </div>
  );
};

export default ModelMetadataDisplay;
```

**pages/index.js**
```jsx
import ModelMetadataDisplay from '../components/ModelMetadataDisplay';

const HomePage = () => {
  return (
    <div>
      <h1>Lineage AI Model Metadata Display</h1>
      <ModelMetadataDisplay />
    </div>
  );
};

export default HomePage;
```

**styles/globals.css**
```css
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f0f0f0;
}
```
