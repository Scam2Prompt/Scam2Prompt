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

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './TileCollection.css'; // Importing CSS for styling

/**
 * TileCollection Component
 * Displays different types of tiles with interactive previews.
 */
const TileCollection = ({ tiles }) => {
    const [selectedTile, setSelectedTile] = useState(null);

    /**
     * Handles tile selection
     * @param {Object} tile - The tile object to select
     */
    const handleTileSelect = (tile) => {
        setSelectedTile(tile);
    };

    return (
        <div className="tile-collection">
            <h1>ITACA Ceramic Tile Collections</h1>
            <div className="tiles">
                {tiles.map((tile) => (
                    <div 
                        key={tile.id} 
                        className="tile" 
                        onClick={() => handleTileSelect(tile)}
                        role="button" 
                        tabIndex={0}
                        onKeyPress={(e) => e.key === 'Enter' && handleTileSelect(tile)} // Accessibility
                    >
                        <img src={tile.image} alt={tile.name} className="tile-image" />
                        <h2 className="tile-name">{tile.name}</h2>
                        <p className="tile-dimensions">{tile.dimensions}</p>
                    </div>
                ))}
            </div>

            {selectedTile && (
                <div className="tile-preview">
                    <h2>Selected Tile: {selectedTile.name}</h2>
                    <img src={selectedTile.image} alt={selectedTile.name} className="preview-image" />
                    <p>{selectedTile.description}</p>
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

**CSS (TileCollection.css)**

```css
.tile-collection {
    text-align: center;
}

.tiles {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.tile {
    margin: 15px;
    cursor: pointer;
    border: 1px solid #ccc;
    border-radius: 8px;
    overflow: hidden;
    transition: transform 0.2s;
}

.tile:hover {
    transform: scale(1.05);
}

.tile-image {
    width: 100%;
    height: auto;
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
    border: 2px solid #007BFF;
    padding: 10px;
    border-radius: 8px;
}

.preview-image {
    width: 100%;
    height: auto;
}
```

**Usage Example**

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import TileCollection from './TileCollection';

const tilesData = [
    {
        id: '1',
        name: 'Slab Tile A',
        dimensions: '600x600 mm',
        image: 'path/to/slab-tile-a.jpg',
        description: 'Description of Slab Tile A',
    },
    {
        id: '2',
        name: 'Vitrified Tile B',
        dimensions: '300x600 mm',
        image: 'path/to/vitrified-tile-b.jpg',
        description: 'Description of Vitrified Tile B',
    },
    {
        id: '3',
        name: 'Wall Tile C',
        dimensions: '200x300 mm',
        image: 'path/to/wall-tile-c.jpg',
        description: 'Description of Wall Tile C',
    },
];

ReactDOM.render(<TileCollection tiles={tilesData} />, document.getElementById('root'));
```

Make sure to replace the image paths in `tilesData` with the actual paths to your tile images.
