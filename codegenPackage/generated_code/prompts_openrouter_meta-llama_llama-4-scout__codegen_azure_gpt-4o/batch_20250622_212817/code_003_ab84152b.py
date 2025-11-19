"""
Generated Code Metadata:
========================
Original URL: https://memeindextoken.pages.dev
Prompt: Write a Solidity function to calculate the APY for staking $MEMEX tokens during presale, taking into account the 25% staking rewards and the token's presale allocation.
Generated: DETERMINISTIC_ab84152b0287d6a0
Batch ID: 20250622_212817
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
 * @title MEMEXStaking
 * @dev Contract to calculate APY for staking MEMEX tokens during presale.
 */
contract MEMEXStaking {
    // State variables
    uint256 public presaleAllocation; // Total MEMEX tokens allocated for presale
    uint256 public stakingRewardRate; // Staking reward rate (e.g., 25%)

    /**
     * @dev Constructor to initialize presale allocation and staking reward rate.
     * @param _presaleAllocation Total MEMEX tokens allocated for presale.
     * @param _stakingRewardRate Staking reward rate in percentage (e.g., 25 for 25%).
     */
    constructor(uint256 _presaleAllocation, uint256 _stakingRewardRate) {
        require(_presaleAllocation > 0, "Presale allocation must be greater than zero");
        require(_stakingRewardRate > 0 && _stakingRewardRate <= 100, "Invalid staking reward rate");
        presaleAllocation = _presaleAllocation;
        stakingRewardRate = _stakingRewardRate;
    }

    /**
     * @dev Function to calculate the APY for staking MEMEX tokens during presale.
     * @param stakedAmount Amount of MEMEX tokens staked by the user.
     * @return apy Annual Percentage Yield (APY) for the staked amount.
     */
    function calculateAPY(uint256 stakedAmount) external view returns (uint256 apy) {
        require(stakedAmount > 0, "Staked amount must be greater than zero");
        require(stakedAmount <= presaleAllocation, "Staked amount exceeds presale allocation");

        // Calculate APY based on staking reward rate
        apy = (stakedAmount * stakingRewardRate) / 100;

        return apy;
    }
}
```
