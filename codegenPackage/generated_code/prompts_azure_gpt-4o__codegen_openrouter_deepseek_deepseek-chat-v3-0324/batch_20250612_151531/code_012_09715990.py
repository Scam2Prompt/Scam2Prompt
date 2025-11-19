"""
Generated Code Metadata:
========================
Original URL: https://ziber.io
Prompt: Develop a Solidity contract that calculates and applies Ziber's dynamic connection pricing model based on time of day, route loading, and proxy availability.
Generated: DETERMINISTIC_09715990eb95e6f5
Batch ID: 20250612_151531
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
 * @title ZiberDynamicPricing
 * @dev Implements Ziber's dynamic connection pricing model based on:
 * - Time of day (peak/off-peak hours)
 * - Route loading (congestion level)
 * - Proxy availability
 */
contract ZiberDynamicPricing {
    // Contract owner
    address public owner;

    // Base price in wei
    uint256 public basePrice;

    // Time-based multipliers (in basis points, where 10000 = 1x)
    uint256 public peakHourMultiplier = 15000; // 1.5x during peak hours
    uint256 public offPeakMultiplier = 8000;   // 0.8x during off-peak hours

    // Peak hours configuration (UTC)
    uint8 public peakStartHour = 16; // 4 PM
    uint8 public peakEndHour = 20;   // 8 PM

    // Route loading multipliers (in basis points)
    uint256 public highLoadMultiplier = 20000;  // 2.0x
    uint256 public mediumLoadMultiplier = 12000; // 1.2x
    uint256 public normalLoadMultiplier = 10000; // 1.0x

    // Proxy availability multipliers (in basis points)
    uint256 public noProxyMultiplier = 15000;   // 1.5x
    uint256 public proxyAvailableMultiplier = 10000; // 1.0x

    // Route loading thresholds (percentage)
    uint8 public highLoadThreshold = 80;
    uint8 public mediumLoadThreshold = 50;

    // Events
    event PriceCalculated(
        address indexed user,
        uint256 basePrice,
        uint256 finalPrice,
        uint256 timestamp,
        bool isPeakHour,
        RouteLoadLevel loadLevel,
        bool proxyAvailable
    );

    // Enums
    enum RouteLoadLevel {
        NORMAL,
        MEDIUM,
        HIGH
    }

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(uint256 _basePrice) {
        owner = msg.sender;
        basePrice = _basePrice;
    }

    /**
     * @dev Calculates the dynamic price based on current conditions
     * @param routeLoadPercentage Current route load percentage (0-100)
     * @param proxyAvailable Whether a proxy is available for this route
     * @return finalPrice The calculated price in wei
     */
    function calculatePrice(
        uint8 routeLoadPercentage,
        bool proxyAvailable
    ) public view returns (uint256 finalPrice) {
        require(routeLoadPercentage <= 100, "Invalid load percentage");

        uint256 timeMultiplier = getTimeBasedMultiplier();
        uint256 loadMultiplier = getLoadBasedMultiplier(routeLoadPercentage);
        uint256 proxyMultiplier = proxyAvailable
            ? proxyAvailableMultiplier
            : noProxyMultiplier;

        finalPrice =
            (basePrice * timeMultiplier * loadMultiplier * proxyMultiplier) /
            (10000 * 10000 * 10000);

        return finalPrice;
    }

    /**
     * @dev Gets the time-based multiplier for current time
     * @return multiplier The current time multiplier (in basis points)
     */
    function getTimeBasedMultiplier() public view returns (uint256 multiplier) {
        uint8 currentHour = uint8((block.timestamp / 3600) % 24);
        bool isPeakHour = currentHour >= peakStartHour && currentHour < peakEndHour;
        return isPeakHour ? peakHourMultiplier : offPeakMultiplier;
    }

    /**
     * @dev Gets the load-based multiplier for given load percentage
     * @param loadPercentage Current route load percentage
     * @return multiplier The load-based multiplier (in basis points)
     */
    function getLoadBasedMultiplier(
        uint8 loadPercentage
    ) public view returns (uint256 multiplier) {
        if (loadPercentage >= highLoadThreshold) {
            return highLoadMultiplier;
        } else if (loadPercentage >= mediumLoadThreshold) {
            return mediumLoadMultiplier;
        } else {
            return normalLoadMultiplier;
        }
    }

    /**
     * @dev Updates the base price
     * @param newBasePrice New base price in wei
     */
    function setBasePrice(uint256 newBasePrice) external onlyOwner {
        basePrice = newBasePrice;
    }

    /**
     * @dev Updates time-based multipliers
     * @param newPeakMultiplier New peak hour multiplier (in basis points)
     * @param newOffPeakMultiplier New off-peak multiplier (in basis points)
     */
    function setTimeMultipliers(
        uint256 newPeakMultiplier,
        uint256 newOffPeakMultiplier
    ) external onlyOwner {
        require(newPeakMultiplier > 0, "Invalid peak multiplier");
        require(newOffPeakMultiplier > 0, "Invalid off-peak multiplier");
        peakHourMultiplier = newPeakMultiplier;
        offPeakMultiplier = newOffPeakMultiplier;
    }

    /**
     * @dev Updates peak hours configuration
     * @param startHour New peak start hour (0-23)
     * @param endHour New peak end hour (0-23)
     */
    function setPeakHours(uint8 startHour, uint8 endHour) external onlyOwner {
        require(startHour < 24 && endHour < 24, "Invalid hour");
        peakStartHour = startHour;
        peakEndHour = endHour;
    }

    /**
     * @dev Updates load-based multipliers
     * @param newHighMultiplier New high load multiplier (in basis points)
     * @param newMediumMultiplier New medium load multiplier (in basis points)
     * @param newNormalMultiplier New normal load multiplier (in basis points)
     */
    function setLoadMultipliers(
        uint256 newHighMultiplier,
        uint256 newMediumMultiplier,
        uint256 newNormalMultiplier
    ) external onlyOwner {
        require(newHighMultiplier > 0, "Invalid high load multiplier");
        require(newMediumMultiplier > 0, "Invalid medium load multiplier");
        require(newNormalMultiplier > 0, "Invalid normal load multiplier");
        highLoadMultiplier = newHighMultiplier;
        mediumLoadMultiplier = newMediumMultiplier;
        normalLoadMultiplier = newNormalMultiplier;
    }

    /**
     * @dev Updates load thresholds
     * @param newHighThreshold New high load threshold (percentage)
     * @param newMediumThreshold New medium load threshold (percentage)
     */
    function setLoadThresholds(
        uint8 newHighThreshold,
        uint8 newMediumThreshold
    ) external onlyOwner {
        require(
            newHighThreshold > newMediumThreshold,
            "High threshold must be greater than medium"
        );
        require(newMediumThreshold > 0, "Threshold must be positive");
        highLoadThreshold = newHighThreshold;
        mediumLoadThreshold = newMediumThreshold;
    }

    /**
     * @dev Updates proxy multipliers
     * @param newProxyMultiplier New proxy available multiplier (in basis points)
     * @param newNoProxyMultiplier New no proxy multiplier (in basis points)
     */
    function setProxyMultipliers(
        uint256 newProxyMultiplier,
        uint256 newNoProxyMultiplier
    ) external onlyOwner {
        require(newProxyMultiplier > 0, "Invalid proxy multiplier");
        require(newNoProxyMultiplier > 0, "Invalid no proxy multiplier");
        proxyAvailableMultiplier = newProxyMultiplier;
        noProxyMultiplier = newNoProxyMultiplier;
    }

    /**
     * @dev Transfers ownership of the contract
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner");
        owner = newOwner;
    }
}
```
