"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://devnet-directory-one.vercel.app
Prompt: Explain the process of verifying a Dev Card on-chain in the Solana Devnet Directory and provide a code example.
Generated: DETERMINISTIC_6fb8c2af8f540232
Batch ID: 20250612_162504
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.devnet.solana.com": {
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
// Import necessary libraries
const { Connection, PublicKey } = require('@solana/web3.js');
const fetch = require('node-fetch');

// Define the Solana Devnet RPC endpoint
const DEVNET_RPC_URL = 'https://api.devnet.solana.com';

// Function to verify a Dev Card on-chain
async function verifyDevCard(devCardAddress) {
    // Create a connection to the Solana Devnet
    const connection = new Connection(DEVNET_RPC_URL, 'confirmed');

    try {
        // Convert the Dev Card address to a PublicKey object
        const devCardPublicKey = new PublicKey(devCardAddress);

        // Fetch the account information for the Dev Card
        const accountInfo = await connection.getAccountInfo(devCardPublicKey);

        // Check if the account exists
        if (accountInfo === null) {
            throw new Error('Dev Card does not exist on-chain.');
        }

        // Log the account information
        console.log('Dev Card Info:', accountInfo.data.toString('hex'));

        // (Optional) Add further verification logic here, e.g., decoding the account data

        return true; // Verification successful

    } catch (error) {
        // Handle errors appropriately
        console.error('Error verifying Dev Card:', error.message);
        return false; // Verification failed
    }
}

// Example usage
(async () => {
    const devCardAddress = 'YourDevCardPublicKeyHere'; // Replace with actual Dev Card address
    const isVerified = await verifyDevCard(devCardAddress);

    if (isVerified) {
        console.log('Dev Card verified successfully.');
    } else {
        console.log('Dev Card verification failed.');
    }
})();
```

**Note**: Ensure to replace `'YourDevCardPublicKeyHere'` with the actual Dev Card public key you wish to verify.
