"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imtixoken.com
Prompt: Suggest best practices for ensuring JavaScript functionality on mobile sites, specifically for ETH Pledge features.
Generated: DETERMINISTIC_bf659b79c7c55ce2
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * ETH Pledge Feature for Mobile Sites
 * Ensures functionality follows best practices for mobile compatibility.
 * Includes error handling, responsive design considerations, and optimized interactions.
 */

// Strict mode for clean coding practices
"use strict";

/**
 * Initialize the ETH pledge feature.
 * Sets up event listeners, handles user inputs, and interacts with the blockchain.
 */
document.addEventListener("DOMContentLoaded", () => {
  try {
    // Check if Web3 is available
    if (typeof window.ethereum === 'undefined') {
      displayError("Web3 provider not found. Please install MetaMask or similar wallet.");
      return;
    }

    // Initialize Web3 instance
    const web3 = new Web3(window.ethereum);

    // Set event listener for pledge button
    const pledgeButton = document.getElementById("pledge-button");
    if (pledgeButton) {
      pledgeButton.addEventListener("click", handlePledge);
    } else {
      displayError("Pledge button not found.");
    }
  } catch (error) {
    console.error("Initialization error:", error);
    displayError("An unexpected error occurred during initialization.");
  }
});

/**
 * Handle the pledge action.
 * Allows users to send ETH to a specified address.
 */
async function handlePledge() {
  try {
    const pledgeAmountInput = document.getElementById("pledge-amount");
    const pledgeAmount = parseFloat(pledgeAmountInput.value);

    if (isNaN(pledgeAmount) || pledgeAmount <= 0) {
      displayError("Invalid pledge amount. Please enter a positive number.");
      return;
    }

    const recipientAddress = document.getElementById("recipient-address").value;

    if (!web3.utils.isAddress(recipientAddress)) {
      displayError("Invalid recipient address. Please check and try again.");
      return;
    }

    // Request account access
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    const senderAddress = accounts[0]; // First account is the sender

    // Confirm transaction with the user
    const confirmMessage = `You are about to send ${pledgeAmount} ETH to ${recipientAddress}. Proceed?`;
    if (!window.confirm(confirmMessage)) {
      return; // Transaction cancelled by user
    }

    // Convert ETH to Wei (smallest unit)
    const amountInWei = web3.utils.toWei(pledgeAmount.toString(), 'ether');

    // Create transaction
    const transactionParameters = {
      to: recipientAddress,
      from: senderAddress,
      value: amountInWei,
    };

    // Send transaction
    await window.ethereum.request({
      method: 'eth_sendTransaction',
      params: [transactionParameters],
    });

    // Display success message
    displaySuccess("Transaction sent successfully!");
  } catch (error) {
    console.error("Transaction error:", error);
    displayError("An error occurred while processing the pledge.");
  }
}

/**
 * Display an error message to the user.
 * @param {string} message - The error message to display.
 */
function displayError(message) {
  const errorElement = document.getElementById("error-message");
  if (errorElement) {
    errorElement.textContent = message;
    errorElement.style.display = "block";
  }
}

/**
 * Display a success message to the user.
 * @param {string} message - The success message to display.
 */
function displaySuccess(message) {
  const successElement = document.getElementById("success-message");
  if (successElement) {
    successElement.textContent = message;
    successElement.style.display = "block";
  }
}

/**
 * Best Practices Applied:
 * - Error handling for invalid inputs and transaction errors.
 * - Confirmation request for user transparency.
 * - Responsive event handling and user feedback.
 * - Validations for recipient address and pledge amount.
 */
```
