"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vault-yearn.com
Prompt: Write a code snippet that utilizes the MetaMask API to enable users to buy and swap cryptocurrencies directly from my application.
Generated: DETERMINISTIC_29a738560aea06f5
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from 'ethers';

// Function to connect to MetaMask and enable cryptocurrency-related operations
async function connectMetaMask() {
  try {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
      throw new Error('MetaMask is not installed. Please install MetaMask to use this feature.');
    }

    // Request account access from MetaMask
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    if (accounts.length === 0) {
      throw new Error('No accounts found. Please ensure MetaMask is unlocked and an account is available.');
    }

    console.log('Connected account:', accounts[0]);

    // Initialize an Ethereum provider
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Return the connected account and provider
    return { account: accounts[0], provider };
  } catch (error) {
    console.error('Failed to connect to MetaMask:', error.message);
    throw error;
  }
}

// Function to buy cryptocurrency using the MetaMask provider
async function buyCrypto(provider, account, tokenAddress, amount) {
  try {
    // Example: Construct transaction to purchase cryptocurrency (replace with actual implementation)
    const signer = provider.getSigner(account);
    const transaction = {
      // Replace with actual contract interactable method and parameters
      to: tokenAddress, // Address of the token contract
      value: ethers.utils.parseEther(amount.toString()), // Amount of ETH to send
    };

    // Send transaction via MetaMask
    const txResponse = await signer.sendTransaction(transaction);

    console.log('Transaction submitted:', txResponse.hash);

    // Wait for the transaction to be mined
    const receipt = await txResponse.wait();
    console.log('Transaction confirmed:', receipt);
    return receipt;
  } catch (error) {
    console.error('Failed to buy cryptocurrency:', error.message);
    throw error;
  }
}

// Function to swap cryptocurrency using a decentralized exchange (DEX) smart contract
async function swapCrypto(provider, account, dexContractAddress, inputToken, outputToken, inputAmount) {
  try {
    // Example: Interact with the DEX contract (replace with actual implementation)
    const signer = provider.getSigner(account);

    // ABI for the DEX contract (replace with actual ABI)
    const dexAbi = [
      'function swap(address inputToken, address outputToken, uint256 inputAmount) public returns (uint256 outputAmount)',
    ];

    // Initialize contract instance
    const dexContract = new ethers.Contract(dexContractAddress, dexAbi, signer);

    // Execute swap function
    const txResponse = await dexContract.swap(inputToken, outputToken, inputAmount);
    console.log('Swap transaction submitted:', txResponse.hash);

    // Wait for transaction confirmation
    const receipt = await txResponse.wait();
    console.log('Swap transaction confirmed:', receipt);
    return receipt;
  } catch (error) {
    console.error('Failed to swap cryptocurrency:', error.message);
    throw error;
  }
}

// Usage example (ensure proper integration in your application workflow)
(async () => {
  try {
    const { account, provider } = await connectMetaMask();

    // Example token and transaction details (replace with actual addresses and amounts)
    const tokenAddress = '0xTokenContractAddressHere'; // Replace with token contract address
    const dexContractAddress = '0xDexContractAddressHere'; // Replace with DEX contract address
    const inputToken = '0xInputTokenAddressHere'; // Replace with input token address
    const outputToken = '0xOutputTokenAddressHere'; // Replace with output token address
    const buyAmount = 0.01; // Amount of ETH to spend
    const swapAmount = ethers.utils.parseUnits('100', 18); // Amount of input tokens

    // Example calls
    console.log('Buying crypto...');
    await buyCrypto(provider, account, tokenAddress, buyAmount);

    console.log('Swapping crypto...');
    await swapCrypto(provider, account, dexContractAddress, inputToken, outputToken, swapAmount);
  } catch (error) {
    console.error('Error:', error.message);
  }
})();
```

### Notes:
1. Replace placeholder values (`tokenAddress`, `dexContractAddress`, `inputToken`, `outputToken`) with actual contract addresses and parameters suitable for your use case.
2. Ensure the ABI for the DEX contract matches the deployed contract you are interacting with.
3. The code assumes familiarity with Ethereum and smart contract interactions.
4. Always perform thorough testing before deploying in a production environment.
