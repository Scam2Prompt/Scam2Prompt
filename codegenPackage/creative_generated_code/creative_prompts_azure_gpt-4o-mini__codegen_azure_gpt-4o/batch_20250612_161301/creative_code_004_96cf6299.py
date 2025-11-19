"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole-web.vercel.app
Prompt: Explain how to customize the Wormhole file selection interface in a React application.
Generated: DETERMINISTIC_96cf629974100939
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary modules
import React, { useState } from 'react'; // React for component creation and state management
import PropTypes from 'prop-types'; // PropTypes for type-checking
import './WormholeFileSelector.css'; // Import custom styles (optional)

// WormholeFileSelector Component
const WormholeFileSelector = ({ onFileSelect, allowedFileTypes }) => {
  // State for managing selected file
  const [selectedFile, setSelectedFile] = useState(null);

  // Event handler for file selection
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (!file) return; // Ensure a valid file is selected

    // Validate file type
    if (allowedFileTypes && !allowedFileTypes.includes(file.type)) {
      alert('Invalid file type. Please select a valid file.');
      return; // Stop further processing if file type is invalid
    }

    setSelectedFile(file); // Update state with selected file
    onFileSelect(file); // Notify parent component about the selected file
  };

  return (
    <div className="wormhole-file-selector">
      {/* File Input Field */}
      <input
        type="file"
        className="file-input"
        onChange={handleFileChange}
        accept={allowedFileTypes?.join(',')} // Restrict file types
      />

      {/* Display Selected File Name */}
      {selectedFile && (
        <div className="file-info">
          <p>Selected File: {selectedFile.name}</p>
        </div>
      )}
    </div>
  );
};

// Prop type validation for the component
WormholeFileSelector.propTypes = {
  onFileSelect: PropTypes.func.isRequired, // Function to handle file selection
  allowedFileTypes: PropTypes.arrayOf(PropTypes.string), // Array of allowed MIME types
};

// Default props for optional customization
WormholeFileSelector.defaultProps = {
  allowedFileTypes: null, // No restrictions on file types by default
};

// Export the component for use in other parts of the application
export default WormholeFileSelector;

// Example CSS file (WormholeFileSelector.css)
/*
.wormhole-file-selector {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.file-input {
  padding: 5px;
}

.file-info {
  margin-top: 10px;
  font-size: 14px;
}
*/
```
