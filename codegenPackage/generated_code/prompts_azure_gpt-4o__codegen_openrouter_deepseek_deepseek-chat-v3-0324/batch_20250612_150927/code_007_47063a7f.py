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
import { Connection, Keypair, PublicKey, Transaction, sendAndConfirmTransaction } from '@solana/web3.js';
import { SolendAction, ActionType } from '@solendprotocol/solend-sdk';
import { TOKEN_PROGRAM_ID } from '@solana/spl-token';

interface LendingActionParams {
  connection: Connection;
  payer: Keypair;
  actionType: ActionType;
  amount: number;
  mint: PublicKey;
  owner: PublicKey;
}

export async function executeLendingAction({
  connection,
  payer,
  actionType,
  amount,
  mint,
  owner,
}: LendingActionParams): Promise<string> {
  try {
    // Initialize Solend action
    const solendAction = await SolendAction.build(
      connection,
      actionType,
      amount,
      mint,
      owner,
      payer.publicKey,
      TOKEN_PROGRAM_ID
    );

    // Get all required transactions
    const { setupTransactions, lendingTransactions, cleanupTransactions } =
      await solendAction.getTransactions();

    // Combine all transactions
    const allTransactions = [
      ...(setupTransactions ?? []),
      ...lendingTransactions,
      ...(cleanupTransactions ?? []),
    ];

    // Execute transactions sequentially
    let lastTxSignature: string = '';
    for (const tx of allTransactions) {
      const transaction = new Transaction().add(...tx.instructions);
      lastTxSignature = await sendAndConfirmTransaction(
        connection,
        transaction,
        [payer],
        { skipPreflight: false }
      );
    }

    return lastTxSignature;
  } catch (error) {
    console.error('Error executing lending action:', error);
    throw new Error(`Failed to execute lending action: ${error.message}`);
  }
}
```
