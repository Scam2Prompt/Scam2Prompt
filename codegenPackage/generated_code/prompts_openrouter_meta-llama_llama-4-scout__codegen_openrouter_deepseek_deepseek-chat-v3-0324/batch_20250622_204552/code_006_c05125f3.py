"""
Generated Code Metadata:
========================
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: How do I create a contract facet bundle in Zoe using the Agoric SDK, and what is the significance of this bundle in contract development?
Generated: DETERMINISTIC_c05125f369bdced7
Batch ID: 20250622_204552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// @ts-check
import { E } from '@endo/far';
import { makeZoeKit } from '@agoric/zoe';
import bundleSource from '@endo/bundle-source';

/**
 * Creates a contract facet bundle using Zoe and the Agoric SDK.
 * 
 * @param {string} contractPath - Path to the contract source code
 * @returns {Promise<{ bundle: any, zoe: any }>} - Returns the bundle and Zoe instance
 */
async function createContractFacetBundle(contractPath) {
  try {
    // Create a new Zoe instance
    const { zoeService } = makeZoeKit();
    const zoe = E(zoeService);

    // Bundle the contract source code
    const bundle = await bundleSource(contractPath);

    return { bundle, zoe };
  } catch (error) {
    console.error('Error creating contract facet bundle:', error);
    throw error;
  }
}

// Example usage:
// (async () => {
//   const { bundle, zoe } = await createContractFacetBundle('./src/contract.js');
//   console.log('Bundle created successfully:', bundle);
// })();

export { createContractFacetBundle };
```
