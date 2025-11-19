"""
Generated Code Metadata:
========================
Original URL: https://retik-claims.pages.dev
Prompt: Develop a Solidity smart contract for managing Retik's tier-based rewards system, including cashback percentages and card costs.
Generated: DETERMINISTIC_2a3b409b5382a477
Batch ID: 20250612_153713
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

/// @title Retik's Tier-Based Rewards System
/// @author Your Name
/// @notice This contract manages a tier-based rewards system with cashback percentages and card costs.
contract RetikRewards {
    // Struct to represent a reward tier
    struct Tier {
        uint256 cashbackPercentage; // Cashback percentage for the tier
        uint256 cardCost;           // Cost of the card for the tier
    }

    // Mapping to store tiers by their ID
    mapping(uint256 => Tier) public tiers;

    // Event emitted when a new tier is created
    event TierCreated(uint256 indexed tierId, uint256 cashbackPercentage, uint256 cardCost);

    // Event emitted when a tier is updated
    event TierUpdated(uint256 indexed tierId, uint256 cashbackPercentage, uint256 cardCost);

    // Event emitted when a tier is deleted
    event TierDeleted(uint256 indexed tierId);

    // Counter for tier IDs
    uint256 public tierCount;

    /// @notice Creates a new tier with specified cashback percentage and card cost
    /// @param _cashbackPercentage The cashback percentage for the new tier
    /// @param _cardCost The cost of the card for the new tier
    function createTier(uint256 _cashbackPercentage, uint256 _cardCost) external {
        require(_cashbackPercentage > 0, "Cashback percentage must be greater than 0");
        require(_cardCost > 0, "Card cost must be greater than 0");

        tierCount++;
        tiers[tierCount] = Tier(_cashbackPercentage, _cardCost);

        emit TierCreated(tierCount, _cashbackPercentage, _cardCost);
    }

    /// @notice Updates an existing tier's cashback percentage and card cost
    /// @param _tierId The ID of the tier to update
    /// @param _cashbackPercentage The new cashback percentage for the tier
    /// @param _cardCost The new cost of the card for the tier
    function updateTier(uint256 _tierId, uint256 _cashbackPercentage, uint256 _cardCost) external {
        require(_tierId > 0 && _tierId <= tierCount, "Invalid tier ID");
        require(_cashbackPercentage > 0, "Cashback percentage must be greater than 0");
        require(_cardCost > 0, "Card cost must be greater than 0");

        tiers[_tierId].cashbackPercentage = _cashbackPercentage;
        tiers[_tierId].cardCost = _cardCost;

        emit TierUpdated(_tierId, _cashbackPercentage, _cardCost);
    }

    /// @notice Deletes a tier by its ID
    /// @param _tierId The ID of the tier to delete
    function deleteTier(uint256 _tierId) external {
        require(_tierId > 0 && _tierId <= tierCount, "Invalid tier ID");

        delete tiers[_tierId];

        emit TierDeleted(_tierId);
    }

    /// @notice Retrieves the details of a specific tier
    /// @param _tierId The ID of the tier to retrieve
    /// @return cashbackPercentage The cashback percentage of the tier
    /// @return cardCost The cost of the card for the tier
    function getTier(uint256 _tierId) external view returns (uint256 cashbackPercentage, uint256 cardCost) {
        require(_tierId > 0 && _tierId <= tierCount, "Invalid tier ID");

        Tier memory tier = tiers[_tierId];
        return (tier.cashbackPercentage, tier.cardCost);
    }
}
```
