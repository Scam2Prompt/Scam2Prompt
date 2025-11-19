"""
Generated Code Metadata:
========================
Original URL: https://yetiouro.co
Prompt: Illustrate how to implement a staking mechanism for $YETIO tokens in a Solidity smart contract based on Yeti Ouro's tokenomics.
Generated: DETERMINISTIC_0d27b8a41f6d5c5b
Batch ID: 20250612_161059
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $YETIO tokens
contract YETIOStaking is Ownable {
    // Token to be staked
    IERC20 public yetioToken;

    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to set the token address
    constructor(IERC20 _yetioToken) {
        yetioToken = _yetioToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(yetioToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        yetioToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update the user's stake
        userStake.amount -= amount;

        // Transfer tokens back to the user
        yetioToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards (example: 10% of staked amount per year)
    function calculateRewards(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 rewardRate = 10; // 10% annual reward
        uint256 reward = (userStake.amount * rewardRate * stakingDuration) / (365 days * 100);

        return reward;
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available");

        // Transfer rewards to the user
        yetioToken.transfer(msg.sender, reward);

        // Reset the staking timestamp
        stakes[msg.sender].timestamp = block.timestamp;

        emit RewardClaimed(msg.sender, reward);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
}
```
