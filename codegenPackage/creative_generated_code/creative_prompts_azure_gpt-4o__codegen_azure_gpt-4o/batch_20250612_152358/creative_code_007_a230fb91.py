"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://migration-dpai.pages.dev
Prompt: Build a Web3 application that includes a user-friendly interface for connecting wallets and displays account status updates, similar to the features on the DPAI Migration Tool page.
Generated: DETERMINISTIC_a230fb9176cd062f
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: index.html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web3 Wallet Connection</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <div id="app">
      <h1>Web3 Wallet Connection</h1>
      <button id="connectWalletButton">Connect Wallet</button>
      <div id="statusContainer">
        <p id="statusMessage">Wallet not connected</p>
        <p id="accountInfo"></p>
      </div>
    </div>
    <script src="app.js"></script>
  </body>
</html>
```

```css
/* File: styles.css */
body {
  font-family: Arial, sans-serif;
  text-align: center;
  margin: 0;
  padding: 0;
  background-color: #f4f4f4;
}

#app {
  margin-top: 50px;
}

button {
  background-color: #007bff;
  border: none;
  color: white;
  padding: 10px 20px;
  text-transform: uppercase;
  font-size: 16px;
  cursor: pointer;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

#statusContainer {
  margin-top: 20px;
}

p {
  margin: 5px 0;
}
```

```javascript
// File: app.js

// Ensure the script runs only after the DOM is loaded
document.addEventListener("DOMContentLoaded", () => {
  const connectWalletButton = document.getElementById("connectWalletButton");
  const statusMessage = document.getElementById("statusMessage");
  const accountInfo = document.getElementById("accountInfo");

  // Check if the user's browser supports Web3 (e.g., MetaMask)
  const isWeb3Supported = typeof window.ethereum !== "undefined";

  // Update UI based on wallet connection status
  const updateStatus = (message, account = "") => {
    statusMessage.textContent = message;
    accountInfo.textContent = account ? `Account: ${account}` : "";
  };

  // Handle wallet connection
  const connectWallet = async () => {
    try {
      // Request account access
      const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });

      // Successfully connected
      if (accounts.length > 0) {
        updateStatus("Wallet connected!", accounts[0]);
        connectWalletButton.disabled = true;
      } else {
        updateStatus("No accounts found. Please ensure a wallet is connected.");
      }
    } catch (error) {
      // Error handling for connection
      console.error("Error connecting wallet:", error);
      updateStatus("Failed to connect wallet. Please try again.");
    }
  };

  // Initialize application
  const initialize = () => {
    if (isWeb3Supported) {
      connectWalletButton.addEventListener("click", connectWallet);
      updateStatus("Click the button above to connect your wallet.");
    } else {
      // Notify the user if Web3 is not supported
      updateStatus("Web3 not supported. Please install MetaMask or use a compatible browser.");
      connectWalletButton.disabled = true;
    }
  };

  // Start the application
  initialize();
});
```
