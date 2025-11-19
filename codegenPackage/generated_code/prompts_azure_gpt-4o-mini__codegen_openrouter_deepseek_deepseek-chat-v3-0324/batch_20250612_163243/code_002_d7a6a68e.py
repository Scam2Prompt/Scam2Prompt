"""
Generated Code Metadata:
========================
Original URL: https://97fec4da.solend-sdk.pages.dev
Prompt: Generate a Solend action to deposit a specific amount of SOL into the lending market using the Solend Typescript SDK.
Generated: DETERMINISTIC_d7a6a68eaefb60e7
Batch ID: 20250612_163243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import { Connection, PublicKey, Transaction } from '@solana/web3.js';
import { SolendAction } from '@solendprotocol/solend-sdk';
import { Wallet } from '@project-serum/anchor';

/**
 * Deposits SOL into the Solend lending market.
 * @param connection Solana connection object
 * @param wallet User's wallet
 * @param amount Amount of SOL to deposit (in lamports)
 * @param environment Solend environment ('production' or 'devnet')
 * @returns Transaction signature
 */
export async function depositSol(
  connection: Connection,
  wallet: Wallet,
  amount: number,
  environment: 'production' | 'devnet' = 'production'
): Promise<string> {
  try {
    // Validate input parameters
    if (!connection || !wallet?.publicKey) {
      throw new Error('Invalid connection or wallet');
    }
    if (amount <= 0) {
      throw new Error('Deposit amount must be positive');
    }

    // Initialize Solend action
    const solendAction = await SolendAction.buildDepositTxns(
      connection,
      wallet.publicKey,
      environment,
      'SOL',
      new PublicKey('So11111111111111111111111111111111111111112'), // SOL mint
      amount,
      wallet.publicKey // Referrer address (optional)
    );

    // Create and sign transaction
    const txs = await solendAction.getTransactions();
    const tx = new Transaction().add(...txs[0].instructions);
    tx.feePayer = wallet.publicKey;
    tx.recentBlockhash = (await connection.getRecentBlockhash()).blockhash;

    const signedTx = await wallet.signTransaction(tx);
    const signature = await connection.sendRawTransaction(signedTx.serialize());

    // Confirm transaction
    await connection.confirmTransaction(signature, 'confirmed');
    return signature;
  } catch (error) {
    console.error('Error depositing SOL:', error);
    throw error;
  }
}
```
