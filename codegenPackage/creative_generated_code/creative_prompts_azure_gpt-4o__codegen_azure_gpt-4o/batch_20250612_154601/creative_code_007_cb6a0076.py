"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okx-web3-usdt-trc20-payfor-00000017.pages.dev
Prompt: Create a user interface component in React for entering USDT amounts, including a keypad and balance display, inspired by the OKX payment page.
Generated: DETERMINISTIC_cb6a0076afa86a9d
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState } from "react";
import PropTypes from "prop-types";
import "./USDTInput.css"; // Include a corresponding CSS file for styling

/**
 * USDTInput Component
 * A user interface for entering USDT amounts with a keypad and balance display.
 *
 * Props:
 * - balance: Number - The user's current USDT balance
 * - onConfirm: Function - Callback function to handle the confirmed USDT amount
 */
const USDTInput = ({ balance, onConfirm }) => {
  const [amount, setAmount] = useState("");

  // Handle keypad button click
  const handleInput = (value) => {
    const newAmount = `${amount}${value}`;
    if (Number(newAmount) <= balance) {
      setAmount(newAmount);
    }
  };

  // Delete the last digit
  const handleDelete = () => {
    setAmount(amount.slice(0, -1));
  };

  // Confirm the entered amount
  const handleConfirm = () => {
    if (amount && Number(amount) <= balance) {
      onConfirm(Number(amount));
    } else {
      alert("Invalid amount or insufficient balance!");
    }
  };

  return (
    <div className="usdt-input">
      {/* Display current balance */}
      <div className="balance-display">
        <span>Balance: </span>
        <strong>{balance.toFixed(2)} USDT</strong>
      </div>

      {/* Input amount display */}
      <div className="amount-display">
        <span>Amount: </span>
        <strong>{amount || "0"} USDT</strong>
      </div>

      {/* Keypad for entering the amount */}
      <div className="keypad">
        {[1, 2, 3, 4, 5, 6, 7, 8, 9, ".", 0].map((key) => (
          <button
            key={key}
            className="keypad-button"
            onClick={() => handleInput(key)}
            disabled={key === "." && amount.includes(".")} // Prevent multiple dots
          >
            {key}
          </button>
        ))}
        <button className="keypad-button delete" onClick={handleDelete}>
          ⌫
        </button>
      </div>

      {/* Confirm button */}
      <button className="confirm-button" onClick={handleConfirm}>
        Confirm
      </button>
    </div>
  );
};

// Prop types for validation
USDTInput.propTypes = {
  balance: PropTypes.number.isRequired,
  onConfirm: PropTypes.func.isRequired,
};

export default USDTInput;
```

```css
/* USDTInput.css */
.usdt-input {
  font-family: Arial, sans-serif;
  max-width: 300px;
  margin: 0 auto;
  text-align: center;
}

.balance-display,
.amount-display {
  margin-bottom: 20px;
  font-size: 1.2em;
}

.keypad {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

.keypad-button {
  padding: 15px;
  font-size: 1.2em;
  border: 1px solid #ccc;
  background-color: #f9f9f9;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.keypad-button:hover {
  background-color: #e0e0e0;
}

.keypad-button.delete {
  background-color: #ffcccc;
}

.keypad-button.delete:hover {
  background-color: #ff9999;
}

.confirm-button {
  margin-top: 20px;
  padding: 15px;
  font-size: 1.2em;
  border: none;
  background-color: #4caf50;
  color: white;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.confirm-button:hover {
  background-color: #45a049;
}
```
