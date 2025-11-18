"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jesse-presale-8r8.pages.dev
Prompt: Implement a feature in a React application that allows users to input BASE amounts and see the equivalent JESSE tokens they would receive, based on the presale rate.
Generated: DETERMINISTIC_476145242a819f09
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries and hooks from React
import React, { useState } from 'react';

// Function to convert BASE amount to JESSE tokens based on a predefined presale rate
const BASE_TO_JESSE_RATE = 100; // Presale rate: 1 BASE = 100 JESSE tokens

const TokenConverter = () => {
  // State to hold the BASE amount input and the calculated JESSE tokens
  const [baseAmount, setBaseAmount] = useState('');
  const [jesseTokens, setJesseTokens] = useState(null);
  
  // Function to handle input change
  const handleInputChange = (event) => {
    const value = event.target.value;
    
    // Update the BASE amount state
    setBaseAmount(value);
    
    // Validate input and calculate JESSE tokens
    if (!isNaN(value) && value.trim() !== '') {
      const tokens = parseFloat(value) * BASE_TO_JESSE_RATE;
      setJesseTokens(tokens);
    } else {
      // Reset JESSE tokens if the input is invalid
      setJesseTokens(null);
    }
  };

  return (
    <div>
      <h2>BASE to JESSE Token Converter</h2>
      <label htmlFor="baseAmount">Enter BASE Amount:</label>
      <input
        type="number"
        id="baseAmount"
        value={baseAmount}
        onChange={handleInputChange}
        placeholder="Enter amount"
        min="0"
        step="0.01"
      />
      <div>
        {jesseTokens !== null && (
          <p>
            You will receive <strong>{jesseTokens}</strong> JESSE tokens.
          </p>
        )}
      </div>
    </div>
  );
};

// Exporting the TokenConverter component for use in other parts of the application
export default TokenConverter;
```
