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
// Import necessary libraries
const { ApiPromise, WsProvider } = require('@polkadot/api');
const fetch = require('node-fetch');

// Define constants
const WS_PROVIDER_URL = 'wss://rpc.polkadot.io'; // WebSocket provider URL for Polkadot
const AFRICAN_VALIDATOR_IDS = [
    // Replace with actual validator IDs from African validators
    '5F3sa1ZQ7U7R3Gp2bn5eY4pR8R2K8pU2Kp5JZ3yn1K6dQ2Zk', // Example validator ID
    // Add more validator IDs as needed
];

// Function to fetch staking rewards for specified validators
async function fetchStakingRewards() {
    try {
        // Connect to the Polkadot network
        const provider = new WsProvider(WS_PROVIDER_URL);
        const api = await ApiPromise.create({ provider });

        // Fetch the staking rewards for each validator
        const rewards = await Promise.all(AFRICAN_VALIDATOR_IDS.map(async (validatorId) => {
            const exposure = await api.query.staking.erasStakers.entries(await api.query.staking.currentEra());
            const validatorExposure = exposure.find(([key]) => key.args[0].toString() === validatorId);

            if (validatorExposure) {
                const { total: totalNominators, own: ownStake } = validatorExposure[1].toJSON();
                const reward = await api.query.staking.erasRewardPoints(await api.query.staking.currentEra());
                
                return {
                    validatorId,
                    totalNominators,
                    ownStake,
                    reward: reward.toJSON(),
                };
            }

            return {
                validatorId,
                totalNominators: 0,
                ownStake: 0,
                reward: 0,
            };
        }));

        // Log the rewards data
        console.log('Staking Rewards for African Validators:', rewards);
    } catch (error) {
        console.error('Error fetching staking rewards:', error);
    }
}

// Execute the fetching function
fetchStakingRewards();
```

Make sure to install the necessary dependencies by running:
```bash
npm install @polkadot/api node-fetch
```

Replace the `AFRICAN_VALIDATOR_IDS` with actual validator IDs to get real data.
