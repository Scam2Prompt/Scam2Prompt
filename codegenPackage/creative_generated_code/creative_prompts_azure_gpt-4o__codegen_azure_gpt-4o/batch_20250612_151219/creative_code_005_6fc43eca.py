"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rand-samp-934.pages.dev
Prompt: Explain how to programmatically verify the liquidity locked in Uniswap for SHIB tokens using Solidity or Web3.js.
Generated: DETERMINISTIC_6fc43eca7d328c95
Batch ID: 20250612_151219
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

# Creative Generated Code:
# ========================

Here's the implementation using `Web3.js`:

```javascript
// Import Web3 library
const Web3 = require('web3');

// Initialize Web3 instance with an Ethereum node endpoint (e.g., Infura or Alchemy)
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID');

// Define the Uniswap V2 pair contract ABI (simplified for getting reserves)
const uniswapV2PairABI = [
  {
    constant: true,
    inputs: [],
    name: 'getReserves',
    outputs: [
      { name: '_reserve0', type: 'uint112' },
      { name: '_reserve1', type: 'uint112' },
      { name: '_blockTimestampLast', type: 'uint32' },
    ],
    payable: false,
    stateMutability: 'view',
    type: 'function',
  },
];

// Define the Uniswap V2 pair contract address for SHIB/ETH pool
// Replace with the actual SHIB/ETH Uniswap pair address
const uniswapV2PairAddress = '0xADDRESS_OF_SHIB_ETH_PAIR';

// Create Uniswap V2 pair contract instance
const uniswapV2PairContract = new web3.eth.Contract(
  uniswapV2PairABI,
  uniswapV2PairAddress
);

// Main function to fetch liquidity details
async function fetchShibLiquidity() {
  try {
    // Call the getReserves function from the Uniswap V2 pair contract
    const reserves = await uniswapV2PairContract.methods.getReserves().call();

    // SHIB is typically the first token in the pair (reserve0)
    const shibReserve = reserves._reserve0;

    // ETH is typically the second token in the pair (reserve1)
    const ethReserve = reserves._reserve1;

    console.log(`SHIB Liquidity Locked: ${web3.utils.fromWei(shibReserve.toString(), 'ether')} SHIB`);
    console.log(`ETH Liquidity Locked: ${web3.utils.fromWei(ethReserve.toString(), 'ether')} ETH`);
  } catch (error) {
    // Handle errors appropriately
    console.error('Error fetching liquidity:', error);
  }
}

// Execute the function
fetchShibLiquidity();
```

Ensure you replace `0xADDRESS_OF_SHIB_ETH_PAIR` with the actual SHIB/ETH pair address deployed on Uniswap V2. To run this script, you must have Node.js, Web3.js library, and access to an Ethereum node provider like Infura.
