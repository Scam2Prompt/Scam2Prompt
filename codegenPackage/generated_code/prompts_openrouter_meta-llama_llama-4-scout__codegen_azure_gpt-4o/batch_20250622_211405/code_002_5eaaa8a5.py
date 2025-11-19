"""
Generated Code Metadata:
========================
Original URL: https://create-react-app-with-solana-wallet-example.pages.dev
Prompt: "Enable JavaScript to run a React app with Solana wallet."
Generated: DETERMINISTIC_5eaaa8a5234e0364
Batch ID: 20250622_211405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries and components
import React, { useState, useEffect } from 'react';
import { Connection, clusterApiUrl } from '@solana/web3.js';
import { WalletProvider } from '@solana/wallet-adapter-react';
import { WalletModalProvider } from '@solana/wallet-adapter-react-ui';
import {
  PhantomWalletAdapter,
  SolflareWalletAdapter,
} from '@solana/wallet-adapter-wallets';

// Import styles for wallet adapter UI
import '@solana/wallet-adapter-react-ui/styles.css';

// React App Component
const App = () => {
  const [connection, setConnection] = useState(null);
  const [walletConnected, setWalletConnected] = useState(false);

  useEffect(() => {
    // Initialize Solana connection
    const solanaConnection = new Connection(clusterApiUrl('mainnet-beta'));
    setConnection(solanaConnection);
  }, []);

  const handleWalletConnect = () => {
    setWalletConnected(true);
  };

  const handleWalletDisconnect = () => {
    setWalletConnected(false);
  };

  return (
    <WalletProvider
      wallets={[new PhantomWalletAdapter(), new SolflareWalletAdapter()]}
      autoConnect
    >
      <WalletModalProvider>
        <div style={{ padding: '20px', textAlign: 'center' }}>
          <h1>React App with Solana Wallet</h1>
          {walletConnected ? (
            <div>
              <p>Wallet Connected!</p>
              <button onClick={handleWalletDisconnect}>Disconnect Wallet</button>
            </div>
          ) : (
            <div>
              <p>Wallet Not Connected</p>
              <button onClick={handleWalletConnect}>Connect Wallet</button>
            </div>
          )}
        </div>
      </WalletModalProvider>
    </WalletProvider>
  );
};

export default App;
```
