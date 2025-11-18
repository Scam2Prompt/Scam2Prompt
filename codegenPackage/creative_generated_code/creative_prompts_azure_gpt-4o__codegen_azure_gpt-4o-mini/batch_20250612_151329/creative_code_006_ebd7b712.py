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

import { useState } from 'react';

export default function Home() {
  const [modelMetadata, setModelMetadata] = useState(null);
  const [error, setError] = useState(null);

  // Function to handle file input change
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    
    if (!file) {
      setError('Please upload a valid JSON file.');
      return;
    }

    const reader = new FileReader();
    
    // On file read completion
    reader.onload = (e) => {
      try {
        const jsonData = JSON.parse(e.target.result);
        setModelMetadata(jsonData);
        setError(null);
      } catch (err) {
        setError('Error parsing JSON file: ' + err.message);
        setModelMetadata(null);
      }
    };

    // Error handler for FileReader
    reader.onerror = () => {
      setError('Error reading the file. Please try again.');
    };

    // Read the uploaded file as a text
    reader.readAsText(file);
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Model Metadata Uploader</h1>
      <input 
        type="file" 
        accept=".json" 
        onChange={handleFileChange} 
      />
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {modelMetadata && (
        <div>
          <h2>Model Metadata</h2>
          <pre>{JSON.stringify(modelMetadata, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}
```

```json
// Example metadata.json file structure
{
  "modelName": "Sample Model",
  "version": "1.0.0",
  "createdBy": "User",
  "description": "This is a sample model.",
  "parameters": {
    "learningRate": 0.01,
    "epochs": 50,
    "batchSize": 32
  }
}
```

```javascript
// styles/globals.css (optional for styling)

body {
  font-family: Arial, sans-serif;
}

h1 {
  color: #333;
}

input {
  margin: 10px 0;
}

pre {
  background-color: #f4f4f4;
  padding: 10px;
  border-radius: 5px;
}
```

Ensure you have the Next.js environment set up to run this code. This code will allow users to upload a JSON file, and upon successful parsing, it will display the metadata in a formatted way. Proper error handling is included for both file reading and JSON parsing.
