"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-monprotocol.pages.dev
Prompt: Create a web interface using React.js that allows users to connect their wallets and view their MON Protocol presale allocations.
Generated: DETERMINISTIC_7437e47b22510409
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the requested code:

```jsx
// Import necessary dependencies
import React, { useState, useEffect } from "react";
import Web3 from "web3";
import "./App.css"; // Include any app-specific styles

// Define constants for contract interaction
const MONProtocolContractAddress = "0xYourContractAddressHere";
const MONProtocolABI = [
  // Replace with the ABI of the MON Protocol contract
];

// Main App Component
const App = () => {
  // State variables
  const [walletAddress, setWalletAddress] = useState(null);
  const [allocation, setAllocation] = useState(null);
  const [error, setError] = useState(null);

  // Function to connect wallet
  const connectWallet = async () => {
    try {
      if (window.ethereum) {
        const web3 = new Web3(window.ethereum);

        // Request account access
        const accounts = await window.ethereum.request({
          method: "eth_requestAccounts",
        });

        // Set wallet address
        setWalletAddress(accounts[0]);
        setError(null);
      } else {
        // If no wallet provider is detected
        setError("Please install MetaMask or another Ethereum wallet.");
      }
    } catch (err) {
      setError("Failed to connect wallet. Please try again.");
    }
  };

  // Function to fetch presale allocation
  const fetchAllocation = async () => {
    try {
      if (!walletAddress) {
        setError("Wallet not connected.");
        return;
      }

      const web3 = new Web3(window.ethereum);
      const contract = new web3.eth.Contract(
        MONProtocolABI,
        MONProtocolContractAddress
      );

      // Call the contract method to get the presale allocation
      const allocation = await contract.methods
        .getPresaleAllocation(walletAddress)
        .call();

      setAllocation(allocation);
      setError(null);
    } catch (err) {
      setError("Failed to fetch presale allocation. Please try again.");
    }
  };

  // Effect hook to clear allocation when wallet disconnects
  useEffect(() => {
    if (!walletAddress) {
      setAllocation(null);
    }
  }, [walletAddress]);

  return (
    <div className="App">
      <header className="App-header">
        <h1>MON Protocol Presale Dashboard</h1>
        {!walletAddress ? (
          <button onClick={connectWallet} className="connect-wallet-button">
            Connect Wallet
          </button>
        ) : (
          <div>
            <p>Connected Wallet: {walletAddress}</p>
            <button onClick={fetchAllocation} className="fetch-allocation-button">
              View Allocation
            </button>
          </div>
        )}
        {allocation !== null && (
          <p>Your Presale Allocation: {allocation} MON Tokens</p>
        )}
        {error && <p className="error-message">{error}</p>}
      </header>
    </div>
  );
};

export default App;
```

### Notes on Code:
1. Replace `0xYourContractAddressHere` and `MONProtocolABI` with the actual contract address and ABI of the MON Protocol contract.
2. Add proper CSS styling in `App.css` to design the UI as per requirements.
3. Ensure the `getPresaleAllocation` function exists in your smart contract and is properly defined in the ABI.
4. This code uses the MetaMask provider (`window.ethereum`) to interact with the blockchain.
5. Error messages are displayed to the user to handle edge cases gracefully.
