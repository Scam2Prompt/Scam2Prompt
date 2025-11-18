"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-react-meutas5kc-uniswap.vercel.app
Prompt: Provide an example of how to use Web3-React to connect a Coinbase Wallet and display the currently selected blockchain network (e.g., Celo Alfajores or Arbitrum One).
Generated: DETERMINISTIC_ade9216c58ea5a1a
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and components
import React, { useEffect, useState } from 'react';
import { Web3ReactProvider, useWeb3React } from '@web3-react/core';
import { InjectedConnector } from '@web3-react/injected-connector';
import { ethers } from 'ethers';

// Create an injected connector for Coinbase Wallet
const injected = new InjectedConnector({
  supportedChainIds: [44787, 42161] // Celo Alfajores and Arbitrum One Chain IDs
});

// Function to get the library (ethers.js)
function getLibrary(provider) {
  const library = new ethers.providers.Web3Provider(provider);
  library.pollingInterval = 12000; // Set polling interval for the library
  return library;
}

// Component to connect to Coinbase Wallet and display the network
function App() {
  const { activate, account, library, chainId, active } = useWeb3React();
  const [error, setError] = useState(null);

  // Function to connect to the Coinbase Wallet
  const connectWallet = async () => {
    try {
      await activate(injected);
    } catch (err) {
      console.error('Failed to connect wallet:', err);
      setError('Could not connect to wallet. Please try again.');
    }
  };

  // Effect to check for connection state changes
  useEffect(() => {
    if (active) {
      console.log(`Connected to account: ${account}`);
    }
  }, [active, account]);

  return (
    <div>
      <h1>Connect to Coinbase Wallet</h1>
      <button onClick={connectWallet}>Connect</button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {active && (
        <div>
          <p>Connected Account: {account}</p>
          <p>Selected Network ID: {chainId}</p>
        </div>
      )}
    </div>
  );
}

// Main render function to wrap App in Web3ReactProvider
function Main() {
  return (
    <Web3ReactProvider getLibrary={getLibrary}>
      <App />
    </Web3ReactProvider>
  );
}

// Export the main function as the default export
export default Main;
```
