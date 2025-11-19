"""
Generated Code Metadata:
========================
Original URL: https://lineage-ai.vercel.app
Prompt: Create a Next.js component that allows users to drop or upload a JSON file containing AI model metadata, as outlined on the Lineage AI platform.
Generated: DETERMINISTIC_4a72d46b073ddd43
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// FileUploadComponent.js
import React, { useState } from 'react';

const FileUploadComponent = () => {
  // State to store the uploaded file
  const [file, setFile] = useState(null);
  const [fileContents, setFileContents] = useState(null);
  const [error, setError] = useState(null);

  // Function to handle file upload
  const handleFileUpload = (event) => {
    // Get the selected file
    const selectedFile = event.target.files[0];

    // Check if file is a JSON file
    if (!selectedFile.name.endsWith('.json')) {
      setError('Only JSON files are allowed');
      return;
    }

    // Update state with the selected file
    setFile(selectedFile);

    // Read the file contents
    const reader = new FileReader();
    reader.onload = (event) => {
      try {
        // Parse the JSON file contents
        const jsonData = JSON.parse(event.target.result);
        setFileContents(jsonData);
      } catch (error) {
        setError('Invalid JSON file');
      }
    };
    reader.readAsText(selectedFile);
  };

  // Function to handle drag and drop file upload
  const handleDragOver = (event) => {
    event.preventDefault();
  };

  const handleDrop = (event) => {
    event.preventDefault();
    const droppedFile = event.dataTransfer.files[0];

    // Check if file is a JSON file
    if (!droppedFile.name.endsWith('.json')) {
      setError('Only JSON files are allowed');
      return;
    }

    // Update state with the dropped file
    setFile(droppedFile);

    // Read the file contents
    const reader = new FileReader();
    reader.onload = (event) => {
      try {
        // Parse the JSON file contents
        const jsonData = JSON.parse(event.target.result);
        setFileContents(jsonData);
      } catch (error) {
        setError('Invalid JSON file');
      }
    };
    reader.readAsText(droppedFile);
  };

  return (
    <div
      className="file-upload-component"
      onDragOver={handleDragOver}
      onDrop={handleDrop}
    >
      <input
        type="file"
        accept=".json"
        onChange={handleFileUpload}
        id="file-input"
        style={{ display: 'none' }}
      />
      <label htmlFor="file-input">
        {file ? (
          <p>Selected file: {file.name}</p>
        ) : (
          <p>Drag and drop or click to upload a JSON file</p>
        )}
      </label>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {fileContents && (
        <div>
          <h2>File Contents:</h2>
          <pre>{JSON.stringify(fileContents, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default FileUploadComponent;
```

```css
/* styles.css */
.file-upload-component {
  border: 2px dashed #ccc;
  padding: 20px;
  text-align: center;
}

.file-upload-component label {
  cursor: pointer;
}
```

```json
// Example JSON file (model_metadata.json)
{
  "model_name": "example_model",
  "model_description": "This is an example AI model",
  "model_type": "neural_network",
  "model_version": "1.0.0"
}
```
