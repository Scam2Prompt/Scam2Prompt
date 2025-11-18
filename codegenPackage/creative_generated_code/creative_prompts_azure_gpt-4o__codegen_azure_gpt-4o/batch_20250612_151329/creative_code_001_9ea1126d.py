"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lineage-ai.vercel.app
Prompt: Provide an example of uploading a JSON file containing model metadata to a web application using Next.js, as supported by the Lineage AI platform.
Generated: DETERMINISTIC_9ea1126dcd4efeb8
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/upload.js

import React, { useState } from 'react';

export default function UploadPage() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState('');

  // Handle file selection
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file && file.type === 'application/json') {
      setSelectedFile(file);
    } else {
      setSelectedFile(null);
      setUploadStatus('Please upload a valid JSON file.');
    }
  };

  // Handle file upload
  const handleUpload = async () => {
    if (!selectedFile) {
      setUploadStatus('No file selected.');
      return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      setUploadStatus('Uploading...');
      const response = await fetch('/api/upload', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        setUploadStatus('File uploaded successfully.');
      } else {
        const errorData = await response.json();
        setUploadStatus(`Error: ${errorData.message || 'Failed to upload file.'}`);
      }
    } catch (error) {
      setUploadStatus(`Error: ${error.message}`);
    }
  };

  return (
    <div>
      <h1>Upload Model Metadata</h1>
      <input type="file" accept=".json" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
      <p>{uploadStatus}</p>
    </div>
  );
}

// pages/api/upload.js

import fs from 'fs';
import path from 'path';

export default async function handler(req, res) {
  if (req.method === 'POST') {
    try {
      // Create a directory to store uploaded files if it doesn't exist
      const uploadsDir = path.join(process.cwd(), 'uploads');
      if (!fs.existsSync(uploadsDir)) {
        fs.mkdirSync(uploadsDir);
      }

      // Parse the uploaded file
      const file = req.body.file; // NOTE: Using `multer` or similar library is recommended in production
      const filePath = path.join(uploadsDir, file.name);

      // Save the file to the server
      fs.writeFileSync(filePath, file.data);

      return res.status(200).json({ message: 'File uploaded successfully.' });
    } catch (error) {
      return res.status(500).json({ message: 'Server error while uploading file.' });
    }
  }

  return res.status(405).json({ message: 'Method not allowed.' });
}
```
