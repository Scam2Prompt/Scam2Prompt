"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-sdk-demo.pages.dev
Prompt: Write a JavaScript function using the MetaMask SDK to fetch the current network ID and display it in a React component.
Generated: DETERMINISTIC_697dcc4e4f398187
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary dependencies
import React, { useState, useEffect } from "react";
import { ethers } from "ethers"; // MetaMask SDK is compatible with ethers.js

// React Component to display the current network ID
const NetworkIdDisplay = () => {
  const [networkId, setNetworkId] = useState(null);
  const [error, setError] = useState(null);

  // Function to fetch the current network ID using MetaMask
  const fetchNetworkId = async () => {
    try {
      // Check if MetaMask is installed
      if (!window.ethereum) {
        throw new Error("MetaMask is not installed. Please install MetaMask.");
      }

      // Use ethers to create a provider from MetaMask
      const provider = new ethers.providers.Web3Provider(window.ethereum);

      // Get the network details
      const network = await provider.getNetwork();

      // Update the state with the network ID
      setNetworkId(network.chainId);
    } catch (err) {
      // Handle errors gracefully
      setError(err.message);
    }
  };

  // Fetch the network ID on component mount
  useEffect(() => {
    fetchNetworkId();
  }, []);

  return (
    <div>
      <h1>Current Network ID</h1>
      {error ? (
        // Display error message if there's an error
        <p style={{ color: "red" }}>Error: {error}</p>
      ) : networkId !== null ? (
        // Display the network ID if fetched successfully
        <p>Network ID: {networkId}</p>
      ) : (
        // Display a loading message while fetching the network ID
        <p>Loading...</p>
      )}
    </div>
  );
};

export default NetworkIdDisplay;
```
