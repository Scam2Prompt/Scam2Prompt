"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot.africa
Prompt: Write code to fetch staking rewards data from the Polkadot network, focusing on African validators using Polkadot.js.
Generated: DETERMINISTIC_5ae239f214cc6186
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

// Define an asynchronous function to fetch staking rewards for African validators
async function fetchStakingRewards() {
  try {
    // Connect to a Polkadot node via WebSocket
    const wsProvider = new WsProvider('wss://rpc.polkadot.io'); // Use an appropriate Polkadot RPC endpoint
    const api = await ApiPromise.create({ provider: wsProvider });

    console.log('Connected to the Polkadot network.');

    // Retrieve all validators
    const [validators, validatorPrefs] = await Promise.all([
      api.query.session.validators(),
      api.query.staking.validators.entries(),
    ]);

    // Filter African validators based on identity information
    const africanValidators = [];
    for (const validator of validators) {
      const identity = await api.query.identity.identityOf(validator);
      if (identity.isSome) {
        const { info } = identity.unwrap();
        const displayName = info.display.toHuman();
        const region = info.additional
          .filter(([key]) => key.toHuman() === 'region')
          .map(([, value]) => value.toHuman())[0];

        // Match African validators based on the "region" field or "display" name
        if (region && region.toLowerCase().includes('africa')) {
          africanValidators.push(validator.toString());
        } else if (displayName && displayName.toLowerCase().includes('africa')) {
          africanValidators.push(validator.toString());
        }
      }
    }

    console.log(`Found ${africanValidators.length} African validators.`);

    // Retrieve staking rewards data for the African validators
    const stakingRewards = {};
    for (const validator of africanValidators) {
      const rewardPoints = await api.query.staking.erasRewardPoints.entries();
      stakingRewards[validator] = rewardPoints.map(([eras, score]));
    }
  } catch
