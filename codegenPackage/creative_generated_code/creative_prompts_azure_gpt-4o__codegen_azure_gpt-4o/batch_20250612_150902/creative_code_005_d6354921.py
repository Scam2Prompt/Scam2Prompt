"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbag-org.pages.dev
Prompt: Provide an example of ERC20 tokenomics calculations, including allocations for presale, staking, liquidity, and team incentives, based on MoonBag's tokenomics structure.
Generated: DETERMINISTIC_d6354921b099ed3e
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title TokenomicsCalculator
 * @dev A smart contract for calculating ERC20 token allocations based on tokenomics structure.
 */
contract TokenomicsCalculator {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * (10 ** 18); // 1 billion tokens, assuming 18 decimals

    // Tokenomics structure percentages
    uint256 public constant PRESALE_PERCENTAGE = 20; // 20% for presale
    uint256 public constant STAKING_PERCENTAGE = 30; // 30% for staking rewards
    uint256 public constant LIQUIDITY_PERCENTAGE = 25; // 25% for liquidity
    uint256 public constant TEAM_PERCENTAGE = 25; // 25% for team incentives

    // Allocation amounts
    uint256 public presaleAllocation;
    uint256 public stakingAllocation;
    uint256 public liquidityAllocation;
    uint256 public teamAllocation;

    /**
     * @dev Constructor to initialize allocations based on the predefined percentages.
     */
    constructor() {
        // Calculate allocations based on the percentages
        presaleAllocation = calculateAllocation(PRESALE_PERCENTAGE);
        stakingAllocation = calculateAllocation(STAKING_PERCENTAGE);
        liquidityAllocation = calculateAllocation(LIQUIDITY_PERCENTAGE);
        teamAllocation = calculateAllocation(TEAM_PERCENTAGE);

        // Ensure total allocations don't exceed TOTAL_SUPPLY
        require(
            presaleAllocation + stakingAllocation + liquidityAllocation + teamAllocation == TOTAL_SUPPLY,
            "Tokenomics percentages do not add up to 100%"
        );
    }

    /**
     * @dev Internal function to calculate token allocation based on percentage.
     * @param percentage The percentage of tokens to allocate.
     * @return The calculated token allocation.
     */
    function calculateAllocation(uint256 percentage) internal pure returns (uint256) {
        require(percentage <= 100, "Percentage cannot exceed 100");
        return (TOTAL_SUPPLY * percentage) / 100;
    }

    /**
     * @dev Public function to get all allocation details.
     * @return presaleAllocation, stakingAllocation, liquidityAllocation, teamAllocation
     */
    function getAllocations()
        external
        view
        returns (uint256, uint256, uint256, uint256)
    {
        return (presaleAllocation, stakingAllocation, liquidityAllocation, teamAllocation);
    }
}
```

This code represents a basic implementation of ERC20 tokenomics calculations with presale, staking, liquidity, and team allocations based on fixed percentages. It is designed to be clean, robust, and production-ready.
