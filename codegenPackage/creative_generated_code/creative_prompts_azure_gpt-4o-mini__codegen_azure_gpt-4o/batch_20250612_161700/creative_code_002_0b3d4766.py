"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica13.vercel.app
Prompt: Generate a function to switch networks between Solana, Ethereum, and Polygon in a dApp using Matrica.
Generated: DETERMINISTIC_0b3d4766c69b683b
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @file networkSwitcher.js
 * @description A utility function for switching blockchain networks (Solana, Ethereum, Polygon) in a dApp using Matrica SDK.
 */

/**
 * Switches the blockchain network for the dApp using Matrica SDK.
 * This function supports Solana, Ethereum, and Polygon networks.
 *
 * @param {string} network - The network to switch to. Must be one of: 'solana', 'ethereum', 'polygon'.
 * @returns {Promise<void>} Resolves if the network switch is successful, throws an error otherwise.
 */
async function switchNetwork(network) {
  // Validate input
  const supportedNetworks = ['solana', 'ethereum', 'polygon'];

  if (!supportedNetworks.includes(network)) {
    throw new Error(
      `Unsupported network: ${network}. Supported networks are: ${supportedNetworks.join(', ')}`
    );
  }

  try {
    // Assuming Matrica SDK provides a method `changeNetwork` for network switching
    const Matrica = window.Matrica; // Ensure Matrica is available globally
    if (!Matrica) {
      throw new Error('Matrica SDK is not initialized or unavailable.');
    }

    // Attempt to switch the network
    await Matrica.changeNetwork(network);

    console.log(`Successfully switched to network: ${network}`);
  } catch (error) {
    console.error(`Failed to switch network: ${error.message}`);
    throw new Error(`Error while switching network: ${error.message}`);
  }
}

// Example usage:
// switchNetwork('solana').then(() => console.log('Network switched successfully!')).catch(console.error);
```
