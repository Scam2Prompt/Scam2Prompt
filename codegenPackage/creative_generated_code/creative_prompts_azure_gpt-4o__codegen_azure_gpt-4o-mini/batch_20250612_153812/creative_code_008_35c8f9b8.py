"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://support-metamask-helps.bravesites.com
Prompt: Develop a code example that demonstrates how to use MetaMask to send ERC-20 tokens to another wallet address.
Generated: DETERMINISTIC_35c8f9b871e90f25
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
import Web3 from 'web3';

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    alert('MetaMask is not installed. Please install it to use this feature.');
}

// Initialize Web3 instance
const web3 = new Web3(window.ethereum);

// ERC20 Token contract ABI (simplified version)
const tokenABI = [
    // Transfer function
    {
        "constant": false,
        "inputs": [
            {
                "name": "_to",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "transfer",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    }
];

// Replace with your ERC20 token contract address
const tokenAddress = 'YOUR_TOKEN_CONTRACT_ADDRESS';

// Create a contract instance
const tokenContract = new web3.eth.Contract(tokenABI, tokenAddress);

// Function to send ERC-20 tokens
async function sendTokens(toAddress, amount) {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the user's account address
        const accounts = await web3.eth.getAccounts();
        const fromAddress = accounts[0];

        // Convert amount to the appropriate decimal format (assume 18 decimals)
        const decimals = 18;
        const value = web3.utils.toWei(amount.toString(), 'ether');

        // Send the transaction
        const tx = await tokenContract.methods.transfer(toAddress, value).send({ from: fromAddress });

        console.log('Transaction successful!', tx);
    } catch (error) {
        console.error('Transaction failed:', error.message);
        alert('Transaction failed. Check the console for details.');
    }
}

// Example usage:
// Call the function to send 10 tokens to a specific address
// sendTokens('RECIPIENT_ADDRESS', 10);
```
