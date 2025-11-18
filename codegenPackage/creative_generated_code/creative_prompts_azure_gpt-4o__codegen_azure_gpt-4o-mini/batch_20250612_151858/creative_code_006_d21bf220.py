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

```javascript
import React from 'react';
import PropTypes from 'prop-types';
import './Gallery.css'; // Assuming you have a separate CSS file for styles

// Gallery Component
const Gallery = ({ items }) => {
  // Error handling for empty items
  if (!items || items.length === 0) {
    return <div className="gallery-error">No items to display.</div>;
  }

  return (
    <div className="gallery-container">
      {items.map((item, index) => (
        <div key={index} className="gallery-item">
          {item.type === 'image' ? (
            <img src={item.src} alt={item.alt || 'Gallery item'} className="gallery-image" />
          ) : item.type === 'video' ? (
            <video controls className="gallery-video">
              <source src={item.src} type="video/mp4" />
              Your browser does not support the video tag.
            </video>
          ) : (
            <div className="gallery-error">Unsupported item type.</div>
          )}
        </div>
      ))}
    </div>
  );
};

// PropTypes for type checking
Gallery.propTypes = {
  items: PropTypes.arrayOf(
    PropTypes.shape({
      type: PropTypes.oneOf(['image', 'video']).isRequired,
      src: PropTypes.string.isRequired,
      alt: PropTypes.string,
    })
  ).isRequired,
};

export default Gallery;
```

```css
/* Gallery.css */
.gallery-container {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  justify-content: center;
}

.gallery-item {
  border: 1px solid #ccc;
  border-radius: 8px;
  overflow: hidden;
  max-width: 300px;
}

.gallery-image {
  width: 100%;
  height: auto;
}

.gallery-video {
  width: 100%;
  height: auto;
}

.gallery-error {
  color: red;
  text-align: center;
  padding: 20px;
}
```

### Usage Example:
```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import Gallery from './Gallery';

const items = [
  { type: 'image', src: 'image1.jpg', alt: 'Beautiful Landscape' },
  { type: 'video', src: 'video1.mp4' },
  { type: 'image', src: 'image2.jpg', alt: 'City View' },
  // Add more items as needed
];

ReactDOM.render(<Gallery items={items} />, document.getElementById('root'));
```
