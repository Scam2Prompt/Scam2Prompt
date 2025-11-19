"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskrectify.com
Prompt: Create a tutorial on how to buy and store tokens using MetaMask, including code examples for interacting with the wallet.
Generated: DETERMINISTIC_20a3164cc9b3d41f
Batch ID: 20250612_155636
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary packages
import Web3 from 'web3';

// Initialize web3 instance
// This assumes that Metamask is installed in the browser
if (typeof window.ethereum !== 'undefined') {
    var web3 = new Web3(window.ethereum);
} else {
    console.error('Please install MetaMask!');
}

// Function to connect to MetaMask
async function connectMetaMask() {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Connected to MetaMask');
    } catch (error) {
        console.error('User denied account access', error);
    }
}

// Function to buy tokens
async function buyTokens(tokenAddress, amount) {
    // Get the user's account address
    const accounts = await web3.eth.getAccounts();
    const account = accounts[0];

    // Token contract ABI (replace with actual ABI)
    const tokenABI = [
        // Only including the transfer function for simplicity
        {
            "constant": false,
            "inputs": [
                {
                    "name": "to",
                    "type": "address"
                },
                {
                    "name": "value",
                    "type": "uint256"
                }
            ],
            "name": "transfer",
            "outputs": [],
            "payable": false,
            "stateMutability": "nonpayable",
            "type": "function"
        }
    ];

    // Create token contract instance
    const tokenContract = new web3.eth.Contract(tokenABI, tokenAddress);

    // Convert amount to wei (assumes 18 decimals)
    const amountInWei = web3.utils.toWei(amount.toString(), 'ether');

    try {
        // Send transaction to buy tokens
        await tokenContract.methods.transfer(account, amountInWei).send({ from: account });
        console.log(`Successfully bought ${amount} tokens`);
    } catch (error) {
        console.error('Transaction failed', error);
    }
}

// Function to check token balance
async function checkTokenBalance(tokenAddress) {
    const accounts = await web3.eth.getAccounts();
    const account = accounts[0];

    // Token contract ABI (replace with actual ABI)
    const tokenABI = [
        {
            "constant": true,
            "inputs": [
                {
                    "name": "owner",
                    "type": "address"
                }
            ],
            "name": "balanceOf",
            "outputs": [
                {
                    "name": "",
                    "type": "uint256"
                }
            ],
            "payable": false,
            "stateMutability": "view",
            "type": "function"
        }
    ];

    // Create token contract instance
    const tokenContract = new web3.eth.Contract(tokenABI, tokenAddress);

    try {
        // Call balanceOf function to get the token balance
        const balance = await tokenContract.methods.balanceOf(account).call();
        console.log(`Token balance: ${web3.utils.fromWei(balance, 'ether')} tokens`);
    } catch (error) {
        console.error('Failed to retrieve token balance', error);
    }
}

// Example usage
(async () => {
    await connectMetaMask();
    
    const tokenAddress = '0xYourTokenAddress'; // Replace with actual token address
    const amountToBuy = 1; // Number of tokens to buy

    await buyTokens(tokenAddress, amountToBuy);
    await checkTokenBalance(tokenAddress);
})();
```
