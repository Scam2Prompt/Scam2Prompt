"""
Generated Code Metadata:
========================
Original URL: https://okx-web3-tron-usdt-trc20-000000325.pages.dev
Prompt: Write code to integrate a numeric keypad for entering USDT (TRC-20) amounts in a web application, similar to the design described on the OKX platform.
Generated: DETERMINISTIC_4e8d5fec8c591225
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// NumericKeypad.js
import React, { useState } from 'react';

/**
 * Numeric keypad component for entering USDT (TRC-20) amounts.
 * 
 * @param {Object} props
 * @param {function} props.onChange - Callback function for when the amount changes.
 * @param {string} [props.value=''] - Initial amount value.
 */
const NumericKeypad = ({ onChange, value = '' }) => {
  const [amount, setAmount] = useState(value);

  const handleKeypadInput = (key) => {
    // Prevent excessive decimal points
    if (key === '.' && amount.includes('.')) return;

    // Prevent leading zeros
    if (key === '0' && amount === '') return;

    // Append or replace the input value
    const newAmount = amount + key;
    setAmount(newAmount);
    onChange(newAmount);
  };

  const handleDelete = () => {
    // Remove the last character
    const newAmount = amount.slice(0, -1);
    setAmount(newAmount);
    onChange(newAmount);
  };

  const handleClear = () => {
    // Reset the amount to empty string
    setAmount('');
    onChange('');
  };

  return (
    <div className="numeric-keypad">
      <div className="keypad-display">{amount}</div>
      <div className="keypad-grid">
        <button onClick={() => handleKeypadInput('1')}>1</button>
        <button onClick={() => handleKeypadInput('2')}>2</button>
        <button onClick={() => handleKeypadInput('3')}>3</button>
        <button onClick={() => handleKeypadInput('4')}>4</button>
        <button onClick={() => handleKeypadInput('5')}>5</button>
        <button onClick={() => handleKeypadInput('6')}>6</button>
        <button onClick={() => handleKeypadInput('7')}>7</button>
        <button onClick={() => handleKeypadInput('8')}>8</button>
        <button onClick={() => handleKeypadInput('9')}>9</button>
        <button onClick={handleDelete}>&#8592;</button>
        <button onClick={() => handleKeypadInput('0')}>0</button>
        <button onClick={() => handleKeypadInput('.')}>.</button>
        <button onClick={handleClear}>C</button>
      </div>
    </div>
  );
};

export default NumericKeypad;
```

```css
/* NumericKeypad.css */
.numeric-keypad {
  width: 250px;
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.keypad-display {
  width: 100%;
  height: 40px;
  margin-bottom: 20px;
  padding: 10px;
  border: none;
  border-radius: 10px;
  font-size: 24px;
  text-align: right;
  background-color: #f9f9f9;
}

.keypad-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 10px;
}

.keypad-grid button {
  height: 50px;
  border: none;
  border-radius: 10px;
  background-color: #4CAF50;
  color: #fff;
  cursor: pointer;
}

.keypad-grid button:hover {
  background-color: #3e8e41;
}
```

```javascript
// App.js
import React, { useState } from 'react';
import NumericKeypad from './NumericKeypad';

const App = () => {
  const [amount, setAmount] = useState('');

  const handleAmountChange = (newAmount) => {
    setAmount(newAmount);
  };

  return (
    <div>
      <h1>USDT (TRC-20) Amount Input</h1>
      <NumericKeypad onChange={handleAmountChange} value={amount} />
      <p>Entered Amount: {amount}</p>
    </div>
  );
};

export default App;
```
