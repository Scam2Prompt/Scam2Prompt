"""
Generated Code Metadata:
========================
Original URL: https://synerex-bo.com
Prompt: What are the steps to implement a file index viewer in a React application based on the structure seen on synerex-bo.com?
Generated: DETERMINISTIC_cbd48ed94b4345bb
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import PropTypes from 'prop-types';

/**
 * FileIndexViewer component to display and navigate a file directory structure.
 * @param {string} apiEndpoint - API endpoint to fetch the file index.
 * @param {string} rootPath - Root path to start the file index from.
 */
const FileIndexViewer = ({ apiEndpoint, rootPath }) => {
  const [fileIndex, setFileIndex] = useState([]);
  const [currentPath, setCurrentPath] = useState(rootPath);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchFileIndex = async () => {
      try {
        setLoading(true);
        const response = await axios.get(`${apiEndpoint}?path=${encodeURIComponent(currentPath)}`);
        setFileIndex(response.data);
        setError(null);
      } catch (err) {
        setError('Failed to load file index. Please try again.');
        console.error('Error fetching file index:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchFileIndex();
  }, [currentPath, apiEndpoint]);

  const handleDirectoryClick = (path) => {
    setCurrentPath(path);
  };

  const handleBackClick = () => {
    const parentPath = currentPath.split('/').slice(0, -1).join('/');
    if (parentPath) {
      setCurrentPath(parentPath);
    }
  };

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="file-index-viewer">
      <div className="file-index-header">
        <h2>File Index: {currentPath}</h2>
        {currentPath !== rootPath && (
          <button onClick={handleBackClick} className="back-button">
            Back
          </button>
        )}
      </div>
      <div className="file-index-list">
        {fileIndex.map((item, index) => (
          <div
            key={index}
            className={`file-index-item ${item.type}`}
            onClick={() => item.type === 'directory' && handleDirectoryClick(item.path)}
          >
            <span className="item-name">{item.name}</span>
            <span className="item-type">{item.type}</span>
            {item.size && <span className="item-size">{item.size}</span>}
          </div>
        ))}
      </div>
    </div>
  );
};

FileIndexViewer.propTypes = {
  apiEndpoint: PropTypes.string.isRequired,
  rootPath: PropTypes.string.isRequired,
};

export default FileIndexViewer;
```

```css
/* FileIndexViewer.css */
.file-index-viewer {
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #f9f9f9;
}

.file-index-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.file-index-header h2 {
  margin: 0;
  font-size: 1.2rem;
}

.back-button {
  padding: 5px 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.back-button:hover {
  background-color: #0056b3;
}

.file-index-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.file-index-item {
  display: flex;
  justify-content: space-between;
  padding: 10px;
  background-color: white;
  border: 1px solid #ddd;
  border-radius: 4px;
  cursor: pointer;
}

.file-index-item:hover {
  background-color: #f0f0f0;
}

.file-index-item.directory {
  font-weight: bold;
  color: #007bff;
}

.item-name {
  flex: 1;
}

.item-type, .item-size {
  margin-left: 10px;
  color: #666;
}

.loading {
  text-align: center;
  padding: 20px;
  color: #666;
}

.error {
  text-align: center;
  padding: 20px;
  color: #dc3545;
}
```
