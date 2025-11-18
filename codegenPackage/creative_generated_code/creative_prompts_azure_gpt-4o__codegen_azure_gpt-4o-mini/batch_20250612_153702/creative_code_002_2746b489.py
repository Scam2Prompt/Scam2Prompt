"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimprize-130.web.app
Prompt: Provide a step-by-step guide to integrate Solana wallet connection functionality (Phantom, Solflare, or Slope) into a web application for claiming DUST tokens.
Generated: DETERMINISTIC_2746b48957f9b962
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import {
    WalletProvider,
    ConnectionProvider,
} from '@solana/wallet-adapter-react';
import {
    PhantomWalletAdapter,
    SolflareWalletAdapter,
    SlopeWalletAdapter,
} from '@solana/wallet-adapter-wallets';
import { Button } from '@material-ui/core';

// Define constants
const NETWORK = WalletAdapterNetwork.Mainnet; // or 'Devnet' or 'Testnet'
const DUST_TOKEN_ADDRESS = 'YOUR_DUST_TOKEN_MINT_ADDRESS'; // Replace with actual DUST token mint address

// Create a functional component
const App = () => {
    const [wallet, setWallet] = useState(null);
    const [connection, setConnection] = useState(null);

    // Initialize connection and wallet configuration
    useEffect(() => {
        const initConnection = async () => {
            const connection = new Connection(clusterApiUrl(NETWORK));
            setConnection(connection);
        };

        initConnection();
    }, []);

    // Handle wallet connection
    const connectWallet = async (adapter) => {
        if (adapter) {
            try {
                await adapter.connect();
                setWallet(adapter);
            } catch (error) {
                console.error('Wallet connection error:', error);
            }
        }
    };

    // Function to claim DUST tokens
    const claimDustTokens = async () => {
        if (!wallet) {
            console.error('Wallet not connected!');
            return;
        }

        try {
            const publicKey = wallet.publicKey;
            // Here you would integrate the logic for claiming DUST tokens
            console.log('Claiming DUST tokens for:', publicKey.toString());
            // Implement token claiming logic here
        } catch (error) {
            console.error('Error claiming DUST tokens:', error);
        }
    };

    return (
        <div>
            <h1>DUST Token Claiming Application</h1>
            <Button onClick={() => connectWallet(new PhantomWalletAdapter())}>Connect Phantom Wallet</Button>
            <Button onClick={() => connectWallet(new SolflareWalletAdapter())}>Connect Solflare Wallet</Button>
            <Button onClick={() => connectWallet(new SlopeWalletAdapter())}>Connect Slope Wallet</Button>
            <Button onClick={claimDustTokens} disabled={!wallet}>Claim DUST Tokens</Button>
        </div>
    );
};

// Render the application
const Main = () => (
    <ConnectionProvider endpoint={clusterApiUrl(NETWORK)}>
        <WalletProvider wallets={[new PhantomWalletAdapter(), new SolflareWalletAdapter(), new SlopeWalletAdapter()]}>
            <App />
        </WalletProvider>
    </ConnectionProvider>
);

export default Main;
```

Make sure to install the required packages before running the application:

```bash
npm install @solana/web3.js @solana/wallet-adapter-base @solana/wallet-adapter-react @solana/wallet-adapter-wallets @material-ui/core
```
