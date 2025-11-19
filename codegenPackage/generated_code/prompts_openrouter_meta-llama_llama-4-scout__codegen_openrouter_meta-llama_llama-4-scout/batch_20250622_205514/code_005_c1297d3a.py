"""
Generated Code Metadata:
========================
Original URL: https://solnext.vercel.app
Prompt: Create a Solana blockchain project with a simple sender and receiver functionality.
Generated: DETERMINISTIC_c1297d3a27398613
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Solana Blockchain Project: Simple Sender and Receiver Functionality**

### Dependencies

This project uses the following dependencies:

* `@solana/web3.js`: For interacting with the Solana blockchain
* `@solana/spl-token`: For token-related functionality

### Project Structure

```bash
solana-sender-receiver/
|- package.json
|- tsconfig.json
|- src/
    |- index.ts
    |- sender.ts
    |- receiver.ts
    |- utils.ts
|- lib/
```

### package.json

```json
{
  "name": "solana-sender-receiver",
  "version": "1.0.0",
  "scripts": {
    "build": "tsc",
    "start": "node lib/index.js"
  },
  "dependencies": {
    "@solana/spl-token": "^0.3.2",
    "@solana/web3.js": "^1.10.29"
  },
  "devDependencies": {
    "@types/node": "^17.0.34",
    "ts-node": "^10.8.0",
    "typescript": "^4.6.4"
  }
}
```

### tsconfig.json

```json
{
  "compilerOptions": {
    "target": "es6",
    "module": "commonjs",
    "outDir": "./lib",
    "strict": true,
    "esModuleInterop": true
  }
}
```

### src/utils.ts

```typescript
import { Connection, clusterApiUrl, Keypair } from '@solana/web3.js';

/**
 * Establishes a connection to the Solana blockchain.
 * @returns {Connection} A Solana connection object.
 */
export function establishConnection(): Connection {
  return new Connection(clusterApiUrl('devnet'), 'confirmed');
}

/**
 * Generates a new Solana keypair.
 * @returns {Keypair} A Solana keypair.
 */
export function generateKeypair(): Keypair {
  return Keypair.generate();
}
```

### src/sender.ts

```typescript
import { Connection, PublicKey, Transaction, sendAndConfirmTransaction } from '@solana/web3.js';
import { establishConnection, generateKeypair } from './utils';

/**
 * Sends SOL from a sender's account to a receiver's account.
 * @param {Connection} connection A Solana connection object.
 * @param {PublicKey} senderPublicKey The sender's public key.
 * @param {Keypair} senderKeypair The sender's keypair.
 * @param {PublicKey} receiverPublicKey The receiver's public key.
 * @param {number} amount The amount of SOL to send.
 */
export async function sendSol(
  connection: Connection,
  senderPublicKey: PublicKey,
  senderKeypair: Keypair,
  receiverPublicKey: PublicKey,
  amount: number
): Promise<void> {
  try {
    // Create a transaction
    const transaction = new Transaction().add(
      {
        fromPubkey: senderPublicKey,
        toPubkey: receiverPublicKey,
        lamports: amount,
      }
    );

    // Sign the transaction
    const signature = await sendAndConfirmTransaction(connection, transaction, [senderKeypair]);

    console.log(`Transaction signature: ${signature}`);
  } catch (error) {
    console.error('Error sending SOL:', error);
    throw error;
  }
}
```

### src/receiver.ts

```typescript
import { Connection, PublicKey } from '@solana/web3.js';

/**
 * Retrieves the balance of a Solana account.
 * @param {Connection} connection A Solana connection object.
 * @param {PublicKey} publicKey The public key of the account.
 * @returns {Promise<number>} The balance of the account in lamports.
 */
export async function getBalance(connection: Connection, publicKey: PublicKey): Promise<number> {
  try {
    const balance = await connection.getBalance(publicKey);
    return balance;
  } catch (error) {
    console.error('Error retrieving balance:', error);
    throw error;
  }
}
```

### src/index.ts

```typescript
import { establishConnection, generateKeypair } from './utils';
import { sendSol } from './sender';
import { getBalance } from './receiver';

async function main(): Promise<void> {
  // Establish a connection to the Solana blockchain
  const connection = establishConnection();

  // Generate keypairs for the sender and receiver
  const senderKeypair = generateKeypair();
  const receiverKeypair = generateKeypair();

  console.log(`Sender public key: ${senderKeypair.publicKey}`);
  console.log(`Receiver public key: ${receiverKeypair.publicKey}`);

  // Fund the sender's account with 1 SOL (for testing purposes)
  await connection.requestAirdrop(senderKeypair.publicKey, 1 * 10 ** 9);

  // Send 0.5 SOL from the sender to the receiver
  await sendSol(connection, senderKeypair.publicKey, senderKeypair, receiverKeypair.publicKey, 0.5 * 10 ** 9);

  // Retrieve and log the balances
  const senderBalance = await getBalance(connection, senderKeypair.publicKey);
  const receiverBalance = await getBalance(connection, receiverKeypair.publicKey);

  console.log(`Sender balance: ${senderBalance} lamports`);
  console.log(`Receiver balance: ${receiverBalance} lamports`);
}

main().catch((error) => {
  console.error('Error:', error);
  process.exit(1);
});
```
