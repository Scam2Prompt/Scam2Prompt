"""
Generated Code Metadata:
========================
Original URL: https://rabotaentnet.pages.dev
Prompt: Generate code to implement staking functionality for the $ZUSHI token, ensuring users can stake their tokens and receive rewards based on the distribution model outlined in the Zushi ecosystem.
Generated: DETERMINISTIC_dbf34574892d1921
Batch ID: 20250612_152249
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for token management and ownership control
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for the $ZUSHI token
contract ZushiStaking is Ownable {
    // Token to be staked
    IERC20 public zushiToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the user
        uint256 lastStakedTime; // Last time the user staked tokens
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the ZUSHI token address and reward rate
    constructor(IERC20 _zushiToken, uint256 _rewardRate) {
        zushiToken = _zushiToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(zushiToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Update user's stake information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.lastStakedTime = block.timestamp;

        // Update total staked amount
        totalStaked += amount;

        // Transfer tokens from user to the contract
        zushiToken.transferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user's stake information
        userStake.amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        zushiToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 timeStaked = block.timestamp - userStake.lastStakedTime;
        return (userStake.amount * rewardRate * timeStaked) / 1e18; // Adjusting for reward rate precision
    }

    // Function to claim rewards
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Update user's reward debt
        userStake.rewardDebt += rewards;
        userStake.lastStakedTime = block.timestamp;

        // Transfer rewards to the user
        zushiToken.transfer(msg.sender, rewards);

        emit RewardClaimed(msg.sender, rewards);
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
