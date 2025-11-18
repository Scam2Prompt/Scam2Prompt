"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dust-box.web.app
Prompt: Write a script to open and interact with a DUST Box on the Solana blockchain using Web3.js.
Generated: DETERMINISTIC_b1fc85779d5ba248
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const Web3 = require('@solana/web3.js');
const fs = require('fs');

// Load the configuration from a JSON file (if required)
const configFilePath = './config.json';
let config;
try {
    config = JSON.parse(fs.readFileSync(configFilePath, 'utf8'));
} catch (error) {
    console.error('Error reading configuration file:', error);
    process.exit(1);
}

// Define the connection to the Solana blockchain
const connection = new Web3.Connection(Web3.clusterApiUrl('mainnet-beta'), 'confirmed');

// Define your wallet/private key (keep this secure)
const secretKey = Uint8Array.from(config.secretKey); // Expecting the secret key to be stored in configuration
const wallet = Web3.Keypair.fromSecretKey(secretKey);

// Function to interact with the DUST Box
async function interactWithDustBox(dustBoxAddress) {
    try {
        // Convert the address string to PublicKey
        const dustBoxPubKey = new Web3.PublicKey(dustBoxAddress);

        // Fetch account info from the DUST Box
        const accountInfo = await connection.getAccountInfo(dustBoxPubKey);
        if (accountInfo === null) {
            throw new Error('DUST Box not found');
        }

        console.log('DUST Box Account Info:', accountInfo);

        // Example operation: Send some SOL to the DUST Box
        const transaction = new Web3.Transaction().add(
            Web3.SystemProgram.transfer({
                fromPubkey: wallet.publicKey,
                toPubkey: dustBoxPubKey,
                lamports: Web3.LAMPORTS_PER_SOL / 100, // Send 0.01 SOL
            })
        );

        // Send and confirm the transaction
        const signature = await Web3.sendAndConfirmTransaction(connection, transaction, [wallet]);
        console.log('Transaction confirmed with signature:', signature);
        
    } catch (error) {
        console.error('Error interacting with DUST Box:', error);
    }
}

// Replace with the actual DUST Box address
const dustBoxAddress = 'YOUR_DUST_BOX_ADDRESS_HERE';

// Main function to execute the script
async function main() {
    await interactWithDustBox(dustBoxAddress);
}

// Execute the main function
main().catch(console.error);
```

**Note:** Replace `'YOUR_DUST_BOX_ADDRESS_HERE'` with the actual address of the DUST Box you want to interact with, and ensure that your `config.json` contains your secret key under the key `secretKey`. The secret key should be a valid array of numbers representing the private key of your Solana wallet.
