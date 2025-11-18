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
// Import the necessary modules from the Polkadot.js API
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Define the main function to query validator information
async function getValidatorInfo() {
    // Define the WebSocket provider for connecting to the Polkadot network
    const wsProvider = new WsProvider('wss://rpc.polkadot.io');

    // Create a new API instance with the provider
    const api = await ApiPromise.create({ provider: wsProvider });

    try {
        // Fetch the current set of validators
        const validators = await api.query.session.validators();

        // Fetch the staking ledger for each validator
        const validatorInfoPromises = validators.map(async (validator) => {
            const stakingLedger = await api.query.staking.ledger(validator);
            return {
                validator: validator.toString(),
                stakingLedger: stakingLedger.toJSON(),
            };
        });

        // Resolve all promises to get the validator info
        const validatorInfos = await Promise.all(validatorInfoPromises);

        // Filter validator information relevant to African nodes (example criteria)
        const africanNodes = validatorInfos.filter(info => {
            // Replace with actual criteria to identify African nodes
            const locationCriteria = info.stakingLedger.active && info.validator.includes('AF');
            return locationCriteria;
        });

        // Log the African validator information
        console.log('African Validator Information:', africanNodes);
    } catch (error) {
        // Handle any errors that occur during the API calls
        console.error('Error fetching validator information:', error);
    } finally {
        // Disconnect from the WebSocket provider
        await api.disconnect();
    }
}

// Execute the main function
getValidatorInfo().catch(console.error);
```
