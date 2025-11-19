"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-git-feat-bridge-sdk-b50625-offchain-labs.vercel.app
Prompt: Create a function to query the status of a token bridge transaction using the Arbitrum Bridge SDK on Arbitrum Sepolia.
Generated: DETERMINISTIC_1b3d131233741e06
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import { Bridge, BridgeTransactionStatus } from '@arbitrum/sdk';
import { providers } from 'ethers';

/**
 * Queries the status of a token bridge transaction on Arbitrum Sepolia.
 * @param transactionHash The transaction hash of the bridge transaction.
 * @param provider The Ethereum provider (e.g., JsonRpcProvider) connected to Arbitrum Sepolia.
 * @returns Promise<BridgeTransactionStatus> The status of the bridge transaction.
 * @throws Error if the transaction status cannot be queried.
 */
export async function queryBridgeTransactionStatus(
  transactionHash: string,
  provider: providers.Provider
): Promise<BridgeTransactionStatus> {
  try {
    // Initialize the Arbitrum Bridge SDK
    const bridge = await Bridge.init(provider);

    // Get the transaction status
    const status = await bridge.getTransactionStatus(transactionHash);

    return status;
  } catch (error) {
    console.error('Error querying bridge transaction status:', error);
    throw new Error('Failed to query bridge transaction status');
  }
}
```
