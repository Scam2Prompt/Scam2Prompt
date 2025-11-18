"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-realio.network
Prompt: Provide an example of how to use MetaMask Snaps to extend wallet functionality with third-party features, such as enabling Solana support.
Generated: DETERMINISTIC_d8276ace9f59c64f
Batch ID: 20250612_150816
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
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
import { OnRpcRequestHandler } from '@metamask/snaps-types';
import { SolanaClient } from 'solana-web3.js';

// Define the Snap's RPC handler
export const onRpcRequest: OnRpcRequestHandler = async ({ origin, request }) => {
    switch (request.method) {
        case 'getSolanaBalance':
            return await getSolanaBalance(request.params);
        case 'sendSolanaTransaction':
            return await sendSolanaTransaction(request.params);
        default:
            throw new Error('Method not found.');
    }
};

// Function to get the Solana balance for a given public key
async function getSolanaBalance({ publicKey }) {
    try {
        // Initialize Solana client
        const solanaClient = new SolanaClient('https://api.mainnet-beta.solana.com');
        
        // Fetch balance in lamports
        const balance = await solanaClient.getBalance(publicKey);
        
        // Convert balance from lamports to SOL
        const balanceInSol = balance / 1e9; // 1 SOL = 1e9 lamports
        
        return {
            success: true,
            balance: balanceInSol,
        };
    } catch (error) {
        console.error('Error fetching balance:', error);
        return {
            success: false,
            error: error.message,
        };
    }
}

// Function to send a Solana transaction
async function sendSolanaTransaction({ fromPublicKey, toPublicKey, amount }) {
    try {
        // Initialize Solana client
        const solanaClient = new SolanaClient('https://api.mainnet-beta.solana.com');
        
        // Create transaction
        const transaction = new solanaClient.Transaction().add(
            solanaClient.SystemProgram.transfer({
                fromPubkey: new solanaClient.PublicKey(fromPublicKey),
                toPubkey: new solanaClient.PublicKey(toPublicKey),
                lamports: amount * 1e9, // Convert SOL to lamports
            }),
        );

        // Send transaction and get signature
        const signature = await solanaClient.sendTransaction(transaction, { skipPreflight: false });

        // Confirm the transaction
        await solanaClient.confirmTransaction(signature);

        return {
            success: true,
            signature: signature,
        };
    } catch (error) {
        console.error('Error sending transaction:', error);
        return {
            success: false,
            error: error.message,
        };
    }
}
```

Make sure to adjust the `SolanaClient` import path based on your project's structure and Solana client library version. Also, ensure you have the required libraries installed in your project.
