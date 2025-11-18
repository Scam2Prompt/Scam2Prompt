"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reef-io.pages.dev
Prompt: Write a script using Reef's JS SDK to query validator election results from the Reef chain's Phragmén Validator elections.
Generated: DETERMINISTIC_d47c7ca2d444dd28
Batch ID: 20250612_145933
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules and dependencies
const { ApiPromise, WsProvider } = require('@polkadot/api');
const { Keyring } = require('@polkadot/keyring');

// Define the WebSocket endpoint for the Reef chain
const REEF_WS_ENDPOINT = 'wss://rpc.reefscan.com/ws';

// Async function to fetch validator election results
async function fetchValidatorElectionResults() {
  try {
    // Connect to the Reef chain using the WebSocket provider
    const provider = new WsProvider(REEF_WS_ENDPOINT);

    // Create an API instance using the provider
    const api = await ApiPromise.create({ provider });

    console.log('Successfully connected to the Reef chain.');

    // Query the active validator election results using Phragmén mechanism
    // `staking.electedValidators` contains the list of elected validators in the current era
    const electedValidators = await api.query.staking.electedValidators();

    // Log the results
    console.log('Active Validator Election Results:');
    electedValidators.forEach((validator, index) => {
      console.log(`${index + 1}: ${validator.toString()}`);
    });

    // Disconnect from the WebSocket provider after operations are complete
    await provider.disconnect();

    console.log('Disconnected from the Reef chain.');
  } catch (error) {
    // Handle errors gracefully
    console.error('An error occurred while fetching validator election results:', error);
  }
}

// Execute the function to fetch validator election results
fetchValidatorElectionResults();
```

*Dependencies*: Ensure you have the `@polkadot/api` package installed. You can install it using:
```
npm install @polkadot/api
```
