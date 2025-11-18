"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wl-usdh-mint.web.app
Prompt: Create a JavaScript function using Solana's web3.js library to interact with a minting platform, ensuring the wallet is connected and the user is entitled to free minting rights.
Generated: DETERMINISTIC_a97d29958b0575df
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import Solana web3.js library
const { Connection, PublicKey, clusterApiUrl } = require("@solana/web3.js");
const { getAssociatedTokenAddress, createAssociatedTokenAccountInstruction, Token } = require("@solana/spl-token");

// Initialize constants
const MINT_ADDRESS = "<REPLACE_WITH_MINT_ADDRESS>"; // Replace with actual mint address
const PLATFORM_PROGRAM_ID = "<REPLACE_WITH_PLATFORM_PROGRAM_ID>"; // Replace with program ID for minting platform
const FREE_MINTING_RIGHTS_ACCOUNT = "<REPLACE_WITH_RIGHTS_ACCOUNT>"; // Replace with free minting rights account address

/**
 * Connect a wallet and check eligibility for free minting, then initiate minting.
 * @param {PublicKey} userWallet - The public key of the user's wallet.
 * @param {Connection} connection - The Solana RPC connection.
 * @returns {Promise<void>} - Resolves when minting is successful or throws an error.
 */
async function mintFreeNFT(userWallet, connection) {
    try {
        // Validate input parameters
        if (!userWallet || !connection) {
            throw new Error("Invalid parameters: Wallet and connection are required.");
        }

        // Establish connection to Solana cluster
        const clusterUrl = clusterApiUrl("mainnet-beta"); // Change to 'devnet' or 'testnet' for testing
        const solanaConnection = connection || new Connection(clusterUrl);

        // Check user's free minting rights
        const freeMintingRightsAcc = new PublicKey(FREE_MINTING_RIGHTS_ACCOUNT);
        const accountInfo = await solanaConnection.getAccountInfo(freeMintingRightsAcc);

        if (!accountInfo || accountInfo.lamports === 0) {
            throw new Error("User is not eligible for free minting rights.");
        }

        // Get associated token account for mint
        const mintPubKey = new PublicKey(MINT_ADDRESS);
        const associatedTokenAccount = await getAssociatedTokenAddress(mintPubKey, userWallet);

        // Check if associated token account already exists
        const associatedAccountInfo = await solanaConnection.getAccountInfo(associatedTokenAccount);

        let transaction = null;

        if (!associatedAccountInfo) {
            // Create associated token account for user
            transaction = createAssociatedTokenAccountInstruction(
                userWallet, // Payer
                associatedTokenAccount, // Associated token account address
                userWallet, // Owner of the account
                mintPubKey // Mint address
            );
        }

        // Mint transaction logic (platform-specific program interaction)
        const mintInstruction = {
            keys: [
                { pubkey: userWallet, isSigner: true, isWritable: true },
                { pubkey: associatedTokenAccount, isSigner: false, isWritable: true },
                { pubkey: freeMintingRightsAcc, isSigner: false, isWritable: false },
            ],
            programId: new PublicKey(PLATFORM_PROGRAM_ID),
            data: Buffer.from([]), // Add minting-specific data here
        };

        transaction = transaction || mintInstruction;

        // Send transaction to the cluster
        const signature = await solanaConnection.sendTransaction(transaction, [userWallet]);

        // Confirm transaction
        await solanaConnection.confirmTransaction(signature, "confirmed");

        console.log("Minting successful!");
    } catch (error) {
        console.error("Error during minting process:", error.message);
        throw error;
    }
}

module.exports = { mintFreeNFT };
```
