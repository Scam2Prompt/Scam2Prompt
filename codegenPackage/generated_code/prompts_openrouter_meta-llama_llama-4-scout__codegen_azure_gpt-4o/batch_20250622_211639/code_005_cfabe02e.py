"""
Generated Code Metadata:
========================
Original URL: https://memes-index.pages.dev
Prompt: Design a smart contract using Solidity to facilitate the $MEMEX presale, including functions for buying, staking, and claiming rewards, while ensuring security and transparency.
Generated: DETERMINISTIC_cfabe02ebe9782f6
Batch ID: 20250622_211639
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
 * @title MEMEXPresale
 * @dev A smart contract to facilitate the $MEMEX token presale, staking, and claiming rewards.
 */
contract MEMEXPresale {
    // State variables
    address public owner; // Contract owner
    uint256 public presalePrice; // Price per token during presale
    uint256 public totalStaked; // Total tokens staked
    uint256 public rewardRate; // Reward rate for staking
    uint256 public presaleEndTime; // Timestamp for presale end

    mapping(address => uint256) public balances; // User token balances
    mapping(address => uint256) public stakedBalances; // User staked balances
    mapping(address => uint256) public stakingStartTime; // Timestamp when user started staking

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensStaked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed staker, uint256 reward);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier presaleActive() {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        _;
    }

    modifier stakingActive(address staker) {
        require(stakedBalances[staker] > 0, "No tokens staked");
        _;
    }

    // Constructor
    constructor(uint256 _presalePrice, uint256 _rewardRate, uint256 _presaleDuration) {
        owner = msg.sender;
        presalePrice = _presalePrice;
        rewardRate = _rewardRate;
        presaleEndTime = block.timestamp + _presaleDuration;
    }

    /**
     * @dev Function to buy tokens during the presale.
     * @param amount The number of tokens to purchase.
     */
    function buyTokens(uint256 amount) external payable presaleActive {
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value == amount * presalePrice, "Incorrect ETH value sent");

        balances[msg.sender] += amount;

        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Function to stake tokens.
     * @param amount The number of tokens to stake.
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient token balance");

        balances[msg.sender] -= amount;
        stakedBalances[msg.sender] += amount;
        stakingStartTime[msg.sender] = block.timestamp;
        totalStaked += amount;

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Function to calculate staking rewards for a user.
     * @param staker The address of the staker.
     * @return The calculated reward.
     */
    function calculateReward(address staker) public view stakingActive(staker) returns (uint256) {
        uint256 stakingDuration = block.timestamp - stakingStartTime[staker];
        uint256 reward = (stakedBalances[staker] * rewardRate * stakingDuration) / (365 days);
        return reward;
    }

    /**
     * @dev Function to claim staking rewards.
     */
    function claimRewards() external stakingActive(msg.sender) {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        stakingStartTime[msg.sender] = block.timestamp; // Reset staking start time
        balances[msg.sender] += reward;

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Function to withdraw staked tokens.
     */
    function withdrawStakedTokens() external stakingActive(msg.sender) {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No staked tokens to withdraw");

        stakedBalances[msg.sender] = 0;
        stakingStartTime[msg.sender] = 0;
        totalStaked -= stakedAmount;
        balances[msg.sender] += stakedAmount;
    }

    /**
     * @dev Function to update presale price. Only owner can call this.
     * @param newPrice The new presale price.
     */
    function updatePresalePrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Price must be greater than zero");
        presalePrice = newPrice;
    }

    /**
     * @dev Function to update reward rate. Only owner can call this.
     * @param newRate The new reward rate.
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be greater than zero");
        rewardRate = newRate;
    }

    /**
     * @dev Function to withdraw contract balance. Only owner can call this.
     */
    function withdrawContractBalance() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No balance to withdraw");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed");
    }
}
```
