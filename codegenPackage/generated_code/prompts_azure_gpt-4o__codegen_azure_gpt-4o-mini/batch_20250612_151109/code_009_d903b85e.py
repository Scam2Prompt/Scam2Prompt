"""
Generated Code Metadata:
========================
Original URL: https://itaca.in
Prompt: Develop a React component to showcase ITACA Ceramic's tile collections, including interactive previews of slab, vitrified, and wall tiles in various dimensions.
Generated: DETERMINISTIC_d903b85e604466dc
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './TileCollection.css'; // Importing CSS for styling

// TileCollection component to showcase ITACA Ceramic's tile collections
const TileCollection = ({ tiles }) => {
  const [selectedTile, setSelectedTile] = useState(null);

  // Function to handle tile selection
  const handleTileSelect = (tile) => {
    setSelectedTile(tile);
  };

  return (
    <div className="tile-collection">
      <h1>ITACA Ceramic Tile Collections</h1>
      <div className="tile-grid">
        {tiles.map((tile) => (
          <div
            key={tile.id}
            className="tile-item"
            onClick={() => handleTileSelect(tile)}
            role="button"
            tabIndex={0}
            onKeyPress={(e) => e.key === 'Enter' && handleTileSelect(tile)}
          >
            <img src={tile.image} alt={tile.name} className="tile-image" />
            <h2 className="tile-name">{tile.name}</h2>
            <p className="tile-dimensions">{tile.dimensions}</p>
          </div>
        ))}
      </div>

      {selectedTile && (
        <div className="tile-preview">
          <h2>Preview: {selectedTile.name}</h2>
          <img src={selectedTile.image} alt={selectedTile.name} className="preview-image" />
          <p>Dimensions: {selectedTile.dimensions}</p>
          <p>Description: {selectedTile.description}</p>
          <button onClick={() => setSelectedTile(null)} className="close-preview">
            Close Preview
          </button>
        </div>
      )}
    </div>
  );
};

// PropTypes for type checking
TileCollection.propTypes = {
  tiles: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      name: PropTypes.string.isRequired,
      dimensions: PropTypes.string.isRequired,
      image: PropTypes.string.isRequired,
      description: PropTypes.string,
    })
  ).isRequired,
};

export default TileCollection;
```

```css
/* TileCollection.css */
.tile-collection {
  padding: 20px;
  font-family: Arial, sans-serif;
}

.tile-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 15px;
}

.tile-item {
  border: 1px solid #ccc;
  border-radius: 5px;
  cursor: pointer;
  transition: transform 0.2s;
}

.tile-item:hover {
  transform: scale(1.05);
}

.tile-image {
  width: 100%;
  height: auto;
  border-radius: 5px 5px 0 0;
}

.tile-name {
  font-size: 1.2em;
  margin: 10px 0;
}

.tile-dimensions {
  color: #666;
}

.tile-preview {
  margin-top: 20px;
  border: 1px solid #ccc;
  padding: 15px;
  border-radius: 5px;
}

.preview-image {
  width: 100%;
  height: auto;
}

.close-preview {
  margin-top: 10px;
  padding: 10px 15px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.close-preview:hover {
  background-color: #0056b3;
}
```
