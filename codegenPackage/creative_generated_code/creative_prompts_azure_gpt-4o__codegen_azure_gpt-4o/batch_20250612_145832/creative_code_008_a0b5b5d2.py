"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suifoundation.com
Prompt: Write a script using the Sui TypeScript SDK to interact with a native central limit order book for on-chain routing and matching.
Generated: DETERMINISTIC_a0b5b5d2c28fd4af
Batch ID: 20250612_145832
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rpc.testnet.sui.io:443": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```typescript
// Import necessary modules from the Sui SDK
import { JsonRpcProvider, Connection, Ed25519Keypair, TransactionBlock } from '@mysten/sui.js';
import dotenv from 'dotenv';

// Load environment variables from a .env file
dotenv.config();

// Define constants for the connection and central limit order book
const SUI_NETWORK_URL = process.env.SUI_NETWORK_URL || 'https://rpc.testnet.sui.io:443';
const ORDER_BOOK_PACKAGE_ID = process.env.ORDER_BOOK_PACKAGE_ID || '<insert-order-book-package-id>';
const ORDER_BOOK_MODULE = process.env.ORDER_BOOK_MODULE || 'order_book';
const ORDER_BOOK_FUNCTION_MATCH = 'match_orders';
const ORDER_BOOK_FUNCTION_ROUTE = 'route_orders';

// Initialize the connection and provider
const connection = new Connection({ fullnode: SUI_NETWORK_URL });
const provider = new JsonRpcProvider(connection);

// Set up the user's keypair for signing transactions
const userPrivateKey = process.env.USER_PRIVATE_KEY;
if (!userPrivateKey) {
  throw new Error('USER_PRIVATE_KEY is not set in the environment variables.');
}
const userKeypair = Ed25519Keypair.fromSecretKey(Buffer.from(userPrivateKey, 'hex'));

// Function to route orders on the central limit order book
async function routeOrders(orderDetails: any): Promise<void> {
  try {
    const tx = new TransactionBlock();
    
    // Add the function call to route orders
    tx.moveCall({
      target: `${ORDER_BOOK_PACKAGE_ID}::${ORDER_BOOK_MODULE}::${ORDER_BOOK_FUNCTION_ROUTE}`,
      arguments: tx.pure(orderDetails),
    });

    // Sign and execute the transaction
    const signedTx = await tx.sign(userKeypair);
    const response = await provider.sendTransactionBlock({ transactionBlock: signedTx });
    console.log('Route Orders Transaction Response:', response);
  } catch (error) {
    console.error('Error occurred during route orders transaction:', error);
  }
}

// Function to match orders on the central limit order book
async function matchOrders(): Promise<void> {
  try {
    const tx = new TransactionBlock();
    
    // Add the function call to match orders
    tx.moveCall({
      target: `${ORDER_BOOK_PACKAGE_ID}::${ORDER_BOOK_MODULE}::${ORDER_BOOK_FUNCTION_MATCH}`,
    });

    // Sign and execute the transaction
    const signedTx = await tx.sign(userKeypair);
    const response = await provider.sendTransactionBlock({ transactionBlock: signedTx });
    console.log('Match Orders Transaction Response:', response);
  } catch (error) {
    console.error('Error occurred during match orders transaction:', error);
  }
}

// Example usage of the functions
async function main() {
  try {
    console.log('Routing orders...');
    await routeOrders({ price: 100, quantity: 10, side: 'buy' });

    console.log('Matching orders...');
    await matchOrders();
  } catch (error) {
    console.error('Error occurred in main function:', error);
  }
}

// Execute the main function
main();
```
