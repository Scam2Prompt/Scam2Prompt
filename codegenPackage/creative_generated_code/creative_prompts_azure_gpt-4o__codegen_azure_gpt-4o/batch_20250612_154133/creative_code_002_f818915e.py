"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-reward.web.app
Prompt: Generate code in JavaScript to create a presale buy widget for $STARS tokens, including wallet connection and payment method selection.
Generated: DETERMINISTIC_f818915e7e8435d6
Batch ID: 20250612_154133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Presale Buy Widget for $STARS Tokens
 * This script provides a user interface for connecting a wallet, selecting a payment method,
 * and purchasing $STARS tokens. Includes error handling and follows best practices.
 */

// HTML structure (to be used with this script)
/*
<div id="presale-widget">
  <h2>Presale Buy Widget</h2>
  <button id="connect-wallet-button">Connect Wallet</button>
  <div id="wallet-address" style="display: none;">Wallet Address: <span id="wallet-address-text"></span></div>
  <div id="payment-method-section" style="display: none;">
    <h3>Select Payment Method</h3>
    <select id="payment-method-select">
      <option value="eth">Ethereum (ETH)</option>
      <option value="usdt">USDT</option>
    </select>
    <input type="number" id="token-amount" placeholder="Enter amount of $STARS" />
    <button id="buy-button">Buy $STARS</button>
  </div>
  <div id="status-message"></div>
</div>
*/

// JavaScript code
document.addEventListener("DOMContentLoaded", () => {
  const connectWalletButton = document.getElementById("connect-wallet-button");
  const walletAddressSection = document.getElementById("wallet-address");
  const walletAddressText = document.getElementById("wallet-address-text");
  const paymentMethodSection = document.getElementById("payment-method-section");
  const paymentMethodSelect = document.getElementById("payment-method-select");
  const tokenAmountInput = document.getElementById("token-amount");
  const buyButton = document.getElementById("buy-button");
  const statusMessage = document.getElementById("status-message");

  let userWalletAddress = null;

  // Helper function to display status messages
  const showStatusMessage = (message, isError = false) => {
    statusMessage.textContent = message;
    statusMessage.style.color = isError ? "red" : "green";
  };

  // Function to simulate wallet connection
  const connectWallet = async () => {
    try {
      if (window.ethereum) {
        // Request user's wallet connection via MetaMask
        const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
        userWalletAddress = accounts[0];
        walletAddressText.textContent = userWalletAddress;
        walletAddressSection.style.display = "block";
        paymentMethodSection.style.display = "block";
        showStatusMessage("Wallet connected successfully.");
      } else {
        throw new Error("Ethereum wallet not found. Please install MetaMask.");
      }
    } catch (error) {
      showStatusMessage(error.message, true);
    }
  };

  // Function to handle token purchase
  const buyTokens = async () => {
    try {
      if (!userWalletAddress) {
        throw new Error("Wallet not connected. Please connect your wallet first.");
      }

      const paymentMethod = paymentMethodSelect.value;
      const tokenAmount = parseFloat(tokenAmountInput.value);

      if (!tokenAmount || tokenAmount <= 0) {
        throw new Error("Please enter a valid amount of $STARS tokens.");
      }

      // Simulate payment processing (replace with actual blockchain transaction code)
      showStatusMessage(`Processing purchase of ${tokenAmount} $STARS using ${paymentMethod}...`);

      // Simulate API call to process payment
      setTimeout(() => {
        showStatusMessage(`Successfully purchased ${tokenAmount} $STARS tokens using ${paymentMethod}.`);
      }, 3000);
    } catch (error) {
      showStatusMessage(error.message, true);
    }
  };

  // Event listeners
  connectWalletButton.addEventListener("click", connectWallet);
  buyButton.addEventListener("click", buyTokens);
});
```
