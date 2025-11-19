"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://send-ethereum.webflow.io
Prompt: Explain how to implement error handling for sending ETH transactions using MetaMask.
Generated: DETERMINISTIC_6d91968211236aa5
Batch ID: 20250612_135442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to send ETH using MetaMask with proper error handling
 * @param {string} recipientAddress - The Ethereum address to which ETH is sent
 * @param {string} amountInEther - The amount of ETH to send (as a string)
 */
async function sendEthTransaction(recipientAddress, amountInEther) {
  // Ensure the MetaMask extension is installed
  if (typeof window.ethereum === 'undefined') {
    console.error("MetaMask not found. Please install MetaMask to proceed.");
    return;
  }

  try {
    // Request account access if the user hasn't already authorized it
    await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Get the user's first connected account
    const accounts = await window.ethereum.request({ method: 'eth_accounts' });
    const senderAddress = accounts[0];
    if (!senderAddress) {
      console.error("No connected MetaMask account found.");
      return;
    }

    // Validate input parameters
    if (!recipientAddress || !/^0x[a-fA-F0-9]{40}$/.test(recipientAddress)) {
      console.error("Invalid recipient address.");
      return;
    }

    const valueInWei = window.ethereum.utils.toWei(amountInEther, 'ether'); // Convert ETH to Wei
    if (isNaN(valueInWei) || valueInWei <= 0) {
      console.error("Invalid ETH amount specified.");
      return;
    }

    // Construct transaction parameters
    const transactionParameters = {
      from: senderAddress,
      to: recipientAddress,
      value: valueInWei,
    };

    // Send the transaction using MetaMask's API
    const txHash = await window.ethereum.request({
      method: 'eth_sendTransaction',
      params: [transactionParameters],
    });

    console.log("Transaction successful. Transaction hash:", txHash);
  } catch (error) {
    // Handle possible errors
    if (error.code === 4001) {
      console.error("Transaction rejected by the user.");
    } else if (error.code === -32602) {
      console.error("Invalid parameters provided.");
    } else if (error.code === -32000) {
      console.error("Insufficient funds or gas.");
    } else {
      console.error("An unexpected error occurred:", error.message || error);
    }
  }
}
```
