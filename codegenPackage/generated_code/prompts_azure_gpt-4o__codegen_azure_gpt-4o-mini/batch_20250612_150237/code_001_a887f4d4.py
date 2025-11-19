"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Generate a Hardhat configuration file for deploying smart contracts in a DApp, using the tools mentioned in the Dapp Starter project.
Generated: DETERMINISTIC_a887f4d46bb278b2
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// hardhat.config.js

require('@nomiclabs/hardhat-waffle'); // Import Waffle for testing and deploying smart contracts
require('@nomiclabs/hardhat-ethers'); // Import Ethers.js for interacting with the Ethereum blockchain
require('dotenv').config(); // Load environment variables from a .env file

/**
 * @type import('hardhat/config').HardhatUserConfig
 */
module.exports = {
  solidity: {
    version: "0.8.4", // Specify the Solidity compiler version
    settings: {
      optimizer: {
        enabled: true, // Enable the optimizer for gas efficiency
        runs: 200, // Set the number of optimization runs
      },
    },
  },
  networks: {
    // Configuration for the Ethereum mainnet
    mainnet: {
      url: process.env.MAINNET_URL, // RPC URL for the mainnet
      accounts: [process.env.MAINNET_PRIVATE_KEY], // Private key for deploying contracts
      gas: 5000000, // Gas limit for transactions
      gasPrice: 20000000000, // Gas price in wei
    },
    // Configuration for the Rinkeby testnet
    rinkeby: {
      url: process.env.RINKEBY_URL, // RPC URL for the Rinkeby testnet
      accounts: [process.env.RINKEBY_PRIVATE_KEY], // Private key for deploying contracts
      gas: 5000000, // Gas limit for transactions
      gasPrice: 20000000000, // Gas price in wei
    },
  },
  // Custom tasks can be defined here
  tasks: {
    // Example task to deploy contracts
    "deploy": {
      description: "Deploys the smart contracts",
      action: async () => {
        const [deployer] = await ethers.getSigners(); // Get the deployer's wallet
        console.log("Deploying contracts with the account:", deployer.address);

        // Example contract deployment
        const ContractFactory = await ethers.getContractFactory("YourContractName");
        const contract = await ContractFactory.deploy(); // Deploy the contract
        await contract.deployed(); // Wait for the contract to be deployed

        console.log("Contract deployed to:", contract.address); // Log the contract address
      },
    },
  },
};

// Error handling for missing environment variables
if (!process.env.MAINNET_URL || !process.env.MAINNET_PRIVATE_KEY) {
  console.error("Please set your MAINNET_URL and MAINNET_PRIVATE_KEY in a .env file");
  process.exit(1); // Exit the process with an error code
}

if (!process.env.RINKEBY_URL || !process.env.RINKEBY_PRIVATE_KEY) {
  console.error("Please set your RINKEBY_URL and RINKEBY_PRIVATE_KEY in a .env file");
  process.exit(1); // Exit the process with an error code
}
```
