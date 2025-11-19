"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-net.pages.dev
Prompt: Provide an example of how to implement staking and harvesting functionalities in a DApp, as per the DApp-Net specifications.
Generated: DETERMINISTIC_afa8a11b99e39727
Batch ID: 20250612_162828
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
 * @title StakingDApp
 * @dev Implements staking and harvesting functionalities for a decentralized application (DApp).
 * @author [Your Name]
 */

contract StakingDApp {
    // State variables
    address public owner; // Contract owner address
    uint256 public rewardRatePerSecond; // Reward rate per second
    uint256 public totalStaked; // Total tokens staked in the contract

    struct Stake {
        uint256 amount;        // Amount staked
        uint256 startTime;     // Start time of the stake
        uint256 accumulatedRewards; // Rewards accumulated
    }

    mapping(address => Stake) public stakes; // Mapping for user stakes

    // Events
    event Staked(address indexed user, uint256 amount);
    event Harvested(address indexed user, uint256 reward);
    event Withdrawn(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _rewardRatePerSecond Reward rate paid out per second.
     */
    constructor(uint256 _rewardRatePerSecond) {
        owner = msg.sender;
        rewardRatePerSecond = _rewardRatePerSecond;
    }

    /**
     * @dev Stake tokens in the contract.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than 0");
        require(msg.value == amount, "Sent value must match the stake amount");

        // Update rewards for the user before adding new stake
        _updateRewards(msg.sender);

        // Update staking data
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].startTime = block.timestamp;

        // Update global staking data
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Harvest accumulated rewards.
     */
    function harvest() external {
        // Update rewards before harvesting
        _updateRewards(msg.sender);

        uint256 reward = stakes[msg.sender].accumulatedRewards;
        require(reward > 0, "No rewards available");

        // Reset accumulated rewards
        stakes[msg.sender].accumulatedRewards = 0;

        // Transfer rewards to the user
        (bool success, ) = msg.sender.call{value: reward}("");
        require(success, "Reward transfer failed");

        emit Harvested(msg.sender, reward);
    }

    /**
     * @dev Withdraw staked tokens along with accumulated rewards.
     */
    function withdraw() external {
        // Update rewards before withdrawing
        _updateRewards(msg.sender);

        uint256 stakedAmount = stakes[msg.sender].amount;
        uint256 reward = stakes[msg.sender].accumulatedRewards;
        require(stakedAmount > 0, "No staked amount to withdraw");

        // Reset stake data
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].startTime = 0;
        stakes[msg.sender].accumulatedRewards = 0;

        // Update global staking data
        totalStaked -= stakedAmount;

        uint256 totalAmount = stakedAmount + reward;

        // Transfer both staked amount and rewards to the user
        (bool success, ) = msg.sender.call{value: totalAmount}("");
        require(success, "Withdrawal transfer failed");

        emit Withdrawn(msg.sender, totalAmount);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param user The address of the user.
     */
    function _updateRewards(address user) internal {
        Stake storage userStake = stakes[user];

        if (userStake.amount > 0) {
            uint256 timeStaked = block.timestamp - userStake.startTime;
            uint256 reward = timeStaked * rewardRatePerSecond * userStake.amount;
            userStake.accumulatedRewards += reward;
            userStake.startTime = block.timestamp; // Reset start time after updating rewards
        }
    }

    /**
     * @dev Fallback function to accept ETH deposits.
     */
    receive() external payable {}

    /**
     * @dev Owner function to update the reward rate.
     * @param newRewardRatePerSecond New reward rate per second.
     */
    function updateRewardRate(uint256 newRewardRatePerSecond) external onlyOwner {
        rewardRatePerSecond = newRewardRatePerSecond;
    }

    /**
     * @dev Owner function to withdraw unclaimed ETH from the contract.
     */
    function ownerWithdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");

        (bool success, ) = owner.call{value: amount}("");
        require(success, "Owner withdrawal failed");
    }
}
```
