"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-token.pages.dev
Prompt: Write a function in Solidity to calculate staking rewards for token holders, with interest rates ranging from 7% to 17%, as outlined in Pushd's staking program.
Generated: DETERMINISTIC_a3e2be19d6b407d4
Batch ID: 20250612_151246
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

contract StakingRewards {
    // Struct to hold staking details for each user
    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Timestamp of staking
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Event to emit when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event to emit when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 reward);

    // Interest rates in basis points (700 to 1700)
    uint256 public constant MIN_INTEREST_RATE = 700; // 7%
    uint256 public constant MAX_INTEREST_RATE = 1700; // 17%
    uint256 public constant INTEREST_RATE_STEP = 100; // 1%

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Update the user's stake information
        stakes[msg.sender] = Stake({
            amount: _amount,
            timestamp: block.timestamp
        });

        // Emit the Staked event
        emit Staked(msg.sender, _amount);
    }

    // Function to calculate staking rewards
    function calculateRewards(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];

        // Ensure the user has staked tokens
        require(userStake.amount > 0, "User has no stake");

        // Calculate the duration for which the tokens have been staked
        uint256 duration = block.timestamp - userStake.timestamp;

        // Determine interest rate based on the staked amount
        uint256 interestRate = getInterestRate(userStake.amount);

        // Calculate rewards: (amount * interestRate * duration) / (365 days)
        uint256 rewards = (userStake.amount * interestRate * duration) / (365 days * 10000);

        return rewards;
    }

    // Function to get the interest rate based on the staked amount
    function getInterestRate(uint256 _amount) internal pure returns (uint256) {
        // For demonstration, let’s assume a linear mapping based on the amount staked
        // This can be adjusted based on actual staking program rules
        if (_amount < 1000 ether) {
            return MIN_INTEREST_RATE; // 7%
        } else if (_amount >= 1000 ether && _amount < 5000 ether) {
            return MIN_INTEREST_RATE + INTEREST_RATE_STEP; // 8%
        } else if (_amount >= 5000 ether && _amount < 10000 ether) {
            return MIN_INTEREST_RATE + (INTEREST_RATE_STEP * 2); // 9%
        } else {
            return MAX_INTEREST_RATE; // 17%
        }
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available to claim");

        // Logic to transfer rewards to the user would go here

        // Emit the RewardsClaimed event
        emit RewardsClaimed(msg.sender, rewards);
    }
}
```
