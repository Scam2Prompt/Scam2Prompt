"""
Generated Code Metadata:
========================
Original URL: https://aydinspirate.com
Prompt: Write JavaScript code to create a user interface for controlling "Toldos Verticales" awnings, referencing the customization options mentioned on the Ayd Inspirate website.
Generated: DETERMINISTIC_28dc9dbf214b4d40
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// AwningsController.js

// Import necessary libraries
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './AwningsController.css'; // Importing CSS for styling

/**
 * AwningsController component for controlling Toldos Verticales awnings.
 * This component allows users to customize their awning options.
 */
const AwningsController = ({ awningOptions }) => {
    // State to hold selected options
    const [selectedOptions, setSelectedOptions] = useState({
        color: '',
        size: '',
        motorized: false,
    });

    // Handle changes in the selection
    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        setSelectedOptions((prevOptions) => ({
            ...prevOptions,
            [name]: type === 'checkbox' ? checked : value,
        }));
    };

    // Handle form submission
    const handleSubmit = (e) => {
        e.preventDefault();
        // Validate selected options
        if (!selectedOptions.color || !selectedOptions.size) {
            alert('Please select both color and size options.');
            return;
        }
        // Process the selected options (e.g., send to server)
        console.log('Selected Options:', selectedOptions);
        alert('Awnings configuration submitted successfully!');
    };

    return (
        <div className="awnings-controller">
            <h1>Toldos Verticales Customization</h1>
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="color">Select Color:</label>
                    <select
                        name="color"
                        id="color"
                        value={selectedOptions.color}
                        onChange={handleChange}
                        required
                    >
                        <option value="">--Choose a color--</option>
                        {awningOptions.colors.map((color) => (
                            <option key={color} value={color}>
                                {color}
                            </option>
                        ))}
                    </select>
                </div>

                <div className="form-group">
                    <label htmlFor="size">Select Size:</label>
                    <select
                        name="size"
                        id="size"
                        value={selectedOptions.size}
                        onChange={handleChange}
                        required
                    >
                        <option value="">--Choose a size--</option>
                        {awningOptions.sizes.map((size) => (
                            <option key={size} value={size}>
                                {size}
                            </option>
                        ))}
                    </select>
                </div>

                <div className="form-group">
                    <label>
                        <input
                            type="checkbox"
                            name="motorized"
                            checked={selectedOptions.motorized}
                            onChange={handleChange}
                        />
                        Motorized
                    </label>
                </div>

                <button type="submit">Submit Configuration</button>
            </form>
        </div>
    );
};

// PropTypes for type checking
AwningsController.propTypes = {
    awningOptions: PropTypes.shape({
        colors: PropTypes.arrayOf(PropTypes.string).isRequired,
        sizes: PropTypes.arrayOf(PropTypes.string).isRequired,
    }).isRequired,
};

export default AwningsController;
```

```css
/* AwningsController.css */

.awnings-controller {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
}

select {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    padding: 10px 15px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
```

### Usage Example
```javascript
// App.js

import React from 'react';
import AwningsController from './AwningsController';

const awningOptions = {
    colors: ['Red', 'Blue', 'Green', 'Yellow'],
    sizes: ['Small', 'Medium', 'Large'],
};

const App = () => {
    return (
        <div>
            <AwningsController awningOptions={awningOptions} />
        </div>
    );
};

export default App;
```
