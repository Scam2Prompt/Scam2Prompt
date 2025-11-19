"""
Generated Code Metadata:
========================
Original URL: https://nft-trades.web.app
Prompt: Illustrate how to implement a feature for users to manage their wallets on a Solana NFT platform, including connecting and disconnecting wallets.
Generated: DETERMINISTIC_61e513507bf83130
Batch ID: 20250612_162716
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { useState } from 'react';
import { Connection, clusterApiUrl } from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import {
  WalletProvider,
  ConnectionProvider,
  useWallet,
} from '@solana/wallet-adapter-react';
import {
  PhantomWalletAdapter,
  SolflareWalletAdapter,
} from '@solana/wallet-adapter-wallets';

// Wallet management component
const WalletManager = () => {
  const { wallet, connect, disconnect, connected } = useWallet();
  const [error, setError] = useState(null);

  // Handle wallet connection
  const handleConnect = async () => {
    try {
      setError(null); // Clear previous errors
      await connect(); // Connect wallet
      console.log('Wallet connected:', wallet.publicKey.toString());
    } catch (err) {
      setError('Failed to connect wallet. Please try again.');
      console.error(err);
    }
  };

  // Handle wallet disconnection
  const handleDisconnect = async () => {
    try {
      setError(null); // Clear previous errors
      await disconnect(); // Disconnect wallet
      console.log('Wallet disconnected');
    } catch (err) {
      setError('Failed to disconnect wallet. Please try again.');
      console.error(err);
    }
  };

  return (
    <div>
      <h1>Solana NFT Platform - Wallet Manager</h1>
      {connected ? (
        <div>
          <p>Wallet Address: {wallet.publicKey.toString()}</p>
          <button onClick={handleDisconnect}>Disconnect Wallet</button>
        </div>
      ) : (
        <div>
          <button onClick={handleConnect}>Connect Wallet</button>
        </div>
      )}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
};

// Main App component
const App = () => {
  // Configure Solana connection and wallet adapters
  const network = WalletAdapterNetwork.Mainnet; // Use Mainnet for production
  const endpoint = clusterApiUrl(network); // Solana RPC endpoint
  const wallets = [
    new PhantomWalletAdapter(),
    new SolflareWalletAdapter(),
  ];

  return (
    <ConnectionProvider endpoint={endpoint}>
      <WalletProvider wallets={wallets} autoConnect>
        <WalletManager />
      </WalletProvider>
    </ConnectionProvider>
  );
};

export default App;
```
