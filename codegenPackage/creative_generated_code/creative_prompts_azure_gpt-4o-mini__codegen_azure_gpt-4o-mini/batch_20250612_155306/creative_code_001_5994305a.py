"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axondao.gitbook.io
Prompt: Write a code snippet to integrate AXGT token functionalities with Metamask for a healthcare project.
Generated: DETERMINISTIC_5994305a06dc6f4a
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';

// Define the AXGT token contract address and ABI
const AXGT_CONTRACT_ADDRESS = '0xYourAXGTTokenAddress'; // Replace with actual AXGT token address
const AXGT_ABI = [
    // Minimal ABI to get started, include necessary functions
    {
        "constant": true,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [{"name": "", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [{"name": "to", "type": "address"}, {"name": "value", "type": "uint256"}],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    }
];

// Initialize Web3 instance
let web3;
if (window.ethereum) {
    web3 = new Web3(window.ethereum);
} else {
    console.error('Please install MetaMask!');
}

// Create an instance of the AXGT token contract
const axgtContract = new web3.eth.Contract(AXGT_ABI, AXGT_CONTRACT_ADDRESS);

/**
 * Get user's account
 * @returns {Promise<string>} user account address
 */
async function getUserAccount() {
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    return accounts[0];
}

/**
 * Get the total supply of AXGT tokens
 * @returns {Promise<string>} total supply
 */
async function getTotalSupply() {
    try {
        const totalSupply = await axgtContract.methods.totalSupply().call();
        return totalSupply;
    } catch (error) {
        console.error('Error fetching total supply:', error);
        throw new Error('Could not fetch total supply');
    }
}

/**
 * Get the balance of a specific address
 * @param {string} address - The address of the user
 * @returns {Promise<string>} balance of the address
 */
async function getBalance(address) {
    try {
        const balance = await axgtContract.methods.balanceOf(address).call();
        return balance;
    } catch (error) {
        console.error('Error fetching balance:', error);
        throw new Error('Could not fetch balance');
    }
}

/**
 * Transfer AXGT tokens to another address
 * @param {string} to - Recipient address
 * @param {number} amount - Amount of tokens to transfer
 * @returns {Promise<void>}
 */
async function transferTokens(to, amount) {
    try {
        const account = await getUserAccount();
        const result = await axgtContract.methods.transfer(to, amount).send({ from: account });
        console.log('Transfer successful:', result);
    } catch (error) {
        console.error('Error during token transfer:', error);
        throw new Error('Token transfer failed');
    }
}

// Example usage
(async () => {
    try {
        const userAccount = await getUserAccount();
        console.log('User Account:', userAccount);

        const totalSupply = await getTotalSupply();
        console.log('Total Supply of AXGT:', totalSupply);

        const balance = await getBalance(userAccount);
        console.log('Your AXGT Balance:', balance);

        // Transfer example (uncomment to use)
        // await transferTokens('0xRecipientAddress', '1000000000000000000'); // Transfer 1 AXGT token
    } catch (error) {
        console.error('An error occurred:', error);
    }
})();
```
> **Note:** Replace the placeholder values (like `0xYourAXGTTokenAddress` and `0xRecipientAddress`) with actual contract and wallet addresses as needed.
