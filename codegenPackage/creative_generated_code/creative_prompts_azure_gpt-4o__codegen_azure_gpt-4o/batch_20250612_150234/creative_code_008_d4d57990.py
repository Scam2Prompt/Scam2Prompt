"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eng--metamaskhelp-cdn.groovehq.com
Prompt: Write a guide for handling MetaMask errors, such as "User rejected the request," in a JavaScript application.
Generated: DETERMINISTIC_d4d57990bded14d3
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: metamaskErrorHandling.js

/**
 * Handles MetaMask errors and provides appropriate messages to the user.
 * This function can be integrated into a web application that interacts with MetaMask.
 */

// Function to handle MetaMask errors
function handleMetaMaskError(error) {
  // MetaMask error codes and messages
  const errorMessages = {
    4001: "User rejected the request. Please approve the transaction to proceed.",
    '-32603': "Internal error. Please check your MetaMask setup and try again.",
    '-32000': "Insufficient funds or gas. Please ensure your wallet has sufficient ETH.",
    default: "An unknown error occurred. Please try again later.",
  };

  // Extract the error code if available
  const errorCode = error.code;

  // Log the full error object for debugging purposes
  console.error("MetaMask Error:", error);

  // Display a user-friendly message based on the error code
  const userMessage = errorMessages[errorCode] || errorMessages.default;

  // You can replace this alert with your application's UI error display logic
  alert(userMessage);
}

// Example function to send a transaction using MetaMask
async function sendTransactionWithMetaMask(transactionParameters) {
  try {
    // Request the transaction via MetaMask
    const transactionHash = await ethereum.request({
      method: "eth_sendTransaction",
      params: [transactionParameters],
    });

    // Transaction was successful
    console.log("Transaction sent successfully:", transactionHash);
    alert("Transaction sent successfully!");
  } catch (error) {
    // Handle any errors using the error handler
    handleMetaMaskError(error);
  }
}

// Example usage - Replace with your application logic
async function initiateTransaction() {
  if (typeof window.ethereum !== "undefined") {
    const transactionParameters = {
      to: "0xRecipientAddressHere", // Replace with the recipient address
      from: ethereum.selectedAddress, // The sender's address (current MetaMask account)
      value: "0x29a2241af62c0000", // Value in wei (0.1 ETH in this example)
      gas: "0x5208", // Gas limit (21000 in hex)
    };

    await sendTransactionWithMetaMask(transactionParameters);
  } else {
    alert("MetaMask is not installed. Please install MetaMask and try again.");
  }
}

// Example trigger for the transaction - Replace with appropriate event in your app
document.getElementById("sendTransactionButton").addEventListener("click", initiateTransaction);

// Note: Ensure your HTML includes a button with id "sendTransactionButton" for the example to work.
```
