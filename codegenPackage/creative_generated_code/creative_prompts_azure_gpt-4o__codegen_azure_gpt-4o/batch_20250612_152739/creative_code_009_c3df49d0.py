"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecom.pages.dev
Prompt: Create a frontend application using React that displays the JESSE token presale details, including the pricing tiers and total supply, and allows users to purchase tokens.
Generated: DETERMINISTIC_c3df49d003bd1b8c
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: src/App.js

import React, { useState, useEffect } from "react";
import axios from "axios";

// App Component
const App = () => {
  // State variables
  const [pricingTiers, setPricingTiers] = useState([]);
  const [totalSupply, setTotalSupply] = useState(0);
  const [purchaseAmount, setPurchaseAmount] = useState(0);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  // Fetch presale details on component mount
  useEffect(() => {
    const fetchPresaleDetails = async () => {
      try {
        setIsLoading(true);
        const response = await axios.get("/api/presale-details"); // Replace with actual API endpoint
        setPricingTiers(response.data.pricingTiers);
        setTotalSupply(response.data.totalSupply);
        setIsLoading(false);
      } catch (err) {
        setError("Failed to fetch presale details");
        setIsLoading(false);
      }
    };

    fetchPresaleDetails();
  }, []);

  // Handle token purchase
  const handlePurchase = async () => {
    try {
      setIsLoading(true);
      setError(null);

      // Validate the purchase amount
      if (purchaseAmount <= 0) {
        setError("Enter a valid token amount");
        setIsLoading(false);
        return;
      }

      // Send POST request to purchase tokens
      const response = await axios.post("/api/purchase-tokens", {
        amount: purchaseAmount, // Replace with the actual API endpoint and payload format
      });

      alert("Purchase successful! Transaction details: " + JSON.stringify(response.data));
      setPurchaseAmount(0); // Reset the purchase amount
      setIsLoading(false);
    } catch (err) {
      setError("Failed to purchase tokens. Please try again.");
      setIsLoading(false);
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>JESSE Token Presale</h1>

      {/* Display loading and error states */}
      {isLoading && <p>Loading...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}

      {/* Display total supply */}
      <div>
        <h2>Total Supply: {totalSupply} JESSE Tokens</h2>
      </div>

      {/* Display pricing tiers */}
      <div>
        <h2>Pricing Tiers</h2>
        <ul>
          {pricingTiers.map((tier, index) => (
            <li key={index}>
              {tier.tokens} tokens for {tier.price} USD
            </li>
          ))}
        </ul>
      </div>

      {/* Token purchase section */}
      <div style={{ marginTop: "20px" }}>
        <h2>Purchase Tokens</h2>
        <input
          type="number"
          placeholder="Enter token amount"
          value={purchaseAmount}
          onChange={(e) => setPurchaseAmount(Number(e.target.value))}
          style={{ marginRight: "10px", padding: "5px" }}
        />
        <button onClick={handlePurchase} style={{ padding: "5px 10px" }}>
          Purchase
        </button>
      </div>
    </div>
  );
};

export default App;

// File: src/index.js

import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

// Render the App component into the DOM
ReactDOM.render(<App />, document.getElementById("root"));

// File: public/index.html

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>JESSE Token Presale</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>

// File: package.json (Ensure you install the required dependencies)

{
  "name": "jesse-token-presale",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "axios": "^1.4.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}
```

This code assumes the existence of an API backend that provides the presale details and handles token purchases. Replace the `/api/presale-details` and `/api/purchase-tokens` endpoints with actual API endpoints.
