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

contract MemexStaking {
    // State variables
    uint256 public constant STAKING_REWARD_PERCENTAGE = 25; // 25% staking rewards
    uint256 public presaleAllocation; // Total presale allocation of $MEMEX tokens

    // Event to log APY calculation
    event APYCalculated(uint256 apy);

    // Constructor to initialize presale allocation
    constructor(uint256 _presaleAllocation) {
        require(_presaleAllocation > 0, "Presale allocation must be greater than zero");
        presaleAllocation = _presaleAllocation;
    }

    /**
     * @dev Function to calculate the Annual Percentage Yield (APY) for staking $MEMEX tokens.
     * @return apy The calculated APY based on the staking rewards and presale allocation.
     */
    function calculateAPY() external view returns (uint256) {
        // Calculate the staking rewards
        uint256 stakingRewards = (presaleAllocation * STAKING_REWARD_PERCENTAGE) / 100;

        // Calculate APY (assuming rewards are distributed annually)
        uint256 apy = (stakingRewards * 100) / presaleAllocation;

        // Emit event with the calculated APY
        emit APYCalculated(apy);

        return apy;
    }
}
```
