"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dao-nfty.web.app
Prompt: Generate code to integrate a Solana wallet connection feature into a web app, allowing users to claim rewards in $TNSR tokens based on their activity on Tensor's NFT trading platform.
Generated: DETERMINISTIC_5ed6f1407f46310e
Batch ID: 20250612_153716
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
    useWallet,
} from '@solana/wallet-adapter-react';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';
import { Token, TOKEN_PROGRAM_ID } from '@solana/spl-token';
import {
    Button,
    Container,
    Typography,
} from '@mui/material';

// Define the network
const network = WalletAdapterNetwork.Mainnet;

// Create an array of wallet adapters
const walletAdapters = [
    new PhantomWalletAdapter(),
];

// Component to handle wallet connection and reward claiming
const App = () => {
    const { wallet, signTransaction } = useWallet();
    const [rewards, setRewards] = useState(0);

    useEffect(() => {
        // Fetch rewards when the component mounts
        const fetchRewards = async () => {
            if (!wallet) return;
            try {
                const connection = new Connection(clusterApiUrl(network), 'confirmed');
                const publicKey = wallet.publicKey;

                // Example: Fetch user activity data (mock implementation)
                const activityData = await getUserActivity(publicKey);
                const claimedRewards = calculateRewards(activityData);

                setRewards(claimedRewards);
            } catch (error) {
                console.error("Error fetching rewards:", error);
            }
        };
        fetchRewards();
    }, [wallet]);

    // Function to simulate fetching user activity
    const getUserActivity = async (publicKey) => {
        // Placeholder for activity fetching logic
        // This would typically involve RPC calls to your backend
        return Promise.resolve({ activityCount: 5 }); // Mock data
    };

    // Function to calculate rewards based on activity
    const calculateRewards = (activityData) => {
        const { activityCount } = activityData;
        return activityCount * 10; // Example reward calculation
    };

    // Function to claim rewards
    const claimRewards = async () => {
        if (!wallet) {
            alert("Please connect your wallet first.");
            return;
        }

        try {
            // Initialize connection
            const connection = new Connection(clusterApiUrl(network), 'confirmed');
            const publicKey = wallet.publicKey;
            const transaction = await createTokenTransaction(publicKey, rewards);
            const signature = await wallet.sendTransaction(transaction, connection);

            // Confirm the transaction
            await connection.confirmTransaction(signature, 'confirmed');
            alert("Rewards claimed successfully!");
        } catch (error) {
            console.error("Error claiming rewards:", error);
            alert("Failed to claim rewards. Please try again.");
        }
    };

    // Function to create a token transaction (mock implementation)
    const createTokenTransaction = async (publicKey, amount) => {
        // This function should create and return a transaction for minting or transferring tokens
        const mintPublicKey = new PublicKey("<TOKEN_MINT_ADDRESS>"); // Replace with actual token mint address
        const transaction = new Token(connection, mintPublicKey, TOKEN_PROGRAM_ID, publicKey);
        
        // Placeholder for token transaction logic
        // e.g., creating a transfer instruction, adding it to a transaction, etc.

        return transaction; // Mock implementation, replace with actual transaction
    };

    return (
        <Container>
            <Typography variant="h4">Claim Your $TNSR Rewards</Typography>
            {!wallet ? (
                <Button onClick={() => wallet.connect()} variant="contained">
                    Connect Wallet
                </Button>
            ) : (
                <>
                    <Typography variant="h6">Available Rewards: ${rewards}</Typography>
                    <Button onClick={claimRewards} variant="contained">
                        Claim Rewards
                    </Button>
                </>
            )}
        </Container>
    );
};

// Main render method
const Main = () => {
    return (
        <ConnectionProvider endpoint={clusterApiUrl(network)}>
            <WalletProvider wallets={walletAdapters}>
                <App />
            </WalletProvider>
        </ConnectionProvider>
    );
};

export default Main;
```
