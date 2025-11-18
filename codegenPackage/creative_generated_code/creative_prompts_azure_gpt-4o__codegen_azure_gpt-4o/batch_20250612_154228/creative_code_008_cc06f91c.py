"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bits-portfolio.web.app
Prompt: Generate a smart contract example for staking assets on Binance, utilizing BITS-powered DeFi tracking.
Generated: DETERMINISTIC_cc06f91cb7c193cf
Batch ID: 20250612_154228
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

/**
 * @title StakingContract
 * @dev A smart contract for staking assets on Binance utilizing BITS-powered DeFi tracking.
 */
contract StakingContract {
    // Variables to track staking
    mapping(address => uint256) public stakes; // Track the amount staked by each user
    mapping(address => uint256) public stakeTimestamps; // Track the time when each user staked

    uint256 public totalStaked; // Total staked amount in the contract
    uint256 public rewardRatePerSecond; // Reward rate per second, configurable by the owner
    address public owner; // Contract owner

    // Events for logging contract activity
    event Stake(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewards);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to initialize contract variables
    constructor(uint256 _rewardRatePerSecond) {
        owner = msg.sender;
        rewardRatePerSecond = _rewardRatePerSecond;
    }

    /**
     * @dev Function for users to stake their assets.
     * @param amount The amount of assets to stake.
     */
    function stake(uint256 amount) external payable {
        require(amount == msg.value, "Amount must match sent value");
        require(amount > 0, "Cannot stake 0");

        // Update staking records
        stakes[msg.sender] += amount;
        stakeTimestamps[msg.sender] = block.timestamp;
        totalStaked += amount;

        emit Stake(msg.sender, amount);
    }

    /**
     * @dev Function to calculate the rewards for a staker.
     * @param user The address of the staker.
     * @return rewards The calculated rewards for the user.
     */
    function calculateRewards(address user) public view returns (uint256) {
        if (stakes[user] == 0) {
            return 0; // If no stake exists, no rewards
        }

        uint256 stakingDuration = block.timestamp - stakeTimestamps[user];
        uint256 rewards = stakingDuration * rewardRatePerSecond * stakes[user] / 1 ether;

        return rewards;
    }

    /**
     * @dev Function for users to claim their rewards.
     */
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Reset staking timestamp to avoid double rewards
        stakeTimestamps[msg.sender] = block.timestamp;

        // Send rewards to user
        (bool success, ) = msg.sender.call{value: rewards}("");
        require(success, "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Function for users to withdraw their staked assets.
     */
    function withdrawStake() external {
        uint256 amountStaked = stakes[msg.sender];
        require(amountStaked > 0, "No stake available to withdraw");

        uint256 rewards = calculateRewards(msg.sender);

        // Update staking records
        stakes[msg.sender] = 0;
        stakeTimestamps[msg.sender] = 0;
        totalStaked -= amountStaked;

        // Send staked amount and rewards back to user
        uint256 totalAmount = amountStaked + rewards;
        (bool success, ) = msg.sender.call{value: totalAmount}("");
        require(success, "Withdrawal transfer failed");

        emit Withdraw(msg.sender, amountStaked);
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Function for the owner to update the reward rate.
     * @param _rewardRatePerSecond The new reward rate per second.
     */
    function updateRewardRate(uint256 _rewardRatePerSecond) external onlyOwner {
        rewardRatePerSecond = _rewardRatePerSecond;
    }

    /**
     * @dev Function to receive ETH directly sent to the contract.
     */
    receive() external payable {}

    /**
     * @dev Function to withdraw contract balance (only for the owner).
     */
    function withdrawContractBalance() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Balance withdrawal failed");
    }
}
```
