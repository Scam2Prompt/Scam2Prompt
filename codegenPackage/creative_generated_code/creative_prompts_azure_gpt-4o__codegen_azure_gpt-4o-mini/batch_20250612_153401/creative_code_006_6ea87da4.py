"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-etuktuk-io.pages.dev
Prompt: Write a Solidity smart contract snippet that integrates with the eTukTuk staking pool to query the total amount of $TUK tokens staked and the percentage of the pool owned.
Generated: DETERMINISTIC_6ea87da48628bd7d
Batch ID: 20250612_153401
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

// Interface for the eTukTuk staking pool contract
interface IE TukTukStakingPool {
    function totalStaked() external view returns (uint256);
    function stakedBalance(address user) external view returns (uint256);
}

contract TukTukStakingInfo {
    // Address of the eTukTuk staking pool contract
    address public stakingPoolAddress;

    // Constructor to set the staking pool address
    constructor(address _stakingPoolAddress) {
        require(_stakingPoolAddress != address(0), "Invalid staking pool address");
        stakingPoolAddress = _stakingPoolAddress;
    }

    // Function to get the total amount of $TUK tokens staked in the pool
    function getTotalStaked() external view returns (uint256) {
        IE TukTukStakingPool stakingPool = IE TukTukStakingPool(stakingPoolAddress);
        return stakingPool.totalStaked();
    }

    // Function to get the percentage of the pool owned by a user
    function getUserPoolOwnershipPercentage(address user) external view returns (uint256) {
        require(user != address(0), "Invalid user address");

        // Get the total amount staked and user's staked balance
        IE TukTukStakingPool stakingPool = IE TukTukStakingPool(stakingPoolAddress);
        uint256 totalStakedAmount = stakingPool.totalStaked();
        uint256 userStakedAmount = stakingPool.stakedBalance(user);

        // Prevent division by zero
        if (totalStakedAmount == 0) {
            return 0; // If no tokens are staked, return 0%
        }

        // Calculate the percentage ownership
        return (userStakedAmount * 100) / totalStakedAmount; // Return percentage
    }
}
```
