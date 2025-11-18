"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sage-croissant-c13d3b.netlify.app
Prompt: Provide a detailed example of using Tether tokens in decentralized applications (dApps) on the Ethereum blockchain. Include code for interacting with USD₮ as an ERC20 token.
Generated: DETERMINISTIC_b990d23d309e90b7
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
const Web3 = require('web3');
const { ethers } = require('ethers');

// Setting up the provider and signer
const provider = new ethers.providers.InfuraProvider('homestead', 'YOUR_INFURA_PROJECT_ID');
const wallet = new ethers.Wallet('YOUR_PRIVATE_KEY', provider);

// Tether Token (USDT) contract address on Ethereum mainnet
const USDT_ADDRESS = '0xdac17f958d2ee523a2206206994597c13d831ec7';

// ERC20 ABI for minimal interaction (balanceOf, transfer)
const ERC20_ABI = [
    "function balanceOf(address owner) view returns (uint256)",
    "function transfer(address to, uint256 value) returns (bool)"
];

// Creating a contract instance for USDT
const usdtContract = new ethers.Contract(USDT_ADDRESS, ERC20_ABI, wallet);

/**
 * Fetches the USDT balance of a given address.
 * @param {string} address - The address to check the balance for.
 * @returns {Promise<string>} - The USDT balance as a string.
 */
async function getUSDTBalance(address) {
    try {
        const balance = await usdtContract.balanceOf(address);
        return ethers.utils.formatUnits(balance, 6); // USDT has 6 decimal places
    } catch (error) {
        console.error('Error fetching USDT balance:', error);
        throw new Error('Failed to fetch balance');
    }
}

/**
 * Transfers USDT from the wallet to a specified address.
 * @param {string} recipient - The address to send USDT to.
 * @param {string} amount - The amount of USDT to send (as a string).
 * @returns {Promise<string>} - The transaction hash.
 */
async function transferUSDT(recipient, amount) {
    try {
        const formattedAmount = ethers.utils.parseUnits(amount, 6); // USDT has 6 decimal places
        const transaction = await usdtContract.transfer(recipient, formattedAmount);
        const receipt = await transaction.wait(); // Wait for the transaction to be mined
        console.log('Transaction successful with hash:', receipt.transactionHash);
        return receipt.transactionHash;
    } catch (error) {
        console.error('Error transferring USDT:', error);
        throw new Error('Transfer failed');
    }
}

// Example usage
(async () => {
    const myAddress = wallet.address;

    // Check balance
    const balance = await getUSDTBalance(myAddress);
    console.log(`Your USDT balance: ${balance}`);

    // Transfer USDT (example values)
    const recipientAddress = 'RECIPIENT_ADDRESS'; // Replace with actual recipient address
    const amountToSend = '10'; // Amount of USDT to transfer
    await transferUSDT(recipientAddress, amountToSend);
})();
```

### Notes:
- Replace `YOUR_INFURA_PROJECT_ID` and `YOUR_PRIVATE_KEY` with your actual Infura project ID and wallet private key.
- Be cautious with managing and storing private keys.
- The example is designed for a production-ready Ethereum dApp context, handling errors and formatting appropriately for the USDT token.
