"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maqicedao.web.app
Prompt: Generate code to connect a Solana-compatible wallet and display the wallet's balance for both the "Основной кошелек" (main wallet) and "Торговый кошелек" (trading wallet) as described on the website.
Generated: DETERMINISTIC_7710ce526734d518
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary Solana web3 and wallet adapter libraries
import { clusterApiUrl, Connection, PublicKey } from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import { WalletAdapter } from '@solana/wallet-adapter-react';

// Constants for Solana connection and wallets
const SOLANA_NETWORK = WalletAdapterNetwork.Mainnet; // Use the Mainnet network
const SOLANA_RPC_ENDPOINT = clusterApiUrl(SOLANA_NETWORK); // Get the RPC endpoint
const MAIN_WALLET_ADDRESS = 'YourMainWalletPublicKeyHere'; // Replace with Main Wallet Public Key
const TRADING_WALLET_ADDRESS = 'YourTradingWalletPublicKeyHere'; // Replace with Trading Wallet Public Key

// Create a connection to the Solana blockchain
const connection = new Connection(SOLANA_RPC_ENDPOINT, 'confirmed');

// Function to get wallet balance in SOL
async function getWalletBalance(walletAddress) {
    try {
        // Validate the wallet address
        const publicKey = new PublicKey(walletAddress);

        // Fetch balance and convert from lamports to SOL (1 SOL = 10^9 lamports)
        const balanceLamports = await connection.getBalance(publicKey);
        const balanceSOL = balanceLamports / 1e9;

        return balanceSOL;
    } catch (error) {
        console.error(`Error fetching balance for wallet ${walletAddress}:`, error);
        return null; // Return null in case of an error
    }
}

// Function to connect the user's wallet and fetch balances
async function connectWalletAndFetchBalances(walletAdapter) {
    try {
        // Ensure the wallet adapter is ready
        if (!walletAdapter || !walletAdapter.connected) {
            console.error('Wallet is not connected. Please connect your wallet first.');
            return;
        }

        // Get Main Wallet Balance
        const mainWalletBalance = await getWalletBalance(MAIN_WALLET_ADDRESS);
        console.log(`Основной кошелек (Main Wallet) Balance: ${mainWalletBalance} SOL`);

        // Get Trading Wallet Balance
        const tradingWalletBalance = await getWalletBalance(TRADING_WALLET_ADDRESS);
        console.log(`Торговый кошелек (Trading Wallet) Balance: ${tradingWalletBalance} SOL`);
    } catch (error) {
        console.error('Error during wallet connection or fetching balances:', error);
    }
}

// Example usage with a wallet adapter (replace with your wallet logic)
const walletAdapter = new WalletAdapter(); // Replace with your wallet adapter initialization
walletAdapter.on('connect', async () => {
    await connectWalletAndFetchBalances(walletAdapter);
});

// Example trigger for connecting the wallet (such as a button click)
document.getElementById('connectWalletButton').addEventListener('click', async () => {
    try {
        await walletAdapter.connect(); // Trigger wallet connection
    } catch (error) {
        console.error('Error connecting wallet:', error);
    }
});
```
