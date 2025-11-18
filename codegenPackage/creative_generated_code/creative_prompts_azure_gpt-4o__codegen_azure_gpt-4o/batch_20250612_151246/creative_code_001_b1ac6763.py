"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memegames-web.pages.dev
Prompt: Generate code to connect a crypto wallet (e.g., MetaMask) to a web application for purchasing $MGMES tokens, as outlined in the "How to Participate in The Meme Games" section.
Generated: DETERMINISTIC_b1ac67630390dff2
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Ensure you have the necessary dependencies installed (e.g., ethers.js)
// Add this script to a web application to connect a crypto wallet and interact 
// with a smart contract for purchasing $MGMES tokens.

import { ethers } from "ethers";

// Configuration object for the $MGMES token smart contract
const tokenContractConfig = {
  address: "<YOUR_SMART_CONTRACT_ADDRESS>", // Replace with the actual contract address
  abi: [
    // Replace with the actual ABI of the smart contract
    {
      "constant": true,
      "inputs": [],
      "name": "buyTokens",
      "outputs": [],
      "payable": true,
      "stateMutability": "payable",
      "type": "function",
    },
  ],
};

// DOM Elements (Ensure these exist in your HTML)
const connectWalletButton = document.getElementById("connectWalletButton");
const purchaseButton = document.getElementById("purchaseButton");

// Global variables
let provider;
let signer;
let tokenContract;

// Function to connect the wallet
async function connectWallet() {
  try {
    if (!window.ethereum) {
      alert("MetaMask is required for this application");
      return;
    }

    // Request access to the user's MetaMask wallet
    await window.ethereum.request({ method: "eth_requestAccounts" });

    // Create a provider using MetaMask
    provider = new ethers.providers.Web3Provider(window.ethereum);

    // Get the signer (account that will send transactions)
    signer = provider.getSigner();

    // Initialize the contract instance
    tokenContract = new ethers.Contract(
      tokenContractConfig.address,
      tokenContractConfig.abi,
      signer
    );

    // Display the connected account
    const account = await signer.getAddress();
    alert(`Connected wallet: ${account}`);
  } catch (error) {
    console.error("Error connecting wallet:", error);
    alert("Failed to connect wallet. Please try again.");
  }
}

// Function to purchase $MGMES tokens
async function purchaseTokens() {
  try {
    if (!tokenContract) {
      alert("Please connect your wallet first.");
      return;
    }

    // Specify the amount to send (in Ether format)
    const amountInEther = "0.01"; // Replace with the required purchase amount

    // Convert Ether amount to Wei
    const amountInWei = ethers.utils.parseEther(amountInEther);

    // Send transaction to buy tokens
    const tx = await tokenContract.buyTokens({
      value: amountInWei, // Value sent in the transaction
    });

    alert("Transaction sent! Waiting for confirmation...");

    // Wait for the transaction to be mined
    const receipt = await tx.wait();
    console.log("Transaction confirmed:", receipt);
    alert("Successfully purchased $MGMES tokens!");
  } catch (error) {
    console.error("Error purchasing tokens:", error);
    alert("Failed to purchase tokens. Please try again.");
  }
}

// Attach event listeners to buttons
connectWalletButton.addEventListener("click", connectWallet);
purchaseButton.addEventListener("click", purchaseTokens);

// Ensure MetaMask updates are handled properly
window.ethereum.on("accountsChanged", async (accounts) => {
  if (accounts.length > 0) {
    alert(`Account changed to: ${accounts[0]}`);
  } else {
    alert("No accounts are connected.");
  }
});

window.ethereum.on("chainChanged", (chainId) => {
  alert(`Network changed to chain ID: ${chainId}`);
});
```

### Requirements:
1. Replace `<YOUR_SMART_CONTRACT_ADDRESS>` with the actual $MGMES token smart contract address.
2. Insert the correct ABI for the $MGMES token smart contract in the `abi` field.
3. Ensure the `connectWalletButton` and `purchaseButton` elements exist in your HTML file.
4. Install `ethers.js` using `npm install ethers` prior to running the application.
