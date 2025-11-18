"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-pay3wfto1-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Generate a Next.js page that connects a crypto wallet using WalletConnect, as outlined in the Dapp Starter framework.
Generated: DETERMINISTIC_67effbbdb4d0e7f6
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/wallet-connect.js

import { useState } from 'react';
import WalletConnectProvider from '@walletconnect/web3-provider';
import Web3 from 'web3';

// Next.js page for connecting a crypto wallet using WalletConnect
export default function WalletConnectPage() {
  const [walletAddress, setWalletAddress] = useState(null);
  const [provider, setProvider] = useState(null);

  // Function to establish wallet connection
  const connectWallet = async () => {
    try {
      // Initialize WalletConnect Provider
      const walletConnectProvider = new WalletConnectProvider({
        infuraId: 'YOUR_INFURA_ID', // Replace with your Infura project ID
      });

      // Enable session (connect to wallet)
      await walletConnectProvider.enable();

      // Create Web3 instance
      const web3 = new Web3(walletConnectProvider);

      // Get wallet accounts
      const accounts = await web3.eth.getAccounts();
      const address = accounts[0];

      setWalletAddress(address); // Save wallet address to state
      setProvider(walletConnectProvider); // Save provider to state
    } catch (error) {
      console.error('Error connecting to wallet:', error); // Log error for debugging
      alert('Failed to connect to wallet. Please try again.');
    }
  };

  // Function to disconnect the wallet
  const disconnectWallet = async () => {
    try {
      if (provider) {
        await provider.disconnect(); // Disconnect WalletConnect provider
        setWalletAddress(null); // Clear wallet address state
        setProvider(null); // Clear provider state
      }
    } catch (error) {
      console.error('Error disconnecting wallet:', error); // Log error for debugging
      alert('Failed to disconnect wallet. Please try again.');
    }
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>WalletConnect Integration</h1>
      {!walletAddress ? (
        <>
          <p>No wallet connected. Please connect your wallet.</p>
          <button
            onClick={connectWallet}
            style={{
              padding: '10px 20px',
              fontSize: '16px',
              cursor: 'pointer',
              backgroundColor: '#0070f3',
              color: '#fff',
              border: 'none',
              borderRadius: '5px',
            }}
          >
            Connect Wallet
          </button>
        </>
      ) : (
        <>
          <p>Wallet connected: {walletAddress}</p>
          <button
            onClick={disconnectWallet}
            style={{
              padding: '10px 20px',
              fontSize: '16px',
              cursor: 'pointer',
              backgroundColor: '#e53e3e',
              color: '#fff',
              border: 'none',
              borderRadius: '5px',
            }}
          >
            Disconnect Wallet
          </button>
        </>
      )}
    </div>
  );
}

// Notes:
// - Replace 'YOUR_INFURA_ID' with your actual Infura project ID.
// - Error handling is implemented to catch connection and disconnection errors.
// - Styling is kept minimal for clarity; consider enhancing it for production use.
// - Ensure the `@walletconnect/web3-provider` and `web3` packages are installed in your project.
```

To use this code:
1. Install the required dependencies with `npm install @walletconnect/web3-provider web3`.
2. Replace `'YOUR_INFURA_ID'` with your actual Infura project ID.
3. Place this file in the `pages` directory of your Next.js project (`pages/wallet-connect.js`).
