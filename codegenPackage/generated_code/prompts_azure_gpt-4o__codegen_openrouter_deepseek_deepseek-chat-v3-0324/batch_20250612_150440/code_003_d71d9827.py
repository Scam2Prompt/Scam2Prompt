"""
Generated Code Metadata:
========================
Original URL: https://metamask-snap-polkadot.pages.dev
Prompt: Generate code for initializing the Polkadot Wallet Snap in a dApp, referencing the implementation details from the Metamask Snap Polkadot example.
Generated: DETERMINISTIC_d71d9827be2bb261
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries and types
import { SnapProvider } from '@metamask/snap-types';
import { MetamaskPolkadotSnap } from '@chainsafe/metamask-polkadot-adapter/build/snap';
import { getPolkadotSnapApi } from '@chainsafe/metamask-polkadot-adapter/build/api';

// Configuration for the Polkadot Snap
const snapId = 'npm:@chainsafe/polkadot-snap';
const snapConfig = {
  networkName: 'polkadot', // Default network
  wsRpcUrl: 'wss://rpc.polkadot.io', // Default RPC endpoint
};

/**
 * Initialize the Polkadot Snap and return the API instance
 * @param provider - Metamask provider
 * @returns Promise<MetamaskPolkadotSnap>
 */
export async function initPolkadotSnap(provider: SnapProvider): Promise<MetamaskPolkadotSnap> {
  try {
    // Check if the Snap is already installed
    const isSnapInstalled = await provider.request({
      method: 'wallet_getSnaps',
    });

    if (!isSnapInstalled[snapId]) {
      // Install the Snap if not already installed
      await provider.request({
        method: 'wallet_requestSnaps',
        params: {
          [snapId]: {},
        },
      });
    }

    // Configure the Snap with default network settings
    const api = await getPolkadotSnapApi(provider);
    await api.configure(snapConfig);

    return api;
  } catch (error) {
    console.error('Error initializing Polkadot Snap:', error);
    throw new Error(`Failed to initialize Polkadot Snap: ${error.message}`);
  }
}

/**
 * Helper function to check if Polkadot Snap is installed
 * @param provider - Metamask provider
 * @returns Promise<boolean>
 */
export async function isPolkadotSnapInstalled(provider: SnapProvider): Promise<boolean> {
  try {
    const snaps = await provider.request({
      method: 'wallet_getSnaps',
    });
    return !!snaps[snapId];
  } catch (error) {
    console.error('Error checking Polkadot Snap installation:', error);
    return false;
  }
}

/**
 * Helper function to connect to the Polkadot Snap
 * @param provider - Metamask provider
 * @returns Promise<MetamaskPolkadotSnap>
 */
export async function connectPolkadotSnap(provider: SnapProvider): Promise<MetamaskPolkadotSnap> {
  try {
    const api = await getPolkadotSnapApi(provider);
    return api;
  } catch (error) {
    console.error('Error connecting to Polkadot Snap:', error);
    throw new Error(`Failed to connect to Polkadot Snap: ${error.message}`);
  }
}
```
