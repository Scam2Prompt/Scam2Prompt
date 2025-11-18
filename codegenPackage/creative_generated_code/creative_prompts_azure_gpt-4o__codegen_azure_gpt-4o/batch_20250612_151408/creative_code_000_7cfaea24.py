"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot.africa
Prompt: Write code to interact with the Polkadot blockchain using the Polkadot.js API, specifically for querying validator information relevant to African nodes.
Generated: DETERMINISTIC_7cfaea24194a4294
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries from Polkadot.js
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Define a function to interact with the Polkadot blockchain
async function queryAfricanValidators() {
  try {
    // Connect to the Polkadot network via the WebSocket provider
    const wsProvider = new WsProvider('wss://rpc.polkadot.io');
    const api = await ApiPromise.create({ provider: wsProvider });

    console.log('Connected to Polkadot network successfully.');

    // Fetch the list of active validators
    const validators = await api.query.session.validators();

    console.log('Retrieved list of validators.');

    // Define an array to store African validators (identified by specific metadata)
    const africanValidators = [];

    // Iterate through the list of validators
    for (const validator of validators) {
      // Query the identity of the validator (if available)
      const identity = await api.query.identity.identityOf(validator);

      // Check if the validator's identity contains metadata for African regions
      if (identity && identity.info && identity.info.display && identity.info.display.toLowerCase().includes('africa')) {
        // Add the validator to the list of African validators
        africanValidators.push({
          validatorAddress: validator.toString(),
          displayName: identity.info.display.toString(),
        });
      }
    }

    // Log the African validators
    console.log('African validators:', africanValidators);

    // Disconnect from the Polkadot network
    await api.disconnect();

    console.log('Disconnected from Polkadot network successfully.');

    // Return the list of African validators
    return africanValidators;
  } catch (error) {
    // Handle errors gracefully
    console.error('An error occurred while querying African validators:', error.message);
    throw error; // Re-throw the error for further handling if necessary
  }
}

// Execute the function
queryAfricanValidators()
  .then((validators) => {
    // Additional processing of African validators can be performed here
    console.log('Query completed successfully:', validators);
  })
  .catch((error) => {
    console.error('Failed to complete query:', error);
  });

/*
 * Notes:
 * - Ensure that Node.js is installed and the Polkadot.js library is installed via `npm install @polkadot/api`.
 * - African validators are identified by the presence of "Africa" in their identity metadata.
 * - This script assumes validators voluntarily provide accurate metadata in their identity.
 */
```
