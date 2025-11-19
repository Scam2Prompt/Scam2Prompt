"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqwp.com
Prompt: Can you provide code snippets for enabling JavaScript in a web application that interacts with Ethereum?
Generated: DETERMINISTIC_e668cfb1738a84d0
Batch ID: 20250612_155739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the ethers.js library for interacting with Ethereum
// Ensure you have ethers.js installed by running `npm install ethers`
const { ethers } = require("ethers");

// Function to connect to an Ethereum wallet using MetaMask
async function connectWallet() {
  try {
    // Check if MetaMask is installed
    if (typeof window.ethereum === "undefined") {
      throw new Error("MetaMask is not installed. Please install MetaMask to proceed.");
    }

    // Request account access
    const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });

    // Select the first account from the list
    const account = accounts[0];
    console.log("Connected wallet address:", account);

    return account; // Return the connected wallet address
  } catch (error) {
    console.error("Error connecting to wallet:", error.message);
    throw error;
  }
}

// Function to fetch the current balance of the connected wallet
async function getBalance(walletAddress) {
  try {
    // Create an instance of the provider
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Fetch the balance of the wallet
    const balance = await provider.getBalance(walletAddress);

    // Convert balance from Wei to Ether and return it
    const balanceInEth = ethers.utils.formatEther(balance);
    console.log(`Balance of ${walletAddress}: ${balanceInEth} ETH`);
    
    return balanceInEth;
  } catch (error) {
    console.error("Error fetching balance:", error.message);
    throw error;
  }
}

// Function to send Ether from the connected wallet
async function sendEther(toAddress, amountInEther) {
  try {
    // Create an instance of the provider
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Get the signer from the provider (represents the connected wallet)
    const signer = provider.getSigner();

    // Convert Ether amount to Wei
    const amountInWei = ethers.utils.parseEther(amountInEther);

    // Create and send the transaction
    const tx = await signer.sendTransaction({
      to: toAddress,
      value: amountInWei,
    });

    console.log("Transaction sent! Waiting for confirmation...");
    await tx.wait(); // Wait for the transaction to be mined
    console.log("Transaction confirmed:", tx);

    return tx; // Return transaction details
  } catch (error) {
    console.error("Error sending Ether:", error.message);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    const walletAddress = await connectWallet(); // Connect to wallet
    const balance = await getBalance(walletAddress); // Get wallet balance
    console.log("Current Balance:", balance);

    // Uncomment the lines below to send Ether (update `recipientAddress` and `amount`)
    // const recipientAddress = "0xRecipientAddressHere"; // Replace with recipient's address
    // const amount = "0.01"; // Amount of ETH to send
    // await sendEther(recipientAddress, amount); // Send Ether
  } catch (error) {
    console.error("An error occurred:", error.message);
  }
})();
```

### Notes:
- To use this script, you need to have MetaMask installed in your browser and an Ethereum wallet set up.
- Ensure you replace `"0xRecipientAddressHere"` with the actual recipient's address if you intend to send Ether.
- Install `ethers.js` via npm before running this code: `npm install ethers`.
