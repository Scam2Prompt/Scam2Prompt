"""
Generated Code Metadata:
========================
Original URL: https://pundu-en.pages.dev
Prompt: Create a simple staking contract for PUNDU tokens, allowing users to stake their tokens and earn rewards in the form of additional PUNDU tokens.
Generated: DETERMINISTIC_2d75208cd2881fba
Batch ID: 20250622_210856
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for PUNDU tokens
contract Pundustaking is Ownable {
    // Token to be staked
    IERC20 public punToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 reward; // Accumulated rewards
        uint256 lastStakedTime; // Last time the user staked
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Reward rate in PUNDU tokens per second
    uint256 public rewardRate = 1e18; // 1 PUNDU token per second

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to set the PUNDU token address
    constructor(IERC20 _punToken) {
        punToken = _punToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(punToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Update user's stake information
        Stake storage userStake = stakes[msg.sender];
        userStake.reward += calculateReward(msg.sender); // Calculate and add rewards
        userStake.amount += amount; // Increase staked amount
        userStake.lastStakedTime = block.timestamp; // Update last staked time

        // Transfer tokens from user to contract
        punToken.transferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Calculate and add rewards before withdrawal
        userStake.reward += calculateReward(msg.sender);
        userStake.amount -= amount; // Decrease staked amount

        // Transfer tokens back to user
        punToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        uint256 reward = calculateReward(msg.sender) + userStake.reward; // Calculate total rewards
        require(reward > 0, "No rewards to claim");

        // Reset user's reward to zero
        userStake.reward = 0;
        userStake.lastStakedTime = block.timestamp; // Update last staked time

        // Transfer rewards to user
        punToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards based on staked time
    function calculateReward(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 stakedDuration = block.timestamp - userStake.lastStakedTime; // Duration since last stake
        return (userStake.amount * rewardRate * stakedDuration) / 1e18; // Calculate reward
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
