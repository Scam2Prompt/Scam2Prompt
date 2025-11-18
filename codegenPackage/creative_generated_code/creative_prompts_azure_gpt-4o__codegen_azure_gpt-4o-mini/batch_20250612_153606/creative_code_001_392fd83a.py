"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint-pixiz.vercel.app
Prompt: Generate a script to mint Yetiz tokens during the whitelist phase by specifying the price of 0.25 SOL and ensuring wallet connection compatibility.
Generated: DETERMINISTIC_392fd83a086f5c48
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import { WalletProvider } from '@solana/wallet-adapter-react';
import { PhantomWalletAdapter } from '@solana/wallet-adapter Phantom';
import { useWallet } from '@solana/wallet-adapter-react';
import React, { useEffect, useState } from 'react';

// Define the Yetiz Token Minting Component
const YetizTokenMinter = () => {
    // State to manage connection and minting status
    const [isConnected, setIsConnected] = useState(false);
    const [error, setError] = useState(null);
    const wallet = useWallet();
    const mintPrice = 0.25; // Price in SOL

    // Function to connect the wallet
    const connectWallet = async () => {
        try {
            await wallet.connect();
            setIsConnected(true);
        } catch (err) {
            setError('Failed to connect wallet: ' + err.message);
        }
    };

    // Function to mint Yetiz tokens
    const mintTokens = async () => {
        if (!isConnected) {
            setError('Wallet is not connected');
            return;
        }

        try {
            // Create a connection to the Solana blockchain
            const connection = new Connection(clusterApiUrl('mainnet-beta'), 'confirmed');

            // Calculate the amount of SOL to send
            const lamports = mintPrice * 1e9; // Convert SOL to lamports (1 SOL = 1e9 lamports)

            // Create a transaction to mint the tokens
            // Replace with your actual minting logic
            const transaction = {
                // Transaction details (to be filled with actual minting logic)
            };

            // Send the transaction to mint tokens
            const signature = await wallet.sendTransaction(transaction, connection);

            // Confirm that the transaction has been processed
            await connection.confirmTransaction(signature, 'confirmed');

            alert('Tokens minted successfully!');
        } catch (err) {
            setError('Failed to mint tokens: ' + err.message);
        }
    };

    // Render the component
    return (
        <div>
            <h1>Yetiz Token Minter</h1>
            {error && <div style={{ color: 'red' }}>{error}</div>}
            {!isConnected ? (
                <button onClick={connectWallet}>Connect Wallet</button>
            ) : (
                <button onClick={mintTokens}>Mint Yetiz Tokens for {mintPrice} SOL</button>
            )}
        </div>
    );
};

// Main App component
const App = () => {
    return (
        <WalletProvider wallets={[new PhantomWalletAdapter()]} autoConnect>
            <YetizTokenMinter />
        </WalletProvider>
    );
};

// Export the App component as the default export
export default App;
```
