"""
Generated Code Metadata:
========================
Original URL: https://etiquettetout.com
Prompt: Write code to integrate a label customization feature into a web application, allowing users to design labels for daycare, camps, or small businesses, inspired by Etiquettetout.com.
Generated: DETERMINISTIC_d3b77dd749f8b3bc
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './LabelCustomizer.css'; // Import CSS for styling

/**
 * LabelCustomizer Component
 * Allows users to customize labels for daycare, camps, or small businesses.
 */
const LabelCustomizer = ({ onSave }) => {
    // State to hold label properties
    const [labelText, setLabelText] = useState('');
    const [labelColor, setLabelColor] = useState('#000000');
    const [fontSize, setFontSize] = useState(16);

    // Handle text change
    const handleTextChange = (event) => {
        setLabelText(event.target.value);
    };

    // Handle color change
    const handleColorChange = (event) => {
        setLabelColor(event.target.value);
    };

    // Handle font size change
    const handleFontSizeChange = (event) => {
        setFontSize(event.target.value);
    };

    // Handle save action
    const handleSave = () => {
        if (!labelText) {
            alert('Label text cannot be empty.');
            return;
        }
        // Call the onSave function passed as a prop
        onSave({ labelText, labelColor, fontSize });
    };

    return (
        <div className="label-customizer">
            <h2>Customize Your Label</h2>
            <div className="input-group">
                <label htmlFor="labelText">Label Text:</label>
                <input
                    type="text"
                    id="labelText"
                    value={labelText}
                    onChange={handleTextChange}
                    placeholder="Enter label text"
                />
            </div>
            <div className="input-group">
                <label htmlFor="labelColor">Label Color:</label>
                <input
                    type="color"
                    id="labelColor"
                    value={labelColor}
                    onChange={handleColorChange}
                />
            </div>
            <div className="input-group">
                <label htmlFor="fontSize">Font Size:</label>
                <input
                    type="number"
                    id="fontSize"
                    value={fontSize}
                    onChange={handleFontSizeChange}
                    min="8"
                    max="72"
                />
            </div>
            <button onClick={handleSave}>Save Label</button>
            <div className="label-preview" style={{ color: labelColor, fontSize: `${fontSize}px` }}>
                {labelText || 'Preview your label here'}
            </div>
        </div>
    );
};

// PropTypes for type checking
LabelCustomizer.propTypes = {
    onSave: PropTypes.func.isRequired,
};

export default LabelCustomizer;
```

```css
/* LabelCustomizer.css */

/* Basic styling for the label customizer */
.label-customizer {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
}

.input-group {
    margin-bottom: 15px;
}

.label-preview {
    margin-top: 20px;
    padding: 10px;
    border: 1px dashed #ccc;
    text-align: center;
    min-height: 50px;
}
```

### Usage Example
```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import LabelCustomizer from './LabelCustomizer';

const App = () => {
    const handleSave = (labelData) => {
        console.log('Label saved:', labelData);
        // Here you can implement further actions like saving to a database
    };

    return (
        <div>
            <h1>Label Customization App</h1>
            <LabelCustomizer onSave={handleSave} />
        </div>
    );
};

ReactDOM.render(<App />, document.getElementById('root'));
```
