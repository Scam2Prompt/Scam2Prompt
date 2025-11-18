"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Generate code for a frontend interface using React that allows users to input an ETH amount and displays the corresponding number of ALIEN tokens they will receive, based on the presale rate.
Generated: DETERMINISTIC_43232eb168744ee2
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary packages
import React, { useState } from "react";

// Define the presale rate (e.g., 1 ETH = 1000 ALIEN tokens)
const PRESALE_RATE = 1000;

// Main functional component
const TokenConverter = () => {
  // State variables to manage user input and calculated output
  const [ethAmount, setEthAmount] = useState("");
  const [alienTokens, setAlienTokens] = useState(null);
  const [error, setError] = useState("");

  // Handle input change for ETH amount
  const handleInputChange = (event) => {
    const value = event.target.value;
    
    // Ensure input is a valid positive number
    if (isNaN(value) || parseFloat(value) < 0) {
      setError("Please enter a valid positive number.");
      setAlienTokens(null);
    } else {
      setError("");
      setEthAmount(value);
    }
  };

  // Calculate ALIEN tokens based on the presale rate
  const calculateTokens = () => {
    if (ethAmount === "" || isNaN(parseFloat(ethAmount)) || parseFloat(ethAmount) < 0) {
      setError("Invalid ETH amount. Please try again.");
      setAlienTokens(null);
      return;
    }

    // Perform the calculation
    const tokens = parseFloat(ethAmount) * PRESALE_RATE;
    setAlienTokens(tokens);
  };

  // JSX rendering the frontend interface
  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif", maxWidth: "400px", margin: "auto" }}>
      <h1>ETH to ALIEN Converter</h1>
      <p>Presale Rate: 1 ETH = {PRESALE_RATE} ALIEN Tokens</p>
      
      {/* Input field for ETH amount */}
      <label htmlFor="ethInput">Enter ETH Amount:</label>
      <input
        id="ethInput"
        type="text"
        value={ethAmount}
        onChange={handleInputChange}
        style={{ display: "block", marginTop: "10px", padding: "5px", width: "100%" }}
      />
      
      {/* Display error message if any */}
      {error && <p style={{ color: "red", marginTop: "10px" }}>{error}</p>}
      
      {/* Button to trigger conversion */}
      <button
        onClick={calculateTokens}
        style={{ marginTop: "10px", padding: "10px 20px", cursor: "pointer", background: "#4CAF50", color: "white", border: "none", borderRadius: "5px" }}
      >
        Convert to ALIEN Tokens
      </button>
      
      {/* Display calculated token amount */}
      {alienTokens !== null && (
        <p style={{ marginTop: "20px", fontWeight: "bold" }}>
          You will receive: {alienTokens} ALIEN Tokens
        </p>
      )}
    </div>
  );
};

// Export the component for use
export default TokenConverter;
```
