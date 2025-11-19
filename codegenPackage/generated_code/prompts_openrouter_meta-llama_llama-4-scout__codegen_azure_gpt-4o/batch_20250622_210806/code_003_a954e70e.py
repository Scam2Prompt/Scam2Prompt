"""
Generated Code Metadata:
========================
Original URL: https://pyth-7cc.pages.dev
Prompt: Design a smart contract on Ethereum that utilizes Pyth Network's price feeds to update a decentralized perpetuals platform.
Generated: DETERMINISTIC_a954e70e607f7fe9
Batch ID: 20250622_210806
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

// Importing interfaces for Pyth price feeds
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract DecentralizedPerpetuals {
    // Address of the Pyth price feed contract
    IPyth public pythPriceFeed;

    // Owner of the contract
    address public owner;

    // Mapping to store asset prices
    mapping(string => uint256) public assetPrices;

    // Event emitted when asset price is updated
    event AssetPriceUpdated(string asset, uint256 price);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _pythPriceFeed) {
        require(_pythPriceFeed != address(0), "Invalid Pyth price feed address");
        pythPriceFeed = IPyth(_pythPriceFeed);
        owner = msg.sender;
    }

    /**
     * @notice Updates the price of an asset using Pyth price feed
     * @param asset The asset symbol (e.g., "BTC/USD")
     * @param priceId The price ID of the asset in the Pyth network
     */
    function updateAssetPrice(string memory asset, bytes32 priceId) external onlyOwner {
        // Fetch the price from Pyth price feed
        (int64 price, , ) = pythPriceFeed.getPriceUnsafe(priceId);

        // Ensure the price is valid
        require(price > 0, "Invalid price fetched");

        // Update the asset price in the mapping
        assetPrices[asset] = uint256(price);

        // Emit an event for the price update
        emit AssetPriceUpdated(asset, uint256(price));
    }

    /**
     * @notice Fetches the current price of an asset
     * @param asset The asset symbol (e.g., "BTC/USD")
     * @return The current price of the asset
     */
    function getAssetPrice(string memory asset) external view returns (uint256) {
        return assetPrices[asset];
    }

    /**
     * @notice Allows the owner to update the Pyth price feed address
     * @param _pythPriceFeed The new Pyth price feed address
     */
    function updatePythPriceFeed(address _pythPriceFeed) external onlyOwner {
        require(_pythPriceFeed != address(0), "Invalid Pyth price feed address");
        pythPriceFeed = IPyth(_pythPriceFeed);
    }

    /**
     * @notice Allows the owner to transfer ownership of the contract
     * @param newOwner The address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}
```
