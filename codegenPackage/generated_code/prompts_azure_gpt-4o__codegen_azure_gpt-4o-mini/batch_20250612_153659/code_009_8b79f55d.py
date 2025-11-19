"""
Generated Code Metadata:
========================
Original URL: https://token-creator-seven.vercel.app
Prompt: Provide an example of integrating Solana wallet functionality into a web application, inspired by the features on the Solana Scaffold Token Creator site.
Generated: DETERMINISTIC_8b79f55d4b221e26
Batch ID: 20250612_153659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import {
    WalletProvider,
    ConnectionProvider,
    useWallet,
} from '@solana/wallet-adapter-react';
import {
    PhantomWalletAdapter,
    SolletWalletAdapter,
} from '@solana/wallet-adapter-wallets';
import { Button } from '@material-ui/core';

// Define the network and connection
const network = WalletAdapterNetwork.Devnet;
const endpoint = clusterApiUrl(network);

// Create a component for wallet connection
const WalletConnection = () => {
    const { connected, wallet, connect, disconnect } = useWallet();

    return (
        <div>
            {connected ? (
                <div>
                    <p>Connected to: {wallet.publicKey.toString()}</p>
                    <Button variant="contained" color="secondary" onClick={disconnect}>
                        Disconnect
                    </Button>
                </div>
            ) : (
                <Button variant="contained" color="primary" onClick={connect}>
                    Connect Wallet
                </Button>
            )}
        </div>
    );
};

// Main App component
const App = () => {
    const [connection, setConnection] = useState(null);

    // Initialize connection to Solana cluster
    useEffect(() => {
        const conn = new Connection(endpoint, 'confirmed');
        setConnection(conn);
    }, []);

    return (
        <ConnectionProvider connection={connection}>
            <WalletProvider wallets={[new PhantomWalletAdapter(), new SolletWalletAdapter()]}>
                <div style={{ padding: '20px' }}>
                    <h1>Solana Wallet Integration</h1>
                    <WalletConnection />
                </div>
            </WalletProvider>
        </ConnectionProvider>
    );
};

// Render the App component
const rootElement = document.getElementById('root');
if (rootElement) {
    ReactDOM.render(<App />, rootElement);
} else {
    console.error('Root element not found');
}
```

### Notes:
- Ensure you have the necessary dependencies installed:
  ```bash
  npm install @solana/web3.js @solana/wallet-adapter-react @solana/wallet-adapter-wallets @material-ui/core react react-dom
  ```
- This code assumes you have a basic React setup. Adjust the imports and rendering logic as necessary for your specific environment.
