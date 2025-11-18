"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskchrameextansun.gitbook.io
Prompt: Write code to retrieve the balance of Ethereum and ERC-20 tokens stored in a user's MetaMask wallet. Include error handling for cases where the wallet is not connected.
Generated: DETERMINISTIC_934783dae6383f0d
Batch ID: 20250612_153848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import Web3 from 'web3';
import { ethers } from 'ethers';

// Define the main function to retrieve balances
async function getWalletBalances() {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        console.error('MetaMask is not installed. Please install it to use this application.');
        return;
    }

    // Create a new Web3 instance using the current provider
    const web3 = new Web3(window.ethereum);

    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        // Get user's accounts
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];

        // Check if the user has any accounts connected
        if (!userAddress) {
            console.error('No connected account found');
            return;
        }

        // Fetching Ethereum balance
        const ethBalance = await web3.eth.getBalance(userAddress);
        console.log(`Ethereum Balance: ${web3.utils.fromWei(ethBalance, 'ether')} ETH`);

        // Example ERC-20 token contract address (replace with actual token address)
        const tokenAddress = '0xYourTokenAddressHere';
        
        // ERC-20 token ABI (simplified for balanceOf function)
        const tokenABI = [
            // BalanceOf function
            {
                "constant": true,
                "inputs": [{ "name": "_owner", "type": "address" }],
                "name": "balanceOf",
                "outputs": [{ "name": "", "type": "uint256" }],
                "payable": false,
                "stateMutability": "view",
                "type": "function"
            }
        ];

        // Create token contract instance
        const tokenContract = new web3.eth.Contract(tokenABI, tokenAddress);

        // Fetching ERC-20 token balance
        const tokenBalance = await tokenContract.methods.balanceOf(userAddress).call();
        console.log(`Token Balance: ${web3.utils.fromWei(tokenBalance, 'ether')} Tokens`);

    } catch (error) {
        // Handle errors gracefully
        console.error('An error occurred while retrieving balances:', error);
    }
}

// Execute the main function
getWalletBalances();
```
