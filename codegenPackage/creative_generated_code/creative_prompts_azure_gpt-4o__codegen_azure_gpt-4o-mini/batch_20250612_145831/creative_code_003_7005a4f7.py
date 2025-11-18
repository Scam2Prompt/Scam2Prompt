"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solvexswap.pages.dev
Prompt: Provide a code example for implementing a "Max" button functionality for token swaps, similar to the Solvex Swap interface.
Generated: DETERMINISTIC_7005a4f70f925f82
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries for React and state management
import React, { useState } from 'react';

// MaxButton component definition
const MaxButton = ({ tokenBalance, onMaxSelect }) => {
  // Local state to hold the amount to swap
  const [amount, setAmount] = useState('');

  // Function to handle the max button click
  const handleMaxClick = () => {
    // Ensure we have a valid token balance
    if (tokenBalance > 0) {
      // Set the amount to the user's token balance
      setAmount(tokenBalance);
      // Call the onMaxSelect prop to notify the parent component
      onMaxSelect(tokenBalance);
    } else {
      console.error("Insufficient balance to select max.");
    }
  };

  return (
    <div>
      <input 
        type="text" 
        value={amount} 
        onChange={(e) => setAmount(e.target.value)} 
        placeholder="Enter amount" 
      />
      <button onClick={handleMaxClick} disabled={tokenBalance <= 0}>
        Max
      </button>
    </div>
  );
};

// Prop types validation for the MaxButton component
MaxButton.propTypes = {
  tokenBalance: PropTypes.number.isRequired, // The balance of tokens available for swap
  onMaxSelect: PropTypes.func.isRequired, // Callback function for when max is selected
};

export default MaxButton;
```
