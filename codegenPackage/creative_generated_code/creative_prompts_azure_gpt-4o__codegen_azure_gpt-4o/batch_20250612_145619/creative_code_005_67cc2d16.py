"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethphbi.com
Prompt: Explain how to use the ethers.js library to sign and verify Ethereum transactions related to pledges, and provide sample code.
Generated: DETERMINISTIC_67cc2d16e55e18fc
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the ethers.js library
const { ethers } = require('ethers');

// Function to sign a pledge with a private key
async function signPledge(privateKey, pledgeMessage) {
    try {
        // Create a wallet instance using the private key
        const wallet = new ethers.Wallet(privateKey);

        // Sign the pledge message
        const signedMessage = await wallet.signMessage(pledgeMessage);

        // Return the signed message
        return signedMessage;
    } catch (error) {
        console.error("Error while signing the pledge:", error);
        throw new Error("Failed to sign the pledge.");
    }
}

// Function to verify a signed pledge
async function verifyPledge(signedMessage, originalMessage, signerAddress) {
    try {
        // Recover the address of the signer from the signed message
        const recoveredAddress = ethers.utils.verifyMessage(originalMessage, signedMessage);

        // Check if the recovered address matches the expected signer address
        return recoveredAddress.toLowerCase() === signerAddress.toLowerCase();
    } catch (error) {
        console.error("Error while verifying the pledge:", error);
        throw new Error("Failed to verify the pledge.");
    }
}

// Example usage
(async () => {
    // Replace with your own private key (DO NOT use in production)
    const privateKey = "0xYOUR_PRIVATE_KEY_HERE";

    // Replace with your own pledge message
    const pledgeMessage = "I pledge 10 ETH to the project.";

    // Replace with the expected Ethereum address of the signer
    const signerAddress = "0xEXPECTED_SIGNER_ADDRESS";

    try {
        // Sign the pledge
        const signedPledge = await signPledge(privateKey, pledgeMessage);
        console.log("Signed Pledge:", signedPledge);

        // Verify the signed pledge
        const isValid = await verifyPledge(signedPledge, pledgeMessage, signerAddress);
        console.log("Is the pledge valid?", isValid);
    } catch (error) {
        console.error("An error occurred:", error.message);
    }
})();
```
