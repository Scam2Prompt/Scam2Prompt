"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meta-mask-wallet-demo.vercel.app
Prompt: Explain how to integrate MetaMask wallet functionalities into a web application for tracking DeFi investments.
Generated: DETERMINISTIC_8146c1017abfc5fe
Batch ID: 20250612_135210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
// Ensure to include Web3.js in your project (e.g., via npm install web3)
import Web3 from 'web3';

// Define the Web3 instance
let web3;

// Function to check if MetaMask is installed and initialize Web3
async function initializeWeb3() {
  if (window.ethereum) {
    try {
      // Request access to the user's Ethereum account
      await window.ethereum.request({ method: 'eth_requestAccounts' });
      // Initialize Web3 instance with MetaMask's provider
      web3 = new Web3(window.ethereum);
      console.log("MetaMask connected successfully");
    } catch (error) {
      console.error("User denied MetaMask access:", error);
    }
  } else {
    console.error("MetaMask is not installed. Please install MetaMask to use this feature.");
  }
}

// Function to retrieve connected wallet address
async function getWalletAddress() {
  try {
    if (!web3) {
      throw new Error("Web3 is not initialized. Make sure to call initializeWeb3 first.");
    }
    const accounts = await web3.eth.getAccounts();
    if (accounts.length === 0) {
      console.warn("No wallet connected.");
      return null;
    }
    return accounts[0]; // Return the first connected wallet address
  } catch (error) {
    console.error("Error fetching wallet address:", error);
    return null;
  }
}

// Function to track DeFi investments (example: retrieving token balance)
async function getTokenBalance(tokenAddress, walletAddress) {
  try {
    if (!web3) {
      throw new Error("Web3 is not initialized. Make sure to call initializeWeb3 first.");
    }
    if (!tokenAddress || !walletAddress) {
      throw new Error("Token address and wallet address are required.");
    }

    // ABI for ERC-20 token contract (simplified version for balanceOf function)
    const tokenABI = [
      {
        constant: true,
        inputs: [{ name: "_owner", type: "address" }],
        name: "balanceOf",
        outputs: [{ name: "balance", type: "uint256" }],
        type: "function",
      },
    ];

    // Create contract instance
    const tokenContract = new web3.eth.Contract(tokenABI, tokenAddress);

    // Call balanceOf function to get the token balance
    const balance = await tokenContract.methods.balanceOf(walletAddress).call();
    return web3.utils.fromWei(balance, "ether"); // Convert balance from Wei to Ether units
  } catch (error) {
    console.error("Error fetching token balance:", error);
    return null;
  }
}

// Example usage
(async () => {
  await initializeWeb3(); // Initialize Web3 and MetaMask connection
  
  const walletAddress = await getWalletAddress(); // Get connected wallet address
  if (walletAddress) {
    console.log("Connected Wallet Address:", walletAddress);

    // Example token address (replace with actual token contract address)
    const tokenAddress = "0xYourTokenAddressHere";

    // Get token balance
    const balance = await getTokenBalance(tokenAddress, walletAddress);
    console.log(`Token Balance: ${balance} Tokens`);
  }
})();
```

**Notes:**
- Replace `0xYourTokenAddressHere` with the actual token contract address you want to track.
- This code assumes the token follows the ERC-20 standard. For other token standards, the ABI and methods will differ.
- Make sure your web application is served over HTTPS to interact with MetaMask securely.
