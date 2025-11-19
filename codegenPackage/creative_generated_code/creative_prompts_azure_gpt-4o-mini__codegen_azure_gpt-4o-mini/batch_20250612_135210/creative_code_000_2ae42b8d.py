"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wap.xushuishiwu.cn
Prompt: How can I use MetaMask to securely manage my ERC20 tokens and perform transactions?
Generated: DETERMINISTIC_2ae42b8d422a3e2e
Batch ID: 20250612_135210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
import Web3 from 'web3';

// Define the ERC20 Token contract ABI (Application Binary Interface)
const ERC20_ABI = [
    // Only the essential ERC20 functions for this example
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
        "inputs": [],
        "name": "balanceOf",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    }
];

// Initialize Web3
let web3;
if (window.ethereum) {
    web3 = new Web3(window.ethereum);
    // Request account access if needed
    window.ethereum.request({ method: 'eth_requestAccounts' })
        .catch((error) => {
            console.error("User denied account access:", error);
        });
} else {
    console.error("MetaMask is not installed. Please install it to use this application.");
}

// Function to get the balance of an ERC20 token for a given address
async function getTokenBalance(tokenAddress, userAddress) {
    try {
        const tokenContract = new web3.eth.Contract(ERC20_ABI, tokenAddress);
        const balance = await tokenContract.methods.balanceOf(userAddress).call();
        return web3.utils.fromWei(balance, 'ether'); // Convert balance from Wei to Ether for display
    } catch (error) {
        console.error("Error fetching balance:", error);
        return null;
    }
}

// Function to transfer ERC20 tokens
async function transferTokens(tokenAddress, toAddress, amount) {
    try {
        const tokenContract = new web3.eth.Contract(ERC20_ABI, tokenAddress);
        const accounts = await web3.eth.getAccounts(); // Get the user's accounts
        const amountInWei = web3.utils.toWei(amount.toString(), 'ether'); // Convert amount to Wei

        // Execute the transfer transaction
        const transaction = await tokenContract.methods.transfer(toAddress, amountInWei).send({ from: accounts[0] });
        console.log("Transaction successful:", transaction);
    } catch (error) {
        console.error("Error transferring tokens:", error);
    }
}

// Usage examples
(async () => {
    const tokenAddress = '0xYourTokenAddress'; // Replace with your ERC20 token address
    const userAddress = '0xYourAddress'; // Replace with your Ethereum address

    // Get the balance
    const balance = await getTokenBalance(tokenAddress, userAddress);
    console.log(`Token balance: ${balance}`);

    // Transfer tokens
    const recipientAddress = '0xRecipientAddress'; // Replace with the recipient's address
    const amountToTransfer = 10; // Amount of tokens to transfer
    await transferTokens(tokenAddress, recipientAddress, amountToTransfer);
})();
```

Note: Replace placeholder addresses (`0xYourTokenAddress`, `0xYourAddress`, and `0xRecipientAddress`) with actual Ethereum addresses when using this code.
