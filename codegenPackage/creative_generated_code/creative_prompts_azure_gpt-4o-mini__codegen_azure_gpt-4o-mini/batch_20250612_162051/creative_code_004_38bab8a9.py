"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emareels.se
Prompt: Construct a user interface component that displays the available leather cases for Emanuelson Reels, ensuring it includes options for customization as mentioned on the website.
Generated: DETERMINISTIC_38bab8a97c09d963
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

// Functional component for displaying available leather cases
const LeatherCaseSelector = ({ cases }) => {
    // State to manage selected case and customization options
    const [selectedCase, setSelectedCase] = useState(null);
    const [customization, setCustomization] = useState({
        color: '',
        size: '',
        engravings: false,
    });

    // Handler for case selection
    const handleCaseSelect = (caseId) => {
        const selected = cases.find((item) => item.id === caseId);
        setSelectedCase(selected);
    };

    // Handler for customization changes
    const handleCustomizationChange = (event) => {
        const { name, value } = event.target;
        setCustomization((prev) => ({
            ...prev,
            [name]: value,
        }));
    };

    // Handler for engravings toggle
    const toggleEngravings = () => {
        setCustomization((prev) => ({
            ...prev,
            engravings: !prev.engravings,
        }));
    };

    // Render the component
    return (
        <div className="leather-case-selector">
            <h2>Select Your Leather Case</h2>
            <ul>
                {cases.map((leatherCase) => (
                    <li key={leatherCase.id}>
                        <button onClick={() => handleCaseSelect(leatherCase.id)}>
                            {leatherCase.name}
                        </button>
                    </li>
                ))}
            </ul>
            {selectedCase && (
                <div className="customization-options">
                    <h3>Customize Your {selectedCase.name}</h3>
                    <label>
                        Color:
                        <select name="color" value={customization.color} onChange={handleCustomizationChange}>
                            <option value="">Select a color</option>
                            {selectedCase.availableColors.map((color) => (
                                <option key={color} value={color}>
                                    {color}
                                </option>
                            ))}
                        </select>
                    </label>
                    <label>
                        Size:
                        <select name="size" value={customization.size} onChange={handleCustomizationChange}>
                            <option value="">Select a size</option>
                            {selectedCase.availableSizes.map((size) => (
                                <option key={size} value={size}>
                                    {size}
                                </option>
                            ))}
                        </select>
                    </label>
                    <label>
                        <input
                            type="checkbox"
                            checked={customization.engravings}
                            onChange={toggleEngravings}
                        />
                        Engravings
                    </label>
                </div>
            )}
            {selectedCase && (
                <div className="summary">
                    <h4>Summary:</h4>
                    <p>Case: {selectedCase.name}</p>
                    <p>Color: {customization.color || 'Not selected'}</p>
                    <p>Size: {customization.size || 'Not selected'}</p>
                    <p>Engravings: {customization.engravings ? 'Yes' : 'No'}</p>
                </div>
            )}
        </div>
    );
};

// Prop types validation
LeatherCaseSelector.propTypes = {
    cases: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.string.isRequired,
            name: PropTypes.string.isRequired,
            availableColors: PropTypes.arrayOf(PropTypes.string).isRequired,
            availableSizes: PropTypes.arrayOf(PropTypes.string).isRequired,
        })
    ).isRequired,
};

export default LeatherCaseSelector;
```
