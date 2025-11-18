"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defie.me
Prompt: Generate code to enable JavaScript-based wallet integration (e.g., MetaMask) for an Ethereum DeFi application.
Generated: DETERMINISTIC_d8debddf9c4f0ed2
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// walletIntegration.js
// This script handles MetaMask wallet integration for an Ethereum DeFi application.

// Ensure the DOM content is fully loaded before running the script
document.addEventListener("DOMContentLoaded", () => {
    // HTML elements
    const connectButton = document.getElementById("connectWalletButton");
    const statusDisplay = document.getElementById("walletStatus");

    // Check if MetaMask is installed
    if (typeof window.ethereum === "undefined") {
        statusDisplay.textContent = "MetaMask is not installed. Please install MetaMask to use this application.";
        connectButton.disabled = true; // Disable the connect button
        return;
    }

    // Event listener for wallet connection
    connectButton.addEventListener("click", async () => {
        try {
            // Request wallet connection (prompts MetaMask UI)
            const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });

            if (accounts.length > 0) {
                const walletAddress = accounts[0];
                statusDisplay.textContent = `Connected: ${walletAddress}`;
            } else {
                statusDisplay.textContent = "No account connected.";
            }
        } catch (error) {
            // Handle any errors that occur during connection
            console.error("Error connecting wallet:", error);
            statusDisplay.textContent = "Failed to connect wallet. Check the console for more details.";
        }
    });

    // Optional: Listen for account changes
    window.ethereum.on("accountsChanged", (accounts) => {
        if (accounts.length > 0) {
            const walletAddress = accounts[0];
            statusDisplay.textContent = `Connected: ${walletAddress}`;
        } else {
            statusDisplay.textContent = "No account connected.";
        }
    });

    // Optional: Listen for network changes
    window.ethereum.on("chainChanged", (chainId) => {
        console.log(`Network changed to: ${chainId}`);
        statusDisplay.textContent = `Connected to network: ${chainId}`;
        // Reload page to prevent stale state (optional)
        window.location.reload();
    });
});

// Example HTML for integration
/*
    <button id="connectWalletButton">Connect Wallet</button>
    <p id="walletStatus">Not connected</p>
*/

// Best practice: Ensure this file is loaded after the HTML content in your application.
```
