"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://midoin.com
Prompt: Generate a code snippet for a JavaScript application that allows users to view their Midoins balance and transaction history using Etherscan.
Generated: DETERMINISTIC_87eb8ef222ba7ff0
Batch ID: 20250612_160411
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=${MIDOINS_CONTRACT_ADDRESS}&address=${walletAddress}&tag=latest&apikey=${API_KEY}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.etherscan.io/api?module=account&action=tokentx&contractaddress=${MIDOINS_CONTRACT_ADDRESS}&address=${walletAddress}&page=1&offset=10&sort=desc&apikey=${API_KEY}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Midoins Balance and Transaction History Viewer
 * This application fetches the user's Midoins balance and transaction history using the Etherscan API.
 * Ensure you replace `API_KEY` with your actual Etherscan API key.
 */

// Required configuration
const API_KEY = 'your-etherscan-api-key'; // Replace with your Etherscan API key
const MIDOINS_CONTRACT_ADDRESS = '0xYourMidoinsContractAddress'; // Replace with the actual contract address

// Function to fetch user balance
async function getBalance(walletAddress) {
    try {
        if (!walletAddress) throw new Error('Wallet address is required.');

        const response = await fetch(
            `https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=${MIDOINS_CONTRACT_ADDRESS}&address=${walletAddress}&tag=latest&apikey=${API_KEY}`
        );

        if (!response.ok) throw new Error('Failed to fetch balance.');

        const data = await response.json();

        if (data.status !== '1') throw new Error(`Error from API: ${data.result}`);

        const balance = data.result; // Balance is in smallest denomination
        // Convert balance to readable format (assuming 18 decimals)
        return parseFloat(balance) / Math.pow(10, 18);
    } catch (error) {
        console.error('Error fetching balance:', error.message);
        throw error; // Propagate error
    }
}

// Function to fetch transaction history
async function getTransactionHistory(walletAddress) {
    try {
        if (!walletAddress) throw new Error('Wallet address is required.');

        const response = await fetch(
            `https://api.etherscan.io/api?module=account&action=tokentx&contractaddress=${MIDOINS_CONTRACT_ADDRESS}&address=${walletAddress}&page=1&offset=10&sort=desc&apikey=${API_KEY}`
        );

        if (!response.ok) throw new Error('Failed to fetch transaction history.');

        const data = await response.json();

        if (data.status !== '1') throw new Error(`Error from API: ${data.result}`);

        return data.result; // Array of transaction objects
    } catch (error) {
        console.error('Error fetching transaction history:', error.message);
        throw error; // Propagate error
    }
}

// Main function to display balance and transaction history
async function displayMidoinsInfo(walletAddress) {
    try {
        console.log('Fetching Midoins balance...');
        const balance = await getBalance(walletAddress);
        console.log(`Midoins Balance: ${balance}`);

        console.log('Fetching transaction history...');
        const transactions = await getTransactionHistory(walletAddress);
        console.log('Transaction History:', transactions);
    } catch (error) {
        console.error('Error displaying Midoins information:', error.message);
    }
}

// Replace '0xYourWalletAddress' with the user's wallet address
const walletAddress = '0xYourWalletAddress';

// Execute the function
displayMidoinsInfo(walletAddress);
```

Note:
- Replace `API_KEY`, `MIDOINS_CONTRACT_ADDRESS`, and `walletAddress` with your actual values.
- Ensure you handle sensitive information securely in production environments.
