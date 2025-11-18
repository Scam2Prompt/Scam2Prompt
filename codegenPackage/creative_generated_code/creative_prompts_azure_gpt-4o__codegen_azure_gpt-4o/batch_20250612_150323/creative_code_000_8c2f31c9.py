"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3modal.com
Prompt: Write a React component that integrates Reown's AppKit to enable web3 wallet login for users, supporting 500+ wallet providers as described on the Web3Modal website.
Generated: DETERMINISTIC_8c2f31c94737f387
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
import React, { useState, useEffect } from 'react';
import { Web3Modal } from '@web3modal/react';
import { EthereumClient, configureChains, createClient } from '@web3modal/ethereum';
import { mainnet, polygon, arbitrum } from '@wagmi/core/chains';
import { getDefaultWallets } from '@rainbow-me/rainbowkit';
import { WagmiConfig } from 'wagmi';

// Configure chains to support multiple blockchains (mainnet, polygon, arbitrum)
const { chains, provider } = configureChains(
  [mainnet, polygon, arbitrum],
  [provider => provider.rpcProvider({ infuraId: process.env.REACT_APP_INFURA_ID })]
);

// Get default wallet options
const { connectors } = getDefaultWallets({
  appName: 'YourAppName',
  chains,
});

// Create Ethereum client for use with Web3Modal
const ethereumClient = createClient({
  autoConnect: true,
  connectors,
  provider,
});

// Main React component for Web3 wallet login
const Web3WalletLogin = () => {
  const [connectedAccount, setConnectedAccount] = useState(null);

  // Handle wallet connection
  const handleConnect = async () => {
    try {
      const accounts = await ethereumClient.getSigner().getAccounts();
      if (accounts.length > 0) {
        setConnectedAccount(accounts[0]); // Set the first account as connected
      }
    } catch (error) {
      console.error('Error connecting to wallet:', error);
      alert('Failed to connect to wallet. Please try again.');
    }
  };

  // Handle wallet disconnection
  const handleDisconnect = async () => {
    try {
      setConnectedAccount(null); // Clear connected account
      await ethereumClient.disconnect(); // Disconnect wallet
    } catch (error) {
      console.error('Error disconnecting wallet:', error);
      alert('Failed to disconnect wallet. Please try again.');
    }
  };

  useEffect(() => {
    // Automatically connect wallet if possible
    if (!connectedAccount) {
      handleConnect();
    }
  }, [connectedAccount]);

  return (
    <WagmiConfig client={ethereumClient}>
      <div style={{ padding: '20px' }}>
        <h1>Web3 Wallet Login</h1>
        {!connectedAccount ? (
          <button onClick={handleConnect}>Connect Wallet</button>
        ) : (
          <div>
            <p>Connected Account: {connectedAccount}</p>
            <button onClick={handleDisconnect}>Disconnect Wallet</button>
          </div>
        )}
      </div>
      {/* Web3Modal component */}
      <Web3Modal
        ethereumClient={ethereumClient}
        projectId={process.env.REACT_APP_WEB3MODAL_PROJECT_ID} // Use your Web3Modal project ID
      />
    </WagmiConfig>
  );
};

export default Web3WalletLogin;
```

**Note:** Replace `process.env.REACT_APP_INFURA_ID` and `process.env.REACT_APP_WEB3MODAL_PROJECT_ID` with your actual Infura and Web3Modal project IDs in your `.env` file for proper configuration.
