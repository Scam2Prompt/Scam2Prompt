"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint-playpixiz.vercel.app
Prompt: Write code to interact with the Pixiz NFT presale on the Solana blockchain, including wallet connection and minting Yetiz NFTs using the specified SOL price tiers.
Generated: DETERMINISTIC_7fd8d21b767f1728
Batch ID: 20250612_153606
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
import { WalletProvider, ConnectionProvider, useWallet } from '@solana/wallet-adapter-react';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';
import { TokenInstructions, createMint, mintTo } from '@solana/spl-token';
import { notify } from './notifications'; // Custom notification utility

// Define constants for the application
const NETWORK = WalletAdapterNetwork.Devnet; // Change to Mainnet for production
const MINT_ADDRESS = "INSERT_YETIZ_MINT_ADDRESS_HERE"; // Replace with actual mint address
const SOL_PRICE_TIERS = [0.5, 1.0, 1.5]; // Specified SOL price tiers for minting

// Component to handle wallet connection and NFT minting
const MintYetizNFT = () => {
    const { publicKey, connected, disconnect } = useWallet(); // Get wallet info
    const [minting, setMinting] = useState(false);
    
    // Function to connect the wallet
    const connectWallet = async () => {
        if (connected) return; // If already connected, do nothing
        try {
            // Attempt to connect to the wallet
            await wallet.connect();
        } catch (error) {
            console.error('Wallet connection failed:', error);
            notify({ message: 'Wallet connection failed.', type: 'error' });
        }
    };

    // Function to mint Yetiz NFT
    const mintNFT = async () => {
        if (!connected || !publicKey) return; // Ensure user is connected

        setMinting(true);
        try {
            const connection = new Connection(clusterApiUrl(NETWORK), 'confirmed');

            // Check SOL balance before minting
            const balance = await connection.getBalance(publicKey);
            const requiredSol = SOL_PRICE_TIERS[0]; // Select price tier for minting

            if (balance < requiredSol * 1e9) { // Convert SOL to lamports
                notify({ message: 'Insufficient SOL balance for minting.', type: 'error' });
                setMinting(false);
                return;
            }

            // Mint the NFT (mock implementation, replace with actual mint function)
            const mint = await createMint(connection, publicKey, publicKey, null, 0);
            await mintTo(connection, publicKey, mint, publicKey, [], 1); // Mint 1 NFT

            notify({ message: 'NFT minted successfully!', type: 'success' });
        } catch (error) {
            console.error('Minting failed:', error);
            notify({ message: 'Minting failed.', type: 'error' });
        } finally {
            setMinting(false);
        }
    };

    return (
        <div>
            <h1>Mint Yetiz NFT</h1>
            <button onClick={connectWallet}>Connect Wallet</button>
            <button onClick={mintNFT} disabled={!connected || minting}>
                {minting ? 'Minting...' : 'Mint NFT'}
            </button>
            {connected && <p>Wallet connected: {publicKey.toString()}</p>}
            {connected && <button onClick={disconnect}>Disconnect Wallet</button>}
        </div>
    );
};

// Main App component
const App = () => {
    return (
        <ConnectionProvider endpoint={clusterApiUrl(NETWORK)}>
            <WalletProvider wallets={[new PhantomWalletAdapter()]}>
                <MintYetizNFT />
            </WalletProvider>
        </ConnectionProvider>
    );
};

// Export the App component
export default App;
```

Ensure to install the required packages before running the code:
```bash
npm install @solana/web3.js @solana/wallet-adapter-react @solana/wallet-adapter-phantom @solana/spl-token
``` 

This code provides a complete setup for connecting a wallet and minting Yetiz NFTs on the Solana blockchain with proper error handling and user notifications.
