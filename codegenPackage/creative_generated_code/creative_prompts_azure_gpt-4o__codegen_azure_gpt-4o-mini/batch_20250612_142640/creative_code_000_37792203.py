"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-pump.fun
Prompt: Write code to connect a Solana wallet and retrieve the current balance in SOL for use in a cryptocurrency pre-sale platform like the $PUMP token sale.
Generated: DETERMINISTIC_37792203decef327
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { Connection, clusterApiUrl, PublicKey } from '@solana/web3.js';

// Define the main function to retrieve the balance
async function getSolanaBalance(walletAddress) {
    // Set the network to the devnet; change to 'mainnet-beta' for production
    const network = clusterApiUrl('devnet');
    
    // Create a connection to the Solana cluster
    const connection = new Connection(network, 'confirmed');

    try {
        // Validate the wallet address
        const publicKey = new PublicKey(walletAddress);

        // Fetch the balance in lamports (1 SOL = 1,000,000,000 lamports)
        const balance = await connection.getBalance(publicKey);

        // Convert lamports to SOL
        const solBalance = balance / 1_000_000_000;

        // Log the balance
        console.log(`Wallet address: ${walletAddress}`);
        console.log(`Current balance: ${solBalance} SOL`);

        return solBalance;
    } catch (error) {
        // Handle errors gracefully
        console.error('Error retrieving balance:', error);
        throw new Error('Unable to retrieve balance. Please check the wallet address and network connection.');
    }
}

// Example usage: Replace with a real wallet address
const walletAddress = 'YOUR_WALLET_ADDRESS_HERE';
getSolanaBalance(walletAddress)
    .then(balance => {
        // Additional logic after retrieving the balance can be added here
    })
    .catch(err => {
        // Handle errors from getSolanaBalance
        console.error(err.message);
    });
```
