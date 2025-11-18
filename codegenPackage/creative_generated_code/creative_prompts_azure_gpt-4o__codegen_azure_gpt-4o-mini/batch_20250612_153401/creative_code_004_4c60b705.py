"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://discoverx.pages.dev
Prompt: Write a function in Solidity to calculate and distribute DXT rewards based on APR rates and lock periods, as outlined in the DiscoverX staking options.
Generated: DETERMINISTIC_4c60b705f817ca01
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

contract DiscoverXStaking {
    // Struct to hold staking details
    struct Stake {
        uint256 amount;       // Amount staked
        uint256 startTime;    // Time when the stake was created
        uint256 lockPeriod;   // Lock period in seconds
        uint256 apr;          // Annual Percentage Rate in basis points (e.g., 500 = 5%)
    }

    // Mapping from address to Stake
    mapping(address => Stake) public stakes;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 rewards);

    // Function to stake tokens with APR and lock period
    function stake(uint256 _amount, uint256 _apr, uint256 _lockPeriod) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_apr > 0 && _apr <= 10000, "APR must be in basis points (0-10000)");
        require(_lockPeriod > 0, "Lock period must be greater than zero");

        // Store the stake
        stakes[msg.sender] = Stake({
            amount: _amount,
            startTime: block.timestamp,
            lockPeriod: _lockPeriod,
            apr: _apr
        });
    }

    // Function to calculate rewards based on the stake
    function calculateRewards(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];

        // Ensure the user has staked
        require(userStake.amount > 0, "No stake found for user");

        // Calculate the time elapsed since staking
        uint256 elapsedTime = block.timestamp - userStake.startTime;

        // Ensure the lock period has passed
        require(elapsedTime >= userStake.lockPeriod, "Stake is still locked");

        // Calculate the rewards (simple interest: principal * rate * time)
        uint256 annualRewards = (userStake.amount * userStake.apr * elapsedTime) / (365 days * 10000);
        return annualRewards;
    }

    // Function to distribute rewards to the user
    function distributeRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to distribute");

        // Reset the stake after rewards are distributed
        stakes[msg.sender].amount = 0;
        
        // Transfer rewards to the user (this assumes an ERC20 token transfer)
        // Replace the following line with your token transfer logic
        // require(token.transfer(msg.sender, rewards), "Transfer failed");

        emit RewardsDistributed(msg.sender, rewards);
    }
}
```
