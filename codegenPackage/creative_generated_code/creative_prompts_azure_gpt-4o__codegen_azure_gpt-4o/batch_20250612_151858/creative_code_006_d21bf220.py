"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marchigue.cl
Prompt: Create a React component that displays a gallery of images and videos, similar to the "Galería Fotográfica" and "Videos" sections on the Turismo Marchigüe website.
Generated: DETERMINISTIC_d21bf220e98e0dac
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary libraries and components
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

// The Gallery component displays a gallery of images and videos
const Gallery = ({ mediaItems }) => {
  // State to track the selected media type (images or videos)
  const [selectedType, setSelectedType] = useState('images');

  // Filters media items based on the selected type (images or videos)
  const filteredItems = mediaItems.filter(item => item.type === selectedType);

  return (
    <div className="gallery-container">
      {/* Media type selector buttons */}
      <div className="gallery-controls">
        <button
          className={`control-button ${selectedType === 'images' ? 'active' : ''}`}
          onClick={() => setSelectedType('images')}
        >
          Images
        </button>
        <button
          className={`control-button ${selectedType === 'videos' ? 'active' : ''}`}
          onClick={() => setSelectedType('videos')}
        >
          Videos
        </button>
      </div>

      {/* Display filtered media items */}
      <div className="gallery-grid">
        {filteredItems.map((item, index) => (
          <div className="gallery-item" key={index}>
            {item.type === 'images' ? (
              // Render image
              <img src={item.url} alt={item.caption || 'Gallery image'} className="gallery-image" />
            ) : (
              // Render video
              <video controls className="gallery-video">
                <source src={item.url} type="video/mp4" />
                Your browser does not support the video tag.
              </video>
            )}
            {/* Display caption if available */}
            {item.caption && <p className="gallery-caption">{item.caption}</p>}
          </div>
        ))}
      </div>
    </div>
  );
};

// Prop validation for the Gallery component
Gallery.propTypes = {
  mediaItems: PropTypes.arrayOf(
    PropTypes.shape({
      type: PropTypes.oneOf(['images', 'videos']).isRequired, // Media type should be 'images' or 'videos'
      url: PropTypes.string.isRequired, // URL of the media item
      caption: PropTypes.string // Optional caption for the media item
    })
  ).isRequired
};

/*
  Example CSS for styling:
  .gallery-container { padding: 20px; }
  .gallery-controls { margin-bottom: 20px; }
  .control-button { margin-right: 10px; padding: 10px; cursor: pointer; }
  .control-button.active { font-weight: bold; }
  .gallery-grid { display: flex; flex-wrap: wrap; gap: 20px; }
  .gallery-item { width: 200px; text-align: center; }
  .gallery-image, .gallery-video { width: 100%; height: auto; }
  .gallery-caption { margin-top: 10px; font-style: italic; }
*/

export default Gallery;

// Usage Example:
// import Gallery from './Gallery';
// const mediaItems = [
//   { type: 'images', url: 'image1.jpg', caption: 'Beautiful Landscape' },
//   { type: 'images', url: 'image2.jpg', caption: 'Sunset' },
//   { type: 'videos', url: 'video1.mp4', caption: 'Tour Marchigüe' },
//   { type: 'videos', url: 'video2.mp4', caption: 'Cultural Event' },
// ];
// <Gallery mediaItems={mediaItems} />;
```
