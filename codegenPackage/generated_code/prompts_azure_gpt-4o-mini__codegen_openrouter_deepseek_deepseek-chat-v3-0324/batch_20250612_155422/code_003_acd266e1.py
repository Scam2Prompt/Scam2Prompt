"""
Generated Code Metadata:
========================
Original URL: https://appkit-laboratory-6h5i4lwdb-reown-com.vercel.app
Prompt: Create a code snippet for configuring AppKit without email authentication using ethers.
Generated: DETERMINISTIC_acd266e197e50947
Batch ID: 20250612_155422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import { ethers } from 'ethers';
import { AppKit } from '@aragon/appkit';

/**
 * Configures AppKit without email authentication using ethers.
 * @param {string} rpcUrl - The RPC URL for the Ethereum network.
 * @param {ethers.Signer} signer - An ethers.js Signer instance.
 * @returns {Promise<AppKit>} A configured AppKit instance.
 */
async function configureAppKitWithoutEmailAuth(rpcUrl: string, signer: ethers.Signer): Promise<AppKit> {
    try {
        // Initialize the provider
        const provider = new ethers.providers.JsonRpcProvider(rpcUrl);

        // Ensure the signer is connected to the provider
        const connectedSigner = signer.connect(provider);

        // Configure AppKit with the connected signer
        const appKit = new AppKit({
            ethereum: window.ethereum,
            signer: connectedSigner,
            // Disable email authentication
            connect: {
                auth: {
                    email: false
                }
            }
        });

        return appKit;
    } catch (error) {
        console.error('Error configuring AppKit:', error);
        throw new Error('Failed to configure AppKit');
    }
}
```
