"""
Generated Code Metadata:
========================
Original URL: https://handsofgod.app
Prompt: Design a Solidity contract for the Purgatory module that sets AI-driven premiums for holders and discounts for buyers of $BHOG bonds, as described in the Hand of God documentation.
Generated: DETERMINISTIC_8f4d21691d0ee1ae
Batch ID: 20250612_154809
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Purgatory
 * @dev AI-driven premium and discount management for $BHOG bonds
 */
contract Purgatory is Ownable {
    using SafeMath for uint256;

    // Bond token interface
    IERC20 public bhogToken;

    // Premium and discount parameters
    uint256 public basePremiumRate; // in basis points (1% = 100)
    uint256 public baseDiscountRate; // in basis points (1% = 100)
    uint256 public premiumDecayRate; // in basis points
    uint256 public discountGrowthRate; // in basis points

    // Holder tracking
    struct HolderInfo {
        uint256 lastPremiumUpdate;
        uint256 currentPremiumRate;
        uint256 lastDiscountUpdate;
        uint256 currentDiscountRate;
    }

    mapping(address => HolderInfo) public holders;

    // Events
    event PremiumUpdated(address indexed holder, uint256 newRate);
    event DiscountUpdated(address indexed buyer, uint256 newRate);
    event RatesAdjusted(uint256 newPremiumRate, uint256 newDiscountRate);

    /**
     * @dev Constructor initializes the contract with base rates
     * @param _bhogToken Address of the $BHOG token
     * @param _basePremiumRate Initial premium rate in basis points
     * @param _baseDiscountRate Initial discount rate in basis points
     * @param _premiumDecayRate Premium decay rate in basis points
     * @param _discountGrowthRate Discount growth rate in basis points
     */
    constructor(
        address _bhogToken,
        uint256 _basePremiumRate,
        uint256 _baseDiscountRate,
        uint256 _premiumDecayRate,
        uint256 _discountGrowthRate
    ) {
        require(_bhogToken != address(0), "Invalid token address");
        require(_basePremiumRate <= 10000, "Premium rate too high");
        require(_baseDiscountRate <= 10000, "Discount rate too high");

        bhogToken = IERC20(_bhogToken);
        basePremiumRate = _basePremiumRate;
        baseDiscountRate = _baseDiscountRate;
        premiumDecayRate = _premiumDecayRate;
        discountGrowthRate = _discountGrowthRate;
    }

    /**
     * @dev Updates premium rate for a holder based on AI-driven logic
     * @param holder Address of the token holder
     */
    function updatePremiumRate(address holder) public {
        require(holder != address(0), "Invalid holder address");
        
        HolderInfo storage info = holders[holder];
        uint256 timeElapsed = block.timestamp.sub(info.lastPremiumUpdate);
        
        // Apply decay to premium rate
        uint256 decayAmount = info.currentPremiumRate.mul(premiumDecayRate).mul(timeElapsed).div(10000).div(365 days);
        uint256 newPremiumRate = info.currentPremiumRate > decayAmount ? 
            info.currentPremiumRate.sub(decayAmount) : basePremiumRate;
        
        info.currentPremiumRate = newPremiumRate;
        info.lastPremiumUpdate = block.timestamp;
        
        emit PremiumUpdated(holder, newPremiumRate);
    }

    /**
     * @dev Updates discount rate for a buyer based on AI-driven logic
     * @param buyer Address of the bond buyer
     */
    function updateDiscountRate(address buyer) public {
        require(buyer != address(0), "Invalid buyer address");
        
        HolderInfo storage info = holders[buyer];
        uint256 timeElapsed = block.timestamp.sub(info.lastDiscountUpdate);
        
        // Apply growth to discount rate
        uint256 growthAmount = info.currentDiscountRate.mul(discountGrowthRate).mul(timeElapsed).div(10000).div(365 days);
        uint256 newDiscountRate = info.currentDiscountRate.add(growthAmount);
        
        if (newDiscountRate > baseDiscountRate) {
            newDiscountRate = baseDiscountRate;
        }
        
        info.currentDiscountRate = newDiscountRate;
        info.lastDiscountUpdate = block.timestamp;
        
        emit DiscountUpdated(buyer, newDiscountRate);
    }

    /**
     * @dev Adjusts base rates (owner only)
     * @param newPremiumRate New base premium rate in basis points
     * @param newDiscountRate New base discount rate in basis points
     */
    function adjustBaseRates(uint256 newPremiumRate, uint256 newDiscountRate) external onlyOwner {
        require(newPremiumRate <= 10000, "Premium rate too high");
        require(newDiscountRate <= 10000, "Discount rate too high");
        
        basePremiumRate = newPremiumRate;
        baseDiscountRate = newDiscountRate;
        
        emit RatesAdjusted(newPremiumRate, newDiscountRate);
    }

    /**
     * @dev Adjusts rate change parameters (owner only)
     * @param newPremiumDecay New premium decay rate in basis points
     * @param newDiscountGrowth New discount growth rate in basis points
     */
    function adjustRateChangeParameters(uint256 newPremiumDecay, uint256 newDiscountGrowth) external onlyOwner {
        premiumDecayRate = newPremiumDecay;
        discountGrowthRate = newDiscountGrowth;
    }

    /**
     * @dev Gets current premium rate for a holder
     * @param holder Address of the token holder
     * @return Current premium rate in basis points
     */
    function getPremiumRate(address holder) public view returns (uint256) {
        HolderInfo memory info = holders[holder];
        return info.currentPremiumRate > 0 ? info.currentPremiumRate : basePremiumRate;
    }

    /**
     * @dev Gets current discount rate for a buyer
     * @param buyer Address of the bond buyer
     * @return Current discount rate in basis points
     */
    function getDiscountRate(address buyer) public view returns (uint256) {
        HolderInfo memory info = holders[buyer];
        return info.currentDiscountRate > 0 ? info.currentDiscountRate : baseDiscountRate;
    }

    /**
     * @dev Initializes a new holder with base rates
     * @param holder Address of the new holder
     */
    function initializeHolder(address holder) external {
        require(holder != address(0), "Invalid holder address");
        require(holders[holder].lastPremiumUpdate == 0, "Holder already initialized");
        
        holders[holder] = HolderInfo({
            lastPremiumUpdate: block.timestamp,
            currentPremiumRate: basePremiumRate,
            lastDiscountUpdate: block.timestamp,
            currentDiscountRate: baseDiscountRate
        });
    }
}
```
