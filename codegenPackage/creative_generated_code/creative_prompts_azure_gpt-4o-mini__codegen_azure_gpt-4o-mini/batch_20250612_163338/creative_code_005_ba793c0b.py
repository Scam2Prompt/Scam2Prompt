"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-f.pages.dev
Prompt: Provide an example of how to handle transaction errors when using the MultiChain Protocol for DApps.
Generated: DETERMINISTIC_ba793c0ba9fc7eaa
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing the MultiChain client library
const multichain = require("multichain-node")({
    host: "localhost",     // Replace with your MultiChain node host
    port: 5000,            // Replace with your MultiChain node port
    user: "your_username", // Replace with your MultiChain username
    pass: "your_password"   // Replace with your MultiChain password
});

// Function to handle a transaction
async function handleTransaction() {
    try {
        // Define transaction parameters
        const txParams = {
            from: "address_from", // The sender address
            to: "address_to",     // The recipient address
            amount: 10,           // Amount to send
            asset: "my_asset"     // The asset to send
        };

        // Attempt to send the transaction
        const txId = await multichain.sendAssetFrom(txParams.from, txParams.to, txParams.amount, txParams.asset);

        console.log(`Transaction successful! Transaction ID: ${txId}`);
        
    } catch (error) {
        // Handle known errors from MultiChain
        if (error.code === -32600) {
            console.error("Invalid request: ", error.message);
        } else if (error.code === -4) {
            console.error("Insufficient funds: ", error.message);
        } else if (error.code === -5) {
            console.error("Unknown address: ", error.message);
        } else {
            // Handle unexpected errors
            console.error("An unexpected error occurred: ", error.message);
        }
    }
}

// Execute the transaction handling function
handleTransaction();
```
