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
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * ComicBookReader - A component to display comic book panels with navigation controls.
 * @param {Object} props - Component props
 * @param {Array} props.panels - Array of panel objects containing image URLs and captions
 * @param {string} props.theme - Theme for the comic reader ('light' or 'dark')
 */
const ComicBookReader = ({ panels = [], theme = 'light' }) => {
  const [currentPanelIndex, setCurrentPanelIndex] = useState(0);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Preload images for better user experience
    const preloadImages = async () => {
      try {
        const imagePromises = panels.map(panel => {
          return new Promise((resolve, reject) => {
            const img = new Image();
            img.src = panel.imageUrl;
            img.onload = resolve;
            img.onerror = reject;
          });
        });

        await Promise.all(imagePromises);
        setIsLoading(false);
      } catch (err) {
        setError('Failed to load comic panels');
        setIsLoading(false);
      }
    };

    if (panels.length > 0) {
      preloadImages();
    }
  }, [panels]);

  const handleNext = () => {
    if (currentPanelIndex < panels.length - 1) {
      setCurrentPanelIndex(currentPanelIndex + 1);
    }
  };

  const handlePrev = () => {
    if (currentPanelIndex > 0) {
      setCurrentPanelIndex(currentPanelIndex - 1);
    }
  };

  const containerStyle = {
    backgroundColor: theme === 'dark' ? '#1a1a1a' : '#f5f5f5',
    color: theme === 'dark' ? '#ffffff' : '#333333',
    padding: '20px',
    borderRadius: '8px',
    maxWidth: '800px',
    margin: '0 auto',
    textAlign: 'center'
  };

  const panelStyle = {
    maxWidth: '100%',
    height: 'auto',
    marginBottom: '20px',
    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.2)'
  };

  const buttonStyle = {
    padding: '10px 20px',
    margin: '0 10px',
    backgroundColor: theme === 'dark' ? '#444' : '#ddd',
    color: theme === 'dark' ? '#fff' : '#333',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
    fontSize: '16px'
  };

  if (error) {
    return (
      <div style={containerStyle}>
        <p>Error: {error}</p>
      </div>
    );
  }

  if (isLoading) {
    return (
      <div style={containerStyle}>
        <p>Loading comic panels...</p>
      </div>
    );
  }

  if (panels.length === 0) {
    return (
      <div style={containerStyle}>
        <p>No comic panels available</p>
      </div>
    );
  }

  return (
    <div style={containerStyle}>
      <h2>Top G Comic Series</h2>
      <div>
        <img 
          src={panels[currentPanelIndex].imageUrl} 
          alt={`Comic panel ${currentPanelIndex + 1}`} 
          style={panelStyle}
        />
        {panels[currentPanelIndex].caption && (
          <p>{panels[currentPanelIndex].caption}</p>
        )}
      </div>
      <div>
        <button 
          onClick={handlePrev} 
          disabled={currentPanelIndex === 0}
          style={buttonStyle}
        >
          Previous
        </button>
        <span style={{ margin: '0 10px' }}>
          Panel {currentPanelIndex + 1} of {panels.length}
        </span>
        <button 
          onClick={handleNext} 
          disabled={currentPanelIndex === panels.length - 1}
          style={buttonStyle}
        >
          Next
        </button>
      </div>
    </div>
  );
};

ComicBookReader.propTypes = {
  panels: PropTypes.arrayOf(
    PropTypes.shape({
      imageUrl: PropTypes.string.isRequired,
      caption: PropTypes.string
    })
  ).isRequired,
  theme: PropTypes.oneOf(['light', 'dark'])
};

export default ComicBookReader;
```
