"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.hq-innovacion.mx
Prompt: Provide an example of how to use MetaMask's API to sign a message and verify the signature in a Node.js application.
Generated: DETERMINISTIC_ce6d06ab2e3affaf
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required modules
const ethers = require('ethers');

// Function to sign a message using MetaMask
async function signMessageWithMetaMask(message) {
    if (!window.ethereum) {
        throw new Error("MetaMask is not installed!");
    }

    // Request account access if needed
    await window.ethereum.request({ method: 'eth_requestAccounts' });

    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();

    // Sign the message
    const signature = await signer.signMessage(message);
    return signature;
}

// Function to verify the signature
function verifySignature(message, signature, signerAddress) {
    // Recover the address from the signature
    const recoveredAddress = ethers.utils.verifyMessage(message, signature);

    // Check if the recovered address matches the signer address
    return recoveredAddress === signerAddress;
}

// Example usage
(async () => {
    try {
        const message = "Hello, this is a test message!";
        
        // Sign a message
        const signature = await signMessageWithMetaMask(message);
        
        // Get the signer address
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();
        const signerAddress = await signer.getAddress();

        // Verify the signature
        const isValid = verifySignature(message, signature, signerAddress);

        console.log("Signature:", signature);
        console.log("Signer Address:", signerAddress);
        console.log("Is signature valid?", isValid);
    } catch (error) {
        console.error("Error:", error.message);
    }
})();
```
