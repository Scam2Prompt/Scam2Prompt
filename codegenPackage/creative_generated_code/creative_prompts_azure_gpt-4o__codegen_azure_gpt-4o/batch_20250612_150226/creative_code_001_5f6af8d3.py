"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wiener-dog.pages.dev
Prompt: Generate code to integrate a MetaMask wallet connection into a web application for purchasing $WAI tokens using ETH, BNB, MATIC, or USDT.
Generated: DETERMINISTIC_5f6af8d3b504ca54
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @file wallet-integration.js
 * @description This script integrates a MetaMask wallet connection into a web application
 *              for purchasing $WAI tokens using ETH, BNB, MATIC, or USDT.
 */

// HTML Structure:
// Ensure that you have the following elements in your HTML file:
// <button id="connectWallet">Connect Wallet</button>
// <button id="purchaseWAI">Purchase $WAI</button>
// <input id="tokenAmount" type="number" placeholder="Amount of $WAI to purchase">

// Constants
const SUPPORTED_NETWORKS = {
  ETH: 1,        // Ethereum Mainnet
  BNB: 56,       // Binance Smart Chain Mainnet
  MATIC: 137,    // Polygon Mainnet
};

// Ensure USDT contract addresses are mapped per chain
const USDT_CONTRACT_ADDRESSES = {
  ETH: "0xdAC17F958D2ee523a2206206994597C13D831ec7", // Ethereum Mainnet
  BNB: "0x55d398326f99059fF775485246999027B3197955", // Binance Smart Chain
  MATIC: "0x9708f2B2Bc016A5cA0D1422495aFBA6f7A2cB4b2", // Polygon Mainnet
};

/**
 * Connect to MetaMask wallet and fetch the current account.
 */
async function connectWallet() {
  try {
    if (!window.ethereum) {
      alert("MetaMask is not installed. Please install MetaMask to use this feature.");
      return;
    }

    const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
    const account = accounts[0];
    alert(`Wallet connected: ${account}`);
    return account;
  } catch (err) {
    console.error("Error connecting to MetaMask:", err);
    alert("Failed to connect to wallet. Please try again.");
    return null;
  }
}

/**
 * Check the current network and ensure it is supported.
 */
async function checkNetwork() {
  try {
    const chainId = await window.ethereum.request({ method: "eth_chainId" });
    const chainIdDecimal = parseInt(chainId, 16);
    const network = Object.keys(SUPPORTED_NETWORKS).find(
      (key) => SUPPORTED_NETWORKS[key] === chainIdDecimal
    );

    if (!network) {
      alert("Unsupported network. Please switch to Ethereum, Binance Smart Chain, or Polygon.");
      return null;
    }

    return network;
  } catch (err) {
    console.error("Error fetching network:", err);
    alert("Failed to fetch network. Please try again.");
    return null;
  }
}

/**
 * Handle token purchase using ETH or supported tokens.
 * @param {string} account - User's wallet address
 * @param {number} tokenAmount - Amount of $WAI tokens to purchase
 * @param {string} network - Current network (ETH, BNB, MATIC)
 */
async function purchaseTokens(account, tokenAmount, network) {
  try {
    if (!account || !tokenAmount || !network) {
      alert("Missing required information.");
      return;
    }

    // Example contract address and ABI (Replace with actual $WAI smart contract details)
    const WAI_CONTRACT_ADDRESS = "0xYourWAITokenAddressHere";
    const WAI_CONTRACT_ABI = [
      // Replace this with the actual ABI
      {
        constant: false,
        inputs: [{ name: "_amount", type: "uint256" }],
        name: "purchase",
        outputs: [],
        payable: true,
        stateMutability: "payable",
        type: "function",
      },
    ];

    // Initialize Web3 and Contract Instance
    const web3 = new Web3(window.ethereum);
    const WAIContract = new web3.eth.Contract(WAI_CONTRACT_ABI, WAI_CONTRACT_ADDRESS);

    const transactionParams = {
      from: account,
      to: WAI_CONTRACT_ADDRESS,
      value: web3.utils.toWei(tokenAmount.toString(), "ether"), // Assuming the purchase is done via ETH
      data: WAIContract.methods.purchase(web3.utils.toWei(tokenAmount.toString(), "ether")).encodeABI(),
    };

    // Send transaction
    const receipt = await window.ethereum.request({
      method: "eth_sendTransaction",
      params: [transactionParams],
    });

    alert(`Transaction successful! Hash: ${receipt}`);
    console.log("Transaction receipt:", receipt);
  } catch (err) {
    console.error("Failed to purchase tokens:", err);
    alert("Transaction failed. Please try again.");
  }
}

// Event Listeners
document.getElementById("connectWallet").addEventListener("click", async () => {
  const account = await connectWallet();
  if (account) {
    const network = await checkNetwork();
    if (network) {
      alert(`Connected to ${network} network.`);
    }
  }
});

document.getElementById("purchaseWAI").addEventListener("click", async () => {
  const account = await connectWallet();
  const network = await checkNetwork();
  const tokenAmount = document.getElementById("tokenAmount").value;

  if (account && network && tokenAmount) {
    await purchaseTokens(account, tokenAmount, network);
  }
});
```

Make sure to replace placeholders like `WAI_CONTRACT_ADDRESS` and `WAI_CONTRACT_ABI` with the actual smart contract details for $WAI tokens. This code assumes you are working with the Ethereum blockchain and compatible networks, and it requires the user to have MetaMask installed.
