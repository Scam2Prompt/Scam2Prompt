"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-sdk-demo.pages.dev
Prompt: Provide code to integrate the MetaMask SDK with a React app to listen for account changes and update the UI accordingly.
Generated: DETERMINISTIC_9525f4890865f513
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary libraries
import React, { useState, useEffect } from 'react';

// Create a React component
const MetaMaskIntegration = () => {
  // State to hold the connected account
  const [account, setAccount] = useState(null);

  // Function to check if MetaMask is installed
  const isMetaMaskInstalled = () => {
    return typeof window.ethereum !== 'undefined';
  };

  // Function to request account access
  const connectMetaMask = async () => {
    try {
      // Request accounts from MetaMask
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      // Set the first account to the state
      setAccount(accounts[0]);
    } catch (error) {
      // Handle errors (e.g., user denied account access)
      console.error('Error connecting to MetaMask:', error.message);
    }
  };

  // Effect to listen for account changes
  useEffect(() => {
    if (isMetaMaskInstalled()) {
      // Listen for account changes
      window.ethereum.on('accountsChanged', (accounts) => {
        if (accounts.length > 0) {
          setAccount(accounts[0]); // Update the account state
        } else {
          setAccount(null); // Clear the account if no accounts are connected
        }
      });

      // Cleanup listener on component unmount
      return () => {
        window.ethereum.removeListener('accountsChanged', () => {});
      };
    }
  }, []);

  return (
    <div>
      <h1>MetaMask Integration</h1>
      {/* Render different UI based on MetaMask installation status */}
      {isMetaMaskInstalled() ? (
        <>
          <button onClick={connectMetaMask}>
            {account ? 'Switch Account' : 'Connect to MetaMask'}
          </button>
          {account && <p>Connected Account: {account}</p>}
        </>
      ) : (
        <p>Please install MetaMask to use this feature.</p>
      )}
    </div>
  );
};

export default MetaMaskIntegration;
```
