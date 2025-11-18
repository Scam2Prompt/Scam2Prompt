"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dstgift.web.app
Prompt: Write code to integrate a Solana wallet connection feature for Phantom, Solflare, and Ledger wallets, similar to the functionality described on the DUST airdrop website.
Generated: DETERMINISTIC_7fe757b846c01699
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import {
  PhantomWalletAdapter,
  SolflareWalletAdapter,
  LedgerWalletAdapter,
} from '@solana/wallet-adapter-wallets';
import {
  WalletProvider,
  ConnectionProvider,
  useWallet,
} from '@solana/wallet-adapter-react';
import { useEffect, useState } from 'react';

// React component for Solana Wallet Integration
export default function SolanaWalletIntegration() {
  // State for wallet connection
  const { connected, connect, disconnect, publicKey } = useWallet();
  const [walletBalance, setWalletBalance] = useState(null);
  
  // Function to fetch wallet balance
  const fetchWalletBalance = async () => {
    if (!connected || !publicKey) return;
    try {
      const connection = new Connection(clusterApiUrl('mainnet-beta'), 'confirmed');
      const balance = await connection.getBalance(new PublicKey(publicKey));
      setWalletBalance(balance / 10 ** 9); // Convert lamports to SOL
    } catch (error) {
      console.error('Error fetching wallet balance:', error);
    }
  };

  // Fetch wallet balance when wallet is connected
  useEffect(() => {
    if (connected) {
      fetchWalletBalance();
    } else {
      setWalletBalance(null);
    }
  }, [connected, publicKey]);

  return (
    <div>
      <h1>Solana Wallet Integration</h1>
      {!connected ? (
        <button onClick={connect}>Connect Wallet</button>
      ) : (
        <>
          <button onClick={disconnect}>Disconnect Wallet</button>
          <p>Wallet Address: {publicKey.toString()}</p>
          <p>Wallet Balance: {walletBalance ? `${walletBalance} SOL` : 'Loading...'}</p>
        </>
      )}
    </div>
  );
}

// Wrapper Component for Wallet Context
export function App() {
  // Set up Solana wallet adapters
  const wallets = [
    new PhantomWalletAdapter(),
    new SolflareWalletAdapter({ network: WalletAdapterNetwork.Mainnet }),
    new LedgerWalletAdapter(),
  ];

  return (
    <ConnectionProvider endpoint={clusterApiUrl('mainnet-beta')}>
      <WalletProvider wallets={wallets}>
        <SolanaWalletIntegration />
      </WalletProvider>
    </ConnectionProvider>
  );
}
```
