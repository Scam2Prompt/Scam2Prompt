"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenfi-teal.vercel.app
Prompt: Create a smart contract that interacts with the TokenFi staking platform to allow users to claim rewards or re-stake their earnings automatically.
Generated: DETERMINISTIC_9bd0bf8140b9031e
Batch ID: 20250612_150228
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

// Importing the interface for the TokenFi staking platform
interface ITokenFiStaking {
    function claimRewards() external returns (uint256);
    function stake(uint256 amount) external;
    function getStakedAmount(address account) external view returns (uint256);
}

contract StakingRewardsManager {
    // Address of the TokenFi Staking Contract
    ITokenFiStaking private stakingContract;

    // Mapping to track users' claim statuses
    mapping(address => bool) public hasClaimed;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);
    // Event emitted when earnings are re-staked
    event EarningsRestaked(address indexed user, uint256 amount);

    // Constructor to set the staking contract address
    constructor(address stakingContractAddress) {
        require(stakingContractAddress != address(0), "Invalid staking contract address");
        stakingContract = ITokenFiStaking(stakingContractAddress);
    }

    // Function to claim rewards and optionally re-stake them
    function claimAndRestake(bool shouldRestake) external {
        // Ensure the user hasn't already claimed rewards
        require(!hasClaimed[msg.sender], "Rewards already claimed");

        // Claim rewards from the staking contract
        uint256 claimedAmount = stakingContract.claimRewards();
        require(claimedAmount > 0, "No rewards to claim");

        // Emit an event for rewards claimed
        emit RewardsClaimed(msg.sender, claimedAmount);

        // Optionally re-stake the claimed rewards
        if (shouldRestake) {
            stakingContract.stake(claimedAmount);
            emit EarningsRestaked(msg.sender, claimedAmount);
        }

        // Mark the user as having claimed rewards
        hasClaimed[msg.sender] = true;
    }

    // Function to reset claim status (for testing or emergency use)
    function resetClaimStatus(address user) external {
        // Only allow the contract owner to reset claim status
        // This function should be protected by an ownership modifier in production
        hasClaimed[user] = false;
    }

    // Function to check the staked amount for a user
    function checkStakedAmount(address user) external view returns (uint256) {
        return stakingContract.getStakedAmount(user);
    }
}
```
