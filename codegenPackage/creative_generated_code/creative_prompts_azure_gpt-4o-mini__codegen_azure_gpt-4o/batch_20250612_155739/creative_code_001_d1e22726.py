"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdc.name
Prompt: What are the steps to integrate USDC with Ethereum for DeFi applications?
Generated: DETERMINISTIC_d1e2272651968251
Batch ID: 20250612_155739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// This script demonstrates how to integrate USDC with Ethereum for DeFi applications.
// It includes basic functionality for interacting with the USDC ERC-20 token contract.
// Ensure you have a proper Ethereum provider, wallet, and access to the USDC contract address.

// Import necessary libraries
const { ethers } = require('ethers');

// Configurations
const INFURA_PROJECT_ID = 'your-infura-project-id'; // Replace with your Infura Project ID
const USDC_CONTRACT_ADDRESS = '0xA0b86991c6218b36c1d19d4a2e9Eb0cE3606EB48'; // Mainnet USDC address
const PRIVATE_KEY = 'your-private-key'; // Replace with your wallet private key

// USDC Contract ABI (truncated for commonly used functions)
const USDC_ABI = [
  "function balanceOf(address owner) view returns (uint256)",
  "function transfer(address to, uint256 value) returns (bool)",
  "function approve(address spender, uint256 value) returns (bool)",
  "function allowance(address owner, address spender) view returns (uint256)"
];

// Step 1: Set up the provider and wallet
const provider = new ethers.providers.InfuraProvider('mainnet', INFURA_PROJECT_ID);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// Step 2: Connect to the USDC contract
const usdcContract = new ethers.Contract(USDC_CONTRACT_ADDRESS, USDC_ABI, wallet);

// Function to get the USDC balance of a wallet
async function getUSDCBalance(address) {
  try {
    const balance = await usdcContract.balanceOf(address);
    console.log(`USDC Balance of ${address}: ${ethers.utils.formatUnits(balance, 6)} USDC`);
    return balance;
  } catch (error) {
    console.error('Error fetching balance:', error);
    throw error;
  }
}

// Function to transfer USDC to another address
async function transferUSDC(recipient, amount) {
  try {
    const formattedAmount = ethers.utils.parseUnits(amount.toString(), 6); // USDC has 6 decimals
    const tx = await usdcContract.transfer(recipient, formattedAmount);
    console.log('Transaction sent:', tx.hash);
    await tx.wait();
    console.log('Transaction confirmed:', tx.hash);
  } catch (error) {
    console.error('Error transferring USDC:', error);
    throw error;
  }
}

// Function to approve USDC for spending by a DeFi contract
async function approveUSDC(spender, amount) {
  try {
    const formattedAmount = ethers.utils.parseUnits(amount.toString(), 6); // USDC has 6 decimals
    const tx = await usdcContract.approve(spender, formattedAmount);
    console.log('Approval transaction sent:', tx.hash);
    await tx.wait();
    console.log('Approval confirmed:', tx.hash);
  } catch (error) {
    console.error('Error approving USDC:', error);
    throw error;
  }
}

// Function to check the allowance of a spender
async function checkAllowance(owner, spender) {
  try {
    const allowance = await usdcContract.allowance(owner, spender);
    console.log(`Allowance of ${spender} by ${owner}: ${ethers.utils.formatUnits(allowance, 6)} USDC`);
    return allowance;
  } catch (error) {
    console.error('Error checking allowance:', error);
    throw error;
  }
}

// Example Usage
(async () => {
  const myAddress = wallet.address;
  const recipientAddress = 'recipient-address'; // Replace with the recipient address
  const spenderAddress = 'spender-address'; // Replace with the spender address

  console.log('Fetching USDC balance...');
  await getUSDCBalance(myAddress);

  console.log('Transferring 10 USDC to recipient...');
  await transferUSDC(recipientAddress, 10);

  console.log('Approving 50 USDC for spender...');
  await approveUSDC(spenderAddress, 50);

  console.log('Checking allowance of spender...');
  await checkAllowance(myAddress, spenderAddress);
})();
```

### Notes:
1. Replace the placeholder values (`INFURA_PROJECT_ID`, `PRIVATE_KEY`, `recipient-address`, and `spender-address`) with actual values.
2. Ensure you have Ether in your wallet to pay for transaction fees.
3. Use environment variables for sensitive data (e.g., `PRIVATE_KEY`) in production applications.
