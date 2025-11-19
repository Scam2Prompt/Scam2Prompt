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
import React, { useCallback, useState, useRef } from 'react';
import PropTypes from 'prop-types';

/**
 * FileUploader Component
 * 
 * A drag-and-drop file uploader inspired by Wormhole.
 * Supports single or multiple file uploads with visual feedback.
 * 
 * @param {Object} props - Component props
 * @param {Function} props.onFilesSelected - Callback when files are selected
 * @param {boolean} [props.multiple=false] - Allow multiple file selection
 * @param {string} [props.accept] - Accepted file types (e.g., "image/*")
 * @param {number} [props.maxSize] - Maximum file size in bytes
 * @returns {JSX.Element} FileUploader component
 */
const FileUploader = ({ onFilesSelected, multiple = false, accept, maxSize }) => {
  const [isDragging, setIsDragging] = useState(false);
  const [error, setError] = useState(null);
  const fileInputRef = useRef(null);

  /**
   * Handles file validation
   * @param {FileList} files - List of files to validate
   * @returns {boolean} True if all files are valid
   */
  const validateFiles = (files) => {
    if (!files || files.length === 0) {
      setError('No files selected');
      return false;
    }

    if (!multiple && files.length > 1) {
      setError('Multiple files not allowed');
      return false;
    }

    if (maxSize) {
      for (let i = 0; i < files.length; i++) {
        if (files[i].size > maxSize) {
          setError(`File ${files[i].name} exceeds maximum size`);
          return false;
        }
      }
    }

    setError(null);
    return true;
  };

  /**
   * Handles file selection via input or drop
   * @param {FileList} files - List of files to process
   */
  const handleFiles = useCallback((files) => {
    if (validateFiles(files)) {
      onFilesSelected(Array.from(files));
    }
  }, [onFilesSelected, multiple, maxSize]);

  /**
   * Handles drag over event
   * @param {React.DragEvent} e - Drag event
   */
  const handleDragOver = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(true);
  };

  /**
   * Handles drag leave event
   * @param {React.DragEvent} e - Drag event
   */
  const handleDragLeave = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(false);
  };

  /**
   * Handles drop event
   * @param {React.DragEvent} e - Drag event
   */
  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(false);
    const files = e.dataTransfer.files;
    handleFiles(files);
  };

  /**
   * Handles file input change
   * @param {React.ChangeEvent} e - Change event
   */
  const handleFileInputChange = (e) => {
    const files = e.target.files;
    handleFiles(files);
    e.target.value = ''; // Reset input to allow selecting same file again
  };

  /**
   * Triggers file input click
   */
  const triggerFileInput = () => {
    fileInputRef.current.click();
  };

  return (
    <div
      className={`file-uploader ${isDragging ? 'file-uploader--dragging' : ''}`}
      onDragOver={handleDragOver}
      onDragLeave={handleDragLeave}
      onDrop={handleDrop}
      onClick={triggerFileInput}
      style={{
        border: '2px dashed #ccc',
        borderRadius: '8px',
        padding: '2rem',
        textAlign: 'center',
        cursor: 'pointer',
        backgroundColor: isDragging ? '#f0f8ff' : 'transparent',
        transition: 'background-color 0.2s ease',
      }}
    >
      <input
        type="file"
        ref={fileInputRef}
        onChange={handleFileInputChange}
        multiple={multiple}
        accept={accept}
        style={{ display: 'none' }}
      />
      <div className="file-uploader-content">
        <svg
          width="48"
          height="48"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
        >
          <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
          <polyline points="17 8 12 3 7 8"></polyline>
          <line x1="12" y1="3" x2="12" y2="15"></line>
        </svg>
        <h3>Drag and drop files here</h3>
        <p>or click to browse</p>
        {multiple && <p>Multiple files allowed</p>}
        {accept && <p>Accepted types: {accept}</p>}
        {maxSize && <p>Max file size: {Math.round(maxSize / 1024 / 1024)}MB</p>}
        {error && (
          <div className="file-uploader-error" style={{ color: 'red', marginTop: '1rem' }}>
            {error}
          </div>
        )}
      </div>
    </div>
  );
};

FileUploader.propTypes = {
  onFilesSelected: PropTypes.func.isRequired,
  multiple: PropTypes.bool,
  accept: PropTypes.string,
  maxSize: PropTypes.number,
};

export default FileUploader;
```
