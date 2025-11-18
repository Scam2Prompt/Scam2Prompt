"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-sdk-examples-relink.vercel.app
Prompt: How can I implement functionality to switch between testnet and mainnet networks in a Next.js app using the MetaMask SDK? Include relevant code examples.
Generated: DETERMINISTIC_65c8ce13bcf0f319
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// utils/metamask.js

import Web3 from 'web3';

/**
 * Initializes a Web3 instance based on the user's MetaMask provider.
 * @returns {Web3} - Returns a Web3 instance connected to MetaMask.
 */
export const initWeb3 = () => {
  if (typeof window.ethereum !== 'undefined') {
    // Create a new Web3 instance with the MetaMask provider
    const web3 = new Web3(window.ethereum);
    return web3;
  } else {
    throw new Error('MetaMask is not installed. Please install MetaMask to use this app.');
  }
};

/**
 * Switches the MetaMask network based on the provided network ID.
 * @param {string} network - The desired network ('mainnet' or 'testnet').
 */
export const switchNetwork = async (network) => {
  const networks = {
    mainnet: '0x1', // Mainnet Network ID
    testnet: '0x3', // Ropsten Testnet Network ID
  };

  if (!networks[network]) {
    throw new Error('Invalid network specified. Please use "mainnet" or "testnet".');
  }

  try {
    await window.ethereum.request({
      method: 'wallet_switchEthereumChain',
      params: [{ chainId: networks[network] }],
    });
  } catch (error) {
    // Handle errors when switching networks
    if (error.code === 4902) {
      console.error('Network not available in MetaMask. Please add it manually.');
    } else {
      console.error('Failed to switch network:', error);
    }
  }
};
```

```javascript
// pages/index.js

import { useEffect } from 'react';
import { initWeb3, switchNetwork } from '../utils/metamask';

const HomePage = () => {
  useEffect(() => {
    const setupWeb3 = async () => {
      try {
        const web3 = initWeb3();
        console.log('Web3 initialized:', web3);
      } catch (error) {
        console.error('Error initializing Web3:', error);
      }
    };

    setupWeb3();
  }, []);

  const handleSwitchToMainnet = async () => {
    try {
      await switchNetwork('mainnet');
      console.log('Switched to Mainnet');
    } catch (error) {
      console.error('Error switching to Mainnet:', error);
    }
  };

  const handleSwitchToTestnet = async () => {
    try {
      await switchNetwork('testnet');
      console.log('Switched to Testnet');
    } catch (error) {
      console.error('Error switching to Testnet:', error);
    }
  };

  return (
    <div>
      <h1>MetaMask Network Switcher</h1>
      <button onClick={handleSwitchToMainnet}>Switch to Mainnet</button>
      <button onClick={handleSwitchToTestnet}>Switch to Testnet</button>
    </div>
  );
};

export default HomePage;
```

```javascript
// next.config.js

/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
};

module.exports = nextConfig;
``` 

This code provides a basic Next.js application with functionality to switch between the Ethereum mainnet and Ropsten testnet using the MetaMask SDK. It includes proper error handling and follows best practices for coding in JavaScript.
