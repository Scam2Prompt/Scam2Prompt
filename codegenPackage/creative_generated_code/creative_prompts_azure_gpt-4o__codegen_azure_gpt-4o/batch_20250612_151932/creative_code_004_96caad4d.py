"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-dapp.vercel.app
Prompt: Write a script to query a specific contract deployed on StarkNet and display its data in a React-based dApp.
Generated: DETERMINISTIC_96caad4ddae6ca69
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

### React Application Code to Query StarkNet Contract

```javascript
// File: src/App.js

import React, { useState } from "react";
import { connect, Contract } from "starknet";

// React app to query a StarkNet contract and display its data
const App = () => {
  // State hooks for contract data and errors
  const [contractData, setContractData] = useState(null);
  const [error, setError] = useState(null);

  // Contract information
  const CONTRACT_ADDRESS = "0x0123456789abcdef0123456789abcdef0123456789abcdef"; // Replace with your contract address
  const CONTRACT_ABI = [ /* Add your ABI here */ ]; // Provide the ABI for the contract being queried

  // Function to query the contract
  const queryContract = async () => {
    try {
      // Connect to StarkNet wallet
      const provider = connect(); // Assumes StarkNet wallet is injected in the browser

      // Create a contract instance
      const contract = new Contract(CONTRACT_ABI, CONTRACT_ADDRESS, provider);

      // Call a contract method (example: `get_data`)
      const result = await contract.call("get_data");

      // Update state with contract data
      setContractData(result);
    } catch (err) {
      // Handle errors gracefully
      console.error("Error querying contract:", err);
      setError(err.message || "An unexpected error occurred");
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>StarkNet Contract Query</h1>
      <button onClick={queryContract}>Query Contract</button>
      <div style={{ marginTop: "1rem" }}>
        {error && <p style={{ color: "red" }}>Error: {error}</p>}
        {contractData ? (
          <div>
            <h2>Contract Data:</h2>
            <pre>{JSON.stringify(contractData, null, 2)}</pre>
          </div>
        ) : (
          <p>No data fetched yet.</p>
        )}
      </div>
    </div>
  );
};

export default App;
```

```javascript
// File: src/index.js

import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

// Render the React app
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);
```

```javascript
// File: src/config.js

// Configuration file for StarkNet-related constants
export const CONTRACT_ADDRESS = "0x0123456789abcdef0123456789abcdef0123456789abcdef"; // Replace with your contract address
export const CONTRACT_ABI = [ /* Add your ABI here */ ]; // Replace with the ABI of your contract
```

```javascript
// File: src/utils.js

// Utility function to handle StarkNet provider connection
import { connect } from "starknet";

export const getStarkNetProvider = () => {
  try {
    const provider = connect(); // Assumes wallet is injected
    if (!provider) {
      throw new Error("StarkNet wallet not detected");
    }
    return provider;
  } catch (error) {
    throw new Error(`Failed to connect to StarkNet: ${error.message}`);
  }
};
```
