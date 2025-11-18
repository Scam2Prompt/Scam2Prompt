"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-daol.web.app
Prompt: Generate code to integrate a Solana wallet connection feature into a web application, allowing users to claim rewards in $TNSR tokens from the Tensor platform.
Generated: DETERMINISTIC_b4fa92e241073e35
Batch ID: 20250612_150557
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
import { WalletProvider, getDefaultWallets } from '@solana/wallet-adapter-react';
import { WalletModalProvider } from '@solana/wallet-adapter-react-ui';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';
import { Button, Alert } from 'react-bootstrap';

// Set the network
const network = WalletAdapterNetwork.Devnet; // Change to Mainnet for production

// Create a Solana connection
const connection = new Connection(clusterApiUrl(network), 'confirmed');

// Main App component
const App = () => {
    const [walletAddress, setWalletAddress] = useState(null);
    const [error, setError] = useState('');

    // Function to handle wallet connection
    const connectWallet = async () => {
        try {
            const provider = window.solana;
            if (provider) {
                const response = await provider.connect();
                setWalletAddress(response.publicKey.toString());
            } else {
                throw new Error('Phantom wallet is not installed');
            }
        } catch (err) {
            setError(err.message);
        }
    };

    // Function to claim rewards
    const claimRewards = async () => {
        if (!walletAddress) {
            setError('Please connect your wallet first');
            return;
        }

        try {
            const transaction = await createRewardTransaction(walletAddress);
            const provider = window.solana;
            const signature = await provider.signAndSendTransaction(transaction);
            await connection.confirmTransaction(signature, 'processed');

            alert('Rewards claimed successfully!');
        } catch (err) {
            setError(`Failed to claim rewards: ${err.message}`);
        }
    };

    // Function to create reward transaction (dummy implementation)
    const createRewardTransaction = async (walletAddress) => {
        // Implement the logic to create a transaction to claim $TNSR tokens
        const transaction = {}; // Replace with actual transaction creation logic
        return transaction;
    };

    return (
        <div className="App">
            <h1>TNSR Token Rewards</h1>
            {error && <Alert variant="danger">{error}</Alert>}
            {walletAddress ? (
                <div>
                    <p>Connected Wallet: {walletAddress}</p>
                    <Button onClick={claimRewards}>Claim $TNSR Rewards</Button>
                </div>
            ) : (
                <Button onClick={connectWallet}>Connect Wallet</Button>
            )}
        </div>
    );
};

// Main render
const Main = () => {
    const { wallets } = getDefaultWallets({
        connection,
        autoConnect: true,
    });

    return (
        <WalletProvider wallets={wallets} autoConnect>
            <WalletModalProvider>
                <App />
            </WalletModalProvider>
        </WalletProvider>
    );
};

export default Main;

// Note: Ensure you have the required packages installed:
// npm install @solana/web3.js @solana/wallet-adapter-react @solana/wallet-adapter-phantom react-bootstrap
// For production, switch 'Devnet' to 'Mainnet' and handle token transaction logic.
```
