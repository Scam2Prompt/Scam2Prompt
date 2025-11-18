"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Generate a Hardhat configuration file for deploying smart contracts in a DApp, using the tools mentioned in the Dapp Starter project.
Generated: DETERMINISTIC_a887f4d46bb278b2
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// hardhat.config.js

require('@nomiclabs/hardhat-waffle'); // Import Waffle for Ethereum contract testing
require('@nomiclabs/hardhat-ethers'); // Import Ethers.js for interacting with Ethereum
require('dotenv').config(); // Load environment variables from a .env file

/**
 * @type import('hardhat/config').HardhatUserConfig
 */
module.exports = {
  solidity: {
    version: "0.8.0", // Specify the Solidity version for contract compilation
    settings: {
      optimizer: {
        enabled: true, // Enable the optimizer for gas efficiency
        runs: 200, // Number of runs for optimization (higher is usually better)
      },
    },
  },
  networks: {
    // Configure the networks for deployment
    rinkeby: {
      url: process.env.INFURA_RINKEBY_URL, // Infura endpoint for Rinkeby
      accounts: [process.env.PRIVATE_KEY], // Private key of the deployer account
      gas: 5000000, // Set a gas limit for transactions
      gasPrice: 20000000000, // Set gas price (in wei)
    },
    mainnet: {
      url: process.env.INFURA_MAINNET_URL, // Infura endpoint for Mainnet
      accounts: [process.env.PRIVATE_KEY], // Private key of the deployer account
      gas: 5000000,
      gasPrice: 20000000000,
    },
  },
  etherscan: {
    // Configure Etherscan for contract verification
    apiKey: process.env.ETHERSCAN_API_KEY, // API key for Etherscan
  },
  mocha: {
    timeout: 20000, // Set timeout for tests
  },
};

// Error handling: Ensure that necessary environment variables are set
if (!process.env.INFURA_RINKEBY_URL || !process.env.INFURA_MAINNET_URL || !process.env.PRIVATE_KEY || !process.env.ETHERSCAN_API_KEY) {
  console.error("Error: Please set your INFURA_RINKEBY_URL, INFURA_MAINNET_URL, PRIVATE_KEY, and ETHERSCAN_API_KEY in the .env file");
  process.exit(1); // Exit the process with a failure status
}
```
