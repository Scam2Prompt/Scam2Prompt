"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sh-haweng12s-projects.vercel.app
Prompt: Generate a function to fetch and display Solana wallet balances after connecting, based on the "SOL Select Wallet" concept.
Generated: DETERMINISTIC_4eff96213ec1fbe9
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const { Connection, clusterApiUrl, PublicKey } = require('@solana/web3.js');

/**
 * Fetch and display Solana wallet balances.
 * 
 * @param {string} walletAddress - The public address of the Solana wallet.
 * @returns {Promise<void>} - Prints the wallet balance to the console.
 */
async function fetchWalletBalance(walletAddress) {
  try {
    // Validate the wallet address
    if (!walletAddress || typeof walletAddress !== 'string') {
      throw new Error('Invalid wallet address provided.');
    }

    // Create a connection to the Solana blockchain (mainnet cluster)
    const connection = new Connection(clusterApiUrl('mainnet-beta'), 'confirmed');

    // Convert the wallet address into a PublicKey object
    const publicKey = new PublicKey(walletAddress);

    // Fetch the balance (in lamports)
    const balanceInLamports = await connection.getBalance(publicKey);

    // Convert lamports to SOL (1 SOL = 1,000,000,000 lamports)
    const balanceInSOL = balanceInLamports / 1_000_000_000;

    // Display the balance
    console.log(`Wallet Address: ${walletAddress}`);
    console.log(`Balance: ${balanceInSOL} SOL`);
  } catch (error) {
    // Handle errors
    console.error('Error fetching wallet balance:', error.message);
  }
}

// Example usage:
// Replace 'YourWalletAddressHere' with a valid Solana wallet address.
fetchWalletBalance('YourWalletAddressHere');
```

Note: Replace `'YourWalletAddressHere'` in the example usage with a valid Solana wallet address. Ensure you have installed the `@solana/web3.js` package before running this code (`npm install @solana/web3.js`).
