"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://example.walletconnect.org
Prompt: Create a React component that utilizes WalletConnect v2.8.6 to connect wallets exclusively to testnet chains.
Generated: DETERMINISTIC_89cd733c1f75a518
Batch ID: 20250612_150323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://bridge.walletconnect.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import { Client, WalletConnect } from '@walletconnect/client';
import { ethers } from 'ethers';

// Create a functional component for WalletConnect
const WalletConnectComponent = () => {
  // State variables to manage connection and wallet address
  const [connector, setConnector] = useState(null);
  const [walletAddress, setWalletAddress] = useState('');
  const [error, setError] = useState(null);

  // Initialize WalletConnect
  useEffect(() => {
    const initWalletConnect = async () => {
      try {
        // Create a new WalletConnect connector instance
        const wcConnector = new WalletConnect({
          bridge: 'https://bridge.walletconnect.org', // Bridge server URL
          qrcodeModal: null, // Disable QR code modal if unnecessary
        });

        // Check if already connected
        if (wcConnector.connected) {
          setConnector(wcConnector);
          setWalletAddress(wcConnector.accounts[0]);
        } else {
          setConnector(wcConnector);
        }
      } catch (err) {
        setError(`Failed to initialize WalletConnect: ${err.message}`);
      }
    };

    initWalletConnect();
  }, []);

  // Function to connect to wallet
  const connectWallet = async () => {
    try {
      if (!connector) {
        throw new Error('WalletConnector not initialized.');
      }

      // Create a new session for connecting to wallet
      await connector.createSession({
        chainId: 97, // BSC Testnet
        qrcode: true, // Display QR code for scanning
      });

      // Subscribe to connection events
      connector.on('connect', (error, payload) => {
        if (error) {
          setError(`Connection Error: ${error.message}`);
          return;
        }

        // Get provided accounts and chainId
        const { accounts } = payload.params[0];
        setWalletAddress(accounts[0]);
      });

      connector.on('disconnect', (error) => {
        if (error) {
          setError(`Disconnection Error: ${error.message}`);
        }
        setWalletAddress('');
      });
    } catch (err) {
      setError(`Failed to connect wallet: ${err.message}`);
    }
  };

  // Function to disconnect wallet
  const disconnectWallet = async () => {
    if (connector) {
      await connector.killSession();
      setWalletAddress('');
    }
  };

  return (
    <div>
      <h1>WalletConnect Testnet Example</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <p>Connected Address: {walletAddress || 'Not connected'}</p>
      <button onClick={connectWallet}>Connect Wallet</button>
      <button onClick={disconnectWallet} disabled={!walletAddress}>
        Disconnect Wallet
      </button>
    </div>
  );
};

export default WalletConnectComponent;
```
