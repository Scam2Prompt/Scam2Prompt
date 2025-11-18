"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polygon6d.com
Prompt: Write a Solidity contract that implements staking rewards based on real-time calculations of pledged funds and staking periods, as described in Polygon6D.
Generated: DETERMINISTIC_d011312ab33f91a5
Batch ID: 20250612_150644
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
 * @title StakingRewards
 * @dev A smart contract for staking and calculating rewards based on staked funds and staking period.
 */
contract StakingRewards {
    // State variables
    address public owner;
    uint256 public rewardRatePerSecond; // Reward rate in tokens per second
    uint256 public totalStaked; // Total staked amount

    // Struct to track stake details
    struct Stake {
        uint256 amount; // Staked amount
        uint256 startTime; // Timestamp when staking started
        uint256 reward; // Accumulated reward
    }

    // Mapping from user address to their stake
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardRateUpdated(uint256 newRewardRate);

    // Constructor
    constructor(uint256 _rewardRatePerSecond) {
        require(_rewardRatePerSecond > 0, "Reward rate must be greater than 0");
        owner = msg.sender;
        rewardRatePerSecond = _rewardRatePerSecond;
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Stake tokens in the contract.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external payable {
        require(amount > 0, "Staking amount must be greater than 0");
        require(msg.value == amount, "Amount mismatch with ether sent");
        
        Stake storage userStake = stakes[msg.sender];

        // Update rewards for the current stake
        if (userStake.amount > 0) {
            userStake.reward += calculateReward(msg.sender);
        }

        userStake.amount += amount;
        userStake.startTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked amount to unstake");

        // Calculate final rewards
        uint256 reward = calculateReward(msg.sender);
        uint256 unstakeAmount = userStake.amount;

        // Reset user stake
        userStake.amount = 0;
        userStake.startTime = 0;
        userStake.reward = 0;

        totalStaked -= unstakeAmount;

        // Transfer staked amount and reward to the user
        payable(msg.sender).transfer(unstakeAmount + reward);

        emit Unstaked(msg.sender, unstakeAmount, reward);
    }

    /**
     * @dev Calculate the reward for a user based on their staked amount and staking period.
     * @param user The address of the user.
     * @return reward The calculated reward.
     */
    function calculateReward(address user) public view returns (uint256 reward) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0 || userStake.startTime == 0) {
            return 0;
        }
        uint256 stakingDuration = block.timestamp - userStake.startTime;
        reward = (userStake.amount * stakingDuration * rewardRatePerSecond) / (1 ether);
        reward += userStake.reward; // Include previously accumulated rewards
        return reward;
    }

    /**
     * @dev Update the reward rate per second.
     * @param newRewardRate The new reward rate per second.
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        require(newRewardRate > 0, "Reward rate must be greater than 0");
        rewardRatePerSecond = newRewardRate;
        emit RewardRateUpdated(newRewardRate);
    }

    /**
     * @dev Fallback function to receive ether.
     */
    receive() external payable {}

    /**
     * @dev Withdraw contract balance to owner address.
     */
    function withdrawContractBalance() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        payable(owner).transfer(contractBalance);
    }
}
```
