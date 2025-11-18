"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://award-particle.pages.dev
Prompt: Provide an example of using the Particle modular access layer to test multi-chain interactions in a Web3 development environment.
Generated: DETERMINISTIC_ea41ef6b1fcf09f6
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries and modules
const { ParticleNetwork } = require('@particle-network/sdk'); // Particle SDK for Web3
const Web3 = require('web3'); // Web3 library for blockchain interactions

// Define configuration for ParticleNetwork
const particleConfig = {
    chainIds: ['1', '56', '137'], // Ethereum Mainnet, Binance Smart Chain, Polygon
    appId: 'your-app-id', // Replace with your Particle application ID
    clientKey: 'your-client-key', // Replace with your Particle client key
    projectId: 'your-project-id', // Replace with your Particle project ID
};

// Initialize the ParticleNetwork instance
const particleNetwork = new ParticleNetwork(particleConfig);

// Helper function to initialize Web3 instance for a specific chain
function getWeb3Instance(chainId) {
    const rpcUrl = particleNetwork.getRpcUrl(chainId); // Retrieve RPC URL using ParticleNetwork
    return new Web3(new Web3.providers.HttpProvider(rpcUrl)); // Create and return Web3 instance
}

// Function to test multi-chain interactions
async function testMultiChainInteractions() {
    try {
        // Define chains to interact with
        const chains = [
            { chainId: '1', name: 'Ethereum' },
            { chainId: '56', name: 'Binance Smart Chain' },
            { chainId: '137', name: 'Polygon' },
        ];

        // Iterate over each chain and perform Web3 operations
        for (const chain of chains) {
            console.log(`\nConnecting to ${chain.name}...`);
            const web3 = getWeb3Instance(chain.chainId); // Initialize Web3 for the chain

            // Fetch the latest block number
            const latestBlock = await web3.eth.getBlockNumber();
            console.log(`Latest block on ${chain.name}: ${latestBlock}`);

            // Fetch gas price
            const gasPrice = await web3.eth.getGasPrice();
            console.log(`Current gas price on ${chain.name}: ${gasPrice}`);
        }

        console.log('\nMulti-chain interaction test completed successfully.');

    } catch (error) {
        // Handle errors during multi-chain interactions
        console.error('An error occurred during multi-chain interactions:', error.message);
    }
}

// Execute the test function
testMultiChainInteractions();
```

Make sure to replace `your-app-id`, `your-client-key`, and `your-project-id` with the actual credentials from your Particle application setup. Also, install necessary dependencies (`npm install @particle-network/sdk web3`) before running the script.
