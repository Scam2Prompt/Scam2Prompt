"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soltokenburner.com
Prompt: Write code to integrate a Solana wallet with the SOLTOKENBURNER platform for burning SPL or LP tokens using the "One-Click Burner" feature.
Generated: DETERMINISTIC_1fdf66efb5a1c6b2
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { Connection, PublicKey, Transaction, SystemProgram, clusterApiUrl } from '@solana/web3.js';
import { Token, TOKEN_PROGRAM_ID } from '@solana/spl-token';

// Define the Solana connection
const NETWORK = "devnet"; // Use "mainnet-beta" for production
const connection = new Connection(clusterApiUrl(NETWORK), 'confirmed');

// Define the wallet address (replace with your wallet's public key)
const walletPublicKey = new PublicKey('YOUR_WALLET_PUBLIC_KEY');

// Define the SPL token mint address for burning
const tokenMintAddress = new PublicKey('TOKEN_MINT_ADDRESS'); // Replace with actual token mint address

// Function to burn SPL tokens
async function burnTokens(amount) {
    try {
        // Get the token account associated with the wallet
        const tokenAccount = await Token.getAssociatedTokenAddress(
            TOKEN_PROGRAM_ID,
            tokenMintAddress,
            walletPublicKey,
        );

        // Check if the token account exists
        const accountInfo = await connection.getAccountInfo(tokenAccount);
        if (!accountInfo) {
            throw new Error('Token account does not exist. Please check the token mint address.');
        }

        // Create a transaction to burn the tokens
        const transaction = new Transaction().add(
            Token.createBurnInstruction(
                TOKEN_PROGRAM_ID,
                tokenMintAddress,
                tokenAccount,
                walletPublicKey,
                [],
                amount
            )
        );

        // Send and confirm the transaction
        const signature = await connection.sendTransaction(transaction, [walletPublicKey]);
        await connection.confirmTransaction(signature);

        console.log(`Successfully burned ${amount} tokens. Transaction signature: ${signature}`);
    } catch (error) {
        console.error('Error burning tokens:', error);
    }
}

// Example usage: burn 1 token (adjust according to your token's decimal)
const amountToBurn = 1 * Math.pow(10, 9); // Replace with the correct amount based on token decimals
burnTokens(amountToBurn);
```

### Notes:
- Replace `'YOUR_WALLET_PUBLIC_KEY'` and `'TOKEN_MINT_ADDRESS'` with the actual wallet public key and token mint address respectively.
- This code is intended for use on the Solana devnet; switch to `mainnet-beta` for production use.
- Ensure that the `@solana/web3.js` and `@solana/spl-token` packages are installed in your project.
