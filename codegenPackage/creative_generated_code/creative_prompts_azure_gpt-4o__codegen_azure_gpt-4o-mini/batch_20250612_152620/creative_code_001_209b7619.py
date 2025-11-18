"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gomble-8xr.pages.dev
Prompt: Generate a script using Solidity to claim staking rewards on the GOMBLE blockchain.
Generated: DETERMINISTIC_209b7619638d86d6
Batch ID: 20250612_152620
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

// Interface for the staking contract
interface IStaking {
    function claimRewards() external returns (uint256);
    function getStakedAmount(address staker) external view returns (uint256);
}

contract StakingRewardsClaimer {
    // Address of the staking contract
    IStaking public stakingContract;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Modifier to ensure caller is a valid address
    modifier onlyValidAddress(address user) {
        require(user != address(0), "Invalid address: zero address");
        _;
    }

    // Constructor to set the staking contract address
    constructor(address _stakingContract) onlyValidAddress(_stakingContract) {
        stakingContract = IStaking(_stakingContract);
    }

    // Function to claim staking rewards
    function claimStakingRewards() external {
        // Get the current user's staked amount
        uint256 stakedAmount = stakingContract.getStakedAmount(msg.sender);
        require(stakedAmount > 0, "No staked amount found");

        // Claim the rewards
        uint256 claimedAmount = stakingContract.claimRewards();
        require(claimedAmount > 0, "No rewards to claim");

        // Emit event for rewards claimed
        emit RewardsClaimed(msg.sender, claimedAmount);
    }
}
```
