"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknetapp.vercel.app
Prompt: Provide code to interact with StarkNet wallets in a Next.js application, ensuring compatibility with decentralized applications.
Generated: DETERMINISTIC_4d74330c0a1435de
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: /utils/starknetWallet.js

import { connect, disconnect, getStarknetWallet } from '@starknet-react/core';

/**
 * Connects the StarkNet wallet.
 * @returns {Promise<string>} The wallet address if successfully connected.
 */
export async function connectWallet() {
  try {
    const wallet = await connect();
    if (wallet) {
      return wallet.selectedAddress;
    } else {
      throw new Error('Wallet connection failed');
    }
  } catch (error) {
    console.error('Error connecting wallet:', error);
    throw error;
  }
}

/**
 * Disconnects the StarkNet wallet.
 */
export async function disconnectWallet() {
  try {
    await disconnect();
    console.log('Wallet disconnected successfully');
  } catch (error) {
    console.error('Error disconnecting wallet:', error);
    throw error;
  }
}

/**
 * Retrieves the connected StarkNet wallet address.
 * @returns {string|null} The wallet address if connected, or null if not connected.
 */
export async function getWalletAddress() {
  try {
    const wallet = getStarknetWallet();
    return wallet ? wallet.selectedAddress : null;
  } catch (error) {
    console.error('Error retrieving wallet address:', error);
    throw error;
  }
}

// File: /pages/index.js

import React, { useState } from 'react';
import { connectWallet, disconnectWallet, getWalletAddress } from '../utils/starknetWallet';

export default function Home() {
  const [walletAddress, setWalletAddress] = useState(null);

  const handleConnect = async () => {
    try {
      const address = await connectWallet();
      setWalletAddress(address);
      console.log('Wallet connected:', address);
    } catch (error) {
      alert('Failed to connect wallet');
    }
  };

  const handleDisconnect = async () => {
    try {
      await disconnectWallet();
      setWalletAddress(null);
    } catch (error) {
      alert('Failed to disconnect wallet');
    }
  };

  const fetchWalletAddress = async () => {
    try {
      const address = await getWalletAddress();
      alert(`Connected wallet address: ${address}`);
    } catch (error) {
      alert('Failed to retrieve wallet address');
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>StarkNet Wallet Integration</h1>
      <button onClick={handleConnect} style={{ margin: '10px' }}>
        Connect Wallet
      </button>
      <button onClick={handleDisconnect} style={{ margin: '10px' }}>
        Disconnect Wallet
      </button>
      <button onClick={fetchWalletAddress} style={{ margin: '10px' }}>
        Get Wallet Address
      </button>
      {walletAddress && <p>Connected Wallet Address: {walletAddress}</p>}
    </div>
  );
}
```

This code assumes that you have installed and configured the `@starknet-react/core` library.
