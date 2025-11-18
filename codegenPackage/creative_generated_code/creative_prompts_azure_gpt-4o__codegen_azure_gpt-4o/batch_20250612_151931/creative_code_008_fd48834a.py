"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wenwen.pages.dev
Prompt: Write a Solidity contract to enable staking of WEN tokens with rewards distributed based on tokenomics principles.
Generated: DETERMINISTIC_fd48834a196172b4
Batch ID: 20250612_151931
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
 * @title WENTokenStaking
 * @dev A staking contract for WEN tokens with reward distribution based on tokenomics principles.
 */
contract WENTokenStaking {
    // Address of the WEN token contract
    IERC20 public wenToken;

    // Struct to store staking information
    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 stakeTimestamp; // Timestamp of when the staking started
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Reward rate per second (e.g., 1 WEN per second per token staked)
    uint256 public rewardRate;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardRateUpdated(uint256 newRewardRate);

    /**
     * @dev Constructor initializes the contract with the WEN token address and reward rate.
     * @param _wenToken Address of the WEN token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(address _wenToken, uint256 _rewardRate) {
        require(_wenToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        wenToken = IERC20(_wenToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to ensure the user has staked tokens.
     */
    modifier hasStake() {
        require(stakes[msg.sender].amount > 0, "No tokens staked");
        _;
    }

    /**
     * @dev Stake WEN tokens in the contract.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(wenToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.stakeTimestamp = block.timestamp;

        // Update total staked
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake WEN tokens and claim rewards.
     */
    function unstake() external hasStake {
        Stake storage userStake = stakes[msg.sender];

        // Calculate rewards based on staking duration and reward rate
        uint256 stakingDuration = block.timestamp - userStake.stakeTimestamp;
        uint256 reward = (stakingDuration * userStake.amount * rewardRate) / 1e18;

        // Update state before transferring tokens
        uint256 amountStaked = userStake.amount;
        userStake.amount = 0;
        userStake.stakeTimestamp = 0;

        // Update total staked
        totalStaked -= amountStaked;

        // Transfer staked tokens and rewards to the user
        require(wenToken.transfer(msg.sender, amountStaked + reward), "Token transfer failed");

        emit Unstaked(msg.sender, amountStaked, reward);
    }

    /**
     * @dev Update the reward rate (onlyOwner functionality could be added if needed).
     * @param _newRewardRate The new reward rate per second.
     */
    function updateRewardRate(uint256 _newRewardRate) external {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");

        rewardRate = _newRewardRate;

        emit RewardRateUpdated(_newRewardRate);
    }
}

// Minimal IERC20 interface for interacting with WEN token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
