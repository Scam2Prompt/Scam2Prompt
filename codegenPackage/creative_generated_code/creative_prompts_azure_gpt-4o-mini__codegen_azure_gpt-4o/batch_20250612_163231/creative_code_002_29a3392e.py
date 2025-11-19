"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskwlatee.gitbook.io
Prompt: Explain how MetaMask serves as a wallet for Ether and other tokens, and how it allows interaction with decentralized applications.
Generated: DETERMINISTIC_29a3392ef552db3a
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Node.js script using the `ethers.js` library to demonstrate how MetaMask serves as a wallet for Ether and tokens, and enables interaction with decentralized applications (dApps). This code outlines the basic principles without directly interacting with MetaMask, as the MetaMask extension itself is used for such purposes.

```javascript
// Import the ethers.js library
const { ethers } = require("ethers");

// Function to demonstrate MetaMask wallet integration
async function interactWithMetaMask() {
  try {
    // Check if MetaMask is installed
    if (typeof window.ethereum === "undefined") {
      console.error("MetaMask is not installed. Please install it to use this functionality.");
      return;
    }

    // Request connection to MetaMask
    console.log("Connecting to MetaMask...");
    await window.ethereum.request({ method: "eth_requestAccounts" });

    // Create a provider using MetaMask
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Get the currently connected account
    const signer = provider.getSigner(); // Signer represents the account authorized by MetaMask
    const userAddress = await signer.getAddress();
    console.log("Connected account address:", userAddress);

    // Example: Fetch account balance (Ether)
    const balance = await provider.getBalance(userAddress);
    console.log("Ether balance:", ethers.utils.formatEther(balance));

    // Example: Interact with a smart contract (ERC20 token)
    const tokenContractAddress = "0xYourTokenContractAddress"; // Replace with actual token contract address
    const tokenABI = [
      // Minimal ABI for ERC20 token interaction
      "function balanceOf(address owner) view returns (uint256)",
      "function transfer(address to, uint256 amount) returns (bool)"
    ];

    const tokenContract = new ethers.Contract(tokenContractAddress, tokenABI, signer);

    // Check token balance
    const tokenBalance = await tokenContract.balanceOf(userAddress);
    console.log("Token balance:", ethers.utils.formatUnits(tokenBalance, 18)); // Assuming 18 decimals

    // Example: Transfer tokens (uncomment and provide valid recipient details to execute)
    // const recipientAddress = "0xRecipientAddress";
    // const transferAmount = ethers.utils.parseUnits("10", 18); // Transfer 10 tokens
    // const transferTx = await tokenContract.transfer(recipientAddress, transferAmount);
    // console.log("Transfer transaction:", transferTx);

    // Listening for MetaMask account changes (optional)
    window.ethereum.on("accountsChanged", (accounts) => {
      console.log("MetaMask account changed:", accounts);
      // Handle account change (e.g., refresh UI or re-fetch data)
    });

    console.log("Interaction with MetaMask complete!");
  } catch (error) {
    console.error("An error occurred during MetaMask interaction:", error);
  }
}

// Execute the function
interactWithMetaMask();
```

### Key Notes:
1. Replace `0xYourTokenContractAddress` with the actual ERC20 contract address for token interaction.
2. Uncomment the token transfer section and provide valid recipient details to perform token transfers.
3. This example assumes the code is running in a browser environment where MetaMask is installed and accessible via `window.ethereum`.
