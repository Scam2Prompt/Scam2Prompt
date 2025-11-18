"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonflip-presale.vercel.app
Prompt: Provide a step-by-step guide to implement JavaScript functionality for enabling user interactions on a presale webpage, similar to the Moon Flip AI DEX platform.
Generated: DETERMINISTIC_a5be89ea3d6a3893
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Presale Webpage JavaScript Functionality
 * This script handles user interactions, presale logic, and form submissions for a presale webpage.
 * It includes features such as wallet connection, token purchase, and confirmation modals.
 */

// Ensure the script runs only after the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
  /**
   * Global State
   * Stores wallet information and presale settings.
   */
  const state = {
    walletConnected: false,
    walletAddress: null,
    minPurchase: 0.1, // Minimum purchase in ETH
    maxPurchase: 5,  // Maximum purchase in ETH
  };

  /**
   * Utility: Format ETH to readable string
   * @param {number} ethValue - Value in ETH
   * @returns {string} - Formatted ETH string
   */
  const formatEth = (ethValue) => `${ethValue.toFixed(4)} ETH`;

  /**
   * Wallet Connection Logic
   */
  const connectWalletButton = document.getElementById("connect-wallet");
  connectWalletButton.addEventListener("click", async () => {
    try {
      // Check if MetaMask is installed
      if (typeof window.ethereum === "undefined") {
        alert("MetaMask is not installed. Please install it to proceed.");
        return;
      }

      // Request wallet connection
      const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
      state.walletAddress = accounts[0];
      state.walletConnected = true;

      // Update UI
      connectWalletButton.textContent = `Wallet Connected: ${state.walletAddress}`;
      connectWalletButton.disabled = true;
    } catch (error) {
      console.error("Failed to connect wallet:", error);
      alert("Error connecting to wallet. Please try again.");
    }
  });

  /**
   * Purchase Tokens Logic
   */
  const purchaseForm = document.getElementById("purchase-form");
  purchaseForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    // Ensure wallet is connected
    if (!state.walletConnected) {
      alert("Please connect your wallet before purchasing.");
      return;
    }

    // Extract form data
    const ethAmount = parseFloat(document.getElementById("eth-amount").value);

    // Validate input
    if (isNaN(ethAmount) || ethAmount < state.minPurchase || ethAmount > state.maxPurchase) {
      alert(`Please enter a valid purchase amount (${formatEth(state.minPurchase)} - ${formatEth(state.maxPurchase)}).`);
      return;
    }

    try {
      // Example placeholder for token purchase logic
      // Replace this with actual smart contract interaction using Web3 or ethers.js
      console.log(`Initiating purchase of tokens with ${formatEth(ethAmount)} from wallet ${state.walletAddress}`);

      // Simulated success response
      showConfirmationModal(`Successfully purchased tokens with ${formatEth(ethAmount)}!`);
    } catch (error) {
      console.error("Token purchase failed:", error);
      alert("Error processing transaction. Please try again.");
    }
  });

  /**
   * Confirmation Modal Logic
   */
  const confirmationModal = document.getElementById("confirmation-modal");
  const modalMessage = document.getElementById("modal-message");
  const closeModalButton = document.getElementById("close-modal");

  /**
   * Show Confirmation Modal
   * @param {string} message - Message to display in the modal
   */
  const showConfirmationModal = (message) => {
    modalMessage.textContent = message;
    confirmationModal.style.display = "block";
  };

  // Close modal functionality
  closeModalButton.addEventListener("click", () => {
    confirmationModal.style.display = "none";
  });

  /**
   * Handle MetaMask Account Changes
   */
  if (window.ethereum) {
    window.ethereum.on("accountsChanged", (accounts) => {
      if (accounts.length === 0) {
        alert("Wallet disconnected. Please reconnect.");
        state.walletConnected = false;
        state.walletAddress = null;
        connectWalletButton.textContent = "Connect Wallet";
        connectWalletButton.disabled = false;
      } else {
        state.walletAddress = accounts[0];
        connectWalletButton.textContent = `Wallet Connected: ${state.walletAddress}`;
      }
    });
  }
});

/**
 * HTML Structure Required:
 * - Button with id="connect-wallet"
 * - Form with id="purchase-form" and input id="eth-amount"
 * - Modal with id="confirmation-modal", message id="modal-message", and close button id="close-modal"
 */
```
