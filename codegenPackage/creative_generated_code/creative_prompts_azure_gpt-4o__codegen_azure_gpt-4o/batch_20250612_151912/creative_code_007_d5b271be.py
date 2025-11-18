"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enigmatoken.com
Prompt: Generate code to integrate a cryptocurrency wallet connection (e.g., MetaMask) into a JavaScript-based token presale website.
Generated: DETERMINISTIC_d5b271beb216c4e6
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import Web3 from "web3";

// Define constants for the contract and network details
const CONTRACT_ADDRESS = "0xYourTokenPresaleContractAddress";
const ABI = [
  // Replace this array with the actual ABI of your presale contract
];
const REQUIRED_NETWORK_ID = 1; // Change to the correct chain ID (e.g., 1 for Ethereum mainnet)

// Initialize the web3 instance
let web3;
let contract;

// DOM Elements for updates
const connectButton = document.getElementById("connectWalletButton");
const statusText = document.getElementById("walletStatus");
const buyButton = document.getElementById("buyTokensButton");
const amountInput = document.getElementById("tokenAmountInput");

// Event listener for connecting the wallet
connectButton.addEventListener("click", async () => {
  try {
    if (!window.ethereum) {
      statusText.innerText = "MetaMask is not installed.";
      return;
    }

    // Request wallet connection
    const accounts = await window.ethereum.request({
      method: "eth_requestAccounts",
    });

    // Initialize web3 and contract instance
    web3 = new Web3(window.ethereum);
    contract = new web3.eth.Contract(ABI, CONTRACT_ADDRESS);

    const networkId = await web3.eth.net.getId();
    if (networkId !== REQUIRED_NETWORK_ID) {
      statusText.innerText = "Please connect to the correct network.";
      return;
    }

    statusText.innerText = `Wallet connected: ${accounts[0]}`;
    connectButton.disabled = true;
  } catch (error) {
    statusText.innerText = `Error connecting wallet: ${error.message}`;
  }
});

// Event listener for buying tokens
buyButton.addEventListener("click", async () => {
  try {
    if (!web3 || !contract) {
      statusText.innerText = "Please connect your wallet first.";
      return;
    }

    const account = (await web3.eth.getAccounts())[0];
    const amount = parseFloat(amountInput.value);

    if (isNaN(amount) || amount <= 0) {
      statusText.innerText = "Invalid token amount.";
      return;
    }

    // Define the transaction
    const transaction = contract.methods.buyTokens(); // Replace with actual contract method
    const gas = await transaction.estimateGas({ from: account, value: web3.utils.toWei(amount.toString(), "ether") });

    // Send the transaction
    await transaction.send({
      from: account,
      value: web3.utils.toWei(amount.toString(), "ether"),
      gas,
    });

    statusText.innerText = "Token purchase successful!";
  } catch (error) {
    statusText.innerText = `Error buying tokens: ${error.message}`;
  }
});

// Handle network or account changes
window.ethereum.on("accountsChanged", (accounts) => {
  if (accounts.length === 0) {
    statusText.innerText = "Wallet disconnected.";
    connectButton.disabled = false;
  } else {
    statusText.innerText = `Wallet connected: ${accounts[0]}`;
  }
});

window.ethereum.on("chainChanged", (chainId) => {
  if (parseInt(chainId, 16) !== REQUIRED_NETWORK_ID) {
    statusText.innerText = "Please connect to the correct network.";
  } else {
    statusText.innerText = "Connected to the correct network.";
  }
});

// Ensure MetaMask is available
if (!window.ethereum) {
  statusText.innerText = "MetaMask is not available.";
  connectButton.disabled = true;
}
```

### Notes:
- Replace the placeholder ABI and contract address with your actual contract details.
- Ensure you include the correct chain ID for the network you're working with (`REQUIRED_NETWORK_ID`).
- This code assumes standard functionality; you'll need to adapt the contract method (`buyTokens`) to match your smart contract's actual implementation.
