"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allorashopping.com
Prompt: Create a React component for a multi-select dropdown menu that allows users to filter clothing items by material (e.g., organic cotton, wool blend) and style (e.g., business casual, streetwear, Y2K).
Generated: DETERMINISTIC_4c99f822b8fdd5e9
Batch ID: 20250612_155115
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
import './MultiSelectDropdown.css'; // Import custom styles

/**
 * MultiSelectDropdown component allows users to filter clothing items by material and style.
 * 
 * @param {Object} props - The properties passed to the component.
 * @param {Array} props.materialOptions - Array of material options for the dropdown.
 * @param {Array} props.styleOptions - Array of style options for the dropdown.
 * @param {Function} props.onFilterChange - Callback function when filter changes.
 * @returns {JSX.Element} The rendered component.
 */
const MultiSelectDropdown = ({ materialOptions, styleOptions, onFilterChange }) => {
    const [selectedMaterials, setSelectedMaterials] = useState([]);
    const [selectedStyles, setSelectedStyles] = useState([]);

    /**
     * Handles the selection of materials.
     * 
     * @param {string} material - The selected material.
     */
    const toggleMaterial = (material) => {
        const updatedMaterials = selectedMaterials.includes(material)
            ? selectedMaterials.filter(m => m !== material)
            : [...selectedMaterials, material];
        setSelectedMaterials(updatedMaterials);
        onFilterChange(updatedMaterials, selectedStyles);
    };

    /**
     * Handles the selection of styles.
     * 
     * @param {string} style - The selected style.
     */
    const toggleStyle = (style) => {
        const updatedStyles = selectedStyles.includes(style)
            ? selectedStyles.filter(s => s !== style)
            : [...selectedStyles, style];
        setSelectedStyles(updatedStyles);
        onFilterChange(selectedMaterials, updatedStyles);
    };

    return (
        <div className="multi-select-dropdown">
            <div className="dropdown-section">
                <h4>Materials</h4>
                {materialOptions.map((material) => (
                    <label key={material}>
                        <input
                            type="checkbox"
                            checked={selectedMaterials.includes(material)}
                            onChange={() => toggleMaterial(material)}
                        />
                        {material}
                    </label>
                ))}
            </div>
            <div className="dropdown-section">
                <h4>Styles</h4>
                {styleOptions.map((style) => (
                    <label key={style}>
                        <input
                            type="checkbox"
                            checked={selectedStyles.includes(style)}
                            onChange={() => toggleStyle(style)}
                        />
                        {style}
                    </label>
                ))}
            </div>
        </div>
    );
};

// PropTypes for type checking
MultiSelectDropdown.propTypes = {
    materialOptions: PropTypes.arrayOf(PropTypes.string).isRequired,
    styleOptions: PropTypes.arrayOf(PropTypes.string).isRequired,
    onFilterChange: PropTypes.func.isRequired,
};

export default MultiSelectDropdown;
```

### CSS (MultiSelectDropdown.css)
```css
.multi-select-dropdown {
    display: flex;
    flex-direction: column;
}

.dropdown-section {
    margin-bottom: 1em;
}

label {
    display: block;
    margin: 0.5em 0;
    cursor: pointer;
}
```

### Usage Example
```javascript
import React from 'react';
import MultiSelectDropdown from './MultiSelectDropdown';

const App = () => {
    const materials = ['Organic Cotton', 'Wool Blend', 'Polyester', 'Linen'];
    const styles = ['Business Casual', 'Streetwear', 'Y2K', 'Athleisure'];

    const handleFilterChange = (materials, styles) => {
        console.log('Selected Materials:', materials);
        console.log('Selected Styles:', styles);
    };

    return (
        <div>
            <h1>Clothing Filter</h1>
            <MultiSelectDropdown
                materialOptions={materials}
                styleOptions={styles}
                onFilterChange={handleFilterChange}
            />
        </div>
    );
};

export default App;
```
