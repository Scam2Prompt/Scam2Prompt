"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nileriver.finance
Prompt: Write a code snippet to integrate wallet connection functionality into a web app similar to Nile River Finance.
Generated: DETERMINISTIC_ff512b57471b2ec8
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { useEffect, useState } from "react";
import Web3 from "web3";

// WalletConnection component
const WalletConnection = () => {
  // State to store the user's wallet address
  const [walletAddress, setWalletAddress] = useState(null);

  // State to track connection status
  const [isConnected, setIsConnected] = useState(false);

  // State to track error messages
  const [errorMessage, setErrorMessage] = useState("");

  // Function to connect wallet
  const connectWallet = async () => {
    try {
      // Check if the browser has an Ethereum provider (e.g., MetaMask)
      if (window.ethereum) {
        const web3 = new Web3(window.ethereum);

        // Request account access from the user
        const accounts = await window.ethereum.request({
          method: "eth_requestAccounts",
        });

        // Set the wallet address and update connection status
        setWalletAddress(accounts[0]);
        setIsConnected(true);
        setErrorMessage("");
      } else {
        // If no provider is detected, display an error message
        setErrorMessage("Ethereum provider not found. Please install MetaMask.");
        setIsConnected(false);
      }
    } catch (error) {
      // Handle errors that occur during wallet connection
      setErrorMessage("Failed to connect wallet: " + error.message);
      setIsConnected(false);
    }
  };

  // Function to disconnect wallet
  const disconnectWallet = () => {
    // Clear the wallet address and update connection status
    setWalletAddress(null);
    setIsConnected(false);
    setErrorMessage("");
  };

  // Automatically check wallet connection on page load
  useEffect(() => {
    const checkWalletConnection = async () => {
      try {
        if (window.ethereum) {
          const web3 = new Web3(window.ethereum);
          const accounts = await web3.eth.getAccounts();

          if (accounts.length > 0) {
            // If wallet is already connected, update state
            setWalletAddress(accounts[0]);
            setIsConnected(true);
          }
        }
      } catch (error) {
        // Handle errors during the wallet connection check
        setErrorMessage("Failed to check wallet connection: " + error.message);
      }
    };

    checkWalletConnection();
  }, []);

  // UI for wallet connection
  return (
    <div>
      <h1>Wallet Connection</h1>

      {/* Show wallet address if connected */}
      {isConnected && walletAddress ? (
        <div>
          <p>Connected Wallet Address: {walletAddress}</p>
          <button onClick={disconnectWallet}>Disconnect Wallet</button>
        </div>
      ) : (
        <div>
          <button onClick={connectWallet}>Connect Wallet</button>
        </div>
      )}

      {/* Display error messages */}
      {errorMessage && <p style={{ color: "red" }}>{errorMessage}</p>}
    </div>
  );
};

export default WalletConnection;
```
