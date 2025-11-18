"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkabot.io
Prompt: Provide an example of using JavaScript to create a bot that interacts with the Polkadot API to fetch staking rewards data.
Generated: DETERMINISTIC_8d5843136847cd96
Batch ID: 20250612_153755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Define the WebSocket endpoint for a Polkadot node
const wsEndpoint = 'wss://rpc.polkadot.io';

// Function to fetch staking rewards data
async function fetchStakingRewards(address) {
  try {
    // Connect to the Polkadot network via WebSocket
    const provider = new WsProvider(wsEndpoint);
    const api = await ApiPromise.create({ provider });

    // Check if the provided address is valid
    if (!address || !api.registry.chainTokens) {
      throw new Error('Invalid address or network connection.');
    }

    // Fetch staking rewards information for the provided address
    const stakingInfo = await api.query.staking.ledger(address);

    // Handle the case where no staking info is available
    if (!stakingInfo || stakingInfo.isEmpty) {
      console.log(`${address} has no staking rewards.`);
      return;
    }

    // Parse rewards data
    const { active, total } = stakingInfo.toJSON();
    console.log('Address:', address);
    console.log('Active Staking:', active);
    console.log('Total Rewards:', total);

    // Disconnect from the network after fetching the data
    await api.disconnect();
  } catch (error) {
    console.error('Error fetching staking rewards:', error.message);
  }
}

// Example usage: Replace with a valid Polkadot address
const exampleAddress = 'INSERT_VALID_POLKADOT_ADDRESS_HERE';

// Fetch staking rewards for the example address
fetchStakingRewards(exampleAddress);
```

> Note: Replace `'INSERT_VALID_POLKADOT_ADDRESS_HERE'` with a valid Polkadot wallet address for testing purposes. This code assumes you have installed the `@polkadot/api` package: `npm install @polkadot/api`.
