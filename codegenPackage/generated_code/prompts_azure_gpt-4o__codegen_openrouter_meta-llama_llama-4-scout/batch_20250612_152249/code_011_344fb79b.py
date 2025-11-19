"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Provide an example of integrating Chainlink Market and Data Feeds to trigger smart contracts based on asset price changes.
Generated: DETERMINISTIC_344fb79b3c2cba60
Batch ID: 20250612_152249
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

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";

/**
 * @title Chainlink Market and Data Feeds Integration
 * @author [Your Name]
 * @notice This contract demonstrates how to integrate Chainlink Market and Data Feeds
 * to trigger smart contracts based on asset price changes.
 */
contract ChainlinkMarketDataFeeds is ChainlinkClient {
    // Mapping of asset symbols to their corresponding aggregator interfaces
    mapping(string => AggregatorV3Interface) public aggregators;

    // Mapping of asset symbols to their price change thresholds
    mapping(string => uint256) public thresholds;

    // Mapping of asset symbols to their current prices
    mapping(string => uint256) public currentPrices;

    // Event emitted when a price change threshold is exceeded
    event PriceChangeThresholdExceeded(string assetSymbol, uint256 currentPrice);

    /**
     * @dev Constructor
     * @param _defaultAdmin The default admin for the contract
     * @param _chainlinkToken The Chainlink token address
     */
    constructor(address _defaultAdmin, address _chainlinkToken) public {
        setDefaultAdmin(_defaultAdmin);
        setChainlinkToken(_chainlinkToken);
    }

    /**
     * @dev Add an aggregator for an asset symbol
     * @param _assetSymbol The asset symbol (e.g. "ETH/USD")
     * @param _aggregator The aggregator address
     */
    function addAggregator(string memory _assetSymbol, address _aggregator) public onlyOwner {
        aggregators[_assetSymbol] = AggregatorV3Interface(_aggregator);
    }

    /**
     * @dev Set the price change threshold for an asset symbol
     * @param _assetSymbol The asset symbol (e.g. "ETH/USD")
     * @param _threshold The price change threshold (in basis points)
     */
    function setThreshold(string memory _assetSymbol, uint256 _threshold) public onlyOwner {
        thresholds[_assetSymbol] = _threshold;
    }

    /**
     * @dev Check if the price change threshold is exceeded for an asset symbol
     * @param _assetSymbol The asset symbol (e.g. "ETH/USD")
     * @return bool Whether the price change threshold is exceeded
     */
    function isThresholdExceeded(string memory _assetSymbol) public view returns (bool) {
        uint256 currentPrice = getLatestPrice(_assetSymbol);
        uint256 threshold = thresholds[_assetSymbol];
        uint256 previousPrice = currentPrices[_assetSymbol];

        // Calculate the price change (in basis points)
        uint256 priceChange = (currentPrice - previousPrice) * 10000 / previousPrice;

        // Update the current price
        currentPrices[_assetSymbol] = currentPrice;

        // Check if the price change threshold is exceeded
        return priceChange > threshold;
    }

    /**
     * @dev Get the latest price for an asset symbol
     * @param _assetSymbol The asset symbol (e.g. "ETH/USD")
     * @return uint256 The latest price
     */
    function getLatestPrice(string memory _assetSymbol) public view returns (uint256) {
        AggregatorV3Interface aggregator = aggregators[_assetSymbol];
        (, int256 price, , , ) = aggregator.latestRoundData();
        return uint256(price * 10**10); // 10^10 for 18 decimal places
    }

    /**
     * @dev Trigger a smart contract based on asset price changes
     * @param _assetSymbol The asset symbol (e.g. "ETH/USD")
     */
    function triggerSmartContract(string memory _assetSymbol) public {
        if (isThresholdExceeded(_assetSymbol)) {
            // Trigger the smart contract
            // Replace this with your smart contract logic
            emit PriceChangeThresholdExceeded(_assetSymbol, currentPrices[_assetSymbol]);
        }
    }

    /**
     * @dev Request data from a Chainlink oracle
     * @param _oracle The oracle address
     * @param _jobId The job ID
     * @param _assetSymbol The asset symbol (e.g. "ETH/USD")
     */
    function requestData(address _oracle, bytes32 _jobId, string memory _assetSymbol) public {
        Chainlink.Request memory request = buildChainlinkRequest(_jobId, address(this), this.fulfill.selector);
        request.add("assetSymbol", _assetSymbol);
        sendChainlinkRequestTo(_oracle, request.encode(), 100000);
    }

    /**
     * @dev Fulfill a Chainlink request
     * @param _requestId The request ID
     * @param _price The price
     */
    function fulfill(bytes32 _requestId, uint256 _price) public recordChainlinkFulfillment(_requestId) {
        string memory assetSymbol = getChainlinkTokenSymbol();
        currentPrices[assetSymbol] = _price;
        triggerSmartContract(assetSymbol);
    }

    /**
     * @dev Get the Chainlink token symbol
     * @return string The Chainlink token symbol
     */
    function getChainlinkTokenSymbol() internal view returns (string memory) {
        // Replace this with your Chainlink token symbol
        return "ETH/USD";
    }
}
```

```javascript
// scripts/deploy.js
const { ethers } = require("hardhat");

async function main() {
  const factory = await ethers.getContractFactory("ChainlinkMarketDataFeeds");
  const contract = await factory.deploy("0x... default admin ...", "0x... chainlink token ...");

  await contract.deployed();

  console.log(`Contract deployed to: ${contract.address}`);

  // Add an aggregator for an asset symbol
  const aggregatorAddress = "0x... aggregator address ...";
  await contract.addAggregator("ETH/USD", aggregatorAddress);

  // Set the price change threshold for an asset symbol
  const threshold = 100; // 1%
  await contract.setThreshold("ETH/USD", threshold);

  // Request data from a Chainlink oracle
  const oracleAddress = "0x... oracle address ...";
  const jobId = "0x... job ID ...";
  await contract.requestData(oracleAddress, jobId, "ETH/USD");
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```
