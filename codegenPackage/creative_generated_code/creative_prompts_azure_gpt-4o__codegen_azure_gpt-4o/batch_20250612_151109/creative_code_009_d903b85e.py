"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itaca.in
Prompt: Develop a React component to showcase ITACA Ceramic's tile collections, including interactive previews of slab, vitrified, and wall tiles in various dimensions.
Generated: DETERMINISTIC_d903b85e604466dc
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// ITACATileCollection.js
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './ITACATileCollection.css'; // Include custom styles for the tile component

/**
 * ITACATileCollection Component
 * Displays interactive previews of tile collections (slab, vitrified, and wall tiles) in various dimensions.
 */
const ITACATileCollection = ({ tileCollections }) => {
  // State to track the selected tile category
  const [selectedCategory, setSelectedCategory] = useState('slab');

  // State to track the selected tile dimension preview
  const [selectedDimension, setSelectedDimension] = useState(null);

  // Function to handle category selection
  const handleCategoryChange = (category) => {
    setSelectedCategory(category);
    setSelectedDimension(null); // Reset dimension when category changes
  };

  // Function to handle dimension selection
  const handleDimensionChange = (dimension) => {
    setSelectedDimension(dimension);
  };

  return (
    <div className="tile-collection-container">
      <h1>ITACA Ceramic Tile Collections</h1>

      {/* Tile Category Selector */}
      <div className="category-selector">
        <button
          className={`category-button ${selectedCategory === 'slab' ? 'active' : ''}`}
          onClick={() => handleCategoryChange('slab')}
        >
          Slab Tiles
        </button>
        <button
          className={`category-button ${selectedCategory === 'vitrified' ? 'active' : ''}`}
          onClick={() => handleCategoryChange('vitrified')}
        >
          Vitrified Tiles
        </button>
        <button
          className={`category-button ${selectedCategory === 'wall' ? 'active' : ''}`}
          onClick={() => handleCategoryChange('wall')}
        >
          Wall Tiles
        </button>
      </div>

      {/* Tile Dimensions Selector */}
      <div className="dimension-selector">
        <h2>Select Dimensions</h2>
        {tileCollections[selectedCategory]?.dimensions.map((dimension) => (
          <button
            key={dimension}
            className={`dimension-button ${selectedDimension === dimension ? 'active' : ''}`}
            onClick={() => handleDimensionChange(dimension)}
          >
            {dimension}
          </button>
        ))}
      </div>

      {/* Tile Preview */}
      <div className="tile-preview">
        <h2>Tile Preview</h2>
        {selectedDimension ? (
          <img
            src={tileCollections[selectedCategory]?.previews[selectedDimension]}
            alt={`${selectedCategory} tile in ${selectedDimension}`}
            className="preview-image"
          />
        ) : (
          <p>Please select a dimension to preview the tile.</p>
        )}
      </div>
    </div>
  );
};

// PropTypes for the component
ITACATileCollection.propTypes = {
  tileCollections: PropTypes.shape({
    slab: PropTypes.shape({
      dimensions: PropTypes.arrayOf(PropTypes.string).isRequired,
      previews: PropTypes.objectOf(PropTypes.string).isRequired,
    }),
    vitrified: PropTypes.shape({
      dimensions: PropTypes.arrayOf(PropTypes.string).isRequired,
      previews: PropTypes.objectOf(PropTypes.string).isRequired,
    }),
    wall: PropTypes.shape({
      dimensions: PropTypes.arrayOf(PropTypes.string).isRequired,
      previews: PropTypes.objectOf(PropTypes.string).isRequired,
    }),
  }).isRequired,
};

export default ITACATileCollection;

/*
ITACATileCollection.css

.tile-collection-container {
  font-family: Arial, sans-serif;
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
}

.category-selector,
.dimension-selector {
  margin-bottom: 20px;
}

.category-button,
.dimension-button {
  margin: 5px;
  padding: 10px 20px;
  border: 1px solid #ccc;
  background-color: #f9f9f9;
  cursor: pointer;
  transition: background-color 0.3s;
}

.category-button.active,
.dimension-button.active {
  background-color: #007bff;
  color: #fff;
}

.preview-image {
  max-width: 100%;
  height: auto;
  border: 1px solid #ddd;
}
*/
```
