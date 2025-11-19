"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pengwu.io
Prompt: Write a code snippet to connect a Phantom wallet for purchasing PENGWU tokens using Solana's network.
Generated: DETERMINISTIC_854947f28ecc47a1
Batch ID: 20250612_155632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules and libraries
import { Connection, PublicKey, Transaction, clusterApiUrl } from "@solana/web3.js";
import { PhantomWalletAdapter } from "@solana/wallet-adapter-phantom";

// Constants
const NETWORK = clusterApiUrl("mainnet-beta"); // Use Mainnet Beta for production
const PENGWU_TOKEN_MINT_ADDRESS = "YourPengwuTokenMintAddressHere"; // Replace with the actual token mint address
const MERCHANT_PUBLIC_KEY = "YourMerchantPublicKeyHere"; // Replace with the merchant's public key

// Initialize Solana connection and Phantom wallet adapter
const connection = new Connection(NETWORK, "confirmed");
const walletAdapter = new PhantomWalletAdapter();

// Function to connect Phantom wallet
async function connectWallet() {
    try {
        // Check if Phantom wallet is installed
        if (!walletAdapter.ready) {
            throw new Error("Phantom wallet is not installed. Please install the extension.");
        }

        // Connect the wallet
        await walletAdapter.connect();
        console.log("Wallet connected:", walletAdapter.publicKey.toString());
    } catch (error) {
        console.error("Error connecting wallet:", error.message);
    }
}

// Function to purchase PENGWU tokens
async function purchasePengwuTokens(amount) {
    try {
        // Ensure wallet is connected
        if (!walletAdapter.connected) {
            throw new Error("Wallet is not connected. Please connect your wallet first.");
        }

        // Create a transfer transaction
        const transaction = new Transaction().add(
            // Add transfer instruction
            {
                keys: [
                    { pubkey: walletAdapter.publicKey, isSigner: true, isWritable: true },
                    { pubkey: new PublicKey(MERCHANT_PUBLIC_KEY), isSigner: false, isWritable: true },
                ],
                programId: new PublicKey(PENGWU_TOKEN_MINT_ADDRESS),
                data: Buffer.from(Uint8Array.of(amount)), // Example: Replace with actual token transfer data
            }
        );

        // Set the recent blockhash
        transaction.recentBlockhash = (await connection.getRecentBlockhash()).blockhash;

        // Sign the transaction
        const signedTransaction = await walletAdapter.signTransaction(transaction);

        // Send the transaction to the network
        const signature = await connection.sendRawTransaction(signedTransaction.serialize());
        console.log("Transaction successful! Signature:", signature);

        // Confirm the transaction
        await connection.confirmTransaction(signature, "confirmed");
        console.log("Transaction confirmed.");
    } catch (error) {
        console.error("Error purchasing PENGWU tokens:", error.message);
    }
}

// Example usage
(async () => {
    await connectWallet(); // Connect the Phantom wallet
    await purchasePengwuTokens(1); // Purchase 1 PENGWU token (replace with desired amount)
})();
```

Replace `YourPengwuTokenMintAddressHere` and `YourMerchantPublicKeyHere` with the actual token mint address and merchant's public key, respectively. Ensure the required libraries (`@solana/web3.js` and `@solana/wallet-adapter-phantom`) are installed in your project.
