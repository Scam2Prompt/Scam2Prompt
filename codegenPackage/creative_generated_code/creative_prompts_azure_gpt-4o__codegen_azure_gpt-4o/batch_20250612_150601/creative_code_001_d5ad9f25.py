"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stelth-mint.web.app
Prompt: Generate code to connect a Solana wallet and display the balance of the "Основной кошелек" (main wallet) and "Торговый кошелек" (trading wallet) as shown on the website.
Generated: DETERMINISTIC_d5ad9f254ee67d06
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries from solana/web3.js
const { Connection, PublicKey, clusterApiUrl } = require('@solana/web3.js');

// Replace with the public keys of your wallets
const MAIN_WALLET = 'YourMainWalletPublicKeyHere'; // Основной кошелек (Main Wallet)
const TRADING_WALLET = 'YourTradingWalletPublicKeyHere'; // Торговый кошелек (Trading Wallet)

// Function to fetch and display wallet balances
async function displayWalletBalances() {
  try {
    // Initialize a connection to the Solana cluster
    const connection = new Connection(clusterApiUrl('mainnet-beta'), 'confirmed'); // Mainnet connection

    // Convert public keys from string to PublicKey objects
    const mainWalletPubKey = new PublicKey(MAIN_WALLET);
    const tradingWalletPubKey = new PublicKey(TRADING_WALLET);

    // Fetch balances for both wallets
    console.log('Fetching balances...');
    const mainWalletBalance = await connection.getBalance(mainWalletPubKey);
    const tradingWalletBalance = await connection.getBalance(tradingWalletPubKey);

    // Convert lamports to SOL (1 SOL = 10^9 lamports)
    const mainWalletBalanceInSOL = mainWalletBalance / 1e9;
    const tradingWalletBalanceInSOL = tradingWalletBalance / 1e9;

    // Log the balances in SOL
    console.log(`Основной кошелек (Main Wallet) Balance: ${mainWalletBalanceInSOL} SOL`);
    console.log(`Торговый кошелек (Trading Wallet) Balance: ${tradingWalletBalanceInSOL} SOL`);
  } catch (error) {
    // Handle errors gracefully
    console.error('Error fetching wallet balances:', error.message);
  }
}

// Call the function to display balances
displayWalletBalances();
```

### Instructions for Using the Code:
1. Replace `YourMainWalletPublicKeyHere` and `YourTradingWalletPublicKeyHere` with the respective public keys of the Main Wallet and Trading Wallet.
2. Ensure you have Node.js installed.
3. Run `npm install @solana/web3.js` to install the required library.
4. Save the script in a `.js` file and execute it using `node filename.js` to see the wallet balances in SOL.
5. This script assumes the Solana Mainnet, but you can modify the cluster URL for testing environments (e.g., `testnet` or `devnet`).
