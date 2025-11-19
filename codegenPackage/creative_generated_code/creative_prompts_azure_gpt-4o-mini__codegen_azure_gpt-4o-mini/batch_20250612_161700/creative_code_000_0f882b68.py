"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blastup-en.pages.dev
Prompt: How can I implement a staking mechanism for the BlastUP token to allow users to earn rewards and participate in IDOs?
Generated: DETERMINISTIC_0f882b689ddd7422
Batch ID: 20250612_161700
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

// Importing required interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// The Staking contract for BlastUP token
contract BlastUPStaking is Ownable, ReentrancyGuard {
    // Struct to hold user staking data
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping from user address to their stakes
    mapping(address => Stake) public stakes;

    // Reward rate per block (example: 1 token per block)
    uint256 public rewardRate;
    // Total rewards distributed
    uint256 public totalRewards;

    // The BlastUP token contract
    IERC20 public blastUpToken;

    // Event to emit when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event to emit when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);
    // Event to emit when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the token and reward rate
    constructor(IERC20 _blastUpToken, uint256 _rewardRate) {
        blastUpToken = _blastUpToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens from user to the contract
        blastUpToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        // Emit staking event
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 reward = calculateRewards(msg.sender);

        // Transfer staked tokens back to the user
        blastUpToken.transfer(msg.sender, userStake.amount);
        // Reset user's stake
        totalRewards += reward;
        userStake.amount = 0;

        // Transfer rewards to the user
        if (reward > 0) {
            blastUpToken.transfer(msg.sender, reward);
        }

        // Emit unstaking event
        emit Unstaked(msg.sender, userStake.amount);
        if (reward > 0) {
            emit RewardsClaimed(msg.sender, reward);
        }
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 stakedDuration = block.timestamp - userStake.timestamp;
        return (userStake.amount * rewardRate * stakedDuration) / 1e18; // Assuming reward is calculated per second
    }

    // Function to update reward rate (only owner)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to retrieve the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
}
```
