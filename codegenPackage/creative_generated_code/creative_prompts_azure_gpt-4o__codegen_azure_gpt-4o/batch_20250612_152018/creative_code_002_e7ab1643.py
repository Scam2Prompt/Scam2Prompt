"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agix-reward.com
Prompt: Generate a smart contract in Solidity to enable AGIX token staking and reward distribution based on on-chain activity, as described in the SingularityNET rewards event.
Generated: DETERMINISTIC_e7ab16435fad68a1
Batch ID: 20250612_152018
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
 * @title AGIX Staking and Reward Distribution Smart Contract
 * @author Your Name
 * @notice This contract enables AGIX token staking and reward distribution based on on-chain activity.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract AGIXStaking {
    // AGIX token contract address
    IERC20 public immutable agixToken;

    // Reward pool for distribution
    uint256 public rewardPool;

    // Staking data
    struct Stake {
        uint256 amount;
        uint256 lastStakeTime;
        uint256 totalRewardsClaimed;
    }

    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed staker, uint256 amount);
    event RewardDistributed(address indexed staker, uint256 rewardAmount);
    event Unstaked(address indexed staker, uint256 amount);

    // Modifier to ensure valid staking amounts
    modifier validAmount(uint256 amount) {
        require(amount > 0, "Staking amount must be greater than zero.");
        _;
    }

    /**
     * @dev Constructor to initialize AGIX token contract address.
     * @param _agixToken Address of the AGIX token contract.
     */
    constructor(address _agixToken) {
        require(_agixToken != address(0), "Invalid token address.");
        agixToken = IERC20(_agixToken);
    }

    /**
     * @notice Stake AGIX tokens into the contract.
     * @param amount The amount of AGIX tokens to stake.
     */
    function stake(uint256 amount) external validAmount(amount) {
        // Transfer AGIX tokens from the staker to the contract
        bool success = agixToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed.");

        // Update staker's stake information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.lastStakeTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Distribute rewards based on on-chain activity.
     * @param staker Address of the staker to distribute rewards to.
     * @param rewardAmount The amount of AGIX tokens to distribute as reward.
     */
    function distributeReward(address staker, uint256 rewardAmount) external {
        require(stakes[staker].amount > 0, "Staker has no active stake.");
        require(rewardAmount > 0 && rewardAmount <= rewardPool, "Invalid reward amount.");

        // Reduce reward pool
        rewardPool -= rewardAmount;

        // Update staker's rewards claimed
        stakes[staker].totalRewardsClaimed += rewardAmount;

        // Transfer reward tokens to the staker
        bool success = agixToken.transfer(staker, rewardAmount);
        require(success, "Reward distribution failed.");

        emit RewardDistributed(staker, rewardAmount);
    }

    /**
     * @notice Unstake AGIX tokens.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens to unstake.");

        // Retrieve the staked amount
        uint256 unstakeAmount = userStake.amount;
        userStake.amount = 0;

        // Transfer staked tokens back to the staker
        bool success = agixToken.transfer(msg.sender, unstakeAmount);
        require(success, "Unstaking failed.");

        emit Unstaked(msg.sender, unstakeAmount);
    }

    /**
     * @notice Fund the reward pool with AGIX tokens.
     * @param amount The amount of tokens to add to the reward pool.
     */
    function fundRewardPool(uint256 amount) external validAmount(amount) {
        // Transfer AGIX tokens from the sender to the contract
        bool success = agixToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Reward pool funding failed.");

        rewardPool += amount;
    }

    /**
     * @notice Retrieve staker details.
     * @param staker Address of the staker.
     * @return amount Amount staked by the staker.
     * @return lastStakeTime Timestamp of the last stake update.
     * @return totalRewardsClaimed Total rewards claimed by the staker.
     */
    function getStakeDetails(address staker) external view returns (uint256 amount, uint256 lastStakeTime, uint256 totalRewardsClaimed) {
        Stake storage userStake = stakes[staker];
        return (userStake.amount, userStake.lastStakeTime, userStake.totalRewardsClaimed);
    }
}
```
