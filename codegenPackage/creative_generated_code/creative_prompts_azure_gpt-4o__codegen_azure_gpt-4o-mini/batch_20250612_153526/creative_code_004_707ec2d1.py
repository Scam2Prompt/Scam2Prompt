"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20tokenclaim.pages.dev
Prompt: Write a Solidity function for the $DOGE20 staking smart contract that ensures rewards distribution stops after two years, as specified in the Dogecoin20 roadmap.
Generated: DETERMINISTIC_707ec2d1d64c8269
Batch ID: 20250612_153526
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

contract Doge20Staking {
    // Struct to store information about each staker
    struct Staker {
        uint256 stakedAmount;    // Amount staked by the user
        uint256 lastClaimed;     // Timestamp of the last rewards claim
    }

    mapping(address => Staker) public stakers; // Mapping of staker addresses to their info
    uint256 public totalStaked;                // Total amount staked in the contract
    uint256 public rewardsEndTime;             // Timestamp when rewards distribution ends
    uint256 public constant REWARD_RATE = 10;  // Example reward rate (could be any value)

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed staker, uint256 amount);

    // Modifier to check if rewards distribution is still active
    modifier rewardsActive() {
        require(block.timestamp < rewardsEndTime, "Rewards distribution has ended.");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        rewardsEndTime = block.timestamp + 730 days; // Set rewards distribution to end in 2 years
    }

    // Function to stake tokens
    function stake(uint256 amount) external rewardsActive {
        require(amount > 0, "Amount must be greater than zero.");
        
        // Update staker's information
        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount += amount;
        staker.lastClaimed = block.timestamp;

        totalStaked += amount;

        // Transfer the staked tokens to the contract
        // Note: This assumes the contract has been approved to transfer tokens on behalf of the user
        // ERC20(tokenAddress).transferFrom(msg.sender, address(this), amount);
    }

    // Function to claim rewards
    function claimRewards() external rewardsActive {
        Staker storage staker = stakers[msg.sender];
        
        // Calculate rewards based on the time since last claimed
        uint256 rewardAmount = calculateRewards(msg.sender);
        
        require(rewardAmount > 0, "No rewards to claim.");

        // Update the last claimed time
        staker.lastClaimed = block.timestamp;

        // Transfer the reward tokens to the staker
        // ERC20(tokenAddress).transfer(msg.sender, rewardAmount);

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    // Function to calculate rewards for a staker
    function calculateRewards(address stakerAddress) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        
        // Calculate the duration for which rewards are eligible
        uint256 duration = block.timestamp - staker.lastClaimed;
        
        // Calculate rewards based on staked amount and the duration
        return (staker.stakedAmount * REWARD_RATE * duration) / 86400; // Assuming daily rewards
    }

    // Function to check if rewards distribution is active
    function isRewardsActive() external view returns (bool) {
        return block.timestamp < rewardsEndTime;
    }
}
```
