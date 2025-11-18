"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lineage-ai.vercel.app
Prompt: Create a Next.js component that allows users to drop or upload a JSON file containing AI model metadata, as outlined on the Lineage AI platform.
Generated: DETERMINISTIC_4a72d46b073ddd43
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// components/JsonUploader.js
import React, { useState } from 'react';
import PropTypes from 'prop-types';

/**
 * JsonUploader Component
 * 
 * Allows users to drag-and-drop or upload a JSON file containing AI model metadata.
 * Displays a preview of the parsed JSON and returns the data to a callback function.
 * 
 * Usage:
 * <JsonUploader onUpload={(data) => console.log(data)} />
 */
const JsonUploader = ({ onUpload }) => {
  const [error, setError] = useState(null);
  const [fileContent, setFileContent] = useState(null);

  // Handle file selection or drop
  const handleFileUpload = async (file) => {
    setError(null); // Clear previous errors

    if (!file) {
      setError('No file selected.');
      return;
    }

    if (file.type !== 'application/json') {
      setError('Please upload a valid JSON file.');
      return;
    }

    try {
      const content = await file.text(); // Read file content
      const parsedData = JSON.parse(content); // Parse JSON
      setFileContent(parsedData);
      onUpload(parsedData); // Pass parsed data to parent callback
    } catch (e) {
      setError('Failed to parse JSON file. Please ensure it is valid.');
    }
  };

  // Handle file input change
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    handleFileUpload(file);
  };

  // Handle drag-and-drop
  const handleDrop = (event) => {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    handleFileUpload(file);
  };

  // Prevent default behavior when dragging over the drop zone
  const handleDragOver = (event) => {
    event.preventDefault();
  };

  return (
    <div>
      <h2>Upload AI Model Metadata JSON</h2>
      
      {/* Drag-and-Drop or File Input Zone */}
      <div
        onDrop={handleDrop}
        onDragOver={handleDragOver}
        style={{
          border: '2px dashed #ccc',
          padding: '20px',
          textAlign: 'center',
          marginBottom: '20px',
        }}
      >
        Drag and drop your JSON file here or{' '}
        <label style={{ color: 'blue', cursor: 'pointer' }}>
          <input
            type="file"
            accept="application/json"
            style={{ display: 'none' }}
            onChange={handleFileChange}
          />
          click to browse
        </label>
      </div>

      {/* Error Message */}
      {error && <p style={{ color: 'red' }}>{error}</p>}

      {/* JSON Preview */}
      {fileContent && (
        <div>
          <h3>JSON Preview:</h3>
          <pre style={{ background: '#f4f4f4', padding: '10px', borderRadius: '5px' }}>
            {JSON.stringify(fileContent, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
};

// Prop Types for the component
JsonUploader.propTypes = {
  onUpload: PropTypes.func.isRequired, // Callback function to handle the uploaded JSON data
};

export default JsonUploader;
```
