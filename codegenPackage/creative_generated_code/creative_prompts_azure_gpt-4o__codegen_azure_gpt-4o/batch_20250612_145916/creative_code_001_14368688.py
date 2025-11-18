"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trump-coin-aidrops.pages.dev
Prompt: Generate code to integrate the Phantom wallet into a web application for purchasing $TRUMP tokens. Ensure the code supports SOL funding and token swapping via Raydium.
Generated: DETERMINISTIC_143686880ada8991
Batch ID: 20250612_145916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { Token, ASSOCIATED_TOKEN_PROGRAM_ID, TOKEN_PROGRAM_ID } from "@solana/spl-token";
import { WalletAdapterNetwork, PhantomWalletAdapter } from '@solana/wallet-adapter-wallets';
import { Raydium } from 'raydium-sdk';
import BigNumber from 'bignumber.js';

// Constants
const NETWORK = WalletAdapterNetwork.Mainnet; // Set to Mainnet for production
const TOKEN_MINT_ADDRESS = "TRUMP_TOKEN_MINT_ADDRESS"; // Replace with the $TRUMP token mint address
const RAYDIUM_POOL_ADDRESS = "RAYDIUM_POOL_ADDRESS"; // Replace with the Raydium pool address for $TRUMP
const SOLANA_RPC_URL = clusterApiUrl(NETWORK);

// Initialize connection
const connection = new Connection(SOLANA_RPC_URL, 'confirmed');

// Initialize Phantom Wallet Adapter
const phantomWallet = new PhantomWalletAdapter();

// Function to connect Phantom wallet
async function connectWallet() {
    try {
        await phantomWallet.connect();
        console.log("Wallet connected:", phantomWallet.publicKey.toString());
    } catch (error) {
        console.error("Failed to connect wallet:", error);
    }
}

// Function to get the wallet's balance in SOL
async function getBalance() {
    try {
        const balance = await connection.getBalance(phantomWallet.publicKey);
        console.log("Wallet balance (SOL):", balance / 10 ** 9);
        return balance;
    } catch (error) {
        console.error("Failed to retrieve wallet balance:", error);
        return 0;
    }
}

// Function to purchase $TRUMP tokens using Raydium
async function purchaseTrumpTokens(amountSOL) {
    try {
        if (!phantomWallet.connected) {
            throw new Error("Wallet not connected");
        }

        const solBalance = await getBalance();
        const amountSOLInLamports = amountSOL * 10 ** 9;

        if (solBalance < amountSOLInLamports) {
            throw new Error("Insufficient SOL balance");
        }

        // Swap SOL to $TRUMP via Raydium
        const raydiumSwap = new Raydium({
            connection,
            poolAddress: new PublicKey(RAYDIUM_POOL_ADDRESS),
            wallet: phantomWallet,
        });

        const transaction = await raydiumSwap.swap({
            inputMint: Token.createMintPublicKey(
                TOKEN_PROGRAM_ID,
                phantomWallet.publicKey,
                SOLANA_RPC_URL
            ),
            outputMint: new PublicKey(TOKEN_MINT_ADDRESS),
            inputAmount: new BigNumber(amountSOLInLamports),
            slippage: 0.01, // Set acceptable slippage
        });

        const signature = await phantomWallet.signTransaction(transaction);
        const txId = await connection.sendRawTransaction(signature.serialize());
        console.log("Transaction successful. Tx ID:", txId);
    } catch (error) {
        console.error("Failed to swap SOL for $TRUMP tokens:", error);
    }
}

// Event listener for wallet connect button
document.getElementById("connectWalletButton").addEventListener("click", () => {
    connectWallet();
});

// Event listener for purchase button
document.getElementById("purchaseButton").addEventListener("click", async () => {
    const amountSOL = parseFloat(document.getElementById("amountInput").value);
    if (isNaN(amountSOL) || amountSOL <= 0) {
        alert("Please enter a valid SOL amount");
        return;
    }

    await purchaseTrumpTokens(amountSOL);
});

// Note: Replace the placeholder IDs in the DOM event listeners with actual IDs from your HTML structure.
```
