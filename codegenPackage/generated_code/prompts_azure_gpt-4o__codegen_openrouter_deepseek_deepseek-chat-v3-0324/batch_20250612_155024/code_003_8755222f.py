"""
Generated Code Metadata:
========================
Original URL: https://pythshop.com
Prompt: How can I use Pyth Network's price feed oracles to ensure accurate and secure market data in my smart contract?
Generated: DETERMINISTIC_8755222f5b74b4c9
Batch ID: 20250612_155024
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

// Import Pyth Network interfaces
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";

contract PythPriceConsumer {
    IPyth public pyth;

    // Mapping to store price feed IDs for different assets
    mapping(string => bytes32) public priceFeedIds;

    // Event to log price updates
    event PriceUpdated(string asset, int64 price, uint64 confidence, uint64 publishTime);

    /**
     * @dev Constructor to initialize the Pyth contract address
     * @param _pyth The address of the Pyth contract
     */
    constructor(address _pyth) {
        pyth = IPyth(_pyth);
    }

    /**
     * @dev Add a new price feed ID for an asset
     * @param asset The symbol/name of the asset (e.g., "BTC/USD")
     * @param priceId The Pyth price feed ID for the asset
     */
    function addPriceFeed(string memory asset, bytes32 priceId) public {
        priceFeedIds[asset] = priceId;
    }

    /**
     * @dev Get the latest price for an asset
     * @param asset The symbol/name of the asset
     * @return price The current price
     * @return confidence The confidence interval of the price
     * @return publishTime The timestamp when the price was published
     */
    function getLatestPrice(
        string memory asset
    ) public view returns (int64 price, uint64 confidence, uint64 publishTime) {
        bytes32 priceId = priceFeedIds[asset];
        require(priceId != bytes32(0), "Price feed not found for this asset");

        PythStructs.Price memory currentPrice = pyth.getPrice(priceId);
        return (currentPrice.price, currentPrice.conf, currentPrice.publishTime);
    }

    /**
     * @dev Update the price feed with the latest Pyth price update data
     * @param updateData The Pyth price update data
     * @param asset The asset symbol to verify the update against
     */
    function updatePrice(
        bytes[] calldata updateData,
        string memory asset
    ) public payable {
        bytes32 priceId = priceFeedIds[asset];
        require(priceId != bytes32(0), "Price feed not found for this asset");

        // Pay the fee to update the price and get the update fee amount
        uint fee = pyth.getUpdateFee(updateData);
        require(msg.value >= fee, "Insufficient fee sent");

        // Update the price data
        pyth.updatePriceFeeds{value: fee}(updateData);

        // Get and verify the updated price
        PythStructs.Price memory updatedPrice = pyth.getPrice(priceId);
        require(updatedPrice.price != 0, "Price update failed");

        emit PriceUpdated(
            asset,
            updatedPrice.price,
            updatedPrice.conf,
            updatedPrice.publishTime
        );
    }

    /**
     * @dev Withdraw any remaining ETH from the contract
     */
    function withdraw() public {
        payable(msg.sender).transfer(address(this).balance);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
