"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okx000000000000000000131.pages.dev
Prompt: Generate code to implement a numeric keypad interface for entering TRX amounts in a React.js application, similar to the one shown on the webpage.
Generated: DETERMINISTIC_6be6f2022a28131c
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// NumericKeypad.jsx
import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './NumericKeypad.css'; // Ensure to create and style this CSS file

const NumericKeypad = ({ onSubmit, maxLength }) => {
  const [inputValue, setInputValue] = useState('');

  // Function to handle button click
  const handleButtonClick = (value) => {
    if (value === 'CLEAR') {
      setInputValue('');
    } else if (value === 'BACKSPACE') {
      setInputValue(inputValue.slice(0, -1));
    } else {
      if (inputValue.length < maxLength) {
        setInputValue(inputValue + value);
      }
    }
  };

  // Function to handle form submission
  const handleSubmit = () => {
    if (inputValue.trim()) {
      onSubmit(parseFloat(inputValue)); // Pass entered amount to parent
      setInputValue(''); // Clear input after submission
    } else {
      alert('Please enter a valid amount.'); // Basic error handling
    }
  };

  return (
    <div className="numeric-keypad">
      {/* Display the entered value */}
      <div className="display">{inputValue || 'Enter Amount'}</div>

      {/* Keypad buttons */}
      <div className="keypad-buttons">
        {['1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '0'].map((key) => (
          <button
            key={key}
            onClick={() => handleButtonClick(key)}
            className="keypad-button"
          >
            {key}
          </button>
        ))}
        <button
          onClick={() => handleButtonClick('BACKSPACE')}
          className="keypad-button action-button"
        >
          ⌫
        </button>
        <button
          onClick={() => handleButtonClick('CLEAR')}
          className="keypad-button action-button"
        >
          C
        </button>
      </div>

      {/* Submit button */}
      <button onClick={handleSubmit} className="submit-button">
        Submit
      </button>
    </div>
  );
};

// Prop validation
NumericKeypad.propTypes = {
  onSubmit: PropTypes.func.isRequired, // Callback function to handle the submitted amount
  maxLength: PropTypes.number, // Maximum length for the entered value
};

// Default props
NumericKeypad.defaultProps = {
  maxLength: 10, // Default maximum length of input
};

export default NumericKeypad;

// NumericKeypad.css (Example CSS)
// Style this file as needed for your application's design
/*
.numeric-keypad {
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 300px;
  margin: 0 auto;
}

.display {
  width: 100%;
  padding: 10px;
  text-align: center;
  font-size: 1.5rem;
  border: 1px solid #ccc;
  margin-bottom: 10px;
}

.keypad-buttons {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

.keypad-button {
  padding: 15px;
  font-size: 1.2rem;
  cursor: pointer;
  background-color: #f0f0f0;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.action-button {
  background-color: #ffcccc;
  color: #333;
}

.submit-button {
  margin-top: 10px;
  padding: 10px 20px;
  font-size: 1.2rem;
  background-color: #4caf50;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
*/
```
