"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-wallet-extension-for-chromes.webflow.io
Prompt: Write JavaScript code to interact with the Phantom Wallet extension for Chrome to fetch the balance of a Solana account.
Generated: DETERMINISTIC_0b2712800132c483
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// This function interacts with the Phantom Wallet to fetch the balance of a Solana account
async function fetchSolanaBalance(accountPublicKey) {
    // Ensure the Phantom wallet is installed
    if (typeof window.solana === 'undefined') {
        throw new Error('Phantom Wallet is not installed. Please install it to use this feature.');
    }

    try {
        // Connect to the Phantom Wallet
        const response = await window.solana.connect();
        console.log('Connected to Phantom Wallet:', response.publicKey.toString());

        // Fetch the balance of the specified Solana account
        const connection = new solanaWeb3.Connection(solanaWeb3.clusterApiUrl('mainnet-beta'), 'confirmed');
        const balance = await connection.getBalance(new solanaWeb3.PublicKey(accountPublicKey));

        // Convert the balance from lamports to SOL
        const balanceInSol = balance / solanaWeb3.LAMPORTS_PER_SOL;
        console.log(`Balance of account ${accountPublicKey}: ${balanceInSol} SOL`);

        return balanceInSol;
    } catch (error) {
        // Handle errors that may occur during fetching balance
        console.error('Error fetching balance:', error);
        throw new Error('Failed to fetch balance. Please try again later.');
    }
}

// Example usage
(async () => {
    const accountPublicKey = 'YOUR_ACCOUNT_PUBLIC_KEY_HERE'; // Replace with your Solana account public key
    try {
        const balance = await fetchSolanaBalance(accountPublicKey);
        console.log(`The balance for account ${accountPublicKey} is ${balance} SOL`);
    } catch (error) {
        console.error(error.message);
    }
})();
```

### Notes:
- Replace `'YOUR_ACCOUNT_PUBLIC_KEY_HERE'` with the actual Solana account public key.
- This code requires the `@solana/web3.js` package to be included in your project. You can install it via npm:
  ```bash
  npm install @solana/web3.js
  ```
- Ensure that the Phantom Wallet extension is installed and the user is logged in before running this code.
