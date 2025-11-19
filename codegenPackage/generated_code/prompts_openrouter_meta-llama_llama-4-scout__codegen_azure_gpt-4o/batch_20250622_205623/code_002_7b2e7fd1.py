"""
Generated Code Metadata:
========================
Original URL: https://trustpad-app.pages.dev
Prompt: Develop a smart contract using Solidity to create a simple staking pool for a blockchain project launching on TrustPad, ensuring fair and transparent allocation of tokens.
Generated: DETERMINISTIC_7b2e7fd1479a12bb
Batch ID: 20250622_205623
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
 * @title StakingPool
 * @dev A simple staking pool smart contract for token allocation.
 * Users can stake tokens, earn rewards, and withdraw their stake.
 */
contract StakingPool {
    // State variables
    address public owner; // Owner of the contract
    uint256 public totalStaked; // Total amount of tokens staked in the pool
    uint256 public rewardRate; // Reward rate per second (e.g., tokens per second)
    uint256 public stakingStartTime; // Timestamp when staking starts
    uint256 public stakingEndTime; // Timestamp when staking ends

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards already paid out
        uint256 lastUpdated; // Last time the stake was updated
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    IERC20 public stakingToken; // ERC20 token used for staking

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier stakingActive() {
        require(block.timestamp >= stakingStartTime, "Staking has not started yet");
        require(block.timestamp <= stakingEndTime, "Staking has ended");
        _;
    }

    modifier stakingEnded() {
        require(block.timestamp > stakingEndTime, "Staking is still active");
        _;
    }

    /**
     * @dev Constructor to initialize the staking pool.
     * @param _stakingToken Address of the ERC20 token used for staking.
     * @param _rewardRate Reward rate per second.
     * @param _stakingStartTime Timestamp when staking starts.
     * @param _stakingEndTime Timestamp when staking ends.
     */
    constructor(
        address _stakingToken,
        uint256 _rewardRate,
        uint256 _stakingStartTime,
        uint256 _stakingEndTime
    ) {
        require(_stakingToken != address(0), "Invalid token address");
        require(_stakingStartTime < _stakingEndTime, "Invalid staking period");

        owner = msg.sender;
        stakingToken = IERC20(_stakingToken);
        rewardRate = _rewardRate;
        stakingStartTime = _stakingStartTime;
        stakingEndTime = _stakingEndTime;
    }

    /**
     * @dev Allows users to stake tokens in the pool.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external stakingActive {
        require(_amount > 0, "Cannot stake zero tokens");

        // Update user's stake and rewards
        Stake storage userStake = stakes[msg.sender];
        _updateRewards(msg.sender);

        // Transfer tokens from user to contract
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        userStake.amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens and rewards.
     */
    function withdraw() external stakingEnded {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens to withdraw");

        // Calculate pending rewards
        _updateRewards(msg.sender);
        uint256 reward = userStake.rewardDebt;

        // Transfer staked tokens and rewards to user
        uint256 amountToWithdraw = userStake.amount;
        userStake.amount = 0;
        userStake.rewardDebt = 0;

        require(stakingToken.transfer(msg.sender, amountToWithdraw), "Token transfer failed");
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");

        totalStaked -= amountToWithdraw;

        emit Withdrawn(msg.sender, amountToWithdraw);
        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        Stake storage userStake = stakes[_user];
        uint256 timeElapsed = block.timestamp - userStake.lastUpdated;
        uint256 pendingReward = (userStake.amount * rewardRate * timeElapsed) / 1e18;

        userStake.rewardDebt += pendingReward;
        userStake.lastUpdated = block.timestamp;
    }

    /**
     * @dev Allows the owner to withdraw remaining tokens after staking ends.
     */
    function withdrawRemainingTokens() external onlyOwner stakingEnded {
        uint256 remainingTokens = stakingToken.balanceOf(address(this));
        require(stakingToken.transfer(owner, remainingTokens), "Token transfer failed");
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
