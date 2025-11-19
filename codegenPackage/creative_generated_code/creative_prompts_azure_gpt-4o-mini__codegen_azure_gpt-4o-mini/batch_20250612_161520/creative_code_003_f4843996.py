"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://issue-connection.pages.dev
Prompt: Provide an example of integrating WalletConnect into a DApp to facilitate user interactions from mobile wallets.
Generated: DETERMINISTIC_f4843996086f7c84
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import WalletConnectProvider from "@walletconnect/web3-provider";
import Web3 from "web3";

// Initialize the provider
const provider = new WalletConnectProvider({
  infuraId: "YOUR_INFURA_PROJECT_ID", // Required
});

// Create a Web3 instance
const web3 = new Web3(provider);

// Function to create a connection to WalletConnect
async function connectWallet() {
  try {
    // Enable session (triggers QR Code modal)
    await provider.enable();

    // Fetch the accounts and set the active account
    const accounts = await web3.eth.getAccounts();
    console.log("Connected account:", accounts[0]);
    
    // Update your UI and state with the connected account
    updateUIWithAccount(accounts[0]);
  } catch (error) {
    console.error("Failed to connect to WalletConnect:", error);
  }
}

// Function to disconnect the wallet
async function disconnectWallet() {
  try {
    await provider.disconnect();
    console.log("Wallet disconnected");
    
    // Reset your UI and state
    resetUI();
  } catch (error) {
    console.error("Failed to disconnect from WalletConnect:", error);
  }
}

// Example function to send a transaction
async function sendTransaction(toAddress, amount) {
  try {
    const accounts = await web3.eth.getAccounts();
    
    // Prepare the transaction
    const transactionParameters = {
      to: toAddress, // Required
      from: accounts[0], // Must match user's active account
      value: web3.utils.toHex(web3.utils.toWei(amount.toString(), 'ether')), // Convert amount to wei
    };

    // Send the transaction
    const txHash = await web3.eth.sendTransaction(transactionParameters);
    console.log("Transaction successful with hash:", txHash);
  } catch (error) {
    console.error("Transaction failed:", error);
  }
}

// Example function to update UI with connected account
function updateUIWithAccount(account) {
  document.getElementById("accountDisplay").innerText = `Connected: ${account}`;
}

// Example function to reset UI
function resetUI() {
  document.getElementById("accountDisplay").innerText = "Wallet disconnected";
}

// Event listener for connect button
document.getElementById("connectButton").addEventListener("click", connectWallet);

// Event listener for disconnect button
document.getElementById("disconnectButton").addEventListener("click", disconnectWallet);

// Example usage of sending a transaction
document.getElementById("sendButton").addEventListener("click", async () => {
  const toAddress = document.getElementById("toAddress").value;
  const amount = document.getElementById("amount").value;
  await sendTransaction(toAddress, amount);
});
```

**HTML Structure (for UI elements referenced above)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WalletConnect DApp Example</title>
</head>
<body>
    <h1>WalletConnect DApp</h1>
    <div id="accountDisplay">Wallet disconnected</div>
    <button id="connectButton">Connect Wallet</button>
    <button id="disconnectButton">Disconnect Wallet</button>
    <hr>
    <input type="text" id="toAddress" placeholder="Recipient Address">
    <input type="text" id="amount" placeholder="Amount in ETH">
    <button id="sendButton">Send Transaction</button>

    <script src="path_to_your_bundled_js_file.js"></script>
</body>
</html>
```

**Note**: Replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura project ID and ensure the appropriate libraries are installed and imported in your project environment.
