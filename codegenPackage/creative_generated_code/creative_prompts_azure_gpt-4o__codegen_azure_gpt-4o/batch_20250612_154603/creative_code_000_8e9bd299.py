"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://react-phantom-wallet.vercel.app
Prompt: Write a React component that integrates Phantom Wallet functionality using the methods described on the React Phantom Wallet webpage.
Generated: DETERMINISTIC_8e9bd29980f5a0af
Batch ID: 20250612_154603
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

// Phantom Wallet integration component
const PhantomWallet = () => {
  // State to manage wallet connection and public key
  const [walletConnected, setWalletConnected] = useState(false);
  const [publicKey, setPublicKey] = useState(null);

  // Check if Phantom Wallet is installed
  const isPhantomInstalled = () => {
    return window?.solana?.isPhantom || false;
  };

  // Connect to Phantom Wallet
  const connectWallet = async () => {
    try {
      if (!isPhantomInstalled()) {
        alert('Phantom Wallet is not installed. Please install it to continue.');
        return;
      }

      const response = await window.solana.connect();
      setWalletConnected(true);
      setPublicKey(response.publicKey.toString());
    } catch (error) {
      console.error('Error connecting to Phantom Wallet:', error);
      alert('Failed to connect to Phantom Wallet. Please try again.');
    }
  };

  // Disconnect from Phantom Wallet
  const disconnectWallet = async () => {
    try {
      await window.solana.disconnect();
      setWalletConnected(false);
      setPublicKey(null);
    } catch (error) {
      console.error('Error disconnecting from Phantom Wallet:', error);
      alert('Failed to disconnect from Phantom Wallet.');
    }
  };

  // Auto-connect wallet if already connected
  useEffect(() => {
    const autoConnect = async () => {
      if (isPhantomInstalled() && window.solana.isConnected) {
        try {
          const response = await window.solana.connect({ onlyIfTrusted: true });
          setWalletConnected(true);
          setPublicKey(response.publicKey.toString());
        } catch (error) {
          console.error('Error during auto-connect:', error);
        }
      }
    };

    autoConnect();
  }, []);

  // Render the component
  return (
    <div style={{ padding: '20px', textAlign: 'center' }}>
      <h1>Phantom Wallet Integration</h1>
      {walletConnected ? (
        <div>
          <p>Wallet Connected!</p>
          <p>Public Key: {publicKey}</p>
          <button onClick={disconnectWallet} style={{ padding: '10px 20px', cursor: 'pointer' }}>
            Disconnect Wallet
          </button>
        </div>
      ) : (
        <div>
          <p>Wallet is not connected.</p>
          <button onClick={connectWallet} style={{ padding: '10px 20px', cursor: 'pointer' }}>
            Connect Wallet
          </button>
        </div>
      )}
    </div>
  );
};

export default PhantomWallet;
```
