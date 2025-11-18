"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gofurs-cash.pages.dev
Prompt: Write a Solidity contract that integrates staking functionality for GOFURS tokens, allowing users to earn rewards while maintaining compatibility with the ERC404 standard.
Generated: DETERMINISTIC_f7e457aa5c148a37
Batch ID: 20250612_153606
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

// Interface for the ERC404 standard
interface IERC404 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Staking contract for GOFURS tokens
contract StakingContract {
    IERC404 public gofursToken; // The GOFURS token contract
    address public owner; // The owner of the contract

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Timestamp when the stake was created
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the GOFURS token address
    constructor(address _gofursToken) {
        require(_gofursToken != address(0), "Invalid token address");
        gofursToken = IERC404(_gofursToken);
        owner = msg.sender; // Set the contract deployer as owner
    }

    // Function to stake GOFURS tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(gofursToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the user to the contract
        require(gofursToken.transfer(address(this), amount), "Token transfer failed");

        // Update the user's staking information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake GOFURS tokens
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate the amount to unstake
        uint256 amountToUnstake = userStake.amount;

        // Reset the user's stake info
        userStake.amount = 0;

        // Transfer the unstaked tokens back to the user
        require(gofursToken.transfer(msg.sender, amountToUnstake), "Token transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
    }

    // Function to claim rewards (dummy implementation)
    function claimRewards() external {
        uint256 rewardAmount = calculateRewards(msg.sender);
        require(rewardAmount > 0, "No rewards to claim");

        // Transfer rewards to the user (dummy transfer, implementation needed)
        require(gofursToken.transfer(msg.sender, rewardAmount), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    // Function to calculate rewards based on staking duration
    function calculateRewards(address user) internal view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }
        // Example reward calculation: 1% reward per day staked (simplified)
        uint256 daysStaked = (block.timestamp - userStake.timestamp) / 1 days;
        return (userStake.amount * daysStaked) / 100; // Adjust reward rate as necessary
    }

    // Function to withdraw tokens in case of emergencies by the owner
    function emergencyWithdraw(uint256 amount) external {
        require(msg.sender == owner, "Only owner can withdraw");
        require(gofursToken.transfer(msg.sender, amount), "Token transfer failed");
    }
}
```
