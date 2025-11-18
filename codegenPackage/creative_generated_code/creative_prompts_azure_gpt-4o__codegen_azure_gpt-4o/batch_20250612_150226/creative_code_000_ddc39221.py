"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dialect-c15.pages.dev
Prompt: Write code to integrate Dialect's Actions API into a Solana-based application for token swaps and NFT purchases. Include support for signable transactions using the Actions spec.
Generated: DETERMINISTIC_ddc39221e63550ed
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
// Import necessary modules and dependencies
import { Connection, PublicKey, clusterApiUrl, Transaction, SystemProgram } from '@solana/web3.js';
import { DialectActionsApi } from '@dialectlabs/actions'; // Dialect's Actions API library
import fs from 'fs';

// Configuration settings
const DIALECT_API_KEY = 'your-dialect-api-key'; // Replace with your Dialect API key
const SOLANA_CLUSTER = 'mainnet-beta'; // Change to 'devnet' or 'testnet' if needed
const WALLET_PRIVATE_KEY_PATH = './wallet.json'; // Path to wallet private key file

/**
 * Initialize the Solana connection and Dialect API client.
 */
const connection = new Connection(clusterApiUrl(SOLANA_CLUSTER), 'confirmed');
const dialectClient = new DialectActionsApi({
  apiKey: DIALECT_API_KEY,
});

/**
 * Load wallet from private key file.
 */
const loadWallet = (): PublicKey => {
  try {
    const privateKeyData = fs.readFileSync(WALLET_PRIVATE_KEY_PATH, 'utf8');
    const privateKey = JSON.parse(privateKeyData);
    return PublicKey.from(privateKey);
  } catch (error) {
    console.error('Failed to load wallet private key:', error.message);
    process.exit(1);
  }
};

/**
 * Create and sign a transaction for a token swap.
 * @param {PublicKey} sender - Sender wallet public key.
 * @param {PublicKey} receiver - Receiver wallet public key.
 * @param {number} amount - Amount of tokens to swap.
 * @returns {Transaction} - Signed transaction object.
 */
const createTokenSwapTransaction = async (
  sender: PublicKey,
  receiver: PublicKey,
  amount: number,
): Promise<Transaction> => {
  try {
    const transaction = new Transaction().add(
      SystemProgram.transfer({
        fromPubkey: sender,
        toPubkey: receiver,
        lamports: amount, // Amount in lamports (1 SOL = 1e9 lamports)
      })
    );
    const { blockhash } = await connection.getRecentBlockhash();
    transaction.recentBlockhash = blockhash;
    transaction.feePayer = sender;

    const wallet = loadWallet();
    transaction.sign(wallet); // Sign the transaction with the wallet
    
    return transaction;
  } catch (error) {
    console.error('Error creating token swap transaction:', error.message);
    throw error;
  }
};

/**
 * Create a transaction for NFT purchase.
 * @param {PublicKey} buyer - Buyer wallet public key.
 * @param {PublicKey} seller - Seller wallet public key.
 * @param {PublicKey} nftTokenAddress - NFT token address.
 * @returns {Transaction} - Signed transaction object.
 */
const createNftPurchaseTransaction = async (
  buyer: PublicKey,
  seller: PublicKey,
  nftTokenAddress: PublicKey,
): Promise<Transaction> => {
  try {
    const transaction = new Transaction().add(
      SystemProgram.transfer({
        fromPubkey: buyer,
        toPubkey: seller,
        lamports: 1000000000, // Example: 1 SOL for the NFT
      }),
      SystemProgram.transfer({
        fromPubkey: seller,
        toPubkey: buyer,
        lamports: 0, // Mock transaction to transfer the NFT (Add your NFT transfer logic)
      })
    );

    const { blockhash } = await connection.getRecentBlockhash();
    transaction.recentBlockhash = blockhash;
    transaction.feePayer = buyer;

    const wallet = loadWallet();
    transaction.sign(wallet); // Sign the transaction with the wallet
    
    return transaction;
  } catch (error) {
    console.error('Error creating NFT purchase transaction:', error.message);
    throw error;
  }
};

/**
 * Submit a signed transaction using Dialect's Actions API.
 * @param {Transaction} transaction - Signed transaction object.
 */
const submitTransaction = async (transaction: Transaction): Promise<void> => {
  try {
    const serializedTransaction = transaction.serialize();
    const response = await dialectClient.submitAction({
      actionType: 'transaction',
      transaction: serializedTransaction.toString('base64'),
    });

    console.log('Transaction submitted successfully:', response);
  } catch (error) {
    console.error('Failed to submit transaction:', error.message);
    throw error;
  }
};

/**
 * Main function for testing the integration.
 */
const main = async (): Promise<void> => {
  try {
    const sender = loadWallet();
    const receiver = new PublicKey('receiver-public-key'); // Replace with actual receiver public key
    const amount = 100000000; // Example: 0.1 SOL in lamports

    // Token Swap Example
    const tokenSwapTransaction = await createTokenSwapTransaction(sender, receiver, amount);
    await submitTransaction(tokenSwapTransaction);

    // NFT Purchase Example
    const buyer = sender;
    const seller = new PublicKey('seller-public-key'); // Replace with actual seller public key
    const nftTokenAddress = new PublicKey('nft-token-address'); // Replace with actual NFT token address
    const nftPurchaseTransaction = await createNftPurchaseTransaction(buyer, seller, nftTokenAddress);
    await submitTransaction(nftPurchaseTransaction);
  } catch (error) {
    console.error('Error in main flow:', error.message);
    process.exit(1);
  }
};

// Execute the main function
main();
```
