"""
Generated Code Metadata:
========================
Original URL: https://token-creator-bellumxyz.vercel.app
Prompt: What are the steps to create a new token using the Solana Token Creator, including wallet connection?
Generated: DETERMINISTIC_ce5eedf9ee8709ad
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { Token, TOKEN_PROGRAM_ID } from '@solana/spl-token';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import { getPhantomWallet } from '@solana/wallet-adapter-wallets';
import { WalletProvider, ConnectionProvider } from '@solana/wallet-adapter-react';
import React, { useEffect, useState } from 'react';

// Define the main application component
const App = () => {
    // State to hold the connection and wallet
    const [connection, setConnection] = useState(null);
    const [wallet, setWallet] = useState(null);
    const [token, setToken] = useState(null);

    // Initialize connection and wallet
    useEffect(() => {
        const init = async () => {
            // Create a connection to the Solana devnet
            const conn = new Connection(clusterApiUrl('devnet'), 'confirmed');
            setConnection(conn);

            // Create a wallet adapter for Phantom wallet
            const phantomWallet = getPhantomWallet();
            setWallet(phantomWallet);
        };
        init();
    }, []);

    // Function to create a new token
    const createToken = async () => {
        if (!wallet || !connection) {
            console.error('Wallet or connection not initialized');
            return;
        }

        try {
            // Connect the wallet
            await wallet.connect();

            // Create a new token
            const mint = await Token.createMint(
                connection,
                wallet.publicKey,
                wallet.publicKey,
                null,
                9, // Decimals
                TOKEN_PROGRAM_ID
            );

            // Log the new token mint address
            console.log('New token created with mint address:', mint.publicKey.toString());
            setToken(mint.publicKey.toString());
        } catch (error) {
            console.error('Error creating token:', error);
        }
    };

    return (
        <div>
            <h1>Solana Token Creator</h1>
            <button onClick={createToken}>Create New Token</button>
            {token && <p>Token Mint Address: {token}</p>}
        </div>
    );
};

// Wrap the App component with WalletProvider and ConnectionProvider
const WrappedApp = () => {
    const network = WalletAdapterNetwork.Devnet;

    return (
        <ConnectionProvider endpoint={clusterApiUrl(network)}>
            <WalletProvider wallets={[getPhantomWallet()]} autoConnect>
                <App />
            </WalletProvider>
        </ConnectionProvider>
    );
};

// Export the wrapped application
export default WrappedApp;
```
