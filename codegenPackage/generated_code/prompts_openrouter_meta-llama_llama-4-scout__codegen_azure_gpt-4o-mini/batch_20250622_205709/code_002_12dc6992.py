"""
Generated Code Metadata:
========================
Original URL: https://scotty-theai-io.web.app
Prompt: Generate a smart contract in Solidity that allows users to stake $SCOTTY tokens and earn rewards based on the project's staking mechanism.
Generated: DETERMINISTIC_12dc69928cf2584b
Batch ID: 20250622_205709
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

// Importing the ERC20 interface for the $SCOTTY token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $SCOTTY token
contract ScottyStaking is Ownable {
    // Token to be staked
    IERC20 public scottyToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the last stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate (in tokens per second)
    uint256 public rewardRate = 1e18; // 1 SCOTTY token per second

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to set the $SCOTTY token address
    constructor(address _scottyToken) {
        scottyToken = IERC20(_scottyToken);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(scottyToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from user to contract
        scottyToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;

        // Update total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user's stake information
        userStake.amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        scottyToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }
        return (block.timestamp - userStake.timestamp) * userStake.amount * rewardRate / 1e18;
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available");

        // Update user's stake timestamp
        stakes[msg.sender].timestamp = block.timestamp;

        // Transfer rewards to user
        scottyToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Function to set the reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(scottyToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        scottyToken.transfer(msg.sender, amount);
    }
}
```
