"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge-coin20.pages.dev
Prompt: Develop a staking incentive program in Solidity that offers higher rewards for early stakers, inspired by DOGE20's early staking incentive feature.
Generated: DETERMINISTIC_4b135f5426183c9b
Batch ID: 20250612_152827
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
 * @title StakingIncentiveProgram
 * @dev Implements a staking contract with early staking incentives.
 */
contract StakingIncentiveProgram {
    // State variables
    address public owner;
    uint256 public totalStaked;
    uint256 public startTime;
    uint256 public constant EARLY_BONUS_PERIOD = 30 days; // Incentive period for early stakers
    uint256 public constant BASE_REWARD_RATE = 5; // Base reward rate in percentage (5%)
    uint256 public constant EARLY_BONUS_RATE = 10; // Extra reward rate for early stakers (10%)

    struct Stake {
        uint256 amount;
        uint256 timestamp;
        bool claimed;
    }

    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event RewardClaimed(address indexed user, uint256 reward);
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Modifier to restrict function calls to only the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Modifier to ensure valid staking amounts.
     */
    modifier validStake(uint256 amount) {
        require(amount > 0, "Staking amount must be greater than zero");
        _;
    }

    constructor() {
        owner = msg.sender;
        startTime = block.timestamp;
    }

    /**
     * @dev Allows users to stake tokens and become eligible for rewards.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external validStake(amount) {
        // Ensure the staker does not already have active stakes
        require(stakes[msg.sender].amount == 0, "You already have an active stake");

        // Store staking details
        stakes[msg.sender] = Stake({
            amount: amount,
            timestamp: block.timestamp,
            claimed: false
        });

        totalStaked += amount;

        emit Staked(msg.sender, amount, block.timestamp);
    }

    /**
     * @dev Calculates the reward for a staker based on the stake amount and time.
     * @return The calculated reward amount.
     */
    function calculateReward(address staker) public view returns (uint256) {
        Stake memory userStake = stakes[staker];
        require(userStake.amount > 0, "No active stake found");

        uint256 rewardRate = BASE_REWARD_RATE;

        // Apply early staking bonus if within the bonus period
        if (userStake.timestamp <= startTime + EARLY_BONUS_PERIOD) {
            rewardRate += EARLY_BONUS_RATE;
        }

        uint256 reward = (userStake.amount * rewardRate) / 100;
        return reward;
    }

    /**
     * @dev Allows stakers to claim their rewards.
     */
    function claimReward() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake found");
        require(!userStake.claimed, "Reward already claimed");

        uint256 reward = calculateReward(msg.sender);
        userStake.claimed = true;

        // Send reward to the user (assuming rewards are paid in ETH for simplicity)
        (bool success, ) = msg.sender.call{value: reward}("");
        require(success, "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Allows users to unstake their tokens after claiming rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake found");
        require(userStake.claimed, "Claim your reward before unstaking");

        uint256 amount = userStake.amount;
        userStake.amount = 0;

        totalStaked -= amount;

        // Send staked amount back to the user (assuming staking was done in ETH for simplicity)
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Unstaking transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Allows the contract to receive ETH directly.
     */
    receive() external payable {}

    /**
     * @dev Allows the contract owner to withdraw unused funds.
     * @param amount Amount of funds to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");

        (bool success, ) = owner.call{value: amount}("");
        require(success, "Withdraw transfer failed");
    }
}
```
