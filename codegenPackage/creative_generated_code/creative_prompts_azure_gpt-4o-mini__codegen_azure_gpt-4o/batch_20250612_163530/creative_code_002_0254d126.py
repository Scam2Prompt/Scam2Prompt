"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-core.com
Prompt: What steps should I follow in the Wallet-Core DevTool Console to troubleshoot a failed transaction or swap?
Generated: DETERMINISTIC_0254d12603ba6ecc
Batch ID: 20250612_163530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Troubleshooting a failed transaction or swap in Wallet-Core DevTool Console.
 * This script provides steps to log and identify the issue systematically.
 * 
 * Prerequisites:
 * 1. Ensure you have access to the Wallet-Core DevTool console.
 * 2. Replace placeholder values with actual values from your environment.
 */

// Step 1: Define the transaction ID or swap information
const transactionId = "your_transaction_id_here"; // Replace with the actual transaction ID
const swapDetails = {
  sourceCurrency: "BTC",
  targetCurrency: "ETH",
  amount: 0.1,
  swapId: "your_swap_id_here" // Replace with the actual swap ID if applicable
};

/**
 * Step 2: Function to fetch transaction details from the wallet-core API
 */
async function getTransactionDetails(transactionId) {
  try {
    console.log("Fetching transaction details...");
    
    // Replace with actual API call to Wallet-Core DevTool to fetch transaction details
    const transactionDetails = await fetch(`/api/transaction/${transactionId}`)
      .then(response => response.json());
    
    console.log("Transaction Details:", transactionDetails);

    return transactionDetails;
  } catch (error) {
    console.error("Error fetching transaction details:", error.message);
    throw new Error("Failed to fetch transaction details. Please check the transaction ID.");
  }
}

/**
 * Step 3: Function to validate the transaction status
 */
function validateTransactionStatus(transactionDetails) {
  try {
    console.log("Validating transaction status...");
    
    if (!transactionDetails || !transactionDetails.status) {
      throw new Error("Invalid transaction details received.");
    }

    switch (transactionDetails.status) {
      case "success":
        console.log("Transaction completed successfully.");
        break;
      case "failed":
        console.warn("Transaction failed. Reason:", transactionDetails.failureReason);
        break;
      case "pending":
        console.warn("Transaction is still pending. Please wait and try again later.");
        break;
      default:
        console.warn("Unknown transaction status:", transactionDetails.status);
    }
  } catch (error) {
    console.error("Error validating transaction status:", error.message);
    throw new Error("Transaction status validation failed.");
  }
}

/**
 * Step 4: Function to fetch swap details if applicable
 */
async function getSwapDetails(swapDetails) {
  try {
    console.log("Fetching swap details...");

    // Replace with actual API call to Wallet-Core DevTool to fetch swap details
    const swapResponse = await fetch(`/api/swap/${swapDetails.swapId}`)
      .then(response => response.json());

    console.log("Swap Details:", swapResponse);
    
    return swapResponse;
  } catch (error) {
    console.error("Error fetching swap details:", error.message);
    throw new Error("Failed to fetch swap details. Please check the swap ID.");
  }
}

/**
 * Step 5: Troubleshooting workflow
 */
async function troubleshootTransactionOrSwap(transactionId, swapDetails) {
  try {
    // Fetch transaction details
    const transactionDetails = await getTransactionDetails(transactionId);

    // Validate transaction status
    validateTransactionStatus(transactionDetails);

    // If the transaction is part of a swap, fetch swap details
    if (swapDetails.swapId) {
      const swapResponse = await getSwapDetails(swapDetails);

      // Additional validation for swap responses can be added here
      console.log("Swap troubleshooting completed.");
    }
  } catch (error) {
    console.error("Troubleshooting failed:", error.message);
  }
}

// Execute the troubleshooting workflow
troubleshootTransactionOrSwap(transactionId, swapDetails);
```
