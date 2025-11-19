"""
Generated Code Metadata:
========================
Original URL: https://cuadrosblangar.es
Prompt: Develop a React component that showcases different styles of wall art, including triptychs and diptychs, as featured on Cuadros Blangar.
Generated: DETERMINISTIC_ee20391cfca57ed1
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState } from 'react';
import PropTypes from 'prop-types';

/**
 * WallArtGallery Component
 * Displays a gallery of wall art styles including triptychs and diptychs.
 * 
 * @param {Array} artworks - Array of artwork objects to display
 * @param {string} defaultStyle - Default art style to display initially
 */
const WallArtGallery = ({ artworks = [], defaultStyle = 'triptych' }) => {
  const [activeStyle, setActiveStyle] = useState(defaultStyle);
  const [selectedArtwork, setSelectedArtwork] = useState(null);

  // Filter artworks by active style
  const filteredArtworks = artworks.filter(art => art.style === activeStyle);

  /**
   * Handles the selection of an artwork
   * @param {Object} artwork - The selected artwork object
   */
  const handleSelectArtwork = (artwork) => {
    setSelectedArtwork(artwork);
  };

  /**
   * Handles closing the artwork detail view
   */
  const handleCloseDetail = () => {
    setSelectedArtwork(null);
  };

  return (
    <div className="wall-art-gallery">
      <div className="style-selector">
        <h2>Select Art Style</h2>
        <div className="style-buttons">
          <button 
            className={activeStyle === 'triptych' ? 'active' : ''}
            onClick={() => setActiveStyle('triptych')}
          >
            Triptychs
          </button>
          <button 
            className={activeStyle === 'diptych' ? 'active' : ''}
            onClick={() => setActiveStyle('diptych')}
          >
            Diptychs
          </button>
          <button 
            className={activeStyle === 'single' ? 'active' : ''}
            onClick={() => setActiveStyle('single')}
          >
            Single Panels
          </button>
        </div>
      </div>

      <div className="artwork-grid">
        {filteredArtworks.length > 0 ? (
          filteredArtworks.map((artwork) => (
            <div 
              key={artwork.id} 
              className="artwork-item"
              onClick={() => handleSelectArtwork(artwork)}
            >
              <img 
                src={artwork.thumbnail} 
                alt={artwork.title} 
                className="artwork-thumbnail"
              />
              <h3>{artwork.title}</h3>
              <p>{artwork.artist}</p>
            </div>
          ))
        ) : (
          <p className="no-artworks">No artworks found for this style.</p>
        )}
      </div>

      {selectedArtwork && (
        <div className="artwork-detail-modal">
          <div className="modal-content">
            <button className="close-button" onClick={handleCloseDetail}>
              &times;
            </button>
            <img 
              src={selectedArtwork.fullImage} 
              alt={selectedArtwork.title} 
              className="detail-image"
            />
            <div className="artwork-info">
              <h2>{selectedArtwork.title}</h2>
              <p className="artist">{selectedArtwork.artist}</p>
              <p className="description">{selectedArtwork.description}</p>
              <p className="price">${selectedArtwork.price.toFixed(2)}</p>
              <button className="purchase-button">Add to Cart</button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

WallArtGallery.propTypes = {
  artworks: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      title: PropTypes.string.isRequired,
      artist: PropTypes.string.isRequired,
      style: PropTypes.oneOf(['triptych', 'diptych', 'single']).isRequired,
      thumbnail: PropTypes.string.isRequired,
      fullImage: PropTypes.string.isRequired,
      description: PropTypes.string,
      price: PropTypes.number.isRequired,
    })
  ),
  defaultStyle: PropTypes.oneOf(['triptych', 'diptych', 'single']),
};

export default WallArtGallery;
```

```css
/* WallArtGallery.css */
.wall-art-gallery {
  font-family: 'Arial', sans-serif;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.style-selector {
  margin-bottom: 30px;
  text-align: center;
}

.style-selector h2 {
  margin-bottom: 15px;
  color: #333;
}

.style-buttons {
  display: flex;
  justify-content: center;
  gap: 15px;
}

.style-buttons button {
  padding: 10px 20px;
  border: none;
  background-color: #f0f0f0;
  cursor: pointer;
  transition: all 0.3s ease;
  border-radius: 4px;
}

.style-buttons button:hover {
  background-color: #ddd;
}

.style-buttons button.active {
  background-color: #333;
  color: white;
}

.artwork-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
}

.artwork-item {
  cursor: pointer;
  transition: transform 0.3s ease;
  border: 1px solid #eee;
  padding: 15px;
  border-radius: 8px;
}

.artwork-item:hover {
  transform: scale(1.03);
}

.artwork-thumbnail {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 4px;
}

.no-artworks {
  text-align: center;
  grid-column: 1 / -1;
  color: #666;
}

.artwork-detail-modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background-color: white;
  padding: 30px;
  border-radius: 8px;
  max-width: 800px;
  width: 90%;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
}

.close-button {
  position: absolute;
  top: 15px;
  right: 15px;
  font-size: 24px;
  background: none;
  border: none;
  cursor: pointer;
}

.detail-image {
  width: 100%;
  max-height: 400px;
  object-fit: contain;
  margin-bottom: 20px;
}

.artwork-info {
  padding: 0 15px;
}

.artwork-info h2 {
  margin-bottom: 10px;
  color: #333;
}

.artist {
  font-style: italic;
  color: #666;
  margin-bottom: 15px;
}

.description {
  margin-bottom: 20px;
  line-height: 1.5;
}

.price {
  font-weight: bold;
  font-size: 18px;
  margin-bottom: 20px;
}

.purchase-button {
  padding: 12px 25px;
  background-color: #333;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.purchase-button:hover {
  background-color: #555;
}
```
