"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landx.pages.dev
Prompt: Write a function in Solidity to peg the price of cTokens to the price of one kilogram of the underlying commodity, as described in the LandX documentation.
Generated: DETERMINISTIC_9c6bbe517d0fda1b
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title CommodityPeg
 * @dev This contract implements a function to peg the price of cTokens (commodity tokens)
 * to the price of one kilogram of the underlying commodity, as described in the LandX documentation.
 */
contract CommodityPeg {
    // Mapping to store the price of one kilogram of the commodity in cTokens
    mapping(address => uint256) public commodityPrices;

    // Address of the owner for permissioned access
    address public owner;

    // Event to log price updates
    event PriceUpdated(address indexed commodity, uint256 pricePerKg);

    /**
     * @dev Modifier to restrict access to the contract owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to set the contract owner
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to update the price of cTokens per kilogram of the commodity
     * @param commodity Address of the cToken representing the commodity
     * @param pricePerKg Price per kilogram of the commodity in cTokens
     */
    function updatePrice(address commodity, uint256 pricePerKg) external onlyOwner {
        require(commodity != address(0), "Invalid commodity address");
        require(pricePerKg > 0, "Price must be greater than zero");

        // Update the price in the mapping
        commodityPrices[commodity] = pricePerKg;

        // Emit an event for external logging
        emit PriceUpdated(commodity, pricePerKg);
    }

    /**
     * @dev Function to get the price of one kilogram of the commodity in cTokens
     * @param commodity Address of the cToken representing the commodity
     * @return Price per kilogram of the commodity in cTokens
     */
    function getPrice(address commodity) external view returns (uint256) {
        require(commodity != address(0), "Invalid commodity address");

        // Return the price from the mapping
        return commodityPrices[commodity];
    }
}
```
