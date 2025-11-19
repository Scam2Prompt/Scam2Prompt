"""
Generated Code Metadata:
========================
Original URL: https://optimismsio.vercel.app
Prompt: Provide an example of deploying an EVM-compatible decentralized application on an Optimism chain, leveraging the OP Stack.
Generated: DETERMINISTIC_8f07e998b6babb1b
Batch ID: 20250612_150028
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.optimism.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/token/ERC20/ERC20.sol": {
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
const { ethers } = require('hardhat');
const { optimism } = require('hardhat/config');

// Define a function to deploy a contract to Optimism chain
async function deployContract(hre, contractName, args) {
    // Get the Optimism chain configuration
    const optimismConfig = optimism;

    // Create a new ethers provider for the Optimism chain
    const provider = new ethers.providers.JsonRpcProvider(optimismConfig.url);

    // Get the deployer wallet
    const deployer = await ethers.getNamedSigner('deployer');

    // Get the contract factory
    const contractFactory = await ethers.getContractFactory(contractName);

    // Deploy the contract to the Optimism chain
    try {
        const contract = await contractFactory.connect(deployer).deploy(...args);
        await contract.deployed();

        // Log the deployed contract address
        console.log(`Contract ${contractName} deployed to: ${contract.address}`);

        return contract;
    } catch (error) {
        console.error(`Error deploying contract ${contractName}:`, error);
        throw error;
    }
}

// Define a function to verify a contract on Optimism Etherscan
async function verifyContract(hre, contractAddress, args) {
    // Get the Optimism Etherscan API key
    const etherscanApiKey = process.env.OPTIMISM_ETHERSCAN_API_KEY;

    // Verify the contract using Etherscan API
    try {
        await hre.run('verify:verify', {
            address: contractAddress,
            constructorArguments: args,
            etherscan: {
                apiKey: etherscanApiKey,
            },
        });

        console.log(`Contract verified at: ${contractAddress}`);
    } catch (error) {
        console.error(`Error verifying contract:`, error);
        throw error;
    }
}

// Define the main deployment script
async function main() {
    // Get the Hardhat runtime environment
    const hre = require('hardhat');

    // Define the contract name and arguments
    const contractName = 'MyContract';
    const args = ['arg1', 'arg2'];

    // Deploy the contract to Optimism chain
    const contract = await deployContract(hre, contractName, args);

    // Verify the contract on Optimism Etherscan
    await verifyContract(hre, contract.address, args);
}

// Run the main deployment script
main().catch((error) => {
    console.error('Error:', error);
    process.exitCode = 1;
});
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/token/ERC20/ERC20.sol";

contract MyContract {
    // Define a simple ERC20 token
    string public name = 'My Token';
    string public symbol = 'MTK';
    uint256 public totalSupply;

    mapping(address => uint256) public balanceOf;

    constructor(string memory _name, string memory _symbol) ERC20(_name, _symbol) {
        // Mint initial supply
        _mint(msg.sender, 1000 ether);
    }

    // Allow minting of new tokens
    function mint(address _to, uint256 _amount) public {
        _mint(_to, _amount);
    }

    // Allow burning of existing tokens
    function burn(uint256 _amount) public {
        _burn(msg.sender, _amount);
    }
}
```

```javascript
// hardhat.config.js
require('@nomiclabs/hardhat-ethers');
require('@nomiclabs/hardhat-waffle');
require('hardhat-deploy');
require('hardhat-etherscan-optimism');

module.exports = {
    solidity: '0.8.10',
    optimism: {
        url: 'https://mainnet.optimism.io',
        accounts: ['your-private-key'],
    },
    etherscan: {
        optimizer: true,
        runs: 200,
        apiKey: 'your-optimism-etherscan-api-key',
    },
    namedAccounts: {
        deployer: {
            default: 0,
        },
    },
};
```
