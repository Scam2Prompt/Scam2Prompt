"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suifoundation.com
Prompt: Provide an example of how to use the Sui SDKs for TypeScript to interact with the Sui blockchain for asset management.
Generated: DETERMINISTIC_93012433fe3880b6
Batch ID: 20250612_160019
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://fullnode.testnet.sui.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```typescript
// Import required modules from the Sui SDK
import { JsonRpcProvider, Ed25519Keypair, RawSigner, TransactionBlock } from '@mysten/sui.js';
import dotenv from 'dotenv';

// Load environment variables from a .env file
dotenv.config();

// Set up Sui RPC connection
const SUI_RPC_URL = process.env.SUI_RPC_URL || 'https://fullnode.testnet.sui.io';
const provider = new JsonRpcProvider(SUI_RPC_URL);

// Set up wallet using environment variables for private key
const PRIVATE_KEY_HEX = process.env.PRIVATE_KEY_HEX;
if (!PRIVATE_KEY_HEX) {
    throw new Error('PRIVATE_KEY_HEX not set in environment variables');
}

// Initialize the keypair and signer
const keypair = Ed25519Keypair.fromSecretKey(Buffer.from(PRIVATE_KEY_HEX, 'hex'));
const signer = new RawSigner(keypair, provider);

// Function to transfer assets on the Sui blockchain
async function transferAsset(
    recipientAddress: string,
    assetObjectId: string,
    gasBudget: number
): Promise<void> {
    try {
        // Validate inputs
        if (!recipientAddress || !assetObjectId || !gasBudget) {
            throw new Error('Invalid input parameters');
        }

        // Prepare the transaction block
        const txBlock = new TransactionBlock();
        txBlock.transferObjects([txBlock.object(assetObjectId)], txBlock.pure(recipientAddress));
        txBlock.setGasBudget(gasBudget);

        // Sign and execute the transaction
        const txResult = await signer.signAndExecuteTransactionBlock({
            transactionBlock: txBlock,
        });

        console.log('Transaction executed successfully:', txResult);
    } catch (error) {
        console.error('Error during asset transfer:', error.message);
    }
}

// Function to check the balance of an address
async function getBalance(address: string): Promise<void> {
    try {
        // Validate input
        if (!address) {
            throw new Error('Address is required');
        }

        // Fetch the user's Sui balance
        const coins = await provider.getCoins(address);
        console.log(`Balance for ${address}:`, coins.totalBalance);
    } catch (error) {
        console.error('Error fetching balance:', error.message);
    }
}

// Example usage
(async () => {
    try {
        // Replace with actual values
        const recipientAddress = '0xRecipientAddressHere';
        const assetObjectId = '0xAssetObjectIdHere';
        const gasBudget = 1000;

        console.log('Checking balance before transfer...');
        await getBalance(keypair.getPublicKey().toSuiAddress());

        console.log('Transferring asset...');
        await transferAsset(recipientAddress, assetObjectId, gasBudget);

        console.log('Checking balance after transfer...');
        await getBalance(keypair.getPublicKey().toSuiAddress());
    } catch (error) {
        console.error('Error in example usage:', error.message);
    }
})();
```
