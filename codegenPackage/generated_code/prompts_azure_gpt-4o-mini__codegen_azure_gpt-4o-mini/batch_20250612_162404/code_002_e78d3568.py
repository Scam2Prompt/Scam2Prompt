"""
Generated Code Metadata:
========================
Original URL: https://tokencatgirl.pages.dev
Prompt: Generate a code snippet for a decentralized application (DApp) that allows users to stake CATGIRL¢ tokens and earn rewards, based on the features outlined in the Catgirl ecosystem.
Generated: DETERMINISTIC_e78d356830c29c88
Batch ID: 20250612_162404
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

// Importing the ERC20 interface for CATGIRL¢ token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for CATGIRL¢ tokens
contract CatgirlStaking is Ownable {
    // Token to be staked
    IERC20 public catgirlToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate (in tokens per second)
    uint256 public rewardRate = 1e18; // Example: 1 CATGIRL¢ per second

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to set the CATGIRL¢ token address
    constructor(address _catgirlToken) {
        catgirlToken = IERC20(_catgirlToken);
    }

    // Function to stake CATGIRL¢ tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(catgirlToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

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

        // Transfer tokens back to the user
        require(catgirlToken.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        // Calculate the time staked
        uint256 stakingDuration = block.timestamp - userStake.timestamp;

        // Calculate rewards based on the staking duration and reward rate
        return (stakingDuration * userStake.amount * rewardRate) / 1e18;
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available");

        // Update user's stake timestamp
        stakes[msg.sender].timestamp = block.timestamp;

        // Transfer rewards to the user
        require(catgirlToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
