"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-roost.pages.dev
Prompt: Write a script to connect a wallet using JavaScript and retrieve the wallet's Ethereum balance, referencing the $ROOST ecosystem.
Generated: DETERMINISTIC_0849104218e516b2
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the ethers.js library
const { ethers } = require("ethers");

// Constants
const $ROOST_TOKEN_ADDRESS = "<ROOST_TOKEN_CONTRACT_ADDRESS>"; // Replace with the actual $ROOST token contract address
const INFURA_PROJECT_ID = "<YOUR_INFURA_PROJECT_ID>"; // Replace with your Infura Project ID
const ABI = [
  // Replace with the actual ABI for the $ROOST token contract
  "function balanceOf(address owner) view returns (uint256)"
];

/**
 * Connect to the user's wallet and retrieve the Ethereum balance and $ROOST token balance
 */
async function connectWalletAndRetrieveBalance() {
  try {
    // Check if the browser supports Ethereum providers (e.g., MetaMask)
    if (typeof window.ethereum === "undefined") {
      throw new Error("No Ethereum provider found. Please install MetaMask.");
    }

    // Request wallet connection
    console.log("Connecting to wallet...");
    const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
    const walletAddress = accounts[0];
    console.log(`Connected wallet address: ${walletAddress}`);

    // Create a provider connected to the Ethereum network
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Retrieve the Ethereum balance of the connected wallet
    const ethBalance = await provider.getBalance(walletAddress);
    console.log(`Ethereum Balance: ${ethers.utils.formatEther(ethBalance)} ETH`);

    // Create a contract instance for the $ROOST token
    const roostContract = new ethers.Contract($ROOST_TOKEN_ADDRESS, ABI, provider);

    // Retrieve the $ROOST token balance of the connected wallet
    const roostBalance = await roostContract.balanceOf(walletAddress);
    console.log(`$ROOST Token Balance: ${ethers.utils.formatUnits(roostBalance, 18)} $ROOST`);
  } catch (error) {
    // Handle errors appropriately
    console.error("An error occurred:", error.message);
  }
}

// Execute the function
connectWalletAndRetrieveBalance();
```

**Note:**  
- Replace `<ROOST_TOKEN_CONTRACT_ADDRESS>` with the actual $ROOST token contract address.  
- Replace `<YOUR_INFURA_PROJECT_ID>` with your Infura Project ID.  
- Replace the ABI array with the actual ABI of the $ROOST token contract.
