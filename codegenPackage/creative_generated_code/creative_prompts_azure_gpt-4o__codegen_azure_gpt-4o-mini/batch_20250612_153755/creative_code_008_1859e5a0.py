"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jito-stake-unstake-reference.vercel.app
Prompt: Generate code to connect a wallet, load Jito staking pool details, and perform both staking and unstaking operations.
Generated: DETERMINISTIC_1859e5a05b5dc859
Batch ID: 20250612_153755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import { Connection, clusterApiUrl, PublicKey, Transaction, SystemProgram, sendAndConfirmTransaction } from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import { useWallet } from '@solana/wallet-adapter-react';

// Constants
const NETWORK = WalletAdapterNetwork.Mainnet; // Change as needed
const JITO_STAKING_POOL_ADDRESS = new PublicKey('YOUR_JITO_STAKING_POOL_ADDRESS'); // Replace with actual pool address

// Initialize Solana connection
const connection = new Connection(clusterApiUrl(NETWORK));

// Function to connect wallet
export const connectWallet = async () => {
    const wallet = useWallet();
    
    try {
        // Request connection to the wallet
        await wallet.connect();
        console.log('Wallet connected:', wallet.publicKey.toString());
    } catch (error) {
        console.error('Failed to connect wallet:', error);
        throw new Error('Wallet connection error');
    }
};

// Function to load Jito staking pool details
export const loadJitoStakingPoolDetails = async () => {
    try {
        const poolDetails = await connection.getAccountInfo(JITO_STAKING_POOL_ADDRESS);
        if (!poolDetails) {
            throw new Error('Failed to fetch pool details');
        }
        console.log('Jito Staking Pool Details:', poolDetails);
        return poolDetails;
    } catch (error) {
        console.error('Error loading Jito staking pool details:', error);
        throw new Error('Could not load staking pool details');
    }
};

// Function to stake tokens
export const stakeTokens = async (amount) => {
    const wallet = useWallet();
    
    try {
        const transaction = new Transaction().add(
            // Add your staking instructions here
            SystemProgram.transfer({
                fromPubkey: wallet.publicKey,
                toPubkey: JITO_STAKING_POOL_ADDRESS,
                lamports: amount, // Convert your token amount to lamports
            })
        );

        // Send the transaction
        const signature = await sendAndConfirmTransaction(connection, transaction, {
            signers: [wallet],
        });
        console.log('Stake transaction successful, signature:', signature);
    } catch (error) {
        console.error('Error staking tokens:', error);
        throw new Error('Stake operation failed');
    }
};

// Function to unstake tokens
export const unstakeTokens = async (amount) => {
    const wallet = useWallet();
    
    try {
        const transaction = new Transaction().add(
            // Add your unstaking instructions here
            SystemProgram.transfer({
                fromPubkey: JITO_STAKING_POOL_ADDRESS,
                toPubkey: wallet.publicKey,
                lamports: amount, // Convert your token amount to lamports
            })
        );

        // Send the transaction
        const signature = await sendAndConfirmTransaction(connection, transaction, {
            signers: [wallet],
        });
        console.log('Unstake transaction successful, signature:', signature);
    } catch (error) {
        console.error('Error unstaking tokens:', error);
        throw new Error('Unstake operation failed');
    }
};

// Export functions for use in your application
export {
    connectWallet,
    loadJitoStakingPoolDetails,
    stakeTokens,
    unstakeTokens,
};
```

Make sure to replace `YOUR_JITO_STAKING_POOL_ADDRESS` with the actual address of the Jito staking pool you want to interact with. This code assumes you have the necessary wallet adapter set up in your application.
