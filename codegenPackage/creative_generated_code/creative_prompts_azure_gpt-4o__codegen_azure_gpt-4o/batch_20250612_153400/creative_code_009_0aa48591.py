"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hpcom.pages.dev
Prompt: Generate a JavaScript function using Solana Web3.js to connect a wallet, calculate the amount of SOL to swap for $SLOTH, and execute the transaction.
Generated: DETERMINISTIC_0aa4859106a2654e
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required Solana Web3.js library
const { Connection, clusterApiUrl, PublicKey, Transaction, SystemProgram } = require('@solana/web3.js');

// Import wallet adapter
const { WalletAdapterNetwork, PhantomWalletAdapter } = require('@solana/wallet-adapter-base');

// Define constants
const SLOTH_TOKEN_MINT_ADDRESS = "Your_SLOTH_Mint_Address"; // Replace with actual SLOTH token mint address
const DECIMALS = 9; // Replace with SLOTH token's decimals
const SLOTH_SWAP_RATE = 0.1; // Replace with the rate (e.g., 1 SOL = 10 SLOTH)

// Connect wallet, calculate swap amount, and execute transaction
async function swapSolForSloth(solAmount) {
    try {
        // Validate input
        if (solAmount <= 0) {
            throw new Error("Invalid SOL amount. Must be greater than 0.");
        }

        // Establish connection to Solana network
        const connection = new Connection(clusterApiUrl('mainnet-beta'), 'confirmed');

        // Initialize wallet adapter (using Phantom wallet as an example)
        const wallet = new PhantomWalletAdapter();
        await wallet.connect();

        // Get public key of the connected wallet
        const walletPublicKey = wallet.publicKey;
        if (!walletPublicKey) {
            throw new Error("Failed to retrieve wallet public key.");
        }

        // Calculate SLOTH amount to swap
        const slothAmount = solAmount / SLOTH_SWAP_RATE;
        const slothAmountInLamports = slothAmount * Math.pow(10, DECIMALS); // Convert to smallest unit

        // Create the transaction
        const transaction = new Transaction().add(
            SystemProgram.transfer({
                fromPubkey: walletPublicKey,
                toPubkey: new PublicKey(SLOTH_TOKEN_MINT_ADDRESS), // Replace with actual recipient address
                lamports: solAmount * Math.pow(10, 9), // Convert SOL to lamports
            })
        );

        // Sign and send the transaction
        const signedTransaction = await wallet.signTransaction(transaction);
        const signature = await connection.sendRawTransaction(signedTransaction.serialize(), {
            skipPreflight: false,
            preflightCommitment: 'confirmed',
        });

        // Confirm the transaction
        await connection.confirmTransaction(signature, 'confirmed');
        console.log(`Transaction successful! Signature: ${signature}`);
        console.log(`Swapped ${solAmount} SOL for ${slothAmount} SLOTH.`);
    } catch (error) {
        console.error("An error occurred during the swap:", error.message);
    }
}

// Example usage: Swap 1 SOL for SLOTH
swapSolForSloth(1);
```

> **Note:** Replace placeholder values (e.g., `Your_SLOTH_Mint_Address`) with actual addresses and configurations tailored to your use case. This code assumes `PhantomWalletAdapter` is installed and properly set up in your project.
