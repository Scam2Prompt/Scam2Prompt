"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inch-docs.vercel.app
Prompt: Provide an example of how to use the 1inch utils library to verify a signature for a limit order created on the 1inch Limit Order Protocol.
Generated: DETERMINISTIC_ade2a1f455a22dff
Batch ID: 20250612_155028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries from ethers.js and 1inch utils
const { ethers } = require('ethers');
const { verifyOrderSignature } = require('@1inch/limit-order-protocol-utils');

/**
 * Verifies a signature for a limit order created on the 1inch Limit Order Protocol.
 * 
 * @param {string} orderHash - The hash of the order to be verified.
 * @param {string} signerAddress - The address of the signer who created the order.
 * @param {string} signature - The signature to verify against the order.
 * @returns {boolean} - Returns true if the signature is valid, otherwise false.
 */
async function verifyLimitOrderSignature(orderHash, signerAddress, signature) {
    try {
        // Ensure all inputs are valid
        if (!ethers.utils.isHexString(orderHash)) {
            throw new Error('Invalid order hash provided');
        }
        if (!ethers.utils.isAddress(signerAddress)) {
            throw new Error('Invalid signer address provided');
        }
        if (!ethers.utils.isHexString(signature)) {
            throw new Error('Invalid signature provided');
        }

        // Verify the signature using the 1inch utils library
        const isValid = await verifyOrderSignature(orderHash, signerAddress, signature);
        
        return isValid;
    } catch (error) {
        console.error('Error verifying limit order signature:', error.message);
        return false; // Return false in case of an error
    }
}

// Example usage
(async () => {
    const orderHash = '0x...'; // Replace with your actual order hash
    const signerAddress = '0x...'; // Replace with the actual signer address
    const signature = '0x...'; // Replace with the actual signature

    const isSignatureValid = await verifyLimitOrderSignature(orderHash, signerAddress, signature);
    
    console.log('Is the signature valid?', isSignatureValid);
})();
```
