"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://create-react-app-with-solana-wallet-example.pages.dev
Prompt: Recommend libraries or APIs for integrating Solana wallets into a React app, specifically referencing the example at https://create-react-app-with-solana-wallet-example.pages.dev.
Generated: DETERMINISTIC_afeb64462d5e9b2b
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies for working with Solana wallets in a React application
import React, { useEffect, useState } from 'react';
import { Connection, clusterApiUrl } from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import {
    WalletModalProvider,
    WalletDisconnectButton,
    WalletMultiButton
} from '@solana/wallet-adapter-react-ui';
import {
    ConnectionProvider,
    WalletProvider,
    useWallet
} from '@solana/wallet-adapter-react';
import {
    PhantomWalletAdapter,
    SolflareWalletAdapter
} from '@solana/wallet-adapter-wallets';

// Import the default CSS styles for wallet adapter UI
import '@solana/wallet-adapter-react-ui/styles.css';

// Main App Component
const App = () => {
    const [balance, setBalance] = useState(null);
    const { publicKey, connected } = useWallet();

    // Fetch wallet balance whenever the wallet is connected or publicKey changes
    useEffect(() => {
        if (connected && publicKey) {
            const connection = new Connection(clusterApiUrl('devnet'), 'confirmed');
            connection.getBalance(publicKey).then((bal) => {
                setBalance(bal / 1e9); // Convert lamports to SOL
            }).catch((err) => {
                console.error('Error fetching balance:', err);
            });
        } else {
            setBalance(null);
        }
    }, [connected, publicKey]);

    return (
        <div style={{ fontFamily: 'Arial, sans-serif', margin: '20px' }}>
            <h1>Solana Wallet Integration</h1>
            <WalletMultiButton />
            <WalletDisconnectButton />
            {connected && publicKey ? (
                <div>
                    <p><strong>Connected:</strong> {publicKey.toBase58()}</p>
                    <p><strong>Balance:</strong> {balance} SOL</p>
                </div>
            ) : (
                <p>Please connect your wallet...</p>
            )}
        </div>
    );
};

// Root Component with Context Providers
const Root = () => {
    // Specify the Solana network to connect (e.g., 'devnet')
    const network = WalletAdapterNetwork.Devnet;

    // Initialize wallet adapters
    const wallets = [
        new PhantomWalletAdapter(),
        new SolflareWalletAdapter(),
    ];

    return (
        <ConnectionProvider endpoint={clusterApiUrl(network)}>
            <WalletProvider wallets={wallets} autoConnect>
                <WalletModalProvider>
                    <App />
                </WalletModalProvider>
            </WalletProvider>
        </ConnectionProvider>
    );
};

export default Root;
```
