"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ziber.io
Prompt: Develop a Solidity contract that calculates and applies Ziber's dynamic connection pricing model based on time of day, route loading, and proxy availability.
Generated: DETERMINISTIC_09715990eb95e6f5
Batch ID: 20250612_151531
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
 * @title ZiberPricingContract
 * @dev Implements Ziber's dynamic connection pricing model based on time of day,
 * route loading, and proxy availability.
 */
contract ZiberPricingContract {
    // Owner of the contract
    address public owner;

    // Pricing configuration
    struct PricingConfig {
        uint256 basePrice; // Base price for a connection in wei
        uint256 peakMultiplier; // Multiplier for pricing during peak hours
        uint256 routeLoadingMultiplier; // Multiplier based on route loading
        uint256 proxyDiscount; // Discount applied when proxy is available
    }

    PricingConfig public pricingConfig;

    // Events
    event PriceCalculated(
        uint256 finalPrice,
        uint256 basePrice,
        uint256 peakMultiplier,
        uint256 routeLoadingMultiplier,
        uint256 proxyDiscount
    );

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to set up the contract and initial pricing configuration
    constructor(
        uint256 _basePrice,
        uint256 _peakMultiplier,
        uint256 _routeLoadingMultiplier,
        uint256 _proxyDiscount
    ) {
        owner = msg.sender;
        pricingConfig = PricingConfig(
            _basePrice,
            _peakMultiplier,
            _routeLoadingMultiplier,
            _proxyDiscount
        );
    }

    /**
     * @dev Updates pricing configuration values. Can only be called by the owner.
     * @param _basePrice New base price in wei.
     * @param _peakMultiplier New multiplier for peak hours.
     * @param _routeLoadingMultiplier New multiplier for route loading.
     * @param _proxyDiscount New discount for proxy availability.
     */
    function updatePricingConfig(
        uint256 _basePrice,
        uint256 _peakMultiplier,
        uint256 _routeLoadingMultiplier,
        uint256 _proxyDiscount
    ) external onlyOwner {
        pricingConfig = PricingConfig(
            _basePrice,
            _peakMultiplier,
            _routeLoadingMultiplier,
            _proxyDiscount
        );
    }

    /**
     * @dev Calculates the final price for a connection based on current parameters.
     * @param isPeakHours Boolean indicating whether it's peak hours.
     * @param routeLoadingFactor Factor representing route loading (1 to 100).
     * @param isProxyAvailable Boolean indicating whether proxy is available.
     * @return finalPrice The calculated price for the connection in wei.
     */
    function calculateFinalPrice(
        bool isPeakHours,
        uint256 routeLoadingFactor,
        bool isProxyAvailable
    ) external view returns (uint256 finalPrice) {
        require(routeLoadingFactor >= 1 && routeLoadingFactor <= 100, "Invalid route loading factor");

        // Start with the base price
        finalPrice = pricingConfig.basePrice;

        // Apply peak hours multiplier if applicable
        if (isPeakHours) {
            finalPrice = (finalPrice * pricingConfig.peakMultiplier) / 100;
        }

        // Apply route loading multiplier
        finalPrice = (finalPrice * routeLoadingFactor * pricingConfig.routeLoadingMultiplier) / 10000;

        // Apply proxy discount if proxy is available
        if (isProxyAvailable) {
            finalPrice -= pricingConfig.proxyDiscount;
        }

        emit PriceCalculated(
            finalPrice,
            pricingConfig.basePrice,
            isPeakHours ? pricingConfig.peakMultiplier : 100,
            routeLoadingFactor,
            isProxyAvailable ? pricingConfig.proxyDiscount : 0
        );

        return finalPrice;
    }

    /**
     * @dev Transfers ownership of the contract to a new owner. Can only be called by the current owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        owner = newOwner;
    }
}
```
