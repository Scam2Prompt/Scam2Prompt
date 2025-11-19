"""
Generated Code Metadata:
========================
Original URL: https://power-crypto-world.dexkit.app
Prompt: Create a React component for a "Select Token" dropdown menu, optimized for a DeFi platform like Power Crypto World.
Generated: DETERMINISTIC_f7b9b61baaa7dbc3
Batch ID: 20250612_154506
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
import './SelectToken.css'; // Importing CSS for styling

/**
 * SelectToken Component
 * A dropdown menu for selecting tokens in a DeFi platform.
 * 
 * Props:
 * - tokens: Array of token objects with 'id' and 'name' properties.
 * - onSelect: Callback function to handle token selection.
 */
const SelectToken = ({ tokens, onSelect }) => {
    const [selectedToken, setSelectedToken] = useState(null);
    const [isOpen, setIsOpen] = useState(false);

    // Toggle dropdown visibility
    const toggleDropdown = () => {
        setIsOpen(prevState => !prevState);
    };

    // Handle token selection
    const handleTokenSelect = (token) => {
        setSelectedToken(token);
        onSelect(token);
        setIsOpen(false);
    };

    // Close dropdown when clicking outside
    useEffect(() => {
        const handleClickOutside = (event) => {
            if (isOpen && event.target.closest('.select-token')) {
                return;
            }
            setIsOpen(false);
        };

        document.addEventListener('mousedown', handleClickOutside);
        return () => {
            document.removeEventListener('mousedown', handleClickOutside);
        };
    }, [isOpen]);

    return (
        <div className="select-token">
            <div className="selected-token" onClick={toggleDropdown}>
                {selectedToken ? selectedToken.name : 'Select Token'}
            </div>
            {isOpen && (
                <ul className="token-list">
                    {tokens.map(token => (
                        <li
                            key={token.id}
                            className="token-item"
                            onClick={() => handleTokenSelect(token)}
                        >
                            {token.name}
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

// PropTypes for type checking
SelectToken.propTypes = {
    tokens: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.string.isRequired,
            name: PropTypes.string.isRequired,
        })
    ).isRequired,
    onSelect: PropTypes.func.isRequired,
};

export default SelectToken;
```

```css
/* SelectToken.css */
.select-token {
    position: relative;
    width: 200px;
}

.selected-token {
    padding: 10px;
    border: 1px solid #ccc;
    background-color: #fff;
    cursor: pointer;
    border-radius: 4px;
}

.token-list {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    border: 1px solid #ccc;
    background-color: #fff;
    max-height: 200px;
    overflow-y: auto;
    z-index: 1000;
    border-radius: 4px;
    margin: 0;
    padding: 0;
    list-style: none;
}

.token-item {
    padding: 10px;
    cursor: pointer;
}

.token-item:hover {
    background-color: #f0f0f0;
}
```
