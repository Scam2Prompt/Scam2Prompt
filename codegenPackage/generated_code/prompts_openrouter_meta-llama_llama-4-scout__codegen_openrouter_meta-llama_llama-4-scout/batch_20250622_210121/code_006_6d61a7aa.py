"""
Generated Code Metadata:
========================
Original URL: https://wormhole-web.vercel.app
Prompt: "Create a React component for a file uploader with drag-and-drop functionality inspired by Wormhole."
Generated: DETERMINISTIC_6d61a7aaba5e776b
Batch ID: 20250622_210121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// FileUploader.js
import React, { useState } from 'react';
import './FileUploader.css';

/**
 * FileUploader component with drag-and-drop functionality.
 * 
 * @returns {JSX.Element} FileUploader component.
 */
function FileUploader() {
  // State to store the uploaded files
  const [files, setFiles] = useState([]);
  const [dragging, setDragging] = useState(false);

  // Handle drag over event
  const handleDragOver = (e) => {
    e.preventDefault();
    setDragging(true);
  };

  // Handle drag leave event
  const handleDragLeave = () => {
    setDragging(false);
  };

  // Handle drop event
  const handleDrop = (e) => {
    e.preventDefault();
    setDragging(false);
    const droppedFiles = e.dataTransfer.files;
    setFiles([...files, ...droppedFiles]);
  };

  // Handle file input change event
  const handleFileChange = (e) => {
    const selectedFiles = e.target.files;
    setFiles([...files, ...selectedFiles]);
  };

  // Handle file removal
  const handleRemoveFile = (index) => {
    const updatedFiles = [...files];
    updatedFiles.splice(index, 1);
    setFiles(updatedFiles);
  };

  return (
    <div
      className={`file-uploader ${dragging ? 'dragging' : ''}`}
      onDragOver={handleDragOver}
      onDragLeave={handleDragLeave}
      onDrop={handleDrop}
    >
      <div className="file-uploader-inner">
        <input
          type="file"
          multiple
          onChange={handleFileChange}
          className="file-input"
        />
        <div className="drop-zone">
          {files.length === 0 ? (
            <p>Drag and drop files or click to upload</p>
          ) : (
            <ul>
              {files.map((file, index) => (
                <li key={index}>
                  {file.name}{' '}
                  <button onClick={() => handleRemoveFile(index)}>
                    Remove
                  </button>
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </div>
  );
}

export default FileUploader;
```

```css
/* FileUploader.css */
.file-uploader {
  width: 500px;
  height: 300px;
  border: 2px dashed #ccc;
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.file-uploader.dragging {
  border-color: #aaa;
  background-color: #f0f0f0;
}

.file-uploader-inner {
  text-align: center;
}

.file-input {
  display: none;
}

.drop-zone {
  padding: 20px;
}

.drop-zone ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.drop-zone li {
  padding: 10px;
  border-bottom: 1px solid #ccc;
}

.drop-zone li:last-child {
  border-bottom: none;
}

.drop-zone button {
  background-color: #4CAF50;
  color: #fff;
  border: none;
  padding: 5px 10px;
  font-size: 16px;
  cursor: pointer;
}

.drop-zone button:hover {
  background-color: #3e8e41;
}
```

```jsx
// App.js
import React from 'react';
import FileUploader from './FileUploader';

function App() {
  return (
    <div>
      <FileUploader />
    </div>
  );
}

export default App;
```
