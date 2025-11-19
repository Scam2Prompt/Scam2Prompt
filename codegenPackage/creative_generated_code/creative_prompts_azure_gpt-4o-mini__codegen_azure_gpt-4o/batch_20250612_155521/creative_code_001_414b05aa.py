"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://move-e87.pages.dev
Prompt: Write a code snippet to integrate EVM wallet connection for the MoveDrop feature on the Movement site.
Generated: DETERMINISTIC_414b05aa1ed674d3
Batch ID: 20250612_155521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { useState, useEffect } from "react";
import Web3 from "web3";

// EVM Wallet Connection Component for MoveDrop feature
const WalletConnection = () => {
  // State to hold wallet address and connection status
  const [walletAddress, setWalletAddress] = useState(null);
  const [isConnected, setIsConnected] = useState(false);
  const [error, setError] = useState(null);

  // Function to connect to the wallet
  const connectWallet = async () => {
    try {
      // Check if the browser supports Ethereum via MetaMask or another provider
      if (window.ethereum) {
        const web3 = new Web3(window.ethereum);

        // Request user wallet connection
        const accounts = await window.ethereum.request({
          method: "eth_requestAccounts",
        });

        if (accounts.length > 0) {
          setWalletAddress(accounts[0]); // Set the first wallet address
          setIsConnected(true); // Update connection status
        } else {
          throw new Error("No accounts found.");
        }
      } else {
        throw new Error("Ethereum provider not found. Please install MetaMask.");
      }
    } catch (err) {
      setError(err.message); // Capture and store error message
    }
  };

  // Function to disconnect the wallet
  const disconnectWallet = () => {
    setWalletAddress(null); // Clear wallet address
    setIsConnected(false); // Update connection status
    setError(null); // Clear any previous errors
  };

  // Automatically attempt wallet connection on component mount
  useEffect(() => {
    const checkWalletConnection = async () => {
      if (window.ethereum) {
        try {
          const web3 = new Web3(window.ethereum);
          const accounts = await web3.eth.getAccounts();

          if (accounts.length > 0) {
            setWalletAddress(accounts[0]);
            setIsConnected(true);
          }
        } catch (err) {
          console.error("Automatic wallet connection failed:", err.message);
        }
      }
    };

    checkWalletConnection();
  }, []);

  return (
    <div>
      <h2>MoveDrop Feature - Wallet Connection</h2>
      {error && <p style={{ color: "red" }}>Error: {error}</p>}
      {!isConnected && (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
      {isConnected && (
        <div>
          <p>Connected Wallet: {walletAddress}</p>
          <button onClick={disconnectWallet}>Disconnect Wallet</button>
        </div>
      )}
    </div>
  );
};

export default WalletConnection;
```
