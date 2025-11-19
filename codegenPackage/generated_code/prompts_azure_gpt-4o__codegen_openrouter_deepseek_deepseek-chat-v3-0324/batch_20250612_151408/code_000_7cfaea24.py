"""
Generated Code Metadata:
========================
Original URL: https://polkadot.africa
Prompt: Write code to interact with the Polkadot blockchain using the Polkadot.js API, specifically for querying validator information relevant to African nodes.
Generated: DETERMINISTIC_7cfaea24194a4294
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required Polkadot.js libraries
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Configuration constants
const WS_ENDPOINT = 'wss://rpc.polkadot.io'; // Mainnet endpoint
const AFRICA_REGION = 'Africa'; // Region filter for validators

// Main function to query African validators
async function queryAfricanValidators() {
    let api;
    try {
        // Initialize the API
        const provider = new WsProvider(WS_ENDPOINT);
        api = await ApiPromise.create({ provider });

        console.log(`Connected to ${WS_ENDPOINT}`);

        // Get the current active era
        const activeEra = await api.query.staking.activeEra();
        const currentEra = activeEra.unwrap().index;

        // Get all validators for the current era
        const validators = await api.query.session.validators();
        const validatorAddresses = validators.toJSON();

        // Get validator information including their identity
        const validatorInfos = await Promise.all(
            validatorAddresses.map(async (address) => {
                const identity = await api.derive.accounts.info(address);
                const stakingInfo = await api.derive.staking.account(address);
                
                return {
                    address,
                    identity: identity.identity,
                    exposure: stakingInfo.stakingLedger,
                    nominators: stakingInfo.nominators
                };
            })
        );

        // Filter validators with African identity
        const africanValidators = validatorInfos.filter(validator => {
            return validator.identity?.display && 
                   validator.identity.display.toLowerCase().includes(AFRICA_REGION.toLowerCase());
        });

        // Display results
        console.log(`Found ${africanValidators.length} validators from ${AFRICA_REGION}:`);
        africanValidators.forEach((validator, index) => {
            console.log(`\nValidator #${index + 1}:`);
            console.log(`Address: ${validator.address}`);
            console.log(`Identity: ${validator.identity.display}`);
            console.log(`Total Stake: ${validator.exposure.total}`);
            console.log(`Nominators: ${validator.nominators?.length || 0}`);
        });

    } catch (error) {
        console.error('Error querying validators:', error);
    } finally {
        // Disconnect from the API when done
        if (api) {
            await api.disconnect();
            console.log('Disconnected from API');
        }
    }
}

// Execute the main function
queryAfricanValidators().catch(console.error);
```
