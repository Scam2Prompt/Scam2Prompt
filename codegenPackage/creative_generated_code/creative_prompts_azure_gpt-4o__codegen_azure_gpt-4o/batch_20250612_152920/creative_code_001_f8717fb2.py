"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wolitpphxatom.webflow.io
Prompt: Recommend libraries or APIs for interacting with the Phantom Wallet in a Solana blockchain project.
Generated: DETERMINISTIC_f8717fb2674ba18a
Batch ID: 20250612_152920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This code demonstrates the use of the `@solana/web3.js` library for interacting with the Solana blockchain
 * and the Phantom Wallet extension.
 * 
 * Prerequisites:
 * 1. Install the necessary dependency: `npm install @solana/web3.js`
 * 2. Ensure the Phantom Wallet is installed in your browser.
 */

// Import the Solana web3.js library
const { Connection, PublicKey, clusterApiUrl } = require('@solana/web3.js');

/** 
 * Function to connect to Phantom Wallet and fetch the user's public key.
 * This function uses the Phantom Wallet's window.solana object for interaction.
 */
async function connectToPhantom() {
  try {
    // Check if Phantom Wallet is installed
    if (!window.solana || !window.solana.isPhantom) {
      throw new Error("Phantom Wallet is not installed. Please install it to proceed.");
    }

    // Request connection to Phantom Wallet (Pop-up will appear)
    const response = await window.solana.connect();

    // Log and return the user's public key
    console.log("Connected to Phantom Wallet. Public Key:", response.publicKey.toString());
    return response.publicKey;
  } catch (error) {
    console.error("Error connecting to Phantom Wallet:", error.message);
    throw error; // Re-throw error for further handling
  }
}

/** 
 * Function to fetch the balance of a given Solana account.
 * 
 * @param {Connection} connection - Solana blockchain connection object.
 * @param {PublicKey} publicKey - Public key for which the balance will be fetched.
 */
async function getBalance(connection, publicKey) {
  try {
    // Fetch the balance (in lamports) from the Solana blockchain
    const balance = await connection.getBalance(publicKey);

    // Convert lamports to SOL (1 SOL = 10^9 lamports)
    const solBalance = balance / Math.pow(10, 9);
    console.log(`Balance for ${publicKey.toString()}: ${solBalance} SOL`);

    return solBalance;
  } catch (error) {
    console.error("Error fetching balance:", error.message);
    throw error; // Re-throw error for further handling
  }
}

/**
 * Main function demonstrating the connection to Phantom Wallet and fetching the account balance.
 */
async function main() {
  try {
    // Connect to the Solana Devnet (change to 'mainnet-beta' for production use)
    const connection = new Connection(clusterApiUrl('devnet'), 'confirmed');

    // Connect to Phantom Wallet and retrieve the user's public key
    const userPublicKey = await connectToPhantom();

    // Fetch and log the balance of the connected account
    await getBalance(connection, userPublicKey);
  } catch (error) {
    console.error("Error in main execution:", error.message);
  }
}

// Execute the main function
main();
```

### Notes:
- Ensure Phantom Wallet is installed before running this code.
- Replace `clusterApiUrl('devnet')` with `clusterApiUrl('mainnet-beta')` in production environments.
