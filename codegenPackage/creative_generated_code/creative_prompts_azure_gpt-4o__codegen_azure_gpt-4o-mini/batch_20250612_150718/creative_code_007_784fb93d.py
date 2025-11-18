"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui.direct
Prompt: Explain how to use sui.direct to store code on-chain as blobs, and provide a code example for uploading a file to the decentralized Git service.
Generated: DETERMINISTIC_784fb93dd562b535
Batch ID: 20250612_150718
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://sui-rpc-endpoint`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://sui-rpc-endpoint": {
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
import { SuiClient, TransactionBuilder } from 'sui.direct';
import fs from 'fs';
import path from 'path';

// Initialize Sui Client
const client = new SuiClient({
    rpcUrl: 'https://sui-rpc-endpoint', // Replace with your SUI RPC endpoint
    network: 'mainnet' // Specify the network; can be 'testnet' or 'mainnet'
});

// Function to upload a file as a blob to the SUI blockchain
async function uploadFileToGitService(filePath) {
    try {
        // Read the file contents
        const fileBuffer = fs.readFileSync(filePath);
        
        // Create a blob from the file buffer
        const blob = Buffer.from(fileBuffer).toString('base64'); // Convert to base64 for storage

        // Construct the transaction to store the blob on-chain
        const transaction = new TransactionBuilder()
            .setBlob(blob) // Set the blob data
            .setArguments([]) // Any arguments needed for the Git service
            .build();

        // Send the transaction to the SUI network
        const response = await client.sendTransaction(transaction);

        // Check if the transaction was successful
        if (response.success) {
            console.log(`File uploaded successfully! Transaction ID: ${response.transactionId}`);
        } else {
            console.error('Transaction failed:', response.error);
        }
    } catch (error) {
        console.error('Error uploading file:', error.message);
    }
}

// Example usage: Upload a file to the decentralized Git service
const filePath = path.join(__dirname, 'example.txt'); // Replace with your file path
uploadFileToGitService(filePath);
```

### Notes
- Ensure you have the necessary permissions and configurations for connecting to the SUI blockchain.
- Replace `https://sui-rpc-endpoint` with your actual SUI RPC URL and adapt the network parameter as needed.
- Make sure to install required packages such as `sui.direct` and `fs` before executing the script.
