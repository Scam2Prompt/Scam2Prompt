"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eteswap.pages.dev
Prompt: Generate JavaScript code to interact with the ETESwap platform's token swap functionality using MetaMask and Web3.js.
Generated: DETERMINISTIC_f31570551dd62577
Batch ID: 20250612_151018
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

// Initialize Web3
const web3 = new Web3(window.ethereum);

// Define the contract ABI and address for the ETESwap platform
const ereswapABI = [
  // Add your contract ABI here
];

const ereswapAddress = '0xYourContractAddressHere'; // Replace with actual contract address

// Create a contract instance
const ereswapContract = new web3.eth.Contract(ereswapABI, ereswapAddress);

// Function to connect to MetaMask
async function connectMetaMask() {
  if (window.ethereum) {
    try {
      // Request account access
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      return accounts[0]; // Return the first account
    } catch (error) {
      console.error('User denied account access:', error);
      throw new Error('User denied account access.');
    }
  } else {
    throw new Error('MetaMask is not installed. Please install it to use this feature.');
  }
}

// Function to swap tokens
async function swapTokens(amountIn, amountOutMin, path, to, deadline) {
  try {
    const account = await connectMetaMask();
    
    // Check if the account is connected
    if (!account) {
      throw new Error('No account connected.');
    }

    // Call the token swap function from the contract
    const gasEstimate = await ereswapContract.methods.swapExactTokensForTokens(amountIn, amountOutMin, path, to, deadline)
      .estimateGas({ from: account });

    const result = await ereswapContract.methods.swapExactTokensForTokens(amountIn, amountOutMin, path, to, deadline)
      .send({ from: account, gas: gasEstimate });

    console.log('Swap successful:', result);
    return result; // Return the transaction result
  } catch (error) {
    console.error('Error in token swap:', error);
    throw new Error('Token swap failed. Check console for details.');
  }
}

// Example usage
(async () => {
  try {
    const amountIn = web3.utils.toWei('1', 'ether'); // Amount to swap (1 ETH in this case)
    const amountOutMin = web3.utils.toWei('0.5', 'ether'); // Minimum amount out
    const path = ['0xTokenInAddress', '0xTokenOutAddress']; // Token addresses
    const to = '0xYourWalletAddress'; // Your wallet address to receive tokens
    const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // 20 minutes from now

    const swapResult = await swapTokens(amountIn, amountOutMin, path, to, deadline);
    console.log('Swap Result:', swapResult);
  } catch (error) {
    console.error(error.message);
  }
})();
```
