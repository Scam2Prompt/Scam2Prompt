"""
Generated Code Metadata:
========================
Original URL: https://be-solana-methods-v1.docs-62t.pages.dev
Prompt: Provide an example of how to use Código's generated client library in TypeScript to interact with a decentralized finance (DeFi) application on Solana.
Generated: DETERMINISTIC_f6c35f1d4580b1cb
Batch ID: 20250612_150946
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```typescript
import { Connection, Keypair, PublicKey, Transaction, sendAndConfirmTransaction } from '@solana/web3.js';
import { DeFiClient } from '@codigo/defi-client'; // Assuming this is the generated client library

// Initialize connection to Solana cluster
const connection = new Connection('https://api.mainnet-beta.solana.com', 'confirmed');

// Load user's keypair (in production, use secure key management)
const userKeypair = Keypair.fromSecretKey(
  Uint8Array.from(JSON.parse(process.env.USER_PRIVATE_KEY as string))
);

// DeFi program ID (replace with actual program ID)
const defiProgramId = new PublicKey('DEF1PR0GR4M1D11111111111111111111111111111');

// Initialize DeFi client
const defiClient = new DeFiClient(connection, defiProgramId);

/**
 * Deposit funds into a DeFi pool
 * @param amount - Amount to deposit in lamports
 * @param poolAddress - Address of the liquidity pool
 */
async function depositToPool(amount: number, poolAddress: PublicKey) {
  try {
    // Get recent blockhash
    const recentBlockhash = await connection.getRecentBlockhash();

    // Create transaction
    const transaction = new Transaction({
      feePayer: userKeypair.publicKey,
      recentBlockhash: recentBlockhash.blockhash,
    });

    // Generate deposit instruction
    const depositInstruction = await defiClient.deposit(
      {
        user: userKeypair.publicKey,
        pool: poolAddress,
      },
      amount
    );

    // Add instruction to transaction
    transaction.add(depositInstruction);

    // Sign and send transaction
    const txSignature = await sendAndConfirmTransaction(
      connection,
      transaction,
      [userKeypair]
    );

    console.log(`Deposit successful. Transaction signature: ${txSignature}`);
    return txSignature;
  } catch (error) {
    console.error('Error depositing to pool:', error);
    throw error;
  }
}

/**
 * Withdraw funds from a DeFi pool
 * @param amount - Amount to withdraw in lamports
 * @param poolAddress - Address of the liquidity pool
 */
async function withdrawFromPool(amount: number, poolAddress: PublicKey) {
  try {
    // Get recent blockhash
    const recentBlockhash = await connection.getRecentBlockhash();

    // Create transaction
    const transaction = new Transaction({
      feePayer: userKeypair.publicKey,
      recentBlockhash: recentBlockhash.blockhash,
    });

    // Generate withdraw instruction
    const withdrawInstruction = await defiClient.withdraw(
      {
        user: userKeypair.publicKey,
        pool: poolAddress,
      },
      amount
    );

    // Add instruction to transaction
    transaction.add(withdrawInstruction);

    // Sign and send transaction
    const txSignature = await sendAndConfirmTransaction(
      connection,
      transaction,
      [userKeypair]
    );

    console.log(`Withdrawal successful. Transaction signature: ${txSignature}`);
    return txSignature;
  } catch (error) {
    console.error('Error withdrawing from pool:', error);
    throw error;
  }
}

/**
 * Get user's balance in a DeFi pool
 * @param poolAddress - Address of the liquidity pool
 */
async function getUserPoolBalance(poolAddress: PublicKey) {
  try {
    const balance = await defiClient.getUserBalance({
      user: userKeypair.publicKey,
      pool: poolAddress,
    });

    console.log(`User balance in pool: ${balance} lamports`);
    return balance;
  } catch (error) {
    console.error('Error fetching user balance:', error);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    const poolAddress = new PublicKey('P00LADDR3SS111111111111111111111111111111');
    
    // Deposit 1 SOL (in lamports)
    await depositToPool(1000000000, poolAddress);
    
    // Check balance
    await getUserPoolBalance(poolAddress);
    
    // Withdraw 0.5 SOL (in lamports)
    await withdrawFromPool(500000000, poolAddress);
  } catch (error) {
    console.error('Example execution failed:', error);
  }
})();
```
