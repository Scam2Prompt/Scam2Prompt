"""
Generated Code Metadata:
========================
Original URL: https://pyth-test.vercel.app
Prompt: How can I use Pyth's pull-based oracle model to fetch real-time price data for crypto assets in an Ethereum-based DeFi application?
Generated: DETERMINISTIC_0f10cc56c60af323
Batch ID: 20250612_153648
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

    // Get the price of a price feed with `id`
    function getPrice(bytes32 id) external view returns (Price memory price);

    // Get the latest price update data for a list of price feed IDs
    function getPriceUpdateData(bytes32[] calldata ids) external view returns (bytes[] memory updateData);
}

contract PythOracleConsumer {
    IPyth public pyth;
    bytes32 public priceFeedId;

    constructor(address _pyth, bytes32 _priceFeedId) {
        pyth = IPyth(_pyth);
        priceFeedId = _priceFeedId;
    }

    function getLatestPrice() public view returns (int64, uint64, uint) {
        IPyth.Price memory priceData = pyth.getPrice(priceFeedId);
        return (priceData.price, priceData.conf, priceData.publishTime);
    }

    function getLatestPriceUpdateData() public view returns (bytes memory) {
        bytes32[] memory ids = new bytes32[](1);
        ids[0] = priceFeedId;
        bytes[] memory updateData = pyth.getPriceUpdateData(ids);
        require(updateData.length > 0, "No update data available");
        return updateData[0];
    }

    function updatePriceFeedId(bytes32 _newPriceFeedId) external {
        priceFeedId = _newPriceFeedId;
    }
}
```

```javascript
// Frontend interaction example using ethers.js
const { ethers } = require('ethers');

async function fetchPythPrice(contractAddress, pythPriceFeedId) {
    try {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();
        
        const pythOracle = new ethers.Contract(
            contractAddress,
            [
                "function getLatestPrice() view returns (int64, uint64, uint)",
                "function getLatestPriceUpdateData() view returns (bytes)"
            ],
            signer
        );

        const [price, confidence, timestamp] = await pythOracle.getLatestPrice();
        const updateData = await pythOracle.getLatestPriceUpdateData();
        
        return {
            price: price.toString(),
            confidence: confidence.toString(),
            timestamp: new Date(timestamp * 1000).toISOString(),
            updateData: ethers.utils.hexlify(updateData)
        };
    } catch (error) {
        console.error("Error fetching Pyth price:", error);
        throw error;
    }
}
```
