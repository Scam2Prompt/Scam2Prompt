"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-wallet-adapter-mantine-ui.pages.dev
Prompt: Provide an example of using the Solana Wallet Adapter with Mantine UI to authenticate a user and retrieve their wallet address.
Generated: DETERMINISTIC_e9f8ba04eddd944c
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// React functional component for Solana Wallet authentication
// using Solana Wallet Adapter and Mantine UI.

import React, { useState } from 'react';
import { Connection, clusterApiUrl } from '@solana/web3.js';
import { WalletProvider, useWallet } from '@solana/wallet-adapter-react';
import { WalletModalProvider, WalletMultiButton } from '@solana/wallet-adapter-react-ui';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-wallets';
import { Button, Notification } from '@mantine/core';

// Ensure to include the Wallet Adapter styles in your project
import '@solana/wallet-adapter-react-ui/styles.css';

// Main Wallet Authentication Component
const WalletAuth = () => {
  const { publicKey, disconnect } = useWallet(); // Access wallet state and methods from the Solana Wallet Adapter
  const [walletAddress, setWalletAddress] = useState(null); // State to hold wallet address

  // Function to handle wallet authentication
  const handleAuthentication = async () => {
    try {
      // Check if the wallet is connected
      if (!publicKey) {
        throw new Error('Wallet is not connected.');
      }

      // Retrieve the wallet address and update state
      const address = publicKey.toString();
      setWalletAddress(address);

      // Optionally, create a connection to the Solana blockchain
      const connection = new Connection(clusterApiUrl('mainnet-beta'), 'confirmed');
      console.log('Successfully connected to Solana blockchain:', connection);
    } catch (error) {
      console.error('Authentication failed:', error);
    }
  };

  // Function to handle disconnecting the wallet
  const handleDisconnect = async () => {
    try {
      await disconnect(); // Disconnect the wallet
      setWalletAddress(null); // Clear wallet address state
    } catch (error) {
      console.error('Error disconnecting wallet:', error);
    }
  };

  return (
    <div style={{ textAlign: 'center', margin: '20px' }}>
      {/* Mantine Notification for displaying wallet connection status */}
      {walletAddress ? (
        <Notification
          color="green"
          title="Wallet Connected"
          onClose={() => setWalletAddress(null)}
        >
          Wallet Address: {walletAddress}
        </Notification>
      ) : (
        <Notification color="red" title="No Wallet Connected">
          Please connect your wallet to proceed.
        </Notification>
      )}

      {/* Wallet Connect Button */}
      <WalletMultiButton style={{ marginTop: '20px' }} />

      {/* Authenticate Button */}
      <Button
        variant="filled"
        color="blue"
        style={{ marginTop: '20px' }}
        onClick={handleAuthentication}
      >
        Authenticate Wallet
      </Button>

      {/* Disconnect Button */}
      {walletAddress && (
        <Button
          variant="filled"
          color="red"
          style={{ marginTop: '20px' }}
          onClick={handleDisconnect}
        >
          Disconnect Wallet
        </Button>
      )}
    </div>
  );
};

// App Component to set up Wallet Provider
const App = () => {
  // Configure wallet adapters
  const wallets = [new PhantomWalletAdapter()];

  return (
    <WalletProvider wallets={wallets} autoConnect>
      <WalletModalProvider>
        <WalletAuth />
      </WalletModalProvider>
    </WalletProvider>
  );
};

export default App;
```
