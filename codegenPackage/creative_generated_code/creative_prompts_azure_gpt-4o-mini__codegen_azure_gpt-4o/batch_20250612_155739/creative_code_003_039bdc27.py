"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqed.com
Prompt: What are some best practices for developing DeFi applications that rely on JavaScript functionality?
Generated: DETERMINISTIC_039bdc27ceeaad2d
Batch ID: 20250612_155739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Best practices for developing DeFi (Decentralized Finance) applications in JavaScript.
 * This code demonstrates key principles, including modularity, security, error handling,
 * and adherence to clean coding practices.
 */

// Import required external libraries
const ethers = require("ethers"); // Ethereum library for interacting with smart contracts
const dotenv = require("dotenv"); // For secure environment variable management

// Load environment variables from .env file
dotenv.config();

if (!process.env.INFURA_API_KEY || !process.env.PRIVATE_KEY) {
  throw new Error("Missing INFURA_API_KEY or PRIVATE_KEY in environment variables");
}

/**
 * Create a secure connection to the Ethereum blockchain using Infura.
 */
const provider = new ethers.providers.InfuraProvider("mainnet", process.env.INFURA_API_KEY);

/**
 * Initialize a wallet instance with proper key management.
 * Always use secure methods to store and handle private keys.
 */
const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider);

/**
 * Utility function: Send ETH securely to a recipient address.
 * @param {string} recipient - The recipient's Ethereum address.
 * @param {string} amount - Amount of ETH to send (in ethers).
 * @returns {Promise<string>} Transaction hash.
 */
async function sendEther(recipient, amount) {
  try {
    // Validate recipient address format
    if (!ethers.utils.isAddress(recipient)) {
      throw new Error("Invalid recipient address");
    }

    // Convert ETH amount to wei
    const value = ethers.utils.parseEther(amount);

    // Create and send the transaction
    const tx = await wallet.sendTransaction({
      to: recipient,
      value,
    });

    console.log("Transaction sent successfully:", tx.hash);
    return tx.hash;
  } catch (error) {
    console.error("Error while sending ETH:", error.message);
    throw error; // Re-throw the error for external handling
  }
}

/**
 * Utility function: Interact with a smart contract.
 * @param {string} contractAddress - Address of the deployed smart contract.
 * @param {Array} abi - ABI of the smart contract.
 * @returns {Object} Contract instance for interaction.
 */
function getContractInstance(contractAddress, abi) {
  try {
    // Validate contract address format
    if (!ethers.utils.isAddress(contractAddress)) {
      throw new Error("Invalid contract address");
    }

    // Create a contract instance using the ABI and address
    return new ethers.Contract(contractAddress, abi, wallet);
  } catch (error) {
    console.error("Error while creating contract instance:", error.message);
    throw error; // Re-throw the error for external handling
  }
}

/**
 * Example usage: Sending ETH and interacting with a token smart contract.
 */
async function runExample() {
  try {
    // Example: Send 0.01 ETH to a recipient
    const recipientAddress = "0xRecipientAddressHere"; // Replace with an actual address
    await sendEther(recipientAddress, "0.01");

    // Example: Interact with a token contract (ERC20)
    const erc20ABI = [
      // Minimal ABI for ERC20 token interactions
      "function balanceOf(address) view returns (uint256)",
      "function transfer(address, uint256) returns (bool)",
    ];
    const tokenAddress = "0xTokenContractAddressHere"; // Replace with actual contract address
    const contract = getContractInstance(tokenAddress, erc20ABI);

    // Check balance and perform a token transfer
    const balance = await contract.balanceOf(wallet.address);
    console.log("Token balance:", ethers.utils.formatUnits(balance, 18));

    const transferTx = await contract.transfer(recipientAddress, ethers.utils.parseUnits("10", 18));
    console.log("Token transfer transaction:", transferTx.hash);
  } catch (error) {
    console.error("Error during example execution:", error.message);
  }
}

// Run the example
runExample();

module.exports = {
  sendEther,
  getContractInstance,
};
```
