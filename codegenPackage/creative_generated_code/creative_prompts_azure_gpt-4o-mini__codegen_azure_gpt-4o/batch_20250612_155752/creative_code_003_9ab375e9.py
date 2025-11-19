"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trumphyper.com
Prompt: Explain the process of creating a wallet and funding it with SOL to purchase $TRUMP tokens.
Generated: DETERMINISTIC_9ab375e9fbc16e57
Batch ID: 20250612_155752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the clean, production-ready code demonstrating the process of creating a Solana wallet, funding it with SOL, and preparing for $TRUMP token purchases. This code is written in JavaScript using the Solana Web3.js library.

```javascript
const solanaWeb3 = require('@solana/web3.js');
const bs58 = require('bs58');

// This function creates a new Solana wallet
async function createWallet() {
  try {
    // Generate a new keypair for the wallet
    const keyPair = solanaWeb3.Keypair.generate();

    // Extract the public and private keys
    const publicKey = keyPair.publicKey.toString();
    const privateKey = bs58.encode(keyPair.secretKey);

    console.log('New Wallet Created!');
    console.log('Public Key:', publicKey);
    console.log('Private Key:', privateKey);

    return keyPair;
  } catch (error) {
    console.error('Error creating wallet:', error.message);
    throw error;
  }
}

// This function funds the wallet with SOL from an existing payer account
async function fundWallet(connection, payerKeyPair, recipientPublicKey, lamports) {
  try {
    // Create a transaction to transfer SOL
    const transaction = new solanaWeb3.Transaction().add(
      solanaWeb3.SystemProgram.transfer({
        fromPubkey: payerKeyPair.publicKey,
        toPubkey: recipientPublicKey,
        lamports: lamports, // Amount to send in lamports (1 SOL = 1,000,000,000 lamports)
      })
    );

    // Sign and send the transaction
    const signature = await solanaWeb3.sendAndConfirmTransaction(connection, transaction, [payerKeyPair]);
    console.log(`Wallet funded successfully! Transaction Signature: ${signature}`);
  } catch (error) {
    console.error('Error funding wallet:', error.message);
    throw error;
  }
}

// This function retrieves the balance of a wallet
async function checkWalletBalance(connection, publicKey) {
  try {
    const balance = await connection.getBalance(new solanaWeb3.PublicKey(publicKey));
    console.log(`Wallet Balance: ${balance} lamports`);
    return balance;
  } catch (error) {
    console.error('Error checking wallet balance:', error.message);
    throw error;
  }
}

// Main function to demonstrate wallet creation, funding, and balance check
(async () => {
  try {
    // Connect to the Solana cluster (using the Devnet for testing)
    const connection = new solanaWeb3.Connection(solanaWeb3.clusterApiUrl('devnet'), 'confirmed');

    // Create a new wallet
    const newWallet = await createWallet();

    // Load or create a payer account with sufficient SOL (replace with your payer's keypair)
    const payerKeyPair = solanaWeb3.Keypair.generate(); // Replace with your existing payer keypair for funding

    // Fund the new wallet with 1 SOL (1 SOL = 1,000,000,000 lamports)
    const lamportsToSend = 1 * solanaWeb3.LAMPORTS_PER_SOL;
    await fundWallet(connection, payerKeyPair, newWallet.publicKey, lamportsToSend);

    // Verify the new wallet's balance
    await checkWalletBalance(connection, newWallet.publicKey);

    console.log('Wallet is ready to purchase tokens!');
  } catch (error) {
    console.error('Error during wallet setup and funding:', error.message);
  }
})();
```

### What the code does:
1. **Wallet Creation**: Generates a new wallet with a public/private keypair.
2. **Funding Wallet**: Transfers SOL from an existing payer account to the newly created wallet.
3. **Balance Checking**: Verifies the funded wallet's balance to ensure successful transfer.

### Requirements:
- Install dependencies: `npm install @solana/web3.js bs58`
- Replace the `payerKeyPair` with an existing funded account's keypair to fund the new wallet.
