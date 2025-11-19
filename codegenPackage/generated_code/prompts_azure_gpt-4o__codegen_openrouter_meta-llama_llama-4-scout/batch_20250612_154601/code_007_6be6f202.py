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

```jsx
import React, { useState } from 'react';

/**
 * NumericKeypad component for entering TRX amounts.
 * 
 * @param {Object} props - Component props.
 * @param {function} props.onChange - Callback function for handling amount changes.
 * @param {string} [props.initialValue=''] - Initial value for the amount input.
 */
function NumericKeypad({ onChange, initialValue = '' }) {
  const [amount, setAmount] = useState(initialValue);

  /**
   * Handles keypad button presses.
   * 
   * @param {string} value - Value of the pressed button.
   */
  const handleButtonPress = (value) => {
    switch (value) {
      case 'C':
        setAmount('');
        onChange('');
        break;
      case '.':
        if (!amount.includes('.')) {
          setAmount(`${amount}${value}`);
          onChange(`${amount}${value}`);
        }
        break;
      default:
        setAmount(`${amount}${value}`);
        onChange(`${amount}${value}`);
    }
  };

  return (
    <div className="numeric-keypad">
      <div className="keypad-display">{amount}</div>
      <div className="keypad-buttons">
        <button onClick={() => handleButtonPress('7')}>7</button>
        <button onClick={() => handleButtonPress('8')}>8</button>
        <button onClick={() => handleButtonPress('9')}>9</button>
        <button onClick={() => handleButtonPress('C')}>C</button>
        <button onClick={() => handleButtonPress('4')}>4</button>
        <button onClick={() => handleButtonPress('5')}>5</button>
        <button onClick={() => handleButtonPress('6')}>6</button>
        <button onClick={() => handleButtonPress('.')}>.</button>
        <button onClick={() => handleButtonPress('1')}>1</button>
        <button onClick={() => handleButtonPress('2')}>2</button>
        <button onClick={() => handleButtonPress('3')}>3</button>
        <button onClick={() => handleButtonPress('0')}>0</button>
      </div>
    </div>
  );
}

export default NumericKeypad;
```

```css
.numeric-keypad {
  display: inline-block;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.keypad-display {
  width: 100%;
  height: 40px;
  margin-bottom: 10px;
  padding: 10px;
  border: none;
  border-radius: 5px;
  font-size: 24px;
  text-align: right;
}

.keypad-buttons {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
}

.keypad-buttons button {
  height: 40px;
  border: none;
  border-radius: 5px;
  background-color: #f0f0f0;
  cursor: pointer;
}

.keypad-buttons button:hover {
  background-color: #e0e0e0;
}
```

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import NumericKeypad from './NumericKeypad';

const App = () => {
  const [amount, setAmount] = React.useState('');

  const handleAmountChange = (newAmount) => {
    setAmount(newAmount);
  };

  return (
    <div>
      <NumericKeypad onChange={handleAmountChange} />
      <p>Entered Amount: {amount}</p>
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));
```
