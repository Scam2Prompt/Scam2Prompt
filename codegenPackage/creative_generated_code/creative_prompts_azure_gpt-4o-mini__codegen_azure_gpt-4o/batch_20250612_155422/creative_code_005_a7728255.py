"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appkit-laboratory-mu63br02c-reown-com.vercel.app
Prompt: How do I implement a demo with sample wallets using wagmi and ethers in AppKit?
Generated: DETERMINISTIC_a7728255c5a3e22f
Batch ID: 20250612_155422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState } from 'react';
import { useAccount, useConnect, useDisconnect } from 'wagmi';
import { InjectedConnector } from 'wagmi/connectors/injected';
import { ethers } from 'ethers';

// Main Wallet Demo Component
const WalletDemo = () => {
  const { address, isConnected } = useAccount(); // Get account information
  const { connect } = useConnect({
    connector: new InjectedConnector(), // Use InjectedConnector for browser wallets like MetaMask
  });
  const { disconnect } = useDisconnect(); // Disconnect wallet
  const [balance, setBalance] = useState(null); // State to store wallet balance

  // Fetch Wallet Balance
  const fetchBalance = async () => {
    if (!isConnected || !address) return;

    try {
      const provider = new ethers.providers.Web3Provider(window.ethereum); // Connect to Web3 provider
      const walletBalance = await provider.getBalance(address); // Fetch balance
      setBalance(ethers.utils.formatEther(walletBalance)); // Convert balance to human-readable format
    } catch (error) {
      console.error('Error fetching balance:', error); // Log errors
      setBalance(null);
    }
  };

  // Render component UI
  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>Wallet Demo</h1>
      {/* Display wallet address if connected */}
      {isConnected ? (
        <div>
          <p>
            <strong>Wallet Address:</strong> {address}
          </p>
          {/* Display wallet balance */}
          <p>
            <strong>Balance:</strong> {balance !== null ? `${balance} ETH` : 'N/A'}
          </p>
          <button onClick={fetchBalance} style={{ marginRight: '10px' }}>
            Fetch Balance
          </button>
          <button onClick={disconnect}>Disconnect Wallet</button>
        </div>
      ) : (
        // Connect wallet button
        <button onClick={connect}>Connect Wallet</button>
      )}
    </div>
  );
};

export default WalletDemo;
```
