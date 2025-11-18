"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.io
Prompt: Write code using the MetaMask SDK to integrate a Web3 wallet into a dapp for Ethereum transactions.
Generated: DETERMINISTIC_d7e3ac0e7fb3d840
Batch ID: 20250612_150323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/ethers@5.4.0/dist/ethers.umd.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary packages
import { ethers } from 'ethers';

// Function to check if MetaMask is installed
const isMetaMaskInstalled = () => {
  return Boolean(window.ethereum && window.ethereum.isMetaMask);
};

// Function to request account access from MetaMask
const requestAccount = async () => {
  try {
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    return accounts[0]; // Return the first account
  } catch (error) {
    console.error("Error requesting account:", error);
    throw new Error("Could not connect to MetaMask.");
  }
};

// Function to send a transaction
const sendTransaction = async (to, amount) => {
  if (!isMetaMaskInstalled()) {
    throw new Error("MetaMask is not installed. Please install it to use this feature.");
  }

  const signer = new ethers.providers.Web3Provider(window.ethereum).getSigner();
  const transaction = {
    to: to, // Recipient address
    value: ethers.utils.parseEther(amount) // Amount in ETH
  };

  try {
    const txResponse = await signer.sendTransaction(transaction);
    // Wait for transaction to be mined
    await txResponse.wait();
    console.log(`Transaction successful: ${txResponse.hash}`);
    return txResponse.hash;
  } catch (error) {
    console.error("Transaction failed:", error);
    throw new Error("Transaction failed.");
  }
};

// Event listener for the connect button
document.getElementById('connectButton').addEventListener('click', async () => {
  try {
    const account = await requestAccount();
    console.log("Connected account:", account);
  } catch (error) {
    alert(error.message);
  }
});

// Event listener for the send transaction button
document.getElementById('sendTransactionButton').addEventListener('click', async () => {
  const recipientAddress = document.getElementById('recipientAddress').value;
  const amount = document.getElementById('amount').value;

  try {
    const txHash = await sendTransaction(recipientAddress, amount);
    alert(`Transaction successful with hash: ${txHash}`);
  } catch (error) {
    alert(error.message);
  }
});
```

```html
<!-- HTML Structure for the DApp -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web3 DApp</title>
</head>
<body>
    <h1>Ethereum DApp Integration</h1>
    <button id="connectButton">Connect MetaMask</button>
    <h2>Send Transaction</h2>
    <input type="text" id="recipientAddress" placeholder="Recipient Address" required>
    <input type="text" id="amount" placeholder="Amount in ETH" required>
    <button id="sendTransactionButton">Send Transaction</button>

    <!-- Include Ethers.js library -->
    <script src="https://cdn.jsdelivr.net/npm/ethers@5.4.0/dist/ethers.umd.min.js"></script>
    <!-- Include the DApp script -->
    <script type="module" src="dapp.js"></script>
</body>
</html>
```
