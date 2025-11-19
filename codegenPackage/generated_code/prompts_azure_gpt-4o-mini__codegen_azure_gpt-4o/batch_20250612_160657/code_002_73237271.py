"""
Generated Code Metadata:
========================
Original URL: https://aave.network
Prompt: What are the steps to integrate Aave's GHO stablecoin into a decentralized application?
Generated: DETERMINISTIC_73237271f4865fcb
Batch ID: 20250612_160657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries and dependencies
const { ethers } = require("ethers");
const { abi: ERC20_ABI } = require("@openzeppelin/contracts/build/contracts/ERC20.json");

// Define constants
const AAVE_GHO_ADDRESS = "0xYourGHOContractAddress"; // Replace with the actual GHO contract address
const INFURA_PROJECT_ID = "your-infura-project-id"; // Replace with your Infura project ID
const PRIVATE_KEY = "your-private-key"; // Replace with your wallet's private key

// Initialize provider and wallet
const provider = new ethers.providers.InfuraProvider("mainnet", INFURA_PROJECT_ID);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// Initialize GHO contract instance
const ghoContract = new ethers.Contract(AAVE_GHO_ADDRESS, ERC20_ABI, wallet);

// Function to check GHO balance
async function getGHOBalance(address) {
  try {
    const balance = await ghoContract.balanceOf(address);
    console.log(`GHO Balance of ${address}:`, ethers.utils.formatUnits(balance, 18));
    return balance;
  } catch (error) {
    console.error("Error fetching GHO balance:", error);
    throw error;
  }
}

// Function to transfer GHO tokens
async function transferGHO(to, amount) {
  try {
    const formattedAmount = ethers.utils.parseUnits(amount.toString(), 18);
    const tx = await ghoContract.transfer(to, formattedAmount);
    console.log("Transaction sent:", tx.hash);
    await tx.wait();
    console.log("Transaction confirmed:", tx.hash);
  } catch (error) {
    console.error("Error transferring GHO tokens:", error);
    throw error;
  }
}

// Function to approve GHO tokens for spending
async function approveGHO(spender, amount) {
  try {
    const formattedAmount = ethers.utils.parseUnits(amount.toString(), 18);
    const tx = await ghoContract.approve(spender, formattedAmount);
    console.log("Approval transaction sent:", tx.hash);
    await tx.wait();
    console.log("Approval transaction confirmed:", tx.hash);
  } catch (error) {
    console.error("Error approving GHO tokens:", error);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    const userAddress = wallet.address;
    const recipientAddress = "0xRecipientAddress"; // Replace with the recipient's address
    const spenderAddress = "0xSpenderAddress"; // Replace with the spender's address
    const transferAmount = 10; // Amount of GHO to transfer
    const approveAmount = 20; // Amount of GHO to approve

    // Check GHO balance
    await getGHOBalance(userAddress);

    // Transfer GHO tokens
    await transferGHO(recipientAddress, transferAmount);

    // Approve GHO tokens for spending
    await approveGHO(spenderAddress, approveAmount);
  } catch (error) {
    console.error("Error in example usage:", error);
  }
})();
```

**Note:** Replace placeholder values (e.g., `0xYourGHOContractAddress`, `your-infura-project-id`, `your-private-key`, etc.) with actual values for your application. Ensure you have the necessary permissions and access to interact with the Aave GHO contract.
