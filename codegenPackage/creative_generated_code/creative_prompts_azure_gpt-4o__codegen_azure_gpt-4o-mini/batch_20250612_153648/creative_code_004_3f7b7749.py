"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dust-21.web.app
Prompt: Create a Solana blockchain script to airdrop DUST tokens to multiple wallets using the DustLabs SPL token specifications.
Generated: DETERMINISTIC_3f7b7749a92602ea
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from the Solana Web3.js library and SPL Token library
const {
    Connection,
    PublicKey,
    clusterApiUrl,
    Keypair,
    sendAndConfirmTransaction,
} = require('@solana/web3.js');
const {
    createTransferInstruction,
    getAccount,
    getAssociatedTokenAddress,
    createAssociatedTokenAccountInstruction,
} = require('@solana/spl-token');

// Configuration
const NETWORK = 'devnet'; // Choose your network (devnet, testnet, mainnet-beta)
const DUST_TOKEN_MINT_ADDRESS = 'Your_DUST_Token_Mint_Address_Here'; // Replace with actual DUST token mint address
const AIRDROP_AMOUNT = 100; // Amount of DUST tokens to airdrop to each wallet
const WALLET_ADDRESSES = [
    'Wallet_Address_1',
    'Wallet_Address_2',
    // Add more wallet addresses here
];

// Create a connection to the Solana cluster
const connection = new Connection(clusterApiUrl(NETWORK), 'confirmed');

// Function to airdrop DUST tokens to multiple wallets
async function airdropDustTokens() {
    // Loop through each wallet address
    for (const walletAddress of WALLET_ADDRESSES) {
        try {
            const recipientPublicKey = new PublicKey(walletAddress);
            const senderKeypair = Keypair.generate(); // Generate a new keypair for sending tokens

            // Create the associated token account for the recipient if it doesn't exist
            const recipientTokenAccount = await getAssociatedTokenAddress(
                DUST_TOKEN_MINT_ADDRESS,
                recipientPublicKey
            );

            // Check if recipient's token account exists
            let recipientAccountInfo;
            try {
                recipientAccountInfo = await getAccount(connection, recipientTokenAccount);
            } catch (error) {
                // If the account does not exist, create it
                const createAccountInstruction = createAssociatedTokenAccountInstruction(
                    senderKeypair.publicKey,
                    recipientTokenAccount,
                    recipientPublicKey,
                    DUST_TOKEN_MINT_ADDRESS
                );

                const transaction = await connection.sendTransaction(
                    new Transaction().add(createAccountInstruction),
                    [senderKeypair],
                    { skipPreflight: false, preflightCommitment: 'confirmed' }
                );

                await sendAndConfirmTransaction(connection, transaction, [senderKeypair]);
            }

            // Create and send the transfer instruction
            const transferInstruction = createTransferInstruction(
                recipientTokenAccount,
                senderKeypair.publicKey,
                senderKeypair,
                AIRDROP_AMOUNT,
                [],
            );

            const transaction = new Transaction().add(transferInstruction);
            await sendAndConfirmTransaction(connection, transaction, [senderKeypair]);
            console.log(`Successfully airdropped ${AIRDROP_AMOUNT} DUST to ${walletAddress}`);
        } catch (error) {
            console.error(`Failed to airdrop to ${walletAddress}: ${error.message}`);
        }
    }
}

// Execute the airdrop function
airdropDustTokens().catch((error) => {
    console.error(`Airdrop process encountered an error: ${error.message}`);
});
```

**Note**: Replace `'Your_DUST_Token_Mint_Address_Here'` and the wallet addresses in the `WALLET_ADDRESSES` array with actual DUST token mint address and valid wallet addresses. Also ensure you have sufficient funds in the sender's account to cover the transaction fees and the amount being sent.
