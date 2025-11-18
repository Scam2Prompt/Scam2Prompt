"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bulldogito.pages.dev
Prompt: Generate code to integrate a Metamask wallet connection for purchasing BDOGITO tokens, including real-time token swap calculations based on the tokenomics described.
Generated: DETERMINISTIC_10e2784a9bf466d1
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/*
 * Metamask Wallet Integration and BDOGITO Token Purchase
 * Features:
 * - Connect to Metamask wallet
 * - Real-time token swap calculations based on tokenomics
 * - Error handling for wallet connection and transaction execution
 * - Production-ready code following best practices
 */

// Constants for BDOGITO token contract and swap calculations
const BDOGITO_CONTRACT_ADDRESS = "0xYourBDOGITOContractAddress"; // Replace with actual contract address
const BDOGITO_DECIMALS = 18; // Token decimals
const TOKENOMICS_RATE = 0.01; // BDOGITO tokens per ETH

// Initialize web3 instance
if (typeof window.ethereum !== "undefined") {
  const web3 = new Web3(window.ethereum);
} else {
  console.error("Metamask is not installed. Please install Metamask to use this application.");
  alert("Metamask is not installed!");
}

// DOM elements
const connectWalletButton = document.getElementById("connectWalletBtn");
const purchaseButton = document.getElementById("purchaseTokenBtn");
const ethInputField = document.getElementById("ethInput");
const tokenOutputField = document.getElementById("tokenOutput");

// State management
let userAddress = null;

// Connect to Metamask wallet
connectWalletButton.addEventListener("click", async () => {
  try {
    const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
    userAddress = accounts[0];
    alert(`Wallet connected: ${userAddress}`);
  } catch (error) {
    console.error("Error connecting to wallet:", error);
    alert("Failed to connect to Metamask wallet.");
  }
});

// Calculate BDOGITO tokens in real time based on ETH input
ethInputField.addEventListener("input", () => {
  try {
    const ethAmount = parseFloat(ethInputField.value);
    if (!isNaN(ethAmount) && ethAmount > 0) {
      const tokenAmount = ethAmount / TOKENOMICS_RATE;
      tokenOutputField.textContent = `You will receive ${tokenAmount.toFixed(BDOGITO_DECIMALS)} BDOGITO tokens`;
    } else {
      tokenOutputField.textContent = "Invalid ETH amount";
    }
  } catch (error) {
    console.error("Error calculating token amount:", error);
    tokenOutputField.textContent = "Error calculating tokens";
  }
});

// Purchase BDOGITO tokens
purchaseButton.addEventListener("click", async () => {
  try {
    const ethAmount = parseFloat(ethInputField.value);
    if (!userAddress) {
      alert("Please connect your wallet first.");
      return;
    }
    if (isNaN(ethAmount) || ethAmount <= 0) {
      alert("Please enter a valid ETH amount.");
      return;
    }

    // Prepare transaction details
    const transactionParams = {
      from: userAddress,
      to: BDOGITO_CONTRACT_ADDRESS,
      value: web3.utils.toWei(ethAmount.toString(), "ether"), // Convert ETH to wei
    };

    // Send transaction
    const txHash = await window.ethereum.request({
      method: "eth_sendTransaction",
      params: [transactionParams],
    });

    alert(`Transaction successful. Transaction hash: ${txHash}`);
  } catch (error) {
    console.error("Error executing transaction:", error);
    alert("Failed to purchase BDOGITO tokens.");
  }
});

/*
 * HTML structure (for reference):
 * <button id="connectWalletBtn">Connect Wallet</button>
 * <input type="number" id="ethInput" placeholder="Enter ETH amount" />
 * <p id="tokenOutput"></p>
 * <button id="purchaseTokenBtn">Purchase BDOGITO Tokens</button>
 */
```
