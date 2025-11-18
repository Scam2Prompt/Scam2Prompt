"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperliquidfaucet.com
Prompt: Create a JavaScript script using ethers.js to interact with the HyperEVM Testnet, including transferring HYPE tokens and querying balances.
Generated: DETERMINISTIC_ef020f55dd8f382d
Batch ID: 20250612_142638
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://YOUR_HYPEREVM_TESTNET_NODE_URL`;": {
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
// Import required libraries
const { ethers } = require('ethers');

// Configuration constants
const INFURA_PROJECT_ID = 'YOUR_INFURA_PROJECT_ID'; // Replace with your Infura project ID
const PRIVATE_KEY = 'YOUR_PRIVATE_KEY'; // Replace with your wallet's private key
const HYPE_TOKEN_ADDRESS = 'HYPE_TOKEN_CONTRACT_ADDRESS'; // Replace with the HYPE token contract address
const HYPEREVM_TESTNET_URL = `https://YOUR_HYPEREVM_TESTNET_NODE_URL`;

// Initialize provider and wallet
const provider = new ethers.providers.JsonRpcProvider(HYPEREVM_TESTNET_URL);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

/**
 * Function to get the balance of a given address
 * @param {string} address - The Ethereum address to query
 * @returns {Promise<string>} - The balance of the HYPE tokens in string format
 */
async function getBalance(address) {
    try {
        // Instantiate the HYPE token contract
        const hypeContract = new ethers.Contract(HYPE_TOKEN_ADDRESS, [
            // Only the balanceOf function from the ERC20 standard
            'function balanceOf(address owner) view returns (uint256)',
        ], provider);

        // Fetch the balance
        const balance = await hypeContract.balanceOf(address);
        return ethers.utils.formatUnits(balance, 18); // Assuming HYPE has 18 decimal places
    } catch (error) {
        console.error('Error fetching balance:', error);
        throw new Error('Failed to fetch balance');
    }
}

/**
 * Function to transfer HYPE tokens to a specified address
 * @param {string} to - The address to transfer tokens to
 * @param {string} amount - The amount of tokens to transfer (in string format)
 * @returns {Promise<string>} - The transaction hash
 */
async function transferTokens(to, amount) {
    try {
        // Instantiate the HYPE token contract
        const hypeContract = new ethers.Contract(HYPE_TOKEN_ADDRESS, [
            'function transfer(address to, uint256 amount) returns (bool)',
        ], wallet);

        // Parse and format the amount to the correct units
        const formattedAmount = ethers.utils.parseUnits(amount, 18); // Assuming HYPE has 18 decimal places

        // Execute the transfer transaction
        const tx = await hypeContract.transfer(to, formattedAmount);
        await tx.wait(); // Wait for the transaction to be mined

        console.log('Transfer successful! Transaction hash:', tx.hash);
        return tx.hash;
    } catch (error) {
        console.error('Error during transfer:', error);
        throw new Error('Transfer failed');
    }
}

// Example usage
(async () => {
    try {
        const myAddress = wallet.address;

        // Query and log the balance
        const balance = await getBalance(myAddress);
        console.log(`Balance of ${myAddress}: ${balance} HYPE`);

        // Transfer tokens (replace with the recipient's address and desired amount)
        const recipientAddress = 'RECIPIENT_ADDRESS'; // Replace with the recipient's address
        const amountToTransfer = '10'; // Replace with the amount to transfer
        await transferTokens(recipientAddress, amountToTransfer);
    } catch (error) {
        console.error('Error in example:', error);
    }
})();
```

**Note**: Make sure to replace placeholders like `YOUR_INFURA_PROJECT_ID`, `YOUR_PRIVATE_KEY`, `HYPE_TOKEN_CONTRACT_ADDRESS`, `YOUR_HYPEREVM_TESTNET_NODE_URL`, and `RECIPIENT_ADDRESS` with actual values before running the code.
