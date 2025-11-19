"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solflarewebwallet.io
Prompt: Write a code snippet that demonstrates how to integrate the Solflare wallet API for sending and receiving Solana assets.
Generated: DETERMINISTIC_8c9a12a2a8219bf4
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { Connection, PublicKey, clusterApiUrl, Transaction, SystemProgram, Keypair } from '@solana/web3.js';
import { SolflareWalletAdapter } from '@solana/wallet-adapter-solflare';
import { WalletProvider } from '@solana/wallet-adapter-react';
import React, { useEffect, useState } from 'react';

// Set the network
const network = clusterApiUrl('mainnet-beta');

// Create a connection to the Solana cluster
const connection = new Connection(network);

// Function to send SOL from one wallet to another
const sendSol = async (senderKeypair, recipientPubKey, amount) => {
    try {
        // Create a transaction
        const transaction = new Transaction().add(
            SystemProgram.transfer({
                fromPubkey: senderKeypair.publicKey,
                toPubkey: new PublicKey(recipientPubKey),
                lamports: amount * 1e9, // Convert SOL to lamports
            })
        );

        // Sign and send the transaction
        const signature = await connection.sendTransaction(transaction, [senderKeypair]);
        
        // Confirm the transaction
        await connection.confirmTransaction(signature, 'processed');
        
        console.log(`Transaction successful with signature: ${signature}`);
    } catch (error) {
        console.error('Transaction failed:', error);
    }
};

// React component to demonstrate wallet integration
const SolanaWalletIntegration = () => {
    const [wallet, setWallet] = useState(null);

    // Effect to initialize wallet connection
    useEffect(() => {
        const walletAdapter = new SolflareWalletAdapter();
        setWallet(walletAdapter);
    }, []);

    // Example usage of sending SOL
    const handleSendSol = async () => {
        if (!wallet || !wallet.publicKey) {
            console.error('Wallet not connected');
            return;
        }

        const recipient = 'RECIPIENT_PUBLIC_KEY'; // Replace with actual recipient's public key
        const amount = 0.01; // Amount in SOL to send
        
        await sendSol(wallet, recipient, amount);
    };

    return (
        <div>
            <h1>Solana Wallet Integration</h1>
            <button onClick={handleSendSol}>Send SOL</button>
        </div>
    );
};

// Main entry point to render the application
const App = () => {
    return (
        <WalletProvider wallets={[new SolflareWalletAdapter()]}>
            <SolanaWalletIntegration />
        </WalletProvider>
    );
};

export default App;
```
