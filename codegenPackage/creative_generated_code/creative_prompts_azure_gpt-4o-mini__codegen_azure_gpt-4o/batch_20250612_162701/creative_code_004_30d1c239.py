"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://support-metamask-helps.bravesites.com
Prompt: What are the advantages of using MetaMask for managing ETH and ERC-20 tokens in a dApp environment?
Generated: DETERMINISTIC_30d1c239e8346ce6
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready code example demonstrating the advantages of using MetaMask for managing ETH and ERC-20 tokens in a dApp environment:

```javascript
/**
 * @file metamask-advantages.js
 * @description Demonstrates the advantages of using MetaMask in a dApp environment for managing ETH and ERC-20 tokens.
 * @author Expert Programmer
 */

// Import necessary modules (if using Node.js or bundler)
// const ethers = require('ethers'); // Uncomment if using ethers.js

// HTML snippet for MetaMask integration (used in front-end):
// <button id="connectWallet">Connect Wallet</button>
// <button id="getBalance">Get ETH Balance</button>
// <button id="transferTokens">Transfer Tokens</button>

// Define the contract address and ABI for ERC-20 token interactions
const tokenContractAddress = "0xYourTokenContractAddress"; // Replace with the actual contract address
const tokenContractABI = [
  // Minimal ABI required for ERC-20 token interaction
  {
    "constant": true,
    "inputs": [{ "name": "owner", "type": "address" }],
    "name": "balanceOf",
    "outputs": [{ "name": "balance", "type": "uint256" }],
    "type": "function",
  },
  {
    "constant": false,
    "inputs": [
      { "name": "to", "type": "address" },
      { "name": "value", "type": "uint256" },
    ],
    "name": "transfer",
    "outputs": [{ "name": "", "type": "bool" }],
    "type": "function",
  },
];

// Define global variables
let userAddress;
let provider;
let signer;

/**
 * @function connectToMetaMask
 * @description Connects the user's MetaMask wallet to the dApp.
 */
async function connectToMetaMask() {
  try {
    // Check if MetaMask is installed
    if (typeof window.ethereum === "undefined") {
      alert("MetaMask is not installed. Please install MetaMask to use this dApp.");
      return;
    }

    // Request account access from MetaMask
    const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
    userAddress = accounts[0]; // First account in MetaMask
    provider = new ethers.providers.Web3Provider(window.ethereum);
    signer = provider.getSigner();

    alert(`Wallet connected: ${userAddress}`);
  } catch (error) {
    console.error("Error connecting to MetaMask:", error);
    alert("Failed to connect wallet. Please try again.");
  }
}

/**
 * @function getETHBalance
 * @description Fetches the ETH balance of the connected wallet.
 */
async function getETHBalance() {
  try {
    if (!userAddress || !provider) {
      alert("Wallet not connected. Please connect your wallet first.");
      return;
    }

    // Fetch the ETH balance
    const balance = await provider.getBalance(userAddress);
    const humanReadableBalance = ethers.utils.formatEther(balance);

    alert(`ETH Balance: ${humanReadableBalance}`);
  } catch (error) {
    console.error("Error fetching ETH balance:", error);
    alert("Failed to fetch ETH balance. Please try again.");
  }
}

/**
 * @function transferERC20Tokens
 * @description Transfers ERC-20 tokens to a recipient address.
 * @param {string} recipientAddress - The recipient's wallet address.
 * @param {number} amount - The amount of tokens to transfer.
 */
async function transferERC20Tokens(recipientAddress, amount) {
  try {
    if (!userAddress || !signer) {
      alert("Wallet not connected. Please connect your wallet first.");
      return;
    }

    // Initialize the ERC-20 contract
    const tokenContract = new ethers.Contract(tokenContractAddress, tokenContractABI, signer);

    // Convert the amount to the correct format (assuming 18 decimals)
    const tokenAmount = ethers.utils.parseUnits(amount.toString(), 18);

    // Perform the token transfer
    const tx = await tokenContract.transfer(recipientAddress, tokenAmount);
    await tx.wait(); // Wait for transaction confirmation

    alert(`Tokens transferred successfully! Tx Hash: ${tx.hash}`);
  } catch (error) {
    console.error("Error transferring tokens:", error);
    alert("Failed to transfer tokens. Please try again.");
  }
}

// Event listeners for HTML buttons
document.getElementById("connectWallet").addEventListener("click", connectToMetaMask);
document.getElementById("getBalance").addEventListener("click", getETHBalance);
document.getElementById("transferTokens").addEventListener("click", () => {
  const recipientAddress = prompt("Enter recipient address:");
  const amount = prompt("Enter token amount:");
  transferERC20Tokens(recipientAddress, amount);
});
```

### Key Features:
1. **MetaMask Connection**: The code connects the user's MetaMask wallet securely.
2. **ETH Management**: Fetches the user's ETH balance from the blockchain.
3. **ERC-20 Token Interaction**: Allows token transfers using the Ethereum blockchain.
4. **Error Handling**: Alerts and logs errors to ensure smooth user experience.
5. **Best Practices**: Clean organization, semantic variable names, and modular functions.
