"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoindapp.pages.dev
Prompt: Create a smart contract in Solidity for implementing a gamified staking mechanism with prediction-based rewards, inspired by Green Bitcoin’s staking model.
Generated: DETERMINISTIC_0a92b792355ca041
Batch ID: 20250612_152739
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract GamifiedStaking is Ownable {
    using SafeMath for uint256;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Timestamp of the stake
        bool isActive; // Status of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // ERC20 token used for staking
    IERC20 public stakingToken;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Event emitted when a user predicts and claims rewards
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the staking token and reward rate
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount.add(amount),
            timestamp: block.timestamp,
            isActive: true
        });

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.isActive, "No active stake found");

        // Calculate reward
        uint256 reward = calculateReward(msg.sender);
        
        // Reset user's stake information
        uint256 stakedAmount = userStake.amount;
        userStake.amount = 0;
        userStake.isActive = false;

        // Transfer staked tokens and rewards to user
        stakingToken.transfer(msg.sender, stakedAmount);
        stakingToken.transfer(msg.sender, reward);

        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    // Function to calculate rewards based on the time staked
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (!userStake.isActive) return 0;

        uint256 stakedDuration = block.timestamp.sub(userStake.timestamp);
        return stakedDuration.mul(rewardRate).mul(userStake.amount).div(1e18); // Adjust for precision
    }

    // Function to update the reward rate (only owner)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= stakingToken.balanceOf(address(this)), "Insufficient contract balance");
        stakingToken.transfer(msg.sender, amount);
    }
}
```
