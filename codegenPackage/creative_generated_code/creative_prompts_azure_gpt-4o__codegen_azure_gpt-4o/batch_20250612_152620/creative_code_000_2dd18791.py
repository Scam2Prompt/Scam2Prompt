"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diamond-7n0.pages.dev
Prompt: Write a smart contract in Solidity for a staking platform similar to "Diamond Mining," where users can lock their tokens and earn additional tokens as rewards. Include mechanisms for security and transparency as described in the Diamond Coin documentation.
Generated: DETERMINISTIC_2dd1879156674c7c
Batch ID: 20250612_152620
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
 * @title StakingPlatform
 * @dev A staking platform contract for locking ERC20 tokens and earning rewards.
 * Users stake tokens to earn additional tokens as rewards. Includes security
 * and transparency measures as described in Diamond Coin documentation.
 */
contract StakingPlatform {
    // Struct to track staking details
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 stakeTimestamp;
    }

    // ERC20 token interface
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    // Reward rate per second
    uint256 public rewardRatePerSecond;

    // Mapping of addresses to their stake data
    mapping(address => Stake) public stakes;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Events for transparency
    event Staked(address indexed staker, uint256 amount);
    event Withdrawn(address indexed staker, uint256 amount);
    event RewardClaimed(address indexed staker, uint256 reward);

    /**
     * @dev Modifier to ensure non-zero amount is provided
     */
    modifier nonZeroAmount(uint256 amount) {
        require(amount > 0, "StakingPlatform: Amount must be greater than zero");
        _;
    }

    /**
     * @dev Modifier to ensure staker has staked tokens
     */
    modifier hasStake() {
        require(stakes[msg.sender].amount > 0, "StakingPlatform: No tokens staked");
        _;
    }

    /**
     * @dev Constructor sets the staking and reward tokens, and reward rate
     * @param _stakingToken Address of the ERC20 token users will stake
     * @param _rewardToken Address of the ERC20 token used for rewards
     * @param _rewardRatePerSecond Reward rate per second
     */
    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _rewardRatePerSecond
    ) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRatePerSecond = _rewardRatePerSecond;
    }

    /**
     * @dev Stake tokens into the contract
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonZeroAmount(amount) {
        // Update rewards before modifying stake
        _updateReward(msg.sender);

        // Transfer tokens and update stake details
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "StakingPlatform: Transfer failed");
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].stakeTimestamp = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract
     */
    function withdraw() external hasStake {
        // Update rewards before withdrawing
        _updateReward(msg.sender);

        uint256 amount = stakes[msg.sender].amount;

        // Transfer tokens back to the user
        stakes[msg.sender].amount = 0;
        totalStaked -= amount;

        require(stakingToken.transfer(msg.sender, amount), "StakingPlatform: Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external hasStake {
        // Update rewards and transfer accumulated rewards
        _updateReward(msg.sender);

        uint256 reward = stakes[msg.sender].rewardDebt;
        stakes[msg.sender].rewardDebt = 0;

        require(rewardToken.transfer(msg.sender, reward), "StakingPlatform: Transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Private function to update reward for a staker
     * @param staker Address of the staker
     */
    function _updateReward(address staker) private {
        Stake storage stakeData = stakes[staker];
        uint256 stakingDuration = block.timestamp - stakeData.stakeTimestamp;
        uint256 pendingReward = (stakeData.amount * stakingDuration * rewardRatePerSecond) / 1 ether;

        stakeData.rewardDebt += pendingReward;
        stakeData.stakeTimestamp = block.timestamp;
    }

    /**
     * @dev Get pending rewards for a staker (view function)
     * @param staker Address of the staker
     * @return pendingReward The pending reward amount
     */
    function pendingRewards(address staker) external view returns (uint256) {
        Stake memory stakeData = stakes[staker];
        uint256 stakingDuration = block.timestamp - stakeData.stakeTimestamp;
        uint256 pendingReward = (stakeData.amount * stakingDuration * rewardRatePerSecond) / 1 ether;

        return stakeData.rewardDebt + pendingReward;
    }
}

// Minimal ERC20 interface for interacting with tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
