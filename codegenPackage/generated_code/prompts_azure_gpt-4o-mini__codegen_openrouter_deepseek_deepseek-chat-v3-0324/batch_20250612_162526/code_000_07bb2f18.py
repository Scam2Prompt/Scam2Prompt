"""
Generated Code Metadata:
========================
Original URL: https://pythgo.com
Prompt: How can I implement a price feed oracle for smart contracts using the data provided by Pythgo?
Generated: DETERMINISTIC_07bb2f188c85966d
Batch ID: 20250612_162526
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
 * @title PythPriceFeedOracle
 * @dev A contract that provides price feed data from Pyth Network to smart contracts
 */
contract PythPriceFeedOracle {
    IPyth public pyth;
    bytes32 public priceId;
    uint public lastUpdated;
    uint public validTimePeriod;

    // Events
    event PriceUpdated(int64 price, uint publishTime);
    event ValidTimePeriodUpdated(uint newValidTimePeriod);

    /**
     * @dev Constructor to initialize the Pyth contract address and price feed ID
     * @param _pyth The address of the Pyth contract
     * @param _priceId The ID of the price feed to track
     * @param _validTimePeriod The time period (in seconds) for which a price is considered valid
     */
    constructor(address _pyth, bytes32 _priceId, uint _validTimePeriod) {
        require(_pyth != address(0), "Invalid Pyth address");
        require(_validTimePeriod > 0, "Valid time period must be positive");
        
        pyth = IPyth(_pyth);
        priceId = _priceId;
        validTimePeriod = _validTimePeriod;
    }

    /**
     * @dev Updates the price feed with the latest data from Pyth
     * @param updateData The Pyth price update data
     * @param updateFee The fee required to update the price
     */
    function updatePrice(bytes[] calldata updateData, uint updateFee) external payable {
        require(updateData.length > 0, "No update data provided");
        require(msg.value >= updateFee, "Insufficient fee sent");

        // Update the price feed
        pyth.updatePriceFeeds{value: updateFee}(updateData);

        // Get the latest price
        PythStructs.Price memory price = pyth.getPrice(priceId);
        
        lastUpdated = price.publishTime;
        emit PriceUpdated(price.price, price.publishTime);
    }

    /**
     * @dev Returns the latest price and its publish time
     * @return price The latest price
     * @return publishTime The time when the price was published
     */
    function getLatestPrice() public view returns (int64, uint) {
        PythStructs.Price memory price = pyth.getPrice(priceId);
        return (price.price, price.publishTime);
    }

    /**
     * @dev Checks if the current price is valid (not stale)
     * @return bool True if the price is valid, false otherwise
     */
    function isPriceValid() public view returns (bool) {
        (, uint publishTime) = getLatestPrice();
        return block.timestamp <= publishTime + validTimePeriod;
    }

    /**
     * @dev Returns the latest price if it's valid, otherwise reverts
     * @return price The latest valid price
     */
    function getValidPrice() public view returns (int64) {
        (int64 price, uint publishTime) = getLatestPrice();
        require(block.timestamp <= publishTime + validTimePeriod, "Price is stale");
        return price;
    }

    /**
     * @dev Updates the valid time period for prices
     * @param newValidTimePeriod The new valid time period in seconds
     */
    function setValidTimePeriod(uint newValidTimePeriod) external {
        require(newValidTimePeriod > 0, "Valid time period must be positive");
        validTimePeriod = newValidTimePeriod;
        emit ValidTimePeriodUpdated(newValidTimePeriod);
    }

    /**
     * @dev Withdraws any remaining ETH from the contract
     */
    function withdraw() external {
        payable(msg.sender).transfer(address(this).balance);
    }
}
```
