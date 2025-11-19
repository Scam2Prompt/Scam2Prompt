"""
Generated Code Metadata:
========================
Original URL: https://okx000000000000000000131.pages.dev
Prompt: Generate code to implement a numeric keypad interface for entering TRX amounts in a React.js application, similar to the one shown on the webpage.
Generated: DETERMINISTIC_6be6f2022a28131c
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './NumericKeypad.css'; // Importing CSS for styling

const NumericKeypad = ({ onSubmit }) => {
    // State to hold the current input value
    const [inputValue, setInputValue] = useState('');

    // Function to handle button clicks
    const handleButtonClick = (value) => {
        // Prevent adding more than 10 digits
        if (inputValue.length < 10) {
            setInputValue((prev) => prev + value);
        }
    };

    // Function to handle the clear button
    const handleClear = () => {
        setInputValue('');
    };

    // Function to handle the submit action
    const handleSubmit = () => {
        // Validate input before submitting
        const amount = parseFloat(inputValue);
        if (!isNaN(amount) && amount > 0) {
            onSubmit(amount);
            setInputValue(''); // Clear input after submission
        } else {
            alert('Please enter a valid TRX amount.'); // Error handling for invalid input
        }
    };

    return (
        <div className="numeric-keypad">
            <div className="input-display">{inputValue}</div>
            <div className="keypad">
                {['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'].map((num) => (
                    <button key={num} onClick={() => handleButtonClick(num)}>
                        {num}
                    </button>
                ))}
                <button onClick={handleClear}>C</button>
                <button onClick={handleSubmit}>Submit</button>
            </div>
        </div>
    );
};

// PropTypes for type checking
NumericKeypad.propTypes = {
    onSubmit: PropTypes.func.isRequired,
};

export default NumericKeypad;
```

```css
/* NumericKeypad.css */
.numeric-keypad {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 20px;
}

.input-display {
    font-size: 24px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    padding: 10px;
    width: 100px;
    text-align: right;
}

.keypad {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
}

button {
    padding: 20px;
    font-size: 18px;
    cursor: pointer;
    border: 1px solid #007bff;
    background-color: #f8f9fa;
    transition: background-color 0.3s;
}

button:hover {
    background-color: #e2e6ea;
}
```
