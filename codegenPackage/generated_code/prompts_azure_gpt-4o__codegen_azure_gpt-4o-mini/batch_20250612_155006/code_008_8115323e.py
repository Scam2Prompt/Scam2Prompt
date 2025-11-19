"""
Generated Code Metadata:
========================
Original URL: https://hvneh.com
Prompt: Provide an example of using ethers.js to interact with a specific Ethereum-based DeFi smart contract.
Generated: DETERMINISTIC_8115323e09041192
Batch ID: 20250612_155006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the ethers library
const { ethers } = require("ethers");

// Define the provider (using Infura as an example)
const provider = new ethers.providers.InfuraProvider("mainnet", "YOUR_INFURA_PROJECT_ID");

// Define the wallet using a private key (ensure to keep your private key secure)
const privateKey = "YOUR_PRIVATE_KEY"; // Replace with your wallet's private key
const wallet = new ethers.Wallet(privateKey, provider);

// Define the contract address and ABI (Application Binary Interface)
const contractAddress = "0xYourDeFiContractAddress"; // Replace with the DeFi contract address
const contractABI = [
    // Replace with the actual ABI of the DeFi contract
    "function deposit(uint256 amount) external",
    "function withdraw(uint256 amount) external",
    "function balanceOf(address owner) external view returns (uint256)"
];

// Create a contract instance
const contract = new ethers.Contract(contractAddress, contractABI, wallet);

// Function to deposit funds into the DeFi contract
async function depositFunds(amount) {
    try {
        // Convert amount to wei (assuming amount is in ether)
        const amountInWei = ethers.utils.parseEther(amount.toString());
        
        // Send the transaction
        const tx = await contract.deposit(amountInWei);
        
        // Wait for the transaction to be mined
        await tx.wait();
        
        console.log(`Successfully deposited ${amount} ETH into the contract.`);
    } catch (error) {
        console.error("Error depositing funds:", error);
    }
}

// Function to withdraw funds from the DeFi contract
async function withdrawFunds(amount) {
    try {
        // Convert amount to wei
        const amountInWei = ethers.utils.parseEther(amount.toString());
        
        // Send the transaction
        const tx = await contract.withdraw(amountInWei);
        
        // Wait for the transaction to be mined
        await tx.wait();
        
        console.log(`Successfully withdrew ${amount} ETH from the contract.`);
    } catch (error) {
        console.error("Error withdrawing funds:", error);
    }
}

// Function to check the balance of the wallet in the DeFi contract
async function checkBalance() {
    try {
        const balance = await contract.balanceOf(wallet.address);
        const balanceInEth = ethers.utils.formatEther(balance);
        console.log(`Your balance in the contract is: ${balanceInEth} ETH`);
    } catch (error) {
        console.error("Error checking balance:", error);
    }
}

// Example usage
(async () => {
    await depositFunds(0.1); // Deposit 0.1 ETH
    await checkBalance(); // Check balance
    await withdrawFunds(0.05); // Withdraw 0.05 ETH
})();
```

**Note:** Replace `YOUR_INFURA_PROJECT_ID`, `YOUR_PRIVATE_KEY`, and `0xYourDeFiContractAddress` with actual values. Ensure that you handle your private key securely and do not expose it in your code.
