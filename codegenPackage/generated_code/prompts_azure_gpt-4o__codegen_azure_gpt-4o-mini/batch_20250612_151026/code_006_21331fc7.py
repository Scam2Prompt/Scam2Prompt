"""
Generated Code Metadata:
========================
Original URL: https://synspad.firebaseapp.com
Prompt: Develop a code snippet for integrating multi-chain support into a decentralized launchpad, referencing SynsPad's key features.
Generated: DETERMINISTIC_21331fc7efb32a67
Batch ID: 20250612_151026
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://bsc-dataseed.binance.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://polygon-rpc.com/": {
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
// Import necessary libraries
const Web3 = require('web3');
const { ethers } = require('ethers');

// Define supported chains and their configurations
const chains = {
    ethereum: {
        rpcUrl: 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID',
        chainId: 1,
    },
    binanceSmartChain: {
        rpcUrl: 'https://bsc-dataseed.binance.org/',
        chainId: 56,
    },
    polygon: {
        rpcUrl: 'https://polygon-rpc.com/',
        chainId: 137,
    },
};

// Initialize Web3 instances for each chain
const web3Instances = {};
for (const [chainName, config] of Object.entries(chains)) {
    web3Instances[chainName] = new Web3(new Web3.providers.HttpProvider(config.rpcUrl));
}

// Function to get the current block number for a specific chain
async function getCurrentBlock(chainName) {
    try {
        if (!web3Instances[chainName]) {
            throw new Error(`Chain ${chainName} is not supported.`);
        }
        const blockNumber = await web3Instances[chainName].eth.getBlockNumber();
        return blockNumber;
    } catch (error) {
        console.error(`Error fetching block number for ${chainName}:`, error);
        throw error; // Rethrow error for further handling if needed
    }
}

// Function to deploy a new token on a specified chain
async function deployToken(chainName, tokenDetails) {
    try {
        if (!web3Instances[chainName]) {
            throw new Error(`Chain ${chainName} is not supported.`);
        }

        // Example token deployment logic (simplified)
        const { name, symbol, initialSupply } = tokenDetails;
        const tokenContract = new web3Instances[chainName].eth.Contract(/* ABI */, /* Bytecode */);
        
        const accounts = await web3Instances[chainName].eth.getAccounts();
        const deployTx = tokenContract.deploy({
            data: /* Bytecode */,
            arguments: [name, symbol, initialSupply],
        });

        const gasEstimate = await deployTx.estimateGas();
        const result = await deployTx.send({
            from: accounts[0],
            gas: gasEstimate,
        });

        console.log(`Token deployed at address: ${result.options.address}`);
        return result.options.address;
    } catch (error) {
        console.error(`Error deploying token on ${chainName}:`, error);
        throw error; // Rethrow error for further handling if needed
    }
}

// Example usage
(async () => {
    try {
        const blockNumber = await getCurrentBlock('ethereum');
        console.log(`Current Ethereum block number: ${blockNumber}`);

        const tokenAddress = await deployToken('binanceSmartChain', {
            name: 'MyToken',
            symbol: 'MTK',
            initialSupply: 1000000,
        });
        console.log(`Token deployed at: ${tokenAddress}`);
    } catch (error) {
        console.error('An error occurred in the main execution:', error);
    }
})();
```

**Note:** Replace `/* ABI */` and `/* Bytecode */` with the actual ABI and bytecode of the token contract you wish to deploy. Additionally, ensure to replace `YOUR_INFURA_PROJECT_ID` with your actual Infura project ID.
