"""
Generated Code Metadata:
========================
Original URL: https://consensysmedia.net
Prompt: Generate sample code for integrating MetaMask Snaps to customize wallet functionality, referencing the features highlighted in Consensys' announcement.
Generated: DETERMINISTIC_88bff0c21d1534f7
Batch ID: 20250612_153812
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://registry.npmjs.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/example/custom-wallet-snap.git": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries and types
import { SnapManifest, SnapPermissions } from '@metamask/snap-types';
import { JsonRpcRequest } from '@metamask/types';

// Interface for custom RPC methods
interface CustomRpcMethods {
  customMethod: (param: string) => Promise<string>;
}

// Snap Manifest - defines the snap's metadata and permissions
const snapManifest: SnapManifest = {
  version: '1.0.0',
  proposedName: 'CustomWalletSnap',
  description: 'A custom wallet snap to extend MetaMask functionality',
  repository: {
    type: 'git',
    url: 'https://github.com/example/custom-wallet-snap.git',
  },
  source: {
    shasum: 'xyz123',
    location: {
      npm: {
        filePath: 'dist/bundle.js',
        packageName: 'custom-wallet-snap',
        registry: 'https://registry.npmjs.org/',
      },
    },
  },
  initialPermissions: {
    'snap_confirm': {},
    'snap_notify': {},
    'snap_getBip44Entropy': {
      coinType: 60, // ETH
    },
  },
};

// Main snap implementation
const walletSnap = {
  // Handle incoming RPC requests
  async onRpcRequest(request: JsonRpcRequest): Promise<any> {
    try {
      switch (request.method) {
        case 'customMethod':
          return await this.handleCustomMethod(request.params[0]);
        case 'anotherMethod':
          return await this.handleAnotherMethod();
        default:
          throw new Error('Method not found.');
      }
    } catch (error) {
      console.error(`RPC request failed: ${request.method}`, error);
      throw error;
    }
  },

  // Example custom method implementation
  async handleCustomMethod(param: string): Promise<string> {
    const approved = await snap.request({
      method: 'snap_confirm',
      params: [
        {
          prompt: 'Confirm Custom Action',
          description: 'Do you want to perform this custom action?',
          textAreaContent: `Parameter: ${param}`,
        },
      ],
    });

    if (!approved) {
      throw new Error('User rejected the request.');
    }

    // Perform custom logic here
    const result = `Processed: ${param}`;
    
    // Notify user
    await snap.request({
      method: 'snap_notify',
      params: {
        type: 'inApp',
        message: `Action completed: ${result}`,
      },
    });

    return result;
  },

  // Another example method
  async handleAnotherMethod(): Promise<any> {
    // Get BIP44 entropy for Ethereum
    const entropy = await snap.request({
      method: 'snap_getBip44Entropy',
      params: {
        coinType: 60,
      },
    });

    // Use the entropy for custom wallet operations
    return {
      derivedAddress: this.deriveAddressFromEntropy(entropy),
    };
  },

  // Helper method to derive address from entropy
  deriveAddressFromEntropy(entropy: any): string {
    // Implementation would use actual cryptographic operations
    return '0x' + Math.random().toString(16).substr(2, 40);
  },
};

// Register the snap with MetaMask
if (typeof snap !== 'undefined') {
  snap.registerRpcMessageHandler(walletSnap.onRpcRequest.bind(walletSnap));
}

// Export types and main functionality
export { snapManifest, walletSnap, CustomRpcMethods };
```
