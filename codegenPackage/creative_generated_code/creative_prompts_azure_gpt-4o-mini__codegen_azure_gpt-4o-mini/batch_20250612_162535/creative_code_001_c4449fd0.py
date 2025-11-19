"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phaantomswalet.github.io
Prompt: Write a code snippet that demonstrates how to connect a Ledger wallet to the Phantom Wallet for enhanced security on the Solana blockchain.
Generated: DETERMINISTIC_c4449fd097375652
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';
import { LedgerWalletAdapter } from '@solana/wallet-adapter-ledger';
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import React, { useEffect, useMemo, useState } from 'react';
import { WalletProvider, useWallet } from '@solana/wallet-adapter-react';

// Define the network to connect to
const network = WalletAdapterNetwork.Mainnet;

// Create a connection to the Solana cluster
const connection = new Connection(clusterApiUrl(network), 'confirmed');

// Wallet component to handle the connection
const WalletConnection = () => {
    const { connected, wallet, connect, disconnect } = useWallet();
    
    // Effect to handle wallet connection
    useEffect(() => {
        // Attempt to connect when the component mounts
        if (!connected) {
            connect().catch(err => console.error('Connection failed:', err));
        }
    }, [connected, connect]);

    // Render wallet status and connection button
    return (
        <div>
            <h1>{connected ? 'Wallet Connected' : 'Connect a Wallet'}</h1>
            {connected ? (
                <button onClick={disconnect}>Disconnect</button>
            ) : (
                <button onClick={connect} disabled={!wallet}>
                    Connect
                </button>
            )}
        </div>
    );
};

// Main App component
const App = () => {
    // Available wallet adapters
    const wallets = useMemo(() => [
        new PhantomWalletAdapter(),
        new LedgerWalletAdapter(),
    ], []);

    return (
        <WalletProvider wallets={wallets} autoConnect>
            <WalletConnection />
        </WalletProvider>
    );
};

// Start the application
const rootElement = document.getElementById('root');
if (rootElement) {
    ReactDOM.render(<App />, rootElement);
} else {
    console.error('Root element not found');
}
```

### Notes:
- Make sure you have the necessary libraries installed: 
  ```bash
  npm install @solana/web3.js @solana/wallet-adapter-react @solana/wallet-adapter-phantom @solana/wallet-adapter-ledger
  ```
- This code assumes you have a React environment set up and that the DOM element with the id `root` exists in your HTML.
- Error handling is included for connection failures and root element checking.
