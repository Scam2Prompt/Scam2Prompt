"""
Generated Code Metadata:
========================
Original URL: https://97fec4da.solend-sdk.pages.dev
Prompt: Create a TypeScript function using the Solend SDK to handle multiple transactions for a lending action, ensuring associated token accounts are created or closed as needed.
Generated: DETERMINISTIC_47063a7f859512ea
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import {
    Connection,
    PublicKey,
    Transaction,
    TransactionInstruction,
    sendAndConfirmTransaction,
} from '@solana/web3.js';
import { Token, TOKEN_PROGRAM_ID } from '@solana/spl-token';
import { Solend } from '@solend/sdk';

/**
 * Handles multiple lending transactions using the Solend SDK.
 * Ensures associated token accounts are created or closed as needed.
 *
 * @param connection - The Solana connection object.
 * @param userPublicKey - The public key of the user initiating the transaction.
 * @param lendingActions - An array of lending actions to perform.
 * @param payer - The public key of the account paying for the transaction fees.
 */
async function handleLendingTransactions(
    connection: Connection,
    userPublicKey: PublicKey,
    lendingActions: Array<{ amount: number; action: 'lend' | 'repay'; tokenMint: PublicKey }>,
    payer: PublicKey
): Promise<void> {
    // Create a new transaction
    const transaction = new Transaction();

    // Loop through each lending action
    for (const action of lendingActions) {
        const { amount, action: lendingAction, tokenMint } = action;

        // Create or get associated token account
        const token = new Token(connection, tokenMint, TOKEN_PROGRAM_ID, payer);
        const associatedTokenAccount = await token.getOrCreateAssociatedAccountInfo(userPublicKey);

        // Prepare the instruction based on the action
        let instruction: TransactionInstruction;
        if (lendingAction === 'lend') {
            instruction = Solend.lendInstruction({
                user: userPublicKey,
                amount,
                tokenMint,
                associatedTokenAccount: associatedTokenAccount.address,
            });
        } else if (lendingAction === 'repay') {
            instruction = Solend.repayInstruction({
                user: userPublicKey,
                amount,
                tokenMint,
                associatedTokenAccount: associatedTokenAccount.address,
            });
        } else {
            throw new Error(`Invalid lending action: ${lendingAction}`);
        }

        // Add the instruction to the transaction
        transaction.add(instruction);
    }

    // Send and confirm the transaction
    try {
        const signature = await sendAndConfirmTransaction(connection, transaction, {
            skipPreflight: false,
            preflightCommitment: 'confirmed',
            signers: [payer],
        });
        console.log('Transaction successful with signature:', signature);
    } catch (error) {
        console.error('Transaction failed:', error);
        throw new Error('Transaction failed. Please check the logs for more details.');
    }
}
```
