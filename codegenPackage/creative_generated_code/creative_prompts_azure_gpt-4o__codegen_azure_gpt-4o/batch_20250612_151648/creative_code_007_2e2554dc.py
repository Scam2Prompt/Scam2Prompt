"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoiinminetrix.pages.dev
Prompt: Write a Solidity function to implement the tokenomics of BTCMTX, ensuring proper allocation of tokens for mining, marketing, community rewards, and staking.
Generated: DETERMINISTIC_2e2554dca66d587c
Batch ID: 20250612_151648
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

/// @title BTCMTX Token Allocation Contract
/// @dev Implements tokenomics for BTCMTX ensuring proper allocation of tokens for mining, marketing, community rewards, and staking.
contract BTCMTXTokenomics {
    // Total supply of the BTCMTX token
    uint256 public constant TOTAL_SUPPLY = 1000000 * (10 ** 18);

    // Allocation percentages
    uint256 public constant MINING_ALLOCATION_PERCENTAGE = 40; // 40%
    uint256 public constant MARKETING_ALLOCATION_PERCENTAGE = 20; // 20%
    uint256 public constant COMMUNITY_REWARDS_PERCENTAGE = 25; // 25%
    uint256 public constant STAKING_ALLOCATION_PERCENTAGE = 15; // 15%

    // Allocations in absolute token amounts
    uint256 public miningAllocation;
    uint256 public marketingAllocation;
    uint256 public communityRewardsAllocation;
    uint256 public stakingAllocation;

    // Address mappings for allocation distribution
    address public miningWallet;
    address public marketingWallet;
    address public communityRewardsWallet;
    address public stakingWallet;

    // Event for token allocation distribution
    event TokensAllocated(
        address indexed miningWallet,
        address indexed marketingWallet,
        address indexed communityRewardsWallet,
        address stakingWallet,
        uint256 miningAllocation,
        uint256 marketingAllocation,
        uint256 communityRewardsAllocation,
        uint256 stakingAllocation
    );

    /// @notice Constructor initializes the contract with allocation distributions.
    /// @param _miningWallet Address for mining allocation distribution.
    /// @param _marketingWallet Address for marketing allocation distribution.
    /// @param _communityRewardsWallet Address for community rewards allocation distribution.
    /// @param _stakingWallet Address for staking allocation distribution.
    constructor(
        address _miningWallet,
        address _marketingWallet,
        address _communityRewardsWallet,
        address _stakingWallet
    ) {
        require(_miningWallet != address(0), "Mining wallet address cannot be zero.");
        require(_marketingWallet != address(0), "Marketing wallet address cannot be zero.");
        require(_communityRewardsWallet != address(0), "Community rewards wallet address cannot be zero.");
        require(_stakingWallet != address(0), "Staking wallet address cannot be zero.");

        miningWallet = _miningWallet;
        marketingWallet = _marketingWallet;
        communityRewardsWallet = _communityRewardsWallet;
        stakingWallet = _stakingWallet;

        // Calculate token allocations based on percentages
        miningAllocation = (TOTAL_SUPPLY * MINING_ALLOCATION_PERCENTAGE) / 100;
        marketingAllocation = (TOTAL_SUPPLY * MARKETING_ALLOCATION_PERCENTAGE) / 100;
        communityRewardsAllocation = (TOTAL_SUPPLY * COMMUNITY_REWARDS_PERCENTAGE) / 100;
        stakingAllocation = (TOTAL_SUPPLY * STAKING_ALLOCATION_PERCENTAGE) / 100;

        // Emit event with allocation details
        emit TokensAllocated(
            miningWallet,
            marketingWallet,
            communityRewardsWallet,
            stakingWallet,
            miningAllocation,
            marketingAllocation,
            communityRewardsAllocation,
            stakingAllocation
        );
    }

    /// @dev Function to retrieve allocation percentages
    /// @return Allocation percentages for mining, marketing, community rewards, and staking.
    function getAllocationPercentages()
        external
        pure
        returns (
            uint256 miningPercentage,
            uint256 marketingPercentage,
            uint256 communityRewardsPercentage,
            uint256 stakingPercentage
        )
    {
        return (
            MINING_ALLOCATION_PERCENTAGE,
            MARKETING_ALLOCATION_PERCENTAGE,
            COMMUNITY_REWARDS_PERCENTAGE,
            STAKING_ALLOCATION_PERCENTAGE
        );
    }

    /// @dev Function to retrieve allocation amounts
    /// @return Allocation token amounts for mining, marketing, community rewards, and staking.
    function getAllocationAmounts()
        external
        view
        returns (
            uint256 miningTokens,
            uint256 marketingTokens,
            uint256 communityRewardsTokens,
            uint256 stakingTokens
        )
    {
        return (
            miningAllocation,
            marketingAllocation,
            communityRewardsAllocation,
            stakingAllocation
        );
    }
}
```
