"""
Generated Code Metadata:
========================
Original URL: https://zora-air-spring.nfts2.me
Prompt: Implement a function in Solidity that calculates referral fees based on the number of NFT mints completed through a referral link, as outlined in the Zora Air Spring system.
Generated: DETERMINISTIC_7d0dc9b29d287847
Batch ID: 20250612_153854
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
 * @title ReferralFeeCalculator
 * @dev Calculates referral fees based on the number of NFT mints completed through a referral link
 */
contract ReferralFeeCalculator {
    // Fee structure for different mint tiers
    struct FeeTier {
        uint256 minMints;  // Minimum mints required for this tier
        uint256 feeBps;    // Fee in basis points (1/100th of a percent)
    }

    // Array of fee tiers sorted by minMints in ascending order
    FeeTier[] public feeTiers;

    // Event emitted when fee tiers are updated
    event FeeTiersUpdated(FeeTier[] newTiers);

    /**
     * @dev Constructor to initialize fee tiers
     * @param initialTiers Array of initial fee tiers
     */
    constructor(FeeTier[] memory initialTiers) {
        _setFeeTiers(initialTiers);
    }

    /**
     * @dev Set new fee tiers
     * @param newTiers Array of new fee tiers
     */
    function setFeeTiers(FeeTier[] memory newTiers) external {
        _setFeeTiers(newTiers);
    }

    /**
     * @dev Internal function to set fee tiers with validation
     * @param newTiers Array of new fee tiers
     */
    function _setFeeTiers(FeeTier[] memory newTiers) internal {
        require(newTiers.length > 0, "At least one fee tier required");
        
        // Validate tiers are in ascending order and have valid BPS
        for (uint256 i = 0; i < newTiers.length; i++) {
            if (i > 0) {
                require(
                    newTiers[i].minMints > newTiers[i-1].minMints,
                    "Tiers must be in ascending order"
                );
            }
            require(newTiers[i].feeBps <= 10000, "Fee cannot exceed 100%");
        }

        // Clear existing tiers
        delete feeTiers;

        // Add new tiers
        for (uint256 i = 0; i < newTiers.length; i++) {
            feeTiers.push(newTiers[i]);
        }

        emit FeeTiersUpdated(newTiers);
    }

    /**
     * @dev Calculate referral fee based on number of mints
     * @param mintCount Number of mints completed through referral
     * @param mintPrice Price of a single mint
     * @return feeAmount Calculated fee amount
     */
    function calculateReferralFee(uint256 mintCount, uint256 mintPrice) external view returns (uint256 feeAmount) {
        require(mintPrice > 0, "Mint price must be positive");
        
        if (feeTiers.length == 0 || mintCount == 0) {
            return 0;
        }

        // Find the highest applicable tier
        FeeTier memory applicableTier;
        for (uint256 i = feeTiers.length; i > 0; i--) {
            if (mintCount >= feeTiers[i-1].minMints) {
                applicableTier = feeTiers[i-1];
                break;
            }
        }

        // Calculate fee: (mintPrice * feeBps) / 10000
        feeAmount = (mintPrice * applicableTier.feeBps) / 10000;
        return feeAmount;
    }

    /**
     * @dev Get current fee tiers
     * @return Array of current fee tiers
     */
    function getFeeTiers() external view returns (FeeTier[] memory) {
        return feeTiers;
    }
}
```
