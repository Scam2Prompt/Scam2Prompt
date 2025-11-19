"""
Generated Code Metadata:
========================
Original URL: https://sui.direct
Prompt: Generate an example of how to store code on-chain using sui.direct and the SUI blockchain.
Generated: DETERMINISTIC_05f327ffa890ba4c
Batch ID: 20250622_212709
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://fullnode.testnet.sui.io:443": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```typescript
// Import required Sui SDK modules
import { Ed25519Keypair, JsonRpcProvider, RawSigner, TransactionBlock } from '@mysten/sui.js';
import * as fs from 'fs';

// Configuration constants
const SUI_NETWORK = 'https://fullnode.testnet.sui.io:443';
const PACKAGE_PATH = './path/to/your/package';
const KEYPAIR_PATH = './path/to/your/keypair.json';

// Main function to publish package
async function publishPackage() {
    try {
        // Load keypair from file
        const keypairData = JSON.parse(fs.readFileSync(KEYPAIR_PATH, 'utf8'));
        const keypair = Ed25519Keypair.fromSecretKey(Uint8Array.from(keypairData));

        // Initialize provider and signer
        const provider = new JsonRpcProvider(SUI_NETWORK);
        const signer = new RawSigner(keypair, provider);

        // Prepare transaction block
        const tx = new TransactionBlock();
        const [upgradeCap] = tx.publish({
            modules: [
                fs.readFileSync(`${PACKAGE_PATH}/bytecode_modules/module1.mv`, 'base64'),
                fs.readFileSync(`${PACKAGE_PATH}/bytecode_modules/module2.mv`, 'base64')
            ],
            dependencies: [
                '0x0000000000000000000000000000000000000001', // Example dependency
                '0x0000000000000000000000000000000000000002'  // Example dependency
            ]
        });

        // Transfer upgrade capability to sender
        tx.transferObjects([upgradeCap], tx.pure(await signer.getAddress()));

        // Execute transaction
        const result = await signer.signAndExecuteTransactionBlock({
            transactionBlock: tx,
            options: {
                showEffects: true,
                showObjectChanges: true
            }
        });

        console.log('Package published successfully!');
        console.log('Transaction digest:', result.digest);
        console.log('Package ID:', result.objectChanges?.find(
            (change) => change.type === 'published'
        )?.packageId);

    } catch (error) {
        console.error('Error publishing package:', error);
        process.exit(1);
    }
}

// Execute the main function
publishPackage();
```
