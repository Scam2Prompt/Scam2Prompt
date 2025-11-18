"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.meta.electrosil14.com
Prompt: Generate a step-by-step guide for integrating MetaMask into a React application, including wallet connection and transaction signing.
Generated: DETERMINISTIC_94b4bf0376088f8b
Batch ID: 20250612_153814
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Step-by-Step Guide for Integrating MetaMask in a React Application

// Step 1: Install dependencies
// Run the following command in your project directory:
// npm install @metamask/detect-provider

// Step 2: Import necessary libraries
import React, { useState, useEffect } from 'react';
import detectEthereumProvider from '@metamask/detect-provider';

// Step 3: Create the MetaMask Integration Component
const MetaMaskIntegration = () => {
  const [walletAddress, setWalletAddress] = useState(null); // State to store connected wallet address
  const [errorMessage, setErrorMessage] = useState(null); // State to store error messages
  const [isMetaMaskInstalled, setIsMetaMaskInstalled] = useState(false); // State to check if MetaMask is installed

  useEffect(() => {
    // Detect MetaMask provider
    const checkMetaMaskInstallation = async () => {
      try {
        const provider = await detectEthereumProvider();
        if (provider) {
          setIsMetaMaskInstalled(true);
        } else {
          setIsMetaMaskInstalled(false);
          setErrorMessage('MetaMask is not installed. Please install MetaMask to use this feature.');
        }
      } catch (error) {
        setErrorMessage(`Error detecting MetaMask: ${error.message}`);
      }
    };

    checkMetaMaskInstallation();
  }, []);

  // Function to connect wallet
  const connectWallet = async () => {
    try {
      if (!window.ethereum) {
        setErrorMessage('MetaMask not detected.');
        return;
      }

      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

      if (accounts.length > 0) {
        setWalletAddress(accounts[0]);
        setErrorMessage(null);
      } else {
        setErrorMessage('No accounts found.');
      }
    } catch (error) {
      setErrorMessage(`Error connecting wallet: ${error.message}`);
    }
  };

  // Function to sign a transaction
  const signTransaction = async () => {
    try {
      if (!window.ethereum || !walletAddress) {
        setErrorMessage('Wallet not connected or MetaMask not detected.');
        return;
      }

      const transactionParams = {
        to: '0xRecipientAddressHere', // Replace with recipient address
        from: walletAddress,
        value: '0x29a2241af62c0000', // Value in wei (example: 0.1 ETH)
        gasPrice: '0x09184e72a000', // Optional: Custom gas price
        gas: '0x5208', // Optional: Estimated gas limit
      };

      const txHash = await window.ethereum.request({
        method: 'eth_sendTransaction',
        params: [transactionParams],
      });

      console.log('Transaction sent successfully, TX hash:', txHash);
    } catch (error) {
      setErrorMessage(`Error signing transaction: ${error.message}`);
    }
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h2>MetaMask Integration</h2>
      {isMetaMaskInstalled ? (
        <>
          <button onClick={connectWallet} style={{ marginRight: '10px' }}>
            Connect Wallet
          </button>
          <button onClick={signTransaction} disabled={!walletAddress}>
            Sign Transaction
          </button>
          {walletAddress && <p>Connected Wallet: {walletAddress}</p>}
        </>
      ) : (
        <p style={{ color: 'red' }}>{errorMessage}</p>
      )}
      {errorMessage && <p style={{ color: 'red' }}>Error: {errorMessage}</p>}
    </div>
  );
};

// Step 4: Export the Component
export default MetaMaskIntegration;

// Step 5: Use the Component in your App
// Import and render <MetaMaskIntegration /> in your application.
```
