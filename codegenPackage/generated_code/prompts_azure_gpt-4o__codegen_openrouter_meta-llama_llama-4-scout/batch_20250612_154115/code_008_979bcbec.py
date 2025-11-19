"""
Generated Code Metadata:
========================
Original URL: https://debridge-finance.org
Prompt: Generate a technical overview of how deBridge utilizes Chainlink oracles for cross-chain transfers, with an example implementation in a DeFi protocol.
Generated: DETERMINISTIC_979bcbeccd496405
Batch ID: 20250612_154115
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://bsc-dataseed1.binance.org": {
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
// debridge.js

/**
 * deBridge utilizes Chainlink oracles for cross-chain transfers.
 * This module demonstrates how to integrate Chainlink oracles into a DeFi protocol.
 */

const Web3 = require('web3');
const { ChainlinkOracle } = require('./chainlink-oracle');

/**
 * deBridge configuration
 */
const deBridgeConfig = {
  // Ethereum mainnet provider URL
  ethProviderUrl: 'https://mainnet.infura.io/v3/YOUR_PROJECT_ID',
  // Binance Smart Chain mainnet provider URL
  bscProviderUrl: 'https://bsc-dataseed1.binance.org',
  // Chainlink oracle address
  chainlinkOracleAddress: '0x...ChainlinkOracleAddress...',
};

/**
 * Initialize Web3 providers
 */
const web3 = new Web3(new Web3.providers.HttpProvider(deBridgeConfig.ethProviderUrl));
const bscWeb3 = new Web3(new Web3.providers.HttpProvider(deBridgeConfig.bscProviderUrl));

/**
 * Initialize Chainlink oracle
 */
const chainlinkOracle = new ChainlinkOracle(
  deBridgeConfig.chainlinkOracleAddress,
  web3
);

/**
 * Get the current price of an asset from Chainlink oracle
 * @param {string} asset - Asset symbol (e.g. ETH, BTC)
 * @returns {Promise<number>} Asset price in USD
 */
async function getAssetPrice(asset) {
  try {
    const price = await chainlinkOracle.getPrice(asset);
    return price;
  } catch (error) {
    console.error(`Error getting asset price: ${error.message}`);
    throw error;
  }
}

/**
 * Perform a cross-chain transfer using deBridge and Chainlink oracle
 * @param {string} fromChain - Source chain (e.g. Ethereum, Binance Smart Chain)
 * @param {string} toChain - Destination chain (e.g. Ethereum, Binance Smart Chain)
 * @param {string} asset - Asset symbol (e.g. ETH, BTC)
 * @param {number} amount - Amount to transfer
 * @returns {Promise<string>} Transaction hash
 */
async function performCrossChainTransfer(fromChain, toChain, asset, amount) {
  try {
    // Get the current asset price from Chainlink oracle
    const assetPrice = await getAssetPrice(asset);

    // Calculate the transfer amount based on the asset price
    const transferAmount = amount * assetPrice;

    // Perform the cross-chain transfer using deBridge
    let transaction;
    if (fromChain === 'Ethereum') {
      // Perform transfer from Ethereum to Binance Smart Chain
      transaction = await deBridgeTransferFromEthereum(
        toChain,
        asset,
        transferAmount
      );
    } else if (fromChain === 'Binance Smart Chain') {
      // Perform transfer from Binance Smart Chain to Ethereum
      transaction = await deBridgeTransferFromBinanceSmartChain(
        toChain,
        asset,
        transferAmount
      );
    } else {
      throw new Error(`Unsupported chain: ${fromChain}`);
    }

    return transaction.hash;
  } catch (error) {
    console.error(`Error performing cross-chain transfer: ${error.message}`);
    throw error;
  }
}

// Example usage
async function main() {
  try {
    const fromChain = 'Ethereum';
    const toChain = 'Binance Smart Chain';
    const asset = 'ETH';
    const amount = 1;

    const transactionHash = await performCrossChainTransfer(
      fromChain,
      toChain,
      asset,
      amount
    );

    console.log(`Cross-chain transfer transaction hash: ${transactionHash}`);
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

main();
```

```javascript
// chainlink-oracle.js

/**
 * Chainlink oracle integration
 */

const Web3 = require('web3');

/**
 * Chainlink oracle contract ABI
 */
const chainlinkOracleAbi = [
  {
    inputs: [],
    stateMutability: 'nonpayable',
    type: 'constructor',
  },
  {
    inputs: [
      {
        internalType: 'bytes32',
        name: '_base',
        type: 'bytes32',
      },
    ],
    name: 'getPrice',
    outputs: [
      {
        internalType: 'int256',
        name: '',
        type: 'int256',
      },
    ],
    stateMutability: 'view',
    type: 'function',
  },
];

/**
 * Chainlink oracle contract
 */
class ChainlinkOracle {
  constructor(address, web3) {
    this.address = address;
    this.web3 = web3;
    this.contract = new web3.eth.Contract(chainlinkOracleAbi, address);
  }

  /**
   * Get the current price of an asset from Chainlink oracle
   * @param {string} asset - Asset symbol (e.g. ETH, BTC)
   * @returns {Promise<number>} Asset price in USD
   */
  async getPrice(asset) {
    const base = web3.utils.keccak256(asset);
    const price = await this.contract.methods.getPrice(base).call();
    return price / 1e18; // Normalize price to 18 decimal places
  }
}

module.exports = { ChainlinkOracle };
```

```javascript
// de-bridge-transfer.js

/**
 * deBridge transfer functions
 */

const Web3 = require('web3');

/**
 * deBridge transfer contract ABI
 */
const deBridgeTransferAbi = [
  {
    inputs: [],
    stateMutability: 'nonpayable',
    type: 'constructor',
  },
  {
    inputs: [
      {
        internalType: 'address',
        name: '_to',
        type: 'address',
      },
      {
        internalType: 'uint256',
        name: '_amount',
        type: 'uint256',
      },
    ],
    name: 'transferFromEthereum',
    outputs: [],
    stateMutability: 'nonpayable',
    type: 'function',
  },
  {
    inputs: [
      {
        internalType: 'address',
        name: '_to',
        type: 'address',
      },
      {
        internalType: 'uint256',
        name: '_amount',
        type: 'uint256',
      },
    ],
    name: 'transferFromBinanceSmartChain',
    outputs: [],
    stateMutability: 'nonpayable',
    type: 'function',
  },
];

/**
 * deBridge transfer contract
 */
class deBridgeTransfer {
  constructor(address, web3) {
    this.address = address;
    this.web3 = web3;
    this.contract = new web3.eth.Contract(deBridgeTransferAbi, address);
  }

  /**
   * Perform transfer from Ethereum to Binance Smart Chain
   * @param {string} toChain - Destination chain (e.g. Binance Smart Chain)
   * @param {string} asset - Asset symbol (e.g. ETH, BTC)
   * @param {number} amount - Amount to transfer
   * @returns {Promise<string>} Transaction hash
   */
  async transferFromEthereum(toChain, asset, amount) {
    const toAddress = '0x...toAddress...';
    const transaction = await this.contract.methods.transferFromEthereum(
      toAddress,
      amount
    ).send({ from: '0x...fromAddress...' });
    return transaction;
  }

  /**
   * Perform transfer from Binance Smart Chain to Ethereum
   * @param {string} toChain - Destination chain (e.g. Ethereum)
   * @param {string} asset - Asset symbol (e.g. ETH, BTC)
   * @param {number} amount - Amount to transfer
   * @returns {Promise<string>} Transaction hash
   */
  async transferFromBinanceSmartChain(toChain, asset, amount) {
    const toAddress = '0x...toAddress...';
    const transaction = await this.contract.methods.transferFromBinanceSmartChain(
      toAddress,
      amount
    ).send({ from: '0x...fromAddress...' });
    return transaction;
  }
}

module.exports = { deBridgeTransfer };
```
