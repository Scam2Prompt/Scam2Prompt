"""
Generated Code Metadata:
========================
Original URL: https://itaca.in
Prompt: Generate a code snippet for a web application that allows users to select and customize ceramic tiles based on size and mood, similar to the "Tile That Change Your Mood" feature on Itaca's website.
Generated: DETERMINISTIC_87c74eeb037a0c9b
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// TileCustomizer.js - A React component for ceramic tile customization

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './TileCustomizer.css';

const TileCustomizer = () => {
  // Available tile sizes
  const tileSizes = [
    { id: 1, name: 'Small', dimensions: '10x10cm' },
    { id: 2, name: 'Medium', dimensions: '20x20cm' },
    { id: 3, name: 'Large', dimensions: '30x30cm' }
  ];

  // Available mood themes
  const moodThemes = [
    { id: 1, name: 'Calm', colors: ['#E6F7FF', '#B3E0FF', '#66C2FF'] },
    { id: 2, name: 'Energetic', colors: ['#FFEEF4', '#FFCCE5', '#FF99D1'] },
    { id: 3, name: 'Natural', colors: ['#F0FFF0', '#C1F0C1', '#7FBF7F'] },
    { id: 4, name: 'Elegant', colors: ['#F5F5F5', '#E0E0E0', '#9E9E9E'] }
  ];

  const [selectedSize, setSelectedSize] = useState(tileSizes[0]);
  const [selectedMood, setSelectedMood] = useState(moodThemes[0]);
  const [customTiles, setCustomTiles] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  // Fetch recommended tile combinations based on selected mood
  useEffect(() => {
    const fetchRecommendedTiles = async () => {
      try {
        setIsLoading(true);
        setError(null);
        // In a real app, this would be an API call
        // const response = await axios.get(`/api/tiles/recommended?mood=${selectedMood.id}`);
        
        // Mock response for demonstration
        const mockResponse = {
          data: [
            { id: 1, pattern: 'Subtle Gradient', colors: selectedMood.colors },
            { id: 2, pattern: 'Geometric', colors: [...selectedMood.colors].reverse() },
            { id: 3, pattern: 'Organic', colors: [selectedMood.colors[1], selectedMood.colors[0], selectedMood.colors[2]] }
          ]
        };
        
        setCustomTiles(mockResponse.data);
      } catch (err) {
        setError('Failed to load recommended tile designs. Please try again.');
        console.error('Error fetching recommended tiles:', err);
      } finally {
        setIsLoading(false);
      }
    };

    fetchRecommendedTiles();
  }, [selectedMood]);

  const handleSizeChange = (size) => {
    setSelectedSize(size);
  };

  const handleMoodChange = (mood) => {
    setSelectedMood(mood);
  };

  const handleAddToCart = (tile) => {
    // In a real app, this would add the tile to cart
    console.log('Added to cart:', {
      size: selectedSize,
      mood: selectedMood,
      design: tile
    });
    alert(`${tile.pattern} tile (${selectedSize.name}) added to cart!`);
  };

  return (
    <div className="tile-customizer">
      <h2>Customize Your Ceramic Tiles</h2>
      
      <div className="selection-section">
        <div className="size-selector">
          <h3>Select Size</h3>
          <div className="size-options">
            {tileSizes.map((size) => (
              <button
                key={size.id}
                className={`size-btn ${selectedSize.id === size.id ? 'active' : ''}`}
                onClick={() => handleSizeChange(size)}
              >
                {size.name}<br/>({size.dimensions})
              </button>
            ))}
          </div>
        </div>

        <div className="mood-selector">
          <h3>Select Mood</h3>
          <div className="mood-options">
            {moodThemes.map((mood) => (
              <button
                key={mood.id}
                className={`mood-btn ${selectedMood.id === mood.id ? 'active' : ''}`}
                onClick={() => handleMoodChange(mood)}
                style={{ backgroundColor: mood.colors[0] }}
                title={mood.name}
              >
                {mood.name}
              </button>
            ))}
          </div>
        </div>
      </div>

      {error && <div className="error-message">{error}</div>}

      <div className="tile-display-section">
        <h3>Recommended Designs for {selectedMood.name} Mood</h3>
        
        {isLoading ? (
          <div className="loading">Loading designs...</div>
        ) : (
          <div className="tile-grid">
            {customTiles.map((tile) => (
              <div key={tile.id} className="tile-preview">
                <div 
                  className="tile-pattern" 
                  style={{ 
                    background: `linear-gradient(135deg, ${tile.colors.join(', ')})`,
                    width: '150px',
                    height: '150px'
                  }}
                ></div>
                <h4>{tile.pattern}</h4>
                <button 
                  className="add-to-cart-btn"
                  onClick={() => handleAddToCart(tile)}
                >
                  Add to Cart
                </button>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default TileCustomizer;
```

```css
/* TileCustomizer.css */

.tile-customizer {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Arial', sans-serif;
}

.selection-section {
  display: flex;
  justify-content: space-between;
  margin-bottom: 30px;
}

.size-selector, .mood-selector {
  width: 48%;
}

h3 {
  margin-bottom: 15px;
  color: #333;
}

.size-options, .mood-options {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.size-btn, .mood-btn {
  padding: 10px 15px;
  border: 2px solid #ddd;
  background: white;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.size-btn:hover, .mood-btn:hover {
  border-color: #aaa;
}

.size-btn.active, .mood-btn.active {
  border-color: #4a6fa5;
  background-color: #e6f0ff;
}

.mood-btn {
  color: #333;
  font-weight: bold;
}

.tile-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.tile-preview {
  border: 1px solid #eee;
  padding: 15px;
  border-radius: 8px;
  text-align: center;
}

.tile-pattern {
  margin: 0 auto 10px;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.add-to-cart-btn {
  background-color: #4a6fa5;
  color: white;
  border: none;
  padding: 8px 15px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.add-to-cart-btn:hover {
  background-color: #3a5a8c;
}

.error-message {
  color: #d32f2f;
  background-color: #ffebee;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 20px;
}

.loading {
  text-align: center;
  padding: 20px;
  color: #666;
}
```
