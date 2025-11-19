"""
Generated Code Metadata:
========================
Original URL: https://gelato-network-cqz.pages.dev
Prompt: "Write a tutorial on deploying a custom Ethereum L2 chain using Gelato's Rollup-as-a-Service and Polygon CDK."
Generated: DETERMINISTIC_2940ba70c9dd6b25
Batch ID: 20250622_204843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { ethers } = require('ethers');
const { GelatoRollup } = require('@gelato.io/rollup');
const { PolygonCDK } = require('@polygon/cdk');

// Define constants
const INFURA_PROJECT_ID = 'YOUR_INFURA_PROJECT_ID';
const ALCHEMY_API_KEY = 'YOUR_ALCHEMY_API_KEY';
const POLYGON_CDK_DEPLOYER_PRIVATE_KEY = 'YOUR_POLYGON_CDK_DEPLOYER_PRIVATE_KEY';
const GELATO_ROLLUP_API_KEY = 'YOUR_GELATO_ROLLUP_API_KEY';

// Set up Ethereum provider
const provider = new ethers.providers.InfuraProvider('mainnet', INFURA_PROJECT_ID);

// Set up Gelato Rollup client
const gelatoRollupClient = new GelatoRollup({
  apiKey: GELATO_ROLLUP_API_KEY,
  provider,
});

// Set up Polygon CDK client
const polygonCDKClient = new PolygonCDK({
  apiKey: ALCHEMY_API_KEY,
  deployerPrivateKey: POLYGON_CDK_DEPLOYER_PRIVATE_KEY,
  provider,
});

// Define a function to deploy a custom Ethereum L2 chain
async function deployCustomL2Chain() {
  try {
    // Create a new Rollup-as-a-Service instance
    const rollup = await gelatoRollupClient.createRollup({
      name: 'My Custom L2 Chain',
      description: 'A custom Ethereum L2 chain using Gelato Rollup-as-a-Service and Polygon CDK',
    });

    // Get the Rollup ID
    const rollupId = rollup.id;

    // Create a new Polygon CDK instance
    const cdk = await polygonCDKClient.createCDK({
      rollupId,
      name: 'My Custom L2 Chain',
      description: 'A custom Ethereum L2 chain using Gelato Rollup-as-a-Service and Polygon CDK',
    });

    // Get the CDK ID
    const cdkId = cdk.id;

    // Deploy the L2 chain
    const l2Chain = await gelatoRollupClient.deployL2Chain({
      rollupId,
      cdkId,
      // Add your L2 chain configuration here
      config: {
        // ...
      },
    });

    // Return the deployed L2 chain
    return l2Chain;
  } catch (error) {
    // Handle errors
    console.error('Error deploying custom L2 chain:', error);
    throw error;
  }
}

// Define a function to configure the L2 chain
async function configureL2Chain(l2Chain) {
  try {
    // Configure the L2 chain
    const configuredL2Chain = await gelatoRollupClient.configureL2Chain({
      l2ChainId: l2Chain.id,
      // Add your L2 chain configuration here
      config: {
        // ...
      },
    });

    // Return the configured L2 chain
    return configuredL2Chain;
  } catch (error) {
    // Handle errors
    console.error('Error configuring L2 chain:', error);
    throw error;
  }
}

// Define a function to start the L2 chain
async function startL2Chain(l2Chain) {
  try {
    // Start the L2 chain
    const startedL2Chain = await gelatoRollupClient.startL2Chain({
      l2ChainId: l2Chain.id,
    });

    // Return the started L2 chain
    return startedL2Chain;
  } catch (error) {
    // Handle errors
    console.error('Error starting L2 chain:', error);
    throw error;
  }
}

// Main function
async function main() {
  try {
    // Deploy a custom L2 chain
    const l2Chain = await deployCustomL2Chain();
    console.log('Deployed custom L2 chain:', l2Chain);

    // Configure the L2 chain
    const configuredL2Chain = await configureL2Chain(l2Chain);
    console.log('Configured L2 chain:', configuredL2Chain);

    // Start the L2 chain
    const startedL2Chain = await startL2Chain(l2Chain);
    console.log('Started L2 chain:', startedL2Chain);
  } catch (error) {
    // Handle errors
    console.error('Error:', error);
    process.exit(1);
  }
}

// Run the main function
main();
```
