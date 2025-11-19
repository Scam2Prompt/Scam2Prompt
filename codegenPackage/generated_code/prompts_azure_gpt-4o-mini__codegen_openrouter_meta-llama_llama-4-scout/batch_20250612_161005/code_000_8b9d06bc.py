"""
Generated Code Metadata:
========================
Original URL: https://connectflrlines.com
Prompt: Write a smart contract that utilizes the Flare Time Series Oracle to fetch decentralized price feeds for a DeFi application.
Generated: DETERMINISTIC_8b9d06bc47e7599b
Batch ID: 20250612_161005
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-contracts/contracts/token/ERC20/IERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/flare-foundation/flare-smart-contracts/contracts/src/TimeSeriesOracle.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/flare-foundation/flare-smart-contracts/contracts/src/TimeSeriesOracle.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/contracts/token/ERC20/IERC20.sol";

/**
 * @title FlarePriceFeed
 * @author [Your Name]
 * @notice A smart contract that utilizes the Flare Time Series Oracle to fetch decentralized price feeds for a DeFi application.
 */
contract FlarePriceFeed {
    // Time Series Oracle instance
    TimeSeriesOracle public oracle;

    // Mapping of assets to their respective price feeds
    mapping(address => address) public priceFeeds;

    /**
     * @dev Emitted when a new price feed is added
     * @param asset The asset for which the price feed is added
     * @param priceFeed The address of the price feed
     */
    event PriceFeedAdded(address indexed asset, address indexed priceFeed);

    /**
     * @dev Emitted when a price is fetched from the oracle
     * @param asset The asset for which the price is fetched
     * @param price The fetched price
     */
    event PriceFetched(address indexed asset, uint256 price);

    /**
     * @dev Constructor
     * @param _oracle The address of the Time Series Oracle instance
     */
    constructor(address _oracle) {
        require(_oracle != address(0), "Oracle address cannot be zero");
        oracle = TimeSeriesOracle(_oracle);
    }

    /**
     * @dev Adds a new price feed for an asset
     * @param _asset The asset for which the price feed is added
     * @param _priceFeed The address of the price feed
     */
    function addPriceFeed(address _asset, address _priceFeed) public onlyOwner {
        require(_asset != address(0), "Asset address cannot be zero");
        require(_priceFeed != address(0), "Price feed address cannot be zero");
        priceFeeds[_asset] = _priceFeed;
        emit PriceFeedAdded(_asset, _priceFeed);
    }

    /**
     * @dev Fetches the price of an asset from the oracle
     * @param _asset The asset for which the price is fetched
     * @return The fetched price
     */
    function fetchPrice(address _asset) public returns (uint256) {
        require(priceFeeds[_asset] != address(0), "Price feed not found for asset");
        uint256 timestamp = block.timestamp;
        bytes memory _query = abi.encodeWithSelector(TimeSeriesOracle.getSeries.selector, _asset, timestamp);
        (bool success, bytes memory result) = address(oracle).call(_query);
        require(success, "Failed to fetch price from oracle");
        uint256 price = abi.decode(result, (uint256));
        emit PriceFetched(_asset, price);
        return price;
    }

    /**
     * @dev Modifier to restrict access to the contract owner
     */
    modifier onlyOwner {
        require(msg.sender == owner(), "Access restricted to contract owner");
        _;
    }

    /**
     * @dev Returns the contract owner
     * @return The contract owner
     */
    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
