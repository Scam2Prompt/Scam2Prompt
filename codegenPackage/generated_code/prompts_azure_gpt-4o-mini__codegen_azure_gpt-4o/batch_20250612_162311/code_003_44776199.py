"""
Generated Code Metadata:
========================
Original URL: https://pythcloud.com
Prompt: Generate a sample smart contract that utilizes Pyth Cloud's price feed oracles for real-time asset pricing.
Generated: DETERMINISTIC_447761993ab5502a
Batch ID: 20250612_162311
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

// Import the Pyth interface
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

contract AssetPriceOracle {
    // Address of the Pyth contract on the blockchain
    IPyth public pyth;

    // Event to log price updates
    event PriceUpdated(string assetId, int64 price, uint64 publishTime);

    // Constructor to initialize the Pyth contract address
    constructor(address _pythContractAddress) {
        require(_pythContractAddress != address(0), "Invalid Pyth contract address");
        pyth = IPyth(_pythContractAddress);
    }

    /**
     * @dev Fetches the latest price of an asset from Pyth price feed.
     * @param assetId The ID of the asset in the Pyth price feed.
     * @param updateData The update data provided by Pyth (off-chain price update payload).
     * @return price The latest price of the asset.
     * @return publishTime The timestamp when the price was published.
     */
    function getAssetPrice(string memory assetId, bytes memory updateData)
        public
        payable
        returns (int64 price, uint64 publishTime)
    {
        // Update the price feed using the provided update data
        pyth.updatePriceFeeds{value: msg.value}(updateData);

        // Fetch the price feed for the given asset ID
        PythStructs.Price memory priceFeed = pyth.getPrice(assetId);

        // Ensure the price feed is valid
        require(priceFeed.price != 0, "Invalid price feed");

        // Emit an event for logging purposes
        emit PriceUpdated(assetId, priceFeed.price, priceFeed.publishTime);

        // Return the price and publish time
        return (priceFeed.price, priceFeed.publishTime);
    }

    /**
     * @dev Allows the contract to receive ETH for Pyth update fees.
     */
    receive() external payable {}

    /**
     * @dev Withdraws any ETH held by the contract to the owner's address.
     * @param recipient The address to send the withdrawn funds to.
     */
    function withdrawFunds(address payable recipient) external {
        require(recipient != address(0), "Invalid recipient address");
        recipient.transfer(address(this).balance);
    }
}
```

### Notes:
- Ensure you have the Pyth SDK installed and the appropriate Pyth contract address for your target blockchain.
- Replace `@pythnetwork/pyth-sdk-solidity/IPyth.sol` with the correct import path based on your project setup.
- This contract assumes the use of Pyth's off-chain price update mechanism (`updatePriceFeeds`).
