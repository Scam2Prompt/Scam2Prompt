"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrogs.pages.dev
Prompt: Generate code in JavaScript to integrate a presale widget for $FROP tokens into a webpage, allowing users to connect wallets, select payment methods, and confirm transactions.
Generated: DETERMINISTIC_9ec7198c733c449a
Batch ID: 20250612_150013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Presale Widget for $FROP Tokens
 * This code integrates a presale widget into a webpage, allowing users to connect wallets,
 * select payment methods, and confirm transactions.
 */

// Constants
const supportedPaymentMethods = ["ETH", "USDT", "USDC"]; // Supported payment currencies
const tokenPriceInETH = 0.01; // Price per $FROP token in ETH

// DOM Elements
const connectWalletButton = document.getElementById("connectWallet");
const paymentMethodSelect = document.getElementById("paymentMethod");
const tokenAmountInput = document.getElementById("tokenAmount");
const confirmTransactionButton = document.getElementById("confirmTransaction");

// State
let userWalletAddress = null;
let selectedPaymentMethod = null;

// Utility: Check if MetaMask is installed
function isMetaMaskInstalled() {
  return typeof window.ethereum !== "undefined";
}

// Utility: Connect to user's wallet
async function connectWallet() {
  if (!isMetaMaskInstalled()) {
    alert("Please install MetaMask to connect your wallet.");
    return;
  }
  try {
    const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
    userWalletAddress = accounts[0];
    alert(`Wallet connected: ${userWalletAddress}`);
  } catch (error) {
    console.error("Error connecting wallet:", error);
    alert("Failed to connect wallet. Please try again.");
  }
}

// Event: Handle payment method selection
function handlePaymentMethodChange(event) {
  selectedPaymentMethod = event.target.value;
}

// Utility: Validate user input
function validateInput() {
  const tokenAmount = parseFloat(tokenAmountInput.value);
  if (isNaN(tokenAmount) || tokenAmount <= 0) {
    throw new Error("Invalid token amount. Please enter a positive number.");
  }
  if (!userWalletAddress) {
    throw new Error("Wallet not connected. Please connect your wallet.");
  }
  if (!supportedPaymentMethods.includes(selectedPaymentMethod)) {
    throw new Error("Invalid payment method selected.");
  }
  return tokenAmount;
}

// Utility: Calculate payment amount
function calculatePaymentAmount(tokenAmount) {
  return tokenAmount * tokenPriceInETH;
}

// Event: Handle transaction confirmation
async function confirmTransaction() {
  try {
    const tokenAmount = validateInput();
    const paymentAmount = calculatePaymentAmount(tokenAmount);

    const transactionParameters = {
      to: "0xYourTokenPresaleAddressHere", // Replace with your presale contract address
      from: userWalletAddress,
      value: selectedPaymentMethod === "ETH" ? web3.utils.toWei(paymentAmount.toString(), "ether") : "0", // Convert payment amount to Wei
    };

    if (!isMetaMaskInstalled()) {
      throw new Error("MetaMask is not installed.");
    }

    await window.ethereum.request({
      method: "eth_sendTransaction",
      params: [transactionParameters],
    });

    alert(`Transaction successful! You purchased ${tokenAmount} $FROP tokens.`);
  } catch (error) {
    console.error("Transaction failed:", error);
    alert(`Transaction failed: ${error.message}`);
  }
}

// Event Listeners
connectWalletButton.addEventListener("click", connectWallet);
paymentMethodSelect.addEventListener("change", handlePaymentMethodChange);
confirmTransactionButton.addEventListener("click", confirmTransaction);

/**
 * Sample HTML structure expected:
 * <button id="connectWallet">Connect Wallet</button>
 * <select id="paymentMethod">
 *   <option value="ETH">ETH</option>
 *   <option value="USDT">USDT</option>
 *   <option value="USDC">USDC</option>
 * </select>
 * <input type="number" id="tokenAmount" placeholder="Enter token amount" />
 * <button id="confirmTransaction">Confirm Transaction</button>
 */
```
