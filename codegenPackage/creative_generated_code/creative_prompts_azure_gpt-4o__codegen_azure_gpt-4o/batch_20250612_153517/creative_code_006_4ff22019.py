"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitrock.pages.dev
Prompt: Generate a step-by-step guide for connecting the Bitrock Wallet to popular EVM chains using Web3.js.
Generated: DETERMINISTIC_4ff22019bd5caa60
Batch ID: 20250612_153517
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://rpc.ftm.tools/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.avax.network/ext/bc/C/rpc": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
const Web3 = require('web3');

// Step 1: Define a function to create a Web3 instance for a given EVM chain
/**
 * Connects to an EVM-compatible blockchain using Web3.js.
 * @param {string} rpcUrl - The RPC URL of the EVM chain.
 * @returns {Web3} - A Web3 instance connected to the specified chain.
 */
function connectToEVMChain(rpcUrl) {
  try {
    // Validate the RPC URL
    if (!rpcUrl || typeof rpcUrl !== 'string') {
      throw new Error('Invalid RPC URL provided.');
    }
    
    // Create a new Web3 instance
    const web3 = new Web3(new Web3.providers.HttpProvider(rpcUrl));
    
    // Check connection by fetching the latest block number
    web3.eth.getBlockNumber()
      .then(blockNumber => {
        console.log(`Connected to chain. Latest Block Number: ${blockNumber}`);
      })
      .catch(err => {
        throw new Error(`Failed to connect to chain: ${err.message}`);
      });
      
    // Return the Web3 instance
    return web3;
  } catch (error) {
    console.error(`Error: ${error.message}`);
    return null;
  }
}

// Step 2: Define a list of popular EVM chains and their RPC URLs
const evmChains = [
  { name: 'Ethereum Mainnet', rpcUrl: 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID' },
  { name: 'Binance Smart Chain', rpcUrl: 'https://bsc-dataseed.binance.org/' },
  { name: 'Polygon', rpcUrl: 'https://polygon-rpc.com/' },
  { name: 'Avalanche', rpcUrl: 'https://api.avax.network/ext/bc/C/rpc' },
  { name: 'Fantom', rpcUrl: 'https://rpc.ftm.tools/' }
];

// Step 3: Connect to each chain and log the status
/**
 * Connects to all popular EVM chains and logs the connection status.
 */
function connectToPopularEVMChains() {
  evmChains.forEach(chain => {
    console.log(`Attempting to connect to ${chain.name}...`);
    const web3Instance = connectToEVMChain(chain.rpcUrl);
    
    if (web3Instance) {
      console.log(`Successfully connected to ${chain.name}`);
    } else {
      console.log(`Failed to connect to ${chain.name}`);
    }
  });
}

// Step 4: Call the function to start connections
connectToPopularEVMChains();
```

**Notes:**
- Replace `YOUR_INFURA_PROJECT_ID` with your actual Infura project ID for Ethereum Mainnet.
- Ensure that Web3.js (`npm install web3`) is installed in your project before running the script.
- Additional chains can be added to the `evmChains` array as needed.
