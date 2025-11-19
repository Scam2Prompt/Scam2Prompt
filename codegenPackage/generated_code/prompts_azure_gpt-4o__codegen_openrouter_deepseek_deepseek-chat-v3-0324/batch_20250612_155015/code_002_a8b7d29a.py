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

import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";
import "@pythnetwork/pyth-sdk-solidity/PythStructs.sol";

/**
 * @title PythPriceFeed
 * @dev A smart contract that retrieves and validates asset prices from PythNet oracle
 */
contract PythPriceFeed {
    IPyth public pyth;
    bytes32 public priceFeedId;
    uint64 public maxPriceAge;

    event PriceUpdated(int64 price, uint64 publishTime);
    event MaxPriceAgeUpdated(uint64 newMaxPriceAge);

    /**
     * @dev Constructor initializes the Pyth oracle and price feed ID
     * @param _pyth The address of the Pyth oracle contract
     * @param _priceFeedId The ID of the price feed to track
     * @param _maxPriceAge Maximum acceptable age of price update (in seconds)
     */
    constructor(
        address _pyth,
        bytes32 _priceFeedId,
        uint64 _maxPriceAge
    ) {
        require(_pyth != address(0), "Invalid Pyth address");
        require(_priceFeedId != bytes32(0), "Invalid price feed ID");
        require(_maxPriceAge > 0, "Max price age must be positive");

        pyth = IPyth(_pyth);
        priceFeedId = _priceFeedId;
        maxPriceAge = _maxPriceAge;
    }

    /**
     * @dev Updates the maximum acceptable price age
     * @param _newMaxPriceAge New maximum age in seconds
     */
    function setMaxPriceAge(uint64 _newMaxPriceAge) external {
        require(_newMaxPriceAge > 0, "Max price age must be positive");
        maxPriceAge = _newMaxPriceAge;
        emit MaxPriceAgeUpdated(_newMaxPriceAge);
    }

    /**
     * @dev Retrieves the latest price from Pyth oracle
     * @return price The current price
     * @return publishTime The timestamp when the price was published
     */
    function getLatestPrice() public view returns (int64 price, uint64 publishTime) {
        PythStructs.Price memory currentPrice = pyth.getPriceUnsafe(priceFeedId);
        return (currentPrice.price, currentPrice.publishTime);
    }

    /**
     * @dev Retrieves and validates the latest price from Pyth oracle
     * @return price The current price
     * @return publishTime The timestamp when the price was published
     */
    function getValidatedPrice() public view returns (int64 price, uint64 publishTime) {
        (int64 currentPrice, uint64 currentPublishTime) = getLatestPrice();

        require(currentPrice > 0, "Invalid price");
        require(
            block.timestamp - currentPublishTime <= maxPriceAge,
            "Price is too old"
        );

        return (currentPrice, currentPublishTime);
    }

    /**
     * @dev Updates the price by submitting the Pyth update data
     * @param updateData The Pyth price update data
     * @param updateFee The fee required for the update
     */
    function updatePrice(bytes[] calldata updateData, uint256 updateFee) external payable {
        require(updateData.length > 0, "No update data provided");
        
        // Pay the required fee for the update
        uint256 requiredFee = pyth.getUpdateFee(updateData);
        require(msg.value >= requiredFee, "Insufficient fee");

        // Submit the price update
        pyth.updatePriceFeeds{value: requiredFee}(updateData);

        // Refund any excess payment
        if (msg.value > requiredFee) {
            payable(msg.sender).transfer(msg.value - requiredFee);
        }

        // Get and emit the updated price
        (int64 price, uint64 publishTime) = getLatestPrice();
        emit PriceUpdated(price, publishTime);
    }

    /**
     * @dev Emergency function to withdraw any accidentally sent ETH
     */
    function withdraw() external {
        payable(msg.sender).transfer(address(this).balance);
    }
}
```
