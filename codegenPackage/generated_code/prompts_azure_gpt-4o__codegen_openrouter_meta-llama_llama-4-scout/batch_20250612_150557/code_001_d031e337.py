"""
Generated Code Metadata:
========================
Original URL: https://boxstelth.web.app
Prompt: Generate a script to connect a Solana wallet to a web application and display wallet balances, including the "Основной кошелек" and "Торговый кошелек" balances.
Generated: DETERMINISTIC_d031e33789dcc1f4
Batch ID: 20250612_150557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { SolletWallet } from '@solana/sollet-wallet';

// Set up the Solana connection
const connection = new Connection(clusterApiUrl('mainnet-beta'));

// Set up the Sollet wallet
const solletWallet = new SolletWallet();

// Function to get wallet balances
async function getWalletBalances(walletAddress) {
    try {
        // Get the wallet's public key
        const publicKey = new PublicKey(walletAddress);

        // Get the account info
        const accountInfo = await connection.getAccountInfo(publicKey);

        // Check if account info exists
        if (!accountInfo) {
            throw new Error(`Account not found: ${walletAddress}`);
        }

        // Get the balance
        const balance = accountInfo.lamports / 1e9; // Convert lamports to SOL

        return balance;
    } catch (error) {
        console.error(`Error getting wallet balance: ${error.message}`);
        return null;
    }
}

// Function to connect to the Solana wallet
async function connectWallet() {
    try {
        // Connect to the Sollet wallet
        await solletWallet.connect();

        // Get the wallet addresses
        const mainWalletAddress = solletWallet.publicKey.toString();
        const tradeWalletAddress = 'trade-wallet-address'; // Replace with trade wallet address

        // Get the wallet balances
        const mainWalletBalance = await getWalletBalances(mainWalletAddress);
        const tradeWalletBalance = await getWalletBalances(tradeWalletAddress);

        // Display wallet balances
        console.log(`Основной кошелек balance: ${mainWalletBalance} SOL`);
        console.log(`Торговый кошелек balance: ${tradeWalletBalance} SOL`);

        // Return wallet balances
        return {
            mainWalletBalance,
            tradeWalletBalance,
        };
    } catch (error) {
        console.error(`Error connecting to wallet: ${error.message}`);
        return null;
    }
}

// Main function
async function main() {
    try {
        // Connect to the wallet
        const walletBalances = await connectWallet();

        // Check if wallet balances exist
        if (!walletBalances) {
            return;
        }

        // Display wallet balances in the web application
        const mainWalletBalanceElement = document.getElementById('main-wallet-balance');
        const tradeWalletBalanceElement = document.getElementById('trade-wallet-balance');

        mainWalletBalanceElement.textContent = `Основной кошелек: ${walletBalances.mainWalletBalance} SOL`;
        tradeWalletBalanceElement.textContent = `Торговый кошелек: ${walletBalances.tradeWalletBalance} SOL`;
    } catch (error) {
        console.error(`Error: ${error.message}`);
    }
}

// Call the main function
main();

// Example HTML elements to display wallet balances
// <p id="main-wallet-balance"></p>
// <p id="trade-wallet-balance"></p>
```
