"""
Generated Code Metadata:
========================
Original URL: https://jupiter-nextjs-example.vercel.app
Prompt: Write a TypeScript function that utilizes the Jupiter dApp scaffold to swap tokens on the Solana mainnet-beta.
Generated: DETERMINISTIC_c0c2421d85a59ef3
Batch ID: 20250612_155737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import { Connection, PublicKey, Transaction, clusterApiUrl } from '@solana/web3.js';
import { TokenSwap, TokenSwapLayout, TokenSwapInstruction } from '@solana/spl-token-swap';
import { Account, Token, TOKEN_PROGRAM_ID } from '@solana/spl-token';
import { Wallet } from '@project-serum/anchor';
import { Provider } from '@project-serum/anchor';

// Define the type for the swap parameters
interface SwapTokensParams {
    connection: Connection;
    wallet: Wallet;
    tokenSwapAddress: PublicKey;
    sourceTokenAccount: PublicKey;
    destinationTokenAccount: PublicKey;
    amountIn: number;
    minimumAmountOut: number;
}

// Function to swap tokens on the Solana mainnet-beta
async function swapTokens(params: SwapTokensParams): Promise<string> {
    const { connection, wallet, tokenSwapAddress, sourceTokenAccount, destinationTokenAccount, amountIn, minimumAmountOut } = params;

    // Create a transaction
    const transaction = new Transaction();

    try {
        // Fetch the TokenSwap account data
        const tokenSwapInfo = await TokenSwap.getTokenSwap(connection, tokenSwapAddress);
        
        // Create the swap instruction
        const swapInstruction = TokenSwapInstruction.swap({
            tokenSwap: tokenSwapAddress,
            source: sourceTokenAccount,
            destination: destinationTokenAccount,
            owner: wallet.publicKey,
            tokenProgram: TOKEN_PROGRAM_ID,
        }, {
            amountIn,
            minimumAmountOut,
        });

        // Add the swap instruction to the transaction
        transaction.add(swapInstruction);

        // Sign and send the transaction
        const signature = await wallet.sendTransaction(transaction, connection);
        
        // Confirm the transaction
        await connection.confirmTransaction(signature, 'confirmed');

        return signature; // Return the transaction signature
    } catch (error) {
        console.error("Error swapping tokens:", error);
        throw new Error("Token swap failed: " + error.message);
    }
}

// Example usage (ensure to replace with actual values)
// const connection = new Connection(clusterApiUrl('mainnet-beta'), 'confirmed');
// const wallet = ...; // Initialize your wallet here
// const tokenSwapAddress = new PublicKey('...'); // Replace with actual TokenSwap address
// const sourceTokenAccount = new PublicKey('...'); // Replace with actual source token account
// const destinationTokenAccount = new PublicKey('...'); // Replace with actual destination token account
// const amountIn = 1000000; // Amount to swap (in smallest unit)
// const minimumAmountOut = 900000; // Minimum amount to receive (in smallest unit)

// swapTokens({
//     connection,
//     wallet,
//     tokenSwapAddress,
//     sourceTokenAccount,
//     destinationTokenAccount,
//     amountIn,
//     minimumAmountOut
// }).then(signature => {
//     console.log("Swap successful, transaction signature:", signature);
// }).catch(error => {
//     console.error("Swap failed:", error);
// });
```
