"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafkreifcnpktapdtapj76jqfg5h4rszqmvsurv5ynmixd4gjkfrhunxfiu.ipfs.dweb.link
Prompt: Provide an example of how to integrate a "Connect Wallet" button into a React-based dApp for Arrow Markets.
Generated: DETERMINISTIC_b02000110c18a8d7
Batch ID: 20250612_152249
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
import { ethers } from "ethers";

// Create a functional React component
const ConnectWalletButton = () => {
  // State to hold wallet connection status and address
  const [walletAddress, setWalletAddress] = useState(null);
  const [errorMessage, setErrorMessage] = useState(null);

  // Function to connect to the user's wallet
  const connectWallet = async () => {
    try {
      // Check if the browser has a MetaMask-compatible provider
      if (!window.ethereum) {
        throw new Error("MetaMask not detected. Please install MetaMask.");
      }

      // Request account access
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const accounts = await provider.send("eth_requestAccounts", []);

      // Update the React state with the connected wallet address
      setWalletAddress(accounts[0]);
      setErrorMessage(null); // Clear any previous error messages
    } catch (error) {
      // Handle errors gracefully
      setErrorMessage(error.message);
      setWalletAddress(null); // Reset the address on error
    }
  };

  return (
    <div>
      {/* Display the Connect Wallet button */}
      <button
        onClick={connectWallet}
        style={{
          padding: "10px 20px",
          fontSize: "16px",
          backgroundColor: "#4CAF50",
          color: "#FFF",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer",
        }}
      >
        {walletAddress ? "Wallet Connected" : "Connect Wallet"}
      </button>

      {/* Display the connected wallet address */}
      {walletAddress && (
        <p style={{ marginTop: "10px", color: "#4CAF50" }}>
          Connected Wallet: <strong>{walletAddress}</strong>
        </p>
      )}

      {/* Display error messages if any */}
      {errorMessage && (
        <p style={{ marginTop: "10px", color: "red" }}>{errorMessage}</p>
      )}
    </div>
  );
};

export default ConnectWalletButton;
```
