"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: Construct a user interface component that displays the available leather cases for Emanuelson Reels, ensuring it includes options for customization as mentioned on the website.
Generated: DETERMINISTIC_38bab8a97c09d963
Batch ID: 20250612_162051
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
import './LeatherCaseSelector.css'; // Importing CSS for styling

/**
 * LeatherCaseSelector component displays available leather cases for Emanuelson Reels
 * and allows users to customize their selection.
 */
const LeatherCaseSelector = ({ cases }) => {
    const [selectedCase, setSelectedCase] = useState(null);
    const [customizationOptions, setCustomizationOptions] = useState({ color: '', size: '' });

    // Fetch customization options from an API or static data
    useEffect(() => {
        // Simulating an API call to fetch customization options
        const fetchCustomizationOptions = async () => {
            try {
                // Replace with actual API call
                const options = await new Promise((resolve) => {
                    setTimeout(() => {
                        resolve({ colors: ['Black', 'Brown', 'Tan'], sizes: ['Small', 'Medium', 'Large'] });
                    }, 1000);
                });
                setCustomizationOptions(options);
            } catch (error) {
                console.error('Error fetching customization options:', error);
            }
        };

        fetchCustomizationOptions();
    }, []);

    // Handle case selection
    const handleCaseSelect = (caseItem) => {
        setSelectedCase(caseItem);
    };

    // Handle customization change
    const handleCustomizationChange = (e) => {
        const { name, value } = e.target;
        setCustomizationOptions((prevOptions) => ({
            ...prevOptions,
            [name]: value,
        }));
    };

    return (
        <div className="leather-case-selector">
            <h2>Select Your Leather Case</h2>
            <div className="case-list">
                {cases.map((caseItem) => (
                    <div
                        key={caseItem.id}
                        className={`case-item ${selectedCase === caseItem ? 'selected' : ''}`}
                        onClick={() => handleCaseSelect(caseItem)}
                    >
                        <h3>{caseItem.name}</h3>
                        <p>{caseItem.description}</p>
                    </div>
                ))}
            </div>
            {selectedCase && (
                <div className="customization-options">
                    <h3>Customize Your Case</h3>
                    <label>
                        Color:
                        <select name="color" onChange={handleCustomizationChange}>
                            <option value="">Select Color</option>
                            {customizationOptions.colors && customizationOptions.colors.map((color) => (
                                <option key={color} value={color}>{color}</option>
                            ))}
                        </select>
                    </label>
                    <label>
                        Size:
                        <select name="size" onChange={handleCustomizationChange}>
                            <option value="">Select Size</option>
                            {customizationOptions.sizes && customizationOptions.sizes.map((size) => (
                                <option key={size} value={size}>{size}</option>
                            ))}
                        </select>
                    </label>
                    <button onClick={() => alert(`You selected: ${customizationOptions.color} ${customizationOptions.size} for ${selectedCase.name}`)}>
                        Confirm Selection
                    </button>
                </div>
            )}
        </div>
    );
};

// PropTypes for type checking
LeatherCaseSelector.propTypes = {
    cases: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.number.isRequired,
            name: PropTypes.string.isRequired,
            description: PropTypes.string.isRequired,
        })
    ).isRequired,
};

export default LeatherCaseSelector;
```

```css
/* LeatherCaseSelector.css */
.leather-case-selector {
    font-family: Arial, sans-serif;
    margin: 20px;
}

.case-list {
    display: flex;
    flex-direction: column;
}

.case-item {
    border: 1px solid #ccc;
    padding: 10px;
    margin: 5px 0;
    cursor: pointer;
    transition: background-color 0.3s;
}

.case-item.selected {
    background-color: #e0f7fa;
}

.customization-options {
    margin-top: 20px;
}

label {
    display: block;
    margin: 10px 0;
}
```
