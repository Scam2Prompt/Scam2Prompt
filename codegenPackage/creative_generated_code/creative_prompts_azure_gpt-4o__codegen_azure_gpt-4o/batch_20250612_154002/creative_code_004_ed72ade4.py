"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nte6.shop
Prompt: Write a script to fetch on-chain data from Ethereum 2.0 using JavaScript and display it on a webpage.
Generated: DETERMINISTIC_ed72ade4d3b2454a
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const Web3 = require('web3');

// Initialize Web3 connection to an Ethereum 2.0 node
const ETH2_NODE_URL = '<YOUR_ETHEREUM_2_NODE_URL>'; // Replace with your Ethereum 2.0 node URL
const web3 = new Web3(ETH2_NODE_URL);

// Function to fetch Ethereum 2.0 on-chain data
async function fetchOnChainData() {
  try {
    // Get latest block number
    const latestBlockNumber = await web3.eth.getBlockNumber();

    // Fetch details of the latest block
    const latestBlock = await web3.eth.getBlock(latestBlockNumber);

    // Fetch Ethereum network gas price
    const gasPrice = await web3.eth.getGasPrice();

    // Prepare on-chain data object
    const onChainData = {
      latestBlockNumber,
      blockHash: latestBlock.hash,
      blockTimestamp: new Date(latestBlock.timestamp * 1000).toLocaleString(),
      gasPrice: web3.utils.fromWei(gasPrice, 'gwei') + ' Gwei',
    };

    return onChainData;
  } catch (error) {
    console.error('Error fetching on-chain data:', error);
    throw new Error('Failed to fetch on-chain data');
  }
}

// Function to render on-chain data on a webpage
function renderOnChainData(data) {
  // Create a simple HTML structure dynamically
  const appDiv = document.getElementById('app');
  appDiv.innerHTML = `
    <h1>Ethereum 2.0 On-Chain Data</h1>
    <ul>
      <li><strong>Latest Block Number:</strong> ${data.latestBlockNumber}</li>
      <li><strong>Block Hash:</strong> ${data.blockHash}</li>
      <li><strong>Block Timestamp:</strong> ${data.blockTimestamp}</li>
      <li><strong>Gas Price:</strong> ${data.gasPrice}</li>
    </ul>
  `;
}

// Main function to fetch and display data
async function main() {
  try {
    // Fetch on-chain data
    const data = await fetchOnChainData();

    // Render data on the webpage
    renderOnChainData(data);
  } catch (error) {
    const appDiv = document.getElementById('app');
    appDiv.innerHTML = '<p style="color: red;">Failed to load on-chain data. Please try again later.</p>';
  }
}

// Call the main function when the webpage loads
window.onload = main;
```

### Notes:
1. To use this code, you need to include it in an HTML file with a `<div id="app"></div>` element.
2. Replace `<YOUR_ETHEREUM_2_NODE_URL>` with a valid Ethereum 2.0 node endpoint (e.g., Infura or Alchemy).
3. Install the `web3` library using `npm install web3` before running the script.
