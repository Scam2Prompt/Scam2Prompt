"""
Generated Code Metadata:
========================
Original URL: https://id.stromkonto.net
Prompt: What are the steps to export and import device keys (Geräteschlüssel) for a Stromkonto user, and how can this be achieved programmatically using a library like MetaMask?
Generated: DETERMINISTIC_39e3106d9e47e36d
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const { ethers } = require('ethers');

// Function to export device keys for a Stromkonto user
async function exportDeviceKeys(userAddress, privateKey) {
    try {
        // Create a wallet instance using the user's private key
        const wallet = new ethers.Wallet(privateKey);
        
        // Simulate the process of exporting device keys
        const deviceKeys = {
            userAddress: userAddress,
            keys: wallet.signMessage("Exporting device keys") // Example of signing a message
        };

        // Return the exported device keys
        return deviceKeys;
    } catch (error) {
        console.error("Error exporting device keys:", error);
        throw new Error("Failed to export device keys.");
    }
}

// Function to import device keys for a Stromkonto user
async function importDeviceKeys(deviceKeys, privateKey) {
    try {
        // Create a wallet instance using the provided private key
        const wallet = new ethers.Wallet(privateKey);
        
        // Simulate the process of importing device keys
        const message = "Importing device keys";
        const signature = await wallet.signMessage(message);

        // Verify the signature to ensure the keys are valid
        if (signature === deviceKeys.keys) {
            console.log("Device keys imported successfully for:", deviceKeys.userAddress);
            return true;
        } else {
            throw new Error("Invalid device keys.");
        }
    } catch (error) {
        console.error("Error importing device keys:", error);
        throw new Error("Failed to import device keys.");
    }
}

// Example usage
(async () => {
    const userAddress = "0xYourUserAddress"; // Replace with actual user address
    const privateKey = "0xYourPrivateKey"; // Replace with actual private key

    try {
        // Export device keys
        const exportedKeys = await exportDeviceKeys(userAddress, privateKey);
        console.log("Exported Device Keys:", exportedKeys);

        // Import device keys
        const importSuccess = await importDeviceKeys(exportedKeys, privateKey);
        console.log("Import Success:", importSuccess);
    } catch (error) {
        console.error("An error occurred:", error);
    }
})();
```
