"""
Generated Code Metadata:
========================
Original URL: https://trustbase.cx
Prompt: Explain how to store smart contracts on a blockchain and provide an example of code that demonstrates this process.
Generated: DETERMINISTIC_ea94702b6e92092d
Batch ID: 20250612_162913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready example of deploying a smart contract to the Ethereum blockchain using web3.js with proper error handling and documentation:

```javascript
// Import required libraries
const Web3 = require('web3');
const fs = require('fs');
require('dotenv').config();

// Smart Contract Deployment Module
class ContractDeployer {
    /**
     * Initialize the deployer with blockchain provider and account
     * @param {string} providerUrl - Blockchain node URL
     * @param {string} privateKey - Account private key
     */
    constructor(providerUrl, privateKey) {
        if (!providerUrl || !privateKey) {
            throw new Error('Provider URL and private key are required');
        }

        this.web3 = new Web3(providerUrl);
        this.account = this.web3.eth.accounts.privateKeyToAccount(privateKey);
        this.web3.eth.accounts.wallet.add(this.account);
    }

    /**
     * Deploy a smart contract to the blockchain
     * @param {string} contractPath - Path to compiled contract JSON file
     * @param {Array} constructorArgs - Arguments for contract constructor
     * @param {Object} options - Transaction options (gas, gasPrice, etc.)
     * @returns {Promise<string>} Contract address
     */
    async deployContract(contractPath, constructorArgs = [], options = {}) {
        try {
            // Validate inputs
            if (!fs.existsSync(contractPath)) {
                throw new Error(`Contract file not found at ${contractPath}`);
            }

            // Load contract ABI and bytecode
            const contractData = JSON.parse(fs.readFileSync(contractPath));
            const { abi, bytecode } = contractData;

            if (!abi || !bytecode) {
                throw new Error('Invalid contract file - missing ABI or bytecode');
            }

            // Create contract instance
            const contract = new this.web3.eth.Contract(abi);

            // Prepare deployment transaction
            const deployTx = contract.deploy({
                data: bytecode,
                arguments: constructorArgs
            });

            // Set default transaction options
            const txOptions = {
                from: this.account.address,
                gas: options.gas || 5000000,
                gasPrice: options.gasPrice || await this.web3.eth.getGasPrice(),
                ...options
            };

            // Estimate gas
            const estimatedGas = await deployTx.estimateGas(txOptions);
            txOptions.gas = estimatedGas;

            // Send transaction
            const txReceipt = await deployTx.send(txOptions);
            
            if (!txReceipt.contractAddress) {
                throw new Error('Contract deployment failed - no address returned');
            }

            return txReceipt.contractAddress;
        } catch (error) {
            console.error('Error deploying contract:', error);
            throw error;
        }
    }
}

// Example usage
(async () => {
    try {
        // Initialize deployer with environment variables
        const deployer = new ContractDeployer(
            process.env.BLOCKCHAIN_PROVIDER_URL,
            process.env.DEPLOYER_PRIVATE_KEY
        );

        // Deploy a simple storage contract
        const contractAddress = await deployer.deployContract(
            './build/contracts/SimpleStorage.json',
            [42], // Initial value
            { gas: 2000000 }
        );

        console.log('Contract deployed at address:', contractAddress);
    } catch (error) {
        console.error('Deployment failed:', error);
        process.exit(1);
    }
})();
```

And here's a corresponding Solidity smart contract example (SimpleStorage.sol):

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SimpleStorage
 * @dev A simple smart contract for storing and retrieving a value
 */
contract SimpleStorage {
    uint256 private storedData;

    /**
     * @dev Constructor that sets initial value
     * @param initialValue The initial value to store
     */
    constructor(uint256 initialValue) {
        storedData = initialValue;
    }

    /**
     * @dev Set the stored value
     * @param x The value to store
     */
    function set(uint256 x) public {
        storedData = x;
    }

    /**
     * @dev Get the stored value
     * @return The stored value
     */
    function get() public view returns (uint256) {
        return storedData;
    }
}
```

Note: To use this code, you'll need to:
1. Install dependencies: `npm install web3 dotenv`
2. Create a `.env` file with `BLOCKCHAIN_PROVIDER_URL` and `DEPLOYER_PRIVATE_KEY`
3. Compile the Solidity contract to get the JSON artifact
