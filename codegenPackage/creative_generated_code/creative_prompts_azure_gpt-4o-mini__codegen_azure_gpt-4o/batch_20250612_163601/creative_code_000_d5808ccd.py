"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://live-tensorians.pages.dev
Prompt: Generate a code snippet for integrating a wallet connection feature in a web application, similar to the one described on the Tensorians website.
Generated: DETERMINISTIC_d5808ccd6044373c
Batch ID: 20250612_163601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules and dependencies
import { useState, useEffect } from 'react';
import Web3 from 'web3';

// Wallet Connection Component
const WalletConnector = () => {
  const [walletAddress, setWalletAddress] = useState(null); // State to store the connected wallet address
  const [errorMessage, setErrorMessage] = useState(null); // State to store errors

  // Function to check if MetaMask is installed
  const isMetaMaskInstalled = () => {
    return typeof window.ethereum !== 'undefined';
  };

  // Function to connect to a wallet
  const connectWallet = async () => {
    try {
      if (!isMetaMaskInstalled()) {
        throw new Error('MetaMask is not installed. Please install MetaMask to continue.');
      }

      const web3 = new Web3(window.ethereum);
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' }); // Request account access
      setWalletAddress(accounts[0]); // Set the connected wallet address
    } catch (error) {
      setErrorMessage(error.message); // Set error message for display
    }
  };

  // Function to disconnect wallet
  const disconnectWallet = () => {
    setWalletAddress(null); // Clear wallet address
    setErrorMessage(null); // Clear error message
  };

  // Effect to check wallet connection state on page load
  useEffect(() => {
    const checkWalletConnection = async () => {
      try {
        if (isMetaMaskInstalled()) {
          const web3 = new Web3(window.ethereum);
          const accounts = await web3.eth.getAccounts();
          if (accounts.length > 0) {
            setWalletAddress(accounts[0]); // Set connected wallet address if available
          }
        }
      } catch (error) {
        setErrorMessage('Error fetching wallet connection status.');
      }
    };
    checkWalletConnection();
  }, []);

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', margin: '20px' }}>
      <h2>Wallet Connection</h2>
      {walletAddress ? (
        <div>
          <p>Connected Wallet Address: {walletAddress}</p>
          <button onClick={disconnectWallet} style={{ padding: '10px', cursor: 'pointer' }}>
            Disconnect Wallet
          </button>
        </div>
      ) : (
        <div>
          <button onClick={connectWallet} style={{ padding: '10px', cursor: 'pointer' }}>
            Connect Wallet
          </button>
        </div>
      )}
      {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}
    </div>
  );
};

export default WalletConnector;
```
