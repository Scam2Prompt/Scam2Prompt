"""
Generated Code Metadata:
========================
Original URL: https://wl-usdh-mint.web.app
Prompt: Create a Solana-based minting dApp that differentiates between whitelist and public minting prices, ensuring free minting rights for eligible token holders.
Generated: DETERMINISTIC_c18af29f80ffa7ce
Batch ID: 20250612_152240
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
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import {
    WalletProvider,
    ConnectionProvider,
} from '@solana/wallet-adapter-react';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';
import React, { useEffect, useState } from 'react';
import './App.css';

// Define constants for minting prices
const WHITELIST_PRICE = 0.01; // Price for whitelisted users in SOL
const PUBLIC_PRICE = 0.02; // Price for public minting in SOL
const FREE_MINTING_TOKEN_ID = 'YOUR_FREE_MINTING_TOKEN_ID'; // Replace with actual token ID

// Main App component
const App = () => {
    const [wallet, setWallet] = useState(null);
    const [isWhitelisted, setIsWhitelisted] = useState(false);
    const [mintingPrice, setMintingPrice] = useState(PUBLIC_PRICE);

    // Connect to Solana network
    const connection = new Connection(clusterApiUrl('devnet'), 'confirmed');

    // Function to check if the user is whitelisted
    const checkWhitelist = async (walletAddress) => {
        try {
            // Logic to check if the wallet is whitelisted
            // This could involve checking a list of addresses or a smart contract
            const isWhitelisted = await fetchWhitelistStatus(walletAddress);
            setIsWhitelisted(isWhitelisted);
            setMintingPrice(isWhitelisted ? WHITELIST_PRICE : PUBLIC_PRICE);
        } catch (error) {
            console.error('Error checking whitelist status:', error);
        }
    };

    // Function to handle minting
    const handleMint = async () => {
        if (!wallet) {
            alert('Please connect your wallet first.');
            return;
        }

        try {
            const mintingCost = isWhitelisted ? WHITELIST_PRICE : PUBLIC_PRICE;

            // Check if the user is eligible for free minting
            const hasFreeMintingRights = await checkFreeMintingRights(wallet.publicKey);

            if (hasFreeMintingRights) {
                // Proceed with free minting
                console.log('Minting for free...');
            } else {
                // Proceed with paid minting
                console.log(`Minting for ${mintingCost} SOL...`);
            }

            // Call the minting function (to be implemented)
            await mintToken(wallet.publicKey, hasFreeMintingRights ? 0 : mintingCost);
        } catch (error) {
            console.error('Error during minting:', error);
        }
    };

    // Function to fetch whitelist status (mock implementation)
    const fetchWhitelistStatus = async (walletAddress) => {
        // Replace with actual logic to check whitelist
        return walletAddress === 'YOUR_WHITELISTED_ADDRESS'; // Example check
    };

    // Function to check free minting rights (mock implementation)
    const checkFreeMintingRights = async (walletAddress) => {
        // Replace with actual logic to check token ownership
        return walletAddress === 'YOUR_FREE_MINTING_ADDRESS'; // Example check
    };

    // Function to mint the token (mock implementation)
    const mintToken = async (walletAddress, cost) => {
        // Replace with actual minting logic
        console.log(`Minting token for ${walletAddress} with cost: ${cost} SOL`);
    };

    // Effect to check whitelist status on wallet change
    useEffect(() => {
        if (wallet) {
            checkWhitelist(wallet.publicKey);
        }
    }, [wallet]);

    return (
        <div className="App">
            <h1>Solana Minting dApp</h1>
            <button onClick={handleMint}>Mint Token</button>
        </div>
    );
};

// Main entry point
const Main = () => {
    const network = WalletAdapterNetwork.Devnet;
    const endpoint = clusterApiUrl(network);

    return (
        <ConnectionProvider endpoint={endpoint}>
            <WalletProvider wallets={[new PhantomWalletAdapter()]}>
                <App />
            </WalletProvider>
        </ConnectionProvider>
    );
};

export default Main;
```
