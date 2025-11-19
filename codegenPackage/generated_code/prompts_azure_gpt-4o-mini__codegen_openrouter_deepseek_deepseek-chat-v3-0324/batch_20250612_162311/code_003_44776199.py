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

// Import Pyth Oracle interfaces
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

    // Get price feed by id
    function getPrice(bytes32 id) external view returns (Price memory price);
}

contract PythPriceConsumer {
    IPyth public pyth;
    bytes32 public priceFeedId;

    // Events
    event PriceUpdated(int64 price, uint64 confidence, uint timestamp);

    /**
     * @dev Initialize contract with Pyth oracle address and price feed ID
     * @param _pyth The address of the Pyth oracle contract
     * @param _priceFeedId The ID of the price feed to use
     */
    constructor(address _pyth, bytes32 _priceFeedId) {
        require(_pyth != address(0), "Invalid Pyth address");
        pyth = IPyth(_pyth);
        priceFeedId = _priceFeedId;
    }

    /**
     * @dev Get the latest price from Pyth oracle
     * @return price The current price
     * @return confidence The confidence interval
     * @return timestamp The time when the price was published
     */
    function getLatestPrice() 
        public 
        view 
        returns (
            int64 price, 
            uint64 confidence, 
            uint timestamp
        ) 
    {
        IPyth.Price memory pythPrice = pyth.getPrice(priceFeedId);
        return (pythPrice.price, pythPrice.conf, pythPrice.publishTime);
    }

    /**
     * @dev Update and emit the latest price
     */
    function updatePrice() external {
        (int64 price, uint64 confidence, uint timestamp) = getLatestPrice();
        require(price > 0, "Invalid price");
        require(timestamp > 0, "Invalid timestamp");
        
        emit PriceUpdated(price, confidence, timestamp);
    }

    /**
     * @dev Get the price with additional safety checks
     * @return The current price adjusted for decimals
     */
    function getPriceWithChecks() external view returns (int64) {
        IPyth.Price memory pythPrice = pyth.getPrice(priceFeedId);
        require(pythPrice.price > 0, "Price not available");
        require(pythPrice.publishTime + 300 >= block.timestamp, "Price too old");
        
        return pythPrice.price;
    }
}
```
