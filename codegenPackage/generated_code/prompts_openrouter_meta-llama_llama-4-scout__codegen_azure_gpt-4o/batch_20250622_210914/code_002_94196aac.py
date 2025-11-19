"""
Generated Code Metadata:
========================
Original URL: https://doge20-claim.pages.dev
Prompt: "Generate a smart contract in Solidity for a staking platform similar to Dogecoin20's, with dynamic rewards rates and monthly, daily return calculations."
Generated: DETERMINISTIC_94196aac735bd0dc
Batch ID: 20250622_210914
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

/**
 * @title StakingPlatform
 * @dev A smart contract for staking tokens with dynamic reward rates and return calculations.
 */
contract StakingPlatform {
    // Struct to represent a staker's information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when staking started
    }

    // Mapping to store stakes for each address
    mapping(address => Stake) public stakes;

    // Reward rate per day (in percentage, e.g., 1 = 1%)
    uint256 public dailyRewardRate;

    // Reward rate per month (in percentage, e.g., 30 = 30%)
    uint256 public monthlyRewardRate;

    // Token balance of the contract (used for rewards distribution)
    uint256 public contractBalance;

    // Owner of the contract
    address public owner;

    // Events
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount, uint256 reward);
    event RewardRateUpdated(uint256 dailyRate, uint256 monthlyRate);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _dailyRewardRate, uint256 _monthlyRewardRate) {
        require(_dailyRewardRate > 0 && _monthlyRewardRate > 0, "Reward rates must be greater than zero");
        dailyRewardRate = _dailyRewardRate;
        monthlyRewardRate = _monthlyRewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Function to stake tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external payable {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(msg.value == _amount, "Sent value must match the stake amount");

        // Update contract balance
        contractBalance += _amount;

        // Update staker's information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].startTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to unstake tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 dailyRewards = (userStake.amount * dailyRewardRate * stakingDuration) / (100 * 1 days);
        uint256 monthlyRewards = (userStake.amount * monthlyRewardRate * stakingDuration) / (100 * 30 days);
        uint256 totalRewards = dailyRewards + monthlyRewards;

        // Ensure contract has enough balance for rewards
        require(contractBalance >= userStake.amount + totalRewards, "Insufficient contract balance");

        // Update contract balance
        contractBalance -= (userStake.amount + totalRewards);

        // Transfer staked amount and rewards to the user
        payable(msg.sender).transfer(userStake.amount + totalRewards);

        // Reset staker's information
        userStake.amount = 0;
        userStake.startTime = 0;

        emit Unstaked(msg.sender, userStake.amount, totalRewards);
    }

    /**
     * @dev Function to update reward rates.
     * @param _dailyRate New daily reward rate.
     * @param _monthlyRate New monthly reward rate.
     */
    function updateRewardRates(uint256 _dailyRate, uint256 _monthlyRate) external onlyOwner {
        require(_dailyRate > 0 && _monthlyRate > 0, "Reward rates must be greater than zero");
        dailyRewardRate = _dailyRate;
        monthlyRewardRate = _monthlyRate;

        emit RewardRateUpdated(_dailyRate, _monthlyRate);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {
        contractBalance += msg.value;
    }

    /**
     * @dev Function to withdraw contract balance (only owner).
     * @param _amount Amount to withdraw.
     */
    function withdraw(uint256 _amount) external onlyOwner {
        require(_amount <= contractBalance, "Insufficient contract balance");
        contractBalance -= _amount;
        payable(owner).transfer(_amount);
    }
}
```
