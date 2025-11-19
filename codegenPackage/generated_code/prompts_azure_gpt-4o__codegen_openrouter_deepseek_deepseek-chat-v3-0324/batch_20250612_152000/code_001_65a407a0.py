"""
Generated Code Metadata:
========================
Original URL: https://y45y45y54.pages.dev
Prompt: How can I use the Pyth Network's on-demand oracle to fetch real-time price updates for multiple assets in an EVM-compatible blockchain? Provide code examples.
Generated: DETERMINISTIC_65a407a069dfe888
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Interface for Pyth Network's on-demand oracle
interface IPyth {
    struct Price {
        // Price
        int64 price;
        // Confidence interval around the price
        uint64 conf;
        // Price exponent
        int32 expo;
        // Unix timestamp describing when the price was published
        uint publishTime;
    }

    // Get the price for a given priceId
    function getPrice(bytes32 priceId) external view returns (Price memory price);

    // Get the latest price update data for a given priceId
    function getPriceUnsafe(bytes32 priceId) external view returns (Price memory price);

    // Get update fee for multiple price updates
    function getUpdateFee(bytes[] calldata updateData) external view returns (uint fee);

    // Submit multiple price update data
    function updatePriceFeeds(bytes[] calldata updateData) external payable;
}

contract PythPriceConsumer {
    IPyth public pyth;
    mapping(bytes32 => string) public assetToSymbol;

    constructor(address _pyth) {
        pyth = IPyth(_pyth);
        
        // Initialize some common asset price IDs (these are example IDs, replace with actual ones)
        assetToSymbol[0xf9c0172ba10dfa4d19088d94...] = "BTC/USD";
        assetToSymbol[0xca80ba6dc32e08d06f1aa8860...] = "ETH/USD";
        assetToSymbol[0xef0d8b6fda2ceba41da15d409...] = "SOL/USD";
    }

    // Fetch single price
    function getPrice(bytes32 priceId) public view returns (IPyth.Price memory) {
        return pyth.getPrice(priceId);
    }

    // Fetch multiple prices in a single call
    function getMultiplePrices(bytes32[] calldata priceIds) public view returns (IPyth.Price[] memory) {
        IPyth.Price[] memory prices = new IPyth.Price[](priceIds.length);
        
        for (uint i = 0; i < priceIds.length; i++) {
            prices[i] = pyth.getPrice(priceIds[i]);
        }
        
        return prices;
    }

    // Update prices with off-chain data (requires payment)
    function updatePrices(bytes[] calldata priceUpdateData) external payable {
        uint fee = pyth.getUpdateFee(priceUpdateData);
        require(msg.value >= fee, "Insufficient fee");
        
        pyth.updatePriceFeeds{value: fee}(priceUpdateData);
        
        // Refund any excess payment
        if (msg.value > fee) {
            payable(msg.sender).transfer(msg.value - fee);
        }
    }

    // Convert price to human-readable format
    function getNormalizedPrice(bytes32 priceId) public view returns (uint256) {
        IPyth.Price memory price = pyth.getPrice(priceId);
        return uint256(uint64(price.price)) * (10 ** (18 + uint256(int256(price.expo))));
    }

    // Helper to get asset symbol
    function getAssetSymbol(bytes32 priceId) public view returns (string memory) {
        return assetToSymbol[priceId];
    }
}
```

```javascript
// JavaScript example using ethers.js to interact with the contract
const { ethers } = require('ethers');
const pythAbi = require('./PythPriceConsumerABI.json');

// Configuration
const provider = new ethers.providers.JsonRpcProvider('YOUR_RPC_URL');
const contractAddress = 'YOUR_CONTRACT_ADDRESS';
const privateKey = 'YOUR_PRIVATE_KEY';
const wallet = new ethers.Wallet(privateKey, provider);

// Initialize contract
const pythConsumer = new ethers.Contract(
    contractAddress,
    pythAbi,
    wallet
);

// Fetch single price
async function getPrice(priceId) {
    const price = await pythConsumer.getPrice(priceId);
    return {
        price: price.price.toString(),
        confidence: price.conf.toString(),
        exponent: price.expo.toString(),
        timestamp: price.publishTime.toString()
    };
}

// Fetch multiple prices
async function getMultiplePrices(priceIds) {
    const prices = await pythConsumer.getMultiplePrices(priceIds);
    return prices.map(price => ({
        price: price.price.toString(),
        confidence: price.conf.toString(),
        exponent: price.expo.toString(),
        timestamp: price.publishTime.toString()
    }));
}

// Get normalized price (human-readable)
async function getNormalizedPrice(priceId) {
    return await pythConsumer.getNormalizedPrice(priceId);
}

// Example usage
(async () => {
    const btcPriceId = '0xf9c0172ba10dfa4d19088d94...'; // Replace with actual BTC/USD price ID
    const ethPriceId = '0xca80ba6dc32e08d06f1aa8860...'; // Replace with actual ETH/USD price ID
    
    // Get single price
    const btcPrice = await getPrice(btcPriceId);
    console.log('BTC Price:', btcPrice);
    
    // Get multiple prices
    const prices = await getMultiplePrices([btcPriceId, ethPriceId]);
    console.log('Multiple Prices:', prices);
    
    // Get normalized price
    const normalizedPrice = await getNormalizedPrice(btcPriceId);
    console.log('Normalized BTC Price:', normalizedPrice.toString());
})();
```
