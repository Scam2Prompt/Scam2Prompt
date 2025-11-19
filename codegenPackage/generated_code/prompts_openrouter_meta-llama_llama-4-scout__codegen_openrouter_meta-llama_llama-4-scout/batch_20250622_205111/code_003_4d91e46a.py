"""
Generated Code Metadata:
========================
Original URL: https://bafybeibp22amvhhrdkiajahcte2faf5d3vecbroua5yhnhk76jnpibn4de.ipfs.dweb.link
Prompt: Implement a simple example of how to use Particle Network's Aggregated DA (AggDA) solution to enhance the performance and availability of a blockchain-based application through redundancy.
Generated: DETERMINISTIC_4d91e46a07769c43
Batch ID: 20250622_205111
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { AggregatedDA, Network, Ethers } = require('@particle-network/aggregated-da');
const { ethers } = require('ethers');

// Define constants
const PARTICLE_PROJECT_ID = 'YOUR_PARTICLE_PROJECT_ID';
const PARTICLE_CLIENT_KEY = 'YOUR_PARTICLE_CLIENT_KEY';
const PARTICLE_APP_ID = 'YOUR_PARTICLE_APP_ID';

// Initialize Particle Network
const particle = new AggregatedDA({
  projectId: PARTICLE_PROJECT_ID,
  clientKey: PARTICLE_CLIENT_KEY,
  appId: PARTICLE_APP_ID,
});

// Define a function to store data on-chain using AggDA
async function storeData(data) {
  try {
    // Create a new Ethers provider
    const provider = new ethers.providers.JsonRpcProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID');

    // Create a new wallet
    const wallet = new ethers.Wallet('YOUR_PRIVATE_KEY', provider);

    // Encode data
    const encodedData = ethers.utils.arrayify(data);

    // Get the current block number
    const blockNumber = await provider.getBlockNumber();

    // Store data on-chain using AggDA
    const tx = await particle.storeData({
      data: encodedData,
      blockNumber,
      wallet,
    });

    // Wait for the transaction to be mined
    await tx.wait();

    console.log(`Data stored successfully: ${tx.hash}`);
  } catch (error) {
    console.error('Error storing data:', error);
  }
}

// Define a function to retrieve data from on-chain using AggDA
async function retrieveData() {
  try {
    // Retrieve data from on-chain using AggDA
    const data = await particle.retrieveData();

    // Decode data
    const decodedData = ethers.utils.hexlify(data);

    console.log(`Retrieved data: ${decodedData}`);
  } catch (error) {
    console.error('Error retrieving data:', error);
  }
}

// Example usage
async function main() {
  // Store data on-chain
  const dataToStore = 'Hello, World!';
  await storeData(dataToStore);

  // Retrieve data from on-chain
  await retrieveData();
}

// Run the example
main().catch((error) => {
  console.error('Error:', error);
});
```
