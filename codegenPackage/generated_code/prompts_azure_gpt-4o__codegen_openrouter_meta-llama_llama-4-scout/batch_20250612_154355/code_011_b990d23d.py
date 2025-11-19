"""
Generated Code Metadata:
========================
Original URL: https://sage-croissant-c13d3b.netlify.app
Prompt: Provide a detailed example of using Tether tokens in decentralized applications (dApps) on the Ethereum blockchain. Include code for interacting with USD₮ as an ERC20 token.
Generated: DETERMINISTIC_b990d23d309e90b7
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const Web3 = require('web3');
const { ethers } = require('ethers');

// Set up Ethereum provider and wallet
const INFURA_PROJECT_ID = 'YOUR_INFURA_PROJECT_ID';
const ALCHEMY_PROJECT_ID = 'YOUR_ALCHEMY_PROJECT_ID';
const provider = new ethers.providers.InfuraProvider('mainnet', INFURA_PROJECT_ID);
// Alternatively, use Alchemy
// const provider = new ethers.providers.AlchemyProvider('mainnet', ALCHEMY_PROJECT_ID);

const privateKey = 'YOUR_PRIVATE_KEY';
const wallet = new ethers.Wallet(privateKey, provider);

// Define Tether (USD₮) contract address and ABI
const TETHER_CONTRACT_ADDRESS = '0xdAC17F958D2ee523a2206206994597C13D831ec7';
const TETHER_CONTRACT_ABI = [
  'function balanceOf(address account) view returns (uint256)',
  'function transfer(address recipient, uint256 amount) returns (bool)',
  'function approve(address spender, uint256 amount) returns (bool)',
  'function allowance(address owner, address spender) view returns (uint256)',
];

// Create Tether contract instance
const TetherContract = new ethers.Contract(TETHER_CONTRACT_ADDRESS, TETHER_CONTRACT_ABI, wallet);

// Example usage: Get USD₮ balance
async function getTetherBalance(address) {
  try {
    const balance = await TetherContract.balanceOf(address);
    console.log(`USD₮ balance: ${ethers.utils.formatUnits(balance, 6)}`);
  } catch (error) {
    console.error('Error getting USD₮ balance:', error);
  }
}

// Example usage: Transfer USD₮
async function transferTether(recipientAddress, amount) {
  try {
    const tx = await TetherContract.transfer(recipientAddress, ethers.utils.parseUnits(amount, 6));
    await tx.wait();
    console.log(`Transferred ${amount} USD₮ to ${recipientAddress}`);
  } catch (error) {
    console.error('Error transferring USD₮:', error);
  }
}

// Example usage: Approve spender
async function approveSpender(spenderAddress, amount) {
  try {
    const tx = await TetherContract.approve(spenderAddress, ethers.utils.parseUnits(amount, 6));
    await tx.wait();
    console.log(`Approved ${spenderAddress} to spend ${amount} USD₮`);
  } catch (error) {
    console.error('Error approving spender:', error);
  }
}

// Example usage: Check allowance
async function checkAllowance(ownerAddress, spenderAddress) {
  try {
    const allowance = await TetherContract.allowance(ownerAddress, spenderAddress);
    console.log(`Allowance for ${spenderAddress}: ${ethers.utils.formatUnits(allowance, 6)}`);
  } catch (error) {
    console.error('Error checking allowance:', error);
  }
}

// Main function with example usage
async function main() {
  const address = wallet.address;
  console.log(`Wallet address: ${address}`);

  // Get USD₮ balance
  await getTetherBalance(address);

  // Transfer USD₮
  const recipientAddress = '0xRecipientAddress';
  const amount = '100';
  await transferTether(recipientAddress, amount);

  // Approve spender
  const spenderAddress = '0xSpenderAddress';
  const approvalAmount = '1000';
  await approveSpender(spenderAddress, approvalAmount);

  // Check allowance
  await checkAllowance(address, spenderAddress);
}

main().catch((error) => {
  console.error('Error:', error);
});
```
