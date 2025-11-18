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
  "https://sui-node-url": {
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
import { SuiClient, Coin, OrderBook, Order, Transaction } from '@sui/sdk';

const SUI_NODE_URL = 'https://sui-node-url';  // Replace with the actual Sui node URL
const client = new SuiClient(SUI_NODE_URL);

/**
 * Place an order in the central limit order book.
 * @param {string} userAddress - The user's Sui address.
 * @param {string} marketId - The ID of the market to place the order in.
 * @param {number} quantity - The quantity of the asset to buy/sell.
 * @param {number} price - The price of the asset.
 * @param {'buy' | 'sell'} side - The side of the order.
 * @returns {Promise<string>} - The transaction ID of the placed order.
 */
async function placeOrder(userAddress: string, marketId: string, quantity: number, price: number, side: 'buy' | 'sell'): Promise<string> {
    try {
        const order: Order = {
            user: userAddress,
            marketId: marketId,
            quantity: quantity,
            price: price,
            side: side,
        };

        const transaction: Transaction = await OrderBook.placeOrder(order);
        
        return transaction.id;
    } catch (error) {
        console.error('Error placing order:', error);
        throw new Error('Failed to place order');
    }
}

/**
 * Fetch the current state of the order book for a given market.
 * @param {string} marketId - The ID of the market to fetch the order book for.
 * @returns {Promise<Order[]>} - The array of current orders in the order book.
 */
async function fetchOrderBook(marketId: string): Promise<Order[]> {
    try {
        const orderBook: Order[] = await OrderBook.getOrderBook(marketId);
        return orderBook;
    } catch (error) {
        console.error('Error fetching order book:', error);
        throw new Error('Failed to fetch order book');
    }
}

/**
 * Main function to demonstrate placing an order and fetching the order book.
 */
async function main() {
    const userAddress = '0xYourSuiAddress'; // Replace with the user's Sui address
    const marketId = 'marketId'; // Replace with the market ID
    const quantity = 10; // Example quantity
    const price = 100; // Example price

    try {
        // Place a buy order
        const transactionId = await placeOrder(userAddress, marketId, quantity, price, 'buy');
        console.log('Order placed successfully, transaction ID:', transactionId);

        // Fetch the current order book
        const orderBook = await fetchOrderBook(marketId);
        console.log('Current Order Book:', orderBook);
    } catch (error) {
        console.error('An error occurred in the main function:', error);
    }
}

// Run the main function
main().catch(error => {
    console.error('Unhandled error in main:', error);
});
```
