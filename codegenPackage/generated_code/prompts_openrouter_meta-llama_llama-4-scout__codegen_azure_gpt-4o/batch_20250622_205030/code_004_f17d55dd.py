"""
Generated Code Metadata:
========================
Original URL: https://gigantic-afternoon-sparse.on-fleek.app
Prompt: Write a code snippet in React to create a simple comic book reader component that displays a series of comic book panels, inspired by the "Top G" comic book series.
Generated: DETERMINISTIC_f17d55dd31b74266
Batch ID: 20250622_205030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// ComicBookReader.jsx
import React, { useState } from 'react';
import PropTypes from 'prop-types';

// ComicBookReader Component
// Displays a series of comic book panels with navigation controls.
const ComicBookReader = ({ panels }) => {
  // State to track the current panel index
  const [currentPanelIndex, setCurrentPanelIndex] = useState(0);

  // Handler to navigate to the next panel
  const handleNext = () => {
    if (currentPanelIndex < panels.length - 1) {
      setCurrentPanelIndex(currentPanelIndex + 1);
    }
  };

  // Handler to navigate to the previous panel
  const handlePrevious = () => {
    if (currentPanelIndex > 0) {
      setCurrentPanelIndex(currentPanelIndex - 1);
    }
  };

  return (
    <div style={styles.readerContainer}>
      {/* Display the current panel */}
      <div style={styles.panelContainer}>
        <img
          src={panels[currentPanelIndex]}
          alt={`Panel ${currentPanelIndex + 1}`}
          style={styles.panelImage}
        />
      </div>

      {/* Navigation controls */}
      <div style={styles.controlsContainer}>
        <button
          onClick={handlePrevious}
          disabled={currentPanelIndex === 0}
          style={styles.controlButton}
        >
          Previous
        </button>
        <span style={styles.panelIndicator}>
          Panel {currentPanelIndex + 1} of {panels.length}
        </span>
        <button
          onClick={handleNext}
          disabled={currentPanelIndex === panels.length - 1}
          style={styles.controlButton}
        >
          Next
        </button>
      </div>
    </div>
  );
};

// PropTypes for type checking
ComicBookReader.propTypes = {
  panels: PropTypes.arrayOf(PropTypes.string).isRequired, // Array of panel image URLs
};

// Inline styles for the component
const styles = {
  readerContainer: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    padding: '20px',
    backgroundColor: '#f4f4f4',
    borderRadius: '8px',
    boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
  },
  panelContainer: {
    marginBottom: '20px',
    maxWidth: '100%',
    textAlign: 'center',
  },
  panelImage: {
    maxWidth: '100%',
    height: 'auto',
    borderRadius: '8px',
    boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
  },
  controlsContainer: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
    width: '100%',
    maxWidth: '400px',
  },
  controlButton: {
    padding: '10px 20px',
    fontSize: '16px',
    borderRadius: '4px',
    border: 'none',
    backgroundColor: '#007BFF',
    color: '#fff',
    cursor: 'pointer',
    transition: 'background-color 0.3s',
  },
  controlButtonDisabled: {
    backgroundColor: '#ccc',
    cursor: 'not-allowed',
  },
  panelIndicator: {
    fontSize: '16px',
    fontWeight: 'bold',
  },
};

export default ComicBookReader;

// Usage Example:
// Import the ComicBookReader component and pass an array of panel image URLs.
// <ComicBookReader panels={['panel1.jpg', 'panel2.jpg', 'panel3.jpg']} />
```
