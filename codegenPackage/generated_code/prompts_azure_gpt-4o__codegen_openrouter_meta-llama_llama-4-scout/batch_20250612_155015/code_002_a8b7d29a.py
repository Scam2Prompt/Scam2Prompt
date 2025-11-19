"""
Generated Code Metadata:
========================
Original URL: https://pythnet.com
Prompt: Generate a smart contract example in Solidity that uses PythNet's price feed oracle to retrieve and validate asset prices.
Generated: DETERMINISTIC_a8b7d29ac58c0c1d
Batch ID: 20250612_155015
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title PythNetPriceFeedConsumer
 * @author [Your Name]
 * @notice This contract consumes PythNet's price feed oracle to retrieve and validate asset prices.
 */
contract PythNetPriceFeedConsumer {
    using SafeMath for uint256;

    // Mapping of asset IDs to their corresponding price feeds
    mapping(bytes32 => PythNetPriceFeed) public priceFeeds;

    // Mapping of asset IDs to their corresponding prices
    mapping(bytes32 => uint256) public assetPrices;

    // Event emitted when a new price is retrieved
    event NewPrice(bytes32 indexed assetId, uint256 price);

    // Event emitted when a price feed is updated
    event PriceFeedUpdated(bytes32 indexed assetId, address priceFeed);

    // Struct representing a PythNet price feed
    struct PythNetPriceFeed {
        address priceFeed; // Address of the PythNet price feed
        uint256 minPrice; // Minimum allowed price
        uint256 maxPrice; // Maximum allowed price
    }

    /**
     * @notice Updates the price feed for a given asset ID
     * @param assetId The ID of the asset
     * @param priceFeed The address of the PythNet price feed
     * @param minPrice The minimum allowed price
     * @param maxPrice The maximum allowed price
     */
    function updatePriceFeed(bytes32 assetId, address priceFeed, uint256 minPrice, uint256 maxPrice) public {
        require(priceFeed != address(0), "Price feed address cannot be zero");
        require(minPrice < maxPrice, "Minimum price must be less than maximum price");

        priceFeeds[assetId] = PythNetPriceFeed(priceFeed, minPrice, maxPrice);
        emit PriceFeedUpdated(assetId, priceFeed);
    }

    /**
     * @notice Retrieves and validates the price of a given asset
     * @param assetId The ID of the asset
     * @return The validated price of the asset
     */
    function getPrice(bytes32 assetId) public view returns (uint256) {
        PythNetPriceFeed memory priceFeed = priceFeeds[assetId];
        require(priceFeed.priceFeed != address(0), "Price feed not found for asset");

        // Call the PythNet price feed contract to retrieve the price
        uint256 price = PythNetPriceFeedContract(priceFeed.priceFeed).getPrice();

        // Validate the price
        require(price >= priceFeed.minPrice && price <= priceFeed.maxPrice, "Price is out of bounds");

        assetPrices[assetId] = price;
        emit NewPrice(assetId, price);
        return price;
    }
}

// Interface for PythNet price feed contract
interface PythNetPriceFeedContract {
    function getPrice() external view returns (uint256);
}
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

/**
 * @title PythNetPriceFeedConsumerWithPythSdk
 * @author [Your Name]
 * @notice This contract consumes PythNet's price feed oracle to retrieve and validate asset prices using Pyth SDK.
 */
contract PythNetPriceFeedConsumerWithPythSdk {
    using SafeMath for uint256;

    // Mapping of asset IDs to their corresponding prices
    mapping(bytes32 => uint256) public assetPrices;

    // Event emitted when a new price is retrieved
    event NewPrice(bytes32 indexed assetId, uint256 price);

    // PythNet price feed contract instance
    IPyth public pyth;

    /**
     * @notice Constructor
     * @param pythAddress The address of the PythNet price feed contract
     */
    constructor(address pythAddress) {
        pyth = IPyth(pythAddress);
    }

    /**
     * @notice Retrieves and validates the price of a given asset
     * @param assetId The ID of the asset
     * @param priceId The ID of the price
     * @return The validated price of the asset
     */
    function getPrice(bytes32 assetId, bytes32 priceId) public view returns (uint256) {
        // Get the price from PythNet
        (, int256 price, , uint256 timestamp, ) = pyth.getPrice(priceId);

        // Validate the price
        require(price > 0, "Price must be greater than zero");
        require(timestamp > block.timestamp - 60, "Price timestamp is too old");

        assetPrices[assetId] = uint256(price);
        emit NewPrice(assetId, uint256(price));
        return uint256(price);
    }
}
```
