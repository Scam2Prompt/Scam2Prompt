"""
Generated Code Metadata:
========================
Original URL: https://memefi-club.pages.dev
Prompt: Develop a React component for navigating MemeFi’s interactive fantasy map, allowing users to explore Vice City and other territories.
Generated: DETERMINISTIC_a7ed2c2c2013d5a6
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './MemeFiMap.css'; // Importing CSS for styling

/**
 * MemeFiMap Component
 * A React component that allows users to navigate an interactive fantasy map of Vice City and other territories.
 */
const MemeFiMap = ({ territories }) => {
    const [currentTerritory, setCurrentTerritory] = useState(null);

    useEffect(() => {
        // Set the initial territory to the first one in the list if available
        if (territories.length > 0) {
            setCurrentTerritory(territories[0]);
        }
    }, [territories]);

    /**
     * Handles territory selection
     * @param {Object} territory - The selected territory object
     */
    const handleTerritorySelect = (territory) => {
        setCurrentTerritory(territory);
    };

    return (
        <div className="memeFiMap">
            <h1>MemeFi Interactive Map</h1>
            <div className="territory-list">
                {territories.map((territory) => (
                    <button
                        key={territory.id}
                        className={`territory-button ${currentTerritory?.id === territory.id ? 'active' : ''}`}
                        onClick={() => handleTerritorySelect(territory)}
                    >
                        {territory.name}
                    </button>
                ))}
            </div>
            {currentTerritory && (
                <div className="territory-details">
                    <h2>{currentTerritory.name}</h2>
                    <p>{currentTerritory.description}</p>
                    <img src={currentTerritory.image} alt={currentTerritory.name} />
                </div>
            )}
        </div>
    );
};

// PropTypes for type checking
MemeFiMap.propTypes = {
    territories: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.string.isRequired,
            name: PropTypes.string.isRequired,
            description: PropTypes.string.isRequired,
            image: PropTypes.string.isRequired,
        })
    ).isRequired,
};

export default MemeFiMap;
```

```css
/* MemeFiMap.css */
.memeFiMap {
    font-family: Arial, sans-serif;
    padding: 20px;
}

.territory-list {
    display: flex;
    flex-wrap: wrap;
    margin-bottom: 20px;
}

.territory-button {
    margin: 5px;
    padding: 10px 15px;
    border: none;
    background-color: #007bff;
    color: white;
    cursor: pointer;
    border-radius: 5px;
    transition: background-color 0.3s;
}

.territory-button:hover {
    background-color: #0056b3;
}

.territory-button.active {
    background-color: #0056b3;
}

.territory-details {
    border: 1px solid #ccc;
    padding: 15px;
    border-radius: 5px;
}

.territory-details img {
    max-width: 100%;
    height: auto;
    border-radius: 5px;
}
```
