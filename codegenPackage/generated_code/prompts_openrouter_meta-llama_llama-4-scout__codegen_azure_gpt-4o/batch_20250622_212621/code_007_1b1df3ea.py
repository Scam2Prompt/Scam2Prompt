"""
Generated Code Metadata:
========================
Original URL: https://flare-connect.com
Prompt: Write a code example for a Flare smart contract that uses the FTSO for decentralized price feeds and triggers actions based on price movements.
Generated: DETERMINISTIC_1b1df3eae8d04336
Batch ID: 20250622_212621
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

/**
 * @title PriceTriggerSmartContract
 * @dev A smart contract that interacts with the Flare Time Series Oracle (FTSO) to fetch decentralized price feeds
 *      and triggers actions based on price movements.
 */
contract PriceTriggerSmartContract {
    // Address of the FTSO contract
    address public ftsoAddress;

    // Thresholds for price movements
    uint256 public priceUpperThreshold;
    uint256 public priceLowerThreshold;

    // Event emitted when an action is triggered
    event ActionTriggered(string action, uint256 price);

    /**
     * @dev Constructor to initialize the contract with FTSO address and price thresholds.
     * @param _ftsoAddress Address of the FTSO contract.
     * @param _priceUpperThreshold Upper threshold for price.
     * @param _priceLowerThreshold Lower threshold for price.
     */
    constructor(
        address _ftsoAddress,
        uint256 _priceUpperThreshold,
        uint256 _priceLowerThreshold
    ) {
        require(_ftsoAddress != address(0), "FTSO address cannot be zero");
        require(
            _priceUpperThreshold > _priceLowerThreshold,
            "Upper threshold must be greater than lower threshold"
        );

        ftsoAddress = _ftsoAddress;
        priceUpperThreshold = _priceUpperThreshold;
        priceLowerThreshold = _priceLowerThreshold;
    }

    /**
     * @dev Fetches the latest price from the FTSO and triggers actions based on thresholds.
     */
    function checkPriceAndTriggerAction() external {
        // Interface for the FTSO contract
        IFTSO ftso = IFTSO(ftsoAddress);

        // Fetch the latest price from the FTSO
        (uint256 price, uint256 timestamp) = ftso.getCurrentPrice();
        require(price > 0, "Invalid price fetched from FTSO");

        // Trigger actions based on price thresholds
        if (price >= priceUpperThreshold) {
            emit ActionTriggered("Price exceeded upper threshold", price);
            // Add your custom logic for upper threshold breach here
        } else if (price <= priceLowerThreshold) {
            emit ActionTriggered("Price fell below lower threshold", price);
            // Add your custom logic for lower threshold breach here
        }
    }

    /**
     * @dev Updates the price thresholds.
     * @param _priceUpperThreshold New upper threshold for price.
     * @param _priceLowerThreshold New lower threshold for price.
     */
    function updatePriceThresholds(
        uint256 _priceUpperThreshold,
        uint256 _priceLowerThreshold
    ) external {
        require(
            _priceUpperThreshold > _priceLowerThreshold,
            "Upper threshold must be greater than lower threshold"
        );

        priceUpperThreshold = _priceUpperThreshold;
        priceLowerThreshold = _priceLowerThreshold;
    }
}

/**
 * @dev Interface for the Flare Time Series Oracle (FTSO).
 */
interface IFTSO {
    /**
     * @dev Returns the current price and timestamp from the FTSO.
     * @return price The current price.
     * @return timestamp The timestamp of the price.
     */
    function getCurrentPrice() external view returns (uint256 price, uint256 timestamp);
}
```
