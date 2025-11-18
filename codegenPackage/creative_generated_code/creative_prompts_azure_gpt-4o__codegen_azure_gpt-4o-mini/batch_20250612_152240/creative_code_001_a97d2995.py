"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wl-usdh-mint.web.app
Prompt: Create a JavaScript function using Solana's web3.js library to interact with a minting platform, ensuring the wallet is connected and the user is entitled to free minting rights.
Generated: DETERMINISTIC_a97d29958b0575df
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const {
    Connection,
    PublicKey,
    clusterApiUrl,
    Keypair,
} = require('@solana/web3.js');

// Define the minting function
async function mintNFT(wallet) {
    // Ensure the wallet is connected
    if (!wallet || !wallet.publicKey) {
        throw new Error("Wallet is not connected. Please connect your wallet.");
    }

    // Define the network and connection
    const network = clusterApiUrl('mainnet-beta');
    const connection = new Connection(network, 'confirmed');

    // Check entitlement for free minting rights (mock function)
    const isEntitled = await checkFreeMintEntitlement(wallet.publicKey);
    if (!isEntitled) {
        throw new Error("User is not entitled to free minting rights.");
    }

    try {
        // Proceed with minting logic (this is a placeholder)
        const mintTransaction = await createMintTransaction(wallet.publicKey);
        const signature = await wallet.sendTransaction(mintTransaction, connection);
        
        // Confirm the transaction
        await connection.confirmTransaction(signature);
        
        console.log(`Minting successful! Transaction Signature: ${signature}`);
    } catch (error) {
        console.error("Error during minting:", error);
        throw new Error("Minting process failed. Please check the console for details.");
    }
}

// Mock function to check free mint entitlement
async function checkFreeMintEntitlement(publicKey) {
    // Implement the logic to verify if the user is entitled to mint for free
    // This can involve checking against a smart contract or off-chain database
    // For the purpose of this example, return true
    return true;
}

// Mock function to create mint transaction
async function createMintTransaction(publicKey) {
    // Implement actual minting transaction logic here
    // Return a transaction object ready to be sent
    const transaction = {}; // Replace with actual transaction building logic
    return transaction;
}

// Example usage - ensure to replace with your actual wallet connection logic
(async () => {
    try {
        const wallet = {
            publicKey: new PublicKey('YOUR_WALLET_PUBLIC_KEY'), // Replace with actual public key
            sendTransaction: async (transaction, connection) => {
                // Mock sendTransaction method
                return 'mock-signature'; // Replace with actual transaction sending logic
            }
        };

        await mintNFT(wallet);
    } catch (error) {
        console.error('An error occurred:', error);
    }
})();
```

**Note:** Replace the placeholder functions with actual implementations relevant to your minting platform and wallet connection logic.
