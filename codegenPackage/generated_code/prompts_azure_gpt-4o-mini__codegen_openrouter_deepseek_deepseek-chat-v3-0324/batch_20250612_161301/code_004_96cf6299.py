"""
Generated Code Metadata:
========================
Original URL: https://wormhole-web.vercel.app
Prompt: Explain how to customize the Wormhole file selection interface in a React application.
Generated: DETERMINISTIC_96cf629974100939
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState, useRef } from 'react';
import PropTypes from 'prop-types';

/**
 * Custom Wormhole File Selector Component
 * 
 * @param {Object} props - Component props
 * @param {Function} props.onFileSelect - Callback when files are selected
 * @param {Array} props.acceptedFileTypes - Array of accepted file types (e.g., ['image/*', '.pdf'])
 * @param {number} props.maxFileSize - Maximum file size in bytes
 * @param {boolean} props.multiple - Allow multiple file selection
 * @param {string} props.theme - Theme color ('light' or 'dark')
 * @param {Object} props.customStyles - Custom CSS styles for the component
 * @returns {JSX.Element} Custom file selector component
 */
const WormholeFileSelector = ({
  onFileSelect,
  acceptedFileTypes = [],
  maxFileSize = 10485760, // 10MB default
  multiple = false,
  theme = 'light',
  customStyles = {}
}) => {
  const [dragActive, setDragActive] = useState(false);
  const [error, setError] = useState(null);
  const fileInputRef = useRef(null);

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === 'dragenter' || e.type === 'dragover') {
      setDragActive(true);
    } else if (e.type === 'dragleave') {
      setDragActive(false);
    }
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      validateAndProcessFiles(e.dataTransfer.files);
    }
  };

  const handleChange = (e) => {
    if (e.target.files && e.target.files.length > 0) {
      validateAndProcessFiles(e.target.files);
    }
  };

  const validateAndProcessFiles = (files) => {
    try {
      const validFiles = [];
      let hasError = false;

      Array.from(files).forEach((file) => {
        // Check file type
        if (acceptedFileTypes.length > 0 && !isFileTypeValid(file)) {
          setError(`File type not allowed: ${file.name}`);
          hasError = true;
          return;
        }

        // Check file size
        if (file.size > maxFileSize) {
          setError(`File too large: ${file.name} (max ${maxFileSize / 1048576}MB)`);
          hasError = true;
          return;
        }

        validFiles.push(file);
      });

      if (!hasError && validFiles.length > 0) {
        setError(null);
        onFileSelect(multiple ? validFiles : validFiles[0]);
      }
    } catch (err) {
      setError('An error occurred while processing files');
      console.error('File processing error:', err);
    }
  };

  const isFileTypeValid = (file) => {
    return acceptedFileTypes.some((type) => {
      if (type.startsWith('.')) {
        return file.name.toLowerCase().endsWith(type.toLowerCase());
      }
      return file.type.match(type);
    });
  };

  const triggerFileInput = () => {
    fileInputRef.current.click();
  };

  const themeStyles = {
    light: {
      backgroundColor: '#ffffff',
      borderColor: '#e2e8f0',
      textColor: '#2d3748',
      highlightColor: '#edf2f7'
    },
    dark: {
      backgroundColor: '#2d3748',
      borderColor: '#4a5568',
      textColor: '#f7fafc',
      highlightColor: '#4a5568'
    }
  };

  const currentTheme = themeStyles[theme] || themeStyles.light;

  return (
    <div
      style={{
        ...customStyles,
        backgroundColor: currentTheme.backgroundColor,
        color: currentTheme.textColor,
        border: `2px dashed ${currentTheme.borderColor}`,
        borderRadius: '8px',
        padding: '2rem',
        textAlign: 'center',
        cursor: 'pointer',
        transition: 'all 0.2s ease',
        ...(dragActive && {
          backgroundColor: currentTheme.highlightColor,
          borderColor: '#4299e1'
        })
      }}
      onClick={triggerFileInput}
      onDragEnter={handleDrag}
      onDragLeave={handleDrag}
      onDragOver={handleDrag}
      onDrop={handleDrop}
    >
      <input
        type="file"
        ref={fileInputRef}
        onChange={handleChange}
        accept={acceptedFileTypes.join(',')}
        multiple={multiple}
        style={{ display: 'none' }}
      />
      
      <div style={{ marginBottom: '1rem' }}>
        <svg
          width="48"
          height="48"
          viewBox="0 0 24 24"
          fill="none"
          stroke={currentTheme.textColor}
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
        >
          <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
          <polyline points="17 8 12 3 7 8"></polyline>
          <line x1="12" y1="3" x2="12" y2="15"></line>
        </svg>
      </div>
      
      <p style={{ fontWeight: 'bold', marginBottom: '0.5rem' }}>
        {dragActive ? 'Drop files here' : 'Click to browse or drag files here'}
      </p>
      
      <p style={{ fontSize: '0.875rem', opacity: 0.7 }}>
        {acceptedFileTypes.length > 0
          ? `Supported formats: ${acceptedFileTypes.join(', ')}`
          : 'All file types supported'}
      </p>
      
      <p style={{ fontSize: '0.875rem', opacity: 0.7 }}>
        Max file size: {maxFileSize / 1048576}MB
      </p>
      
      {error && (
        <p style={{ color: '#e53e3e', marginTop: '1rem' }}>
          {error}
        </p>
      )}
    </div>
  );
};

WormholeFileSelector.propTypes = {
  onFileSelect: PropTypes.func.isRequired,
  acceptedFileTypes: PropTypes.arrayOf(PropTypes.string),
  maxFileSize: PropTypes.number,
  multiple: PropTypes.bool,
  theme: PropTypes.oneOf(['light', 'dark']),
  customStyles: PropTypes.object
};

export default WormholeFileSelector;
```
