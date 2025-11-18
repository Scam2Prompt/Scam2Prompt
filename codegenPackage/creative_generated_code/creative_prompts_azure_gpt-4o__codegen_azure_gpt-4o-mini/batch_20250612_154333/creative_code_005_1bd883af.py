"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flockerz-staking.pages.dev
Prompt: Create a Solidity function to allow users to claim their $FLOCK staking rewards, ensuring the rewards are calculated dynamically based on the staking pool percentage and the elapsed ETH blocks.
Generated: DETERMINISTIC_1bd883af5293de79
Batch ID: 20250612_154333
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

contract FlockStaking {
    // State variables
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public lastClaimedBlock; // Last block where rewards were claimed
    uint256 public totalStaked; // Total amount of tokens staked in the contract
    uint256 public rewardRate; // Reward rate per block in FLOCK tokens
    uint256 public constant BLOCKS_PER_REWARD = 1; // Blocks used for reward calculation

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Modifier to check if user has staked tokens
    modifier hasStaked() {
        require(stakedAmount[msg.sender] > 0, "No staked tokens found");
        _;
    }

    // Function to stake tokens (example purpose, not part of user request)
    function stake(uint256 amount) external {
        // Logic to handle the staking of tokens (not implemented)
    }

    // Function to claim staking rewards
    function claimRewards() external hasStaked {
        uint256 claimableRewards = calculateRewards(msg.sender);
        require(claimableRewards > 0, "No rewards to claim");

        // Update the last claimed block to the current block
        lastClaimedBlock[msg.sender] = block.number;

        // Transfer rewards to the user
        // Assuming a function 'transfer' exists to handle token transfers (not implemented)
        // transfer(msg.sender, claimableRewards);

        emit RewardsClaimed(msg.sender, claimableRewards);
    }

    // Function to calculate the rewards for a user
    function calculateRewards(address user) internal view returns (uint256) {
        // Calculate the number of blocks elapsed since the last claim
        uint256 blocksElapsed = block.number - lastClaimedBlock[user];

        // Calculate the user's share of the rewards
        uint256 userShare = (stakedAmount[user] * rewardRate * blocksElapsed) / totalStaked;

        return userShare;
    }

    // Function to update the reward rate (only owner can call)
    function updateRewardRate(uint256 newRate) external {
        // Logic to ensure that only the contract owner can call (not implemented)
        rewardRate = newRate;
    }
}
```
