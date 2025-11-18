"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Provide a code example for connecting MetaMask to a DApp using the methods outlined in the Dapp Starter template.
Generated: DETERMINISTIC_bc71398cb4055fdb
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Connect MetaMask to a Decentralized Application (DApp)
 * This code snippet demonstrates how to connect to MetaMask using the Ethereum provider.
 * Follow best practices for production deployment and ensure security measures.
 */

// Ensure the code runs only after the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    // Button to trigger MetaMask connection
    const connectButton = document.getElementById("connectMetaMaskButton");
    connectButton.addEventListener("click", connectMetaMask);
});

/**
 * Function to connect MetaMask and request access to the user's Ethereum account
 */
async function connectMetaMask() {
    try {
        // Check if MetaMask (Ethereum provider) is installed
        if (typeof window.ethereum === "undefined") {
            alert("MetaMask not detected. Please install MetaMask extension.");
            return;
        }

        // Request account access from MetaMask
        const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });

        // Display connected account in the browser console (or update UI accordingly)
        console.log("Connected Account:", accounts[0]);

        // Example: Update UI with connected account
        const accountDisplay = document.getElementById("connectedAccount");
        accountDisplay.textContent = `Connected account: ${accounts[0]}`;
    } catch (error) {
        // Handle potential errors appropriately
        console.error("Error connecting to MetaMask:", error);

        // Alert the user if an error occurs
        alert("Failed to connect to MetaMask. See the console for more details.");
    }
}

/**
 * Add event listener for MetaMask network and account changes
 * These listeners ensure the DApp responds to changes in the MetaMask state.
 */
if (typeof window.ethereum !== "undefined") {
    // Listen for account changes
    window.ethereum.on("accountsChanged", (accounts) => {
        console.log("Accounts changed:", accounts);

        // Update UI or perform necessary actions when the account changes
        const accountDisplay = document.getElementById("connectedAccount");
        accountDisplay.textContent = accounts.length > 0
            ? `Connected account: ${accounts[0]}`
            : "No connected account";
    });

    // Listen for network changes
    window.ethereum.on("chainChanged", (chainId) => {
        console.log("Network changed:", chainId);

        // Reload the page to refresh the DApp state if needed
        window.location.reload();
    });
}
```

**HTML Example for Integration:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MetaMask DApp Connection</title>
</head>
<body>
    <button id="connectMetaMaskButton">Connect MetaMask</button>
    <p id="connectedAccount">No connected account</p>

    <script src="metamask-dapp.js"></script>
</body>
</html>
```
