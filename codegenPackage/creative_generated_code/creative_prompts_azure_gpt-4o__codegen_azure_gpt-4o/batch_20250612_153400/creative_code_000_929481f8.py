"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-live.pages.dev
Prompt: Write a smart contract in Solidity for staking DOGE20 tokens that calculates rewards dynamically based on the percentage of the staking pool and annual returns, as described on the Dogecoin20 staking platform.
Generated: DETERMINISTIC_929481f8cb4d73a0
Batch ID: 20250612_153400
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
 * @title DOGE20 Staking Contract
 * @dev A smart contract for staking DOGE20 tokens, calculating dynamic rewards based on pool share and annual returns.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract DOGE20Staking {
    // Token used for staking
    IERC20 public immutable stakingToken;

    // Annual return rate expressed in basis points (e.g., 500 = 5% annual return)
    uint256 public immutable annualReturnRate;

    // Total amount staked in the contract
    uint256 public totalStaked;

    // Mapping to track user stakes and rewards
    struct Stake {
        uint256 amount;         // Amount staked
        uint256 rewardDebt;     // Rewards already paid out
        uint256 lastUpdated;    // Last time the user interacted with their stake
    }
    mapping(address => Stake) public stakes;

    // Event declarations for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor initializes the staking token and annual return rate.
     * @param _stakingToken Address of the DOGE20 token contract.
     * @param _annualReturnRate Annual return rate in basis points (e.g., 500 = 5%).
     */
    constructor(IERC20 _stakingToken, uint256 _annualReturnRate) {
        require(address(_stakingToken) != address(0), "Invalid token address");
        require(_annualReturnRate > 0, "Annual return rate must be positive");

        stakingToken = _stakingToken;
        annualReturnRate = _annualReturnRate;
    }

    /**
     * @dev Stake DOGE20 tokens in the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Update user rewards before changing the stake amount
        _updateRewards(msg.sender);

        // Transfer tokens from the sender to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update total staked and user stake
        totalStaked += _amount;
        stakes[msg.sender].amount += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake DOGE20 tokens and claim rewards.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked balance");

        // Update user rewards before changing the stake amount
        _updateRewards(msg.sender);

        // Update total staked and user stake
        totalStaked -= _amount;
        stakes[msg.sender].amount -= _amount;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim accumulated rewards without unstaking.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        uint256 reward = stakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards to claim");

        stakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Private function to update rewards for a user.
     * @param _user Address of the user to update rewards for.
     */
    function _updateRewards(address _user) private {
        Stake storage userStake = stakes[_user];

        if (userStake.amount > 0) {
            uint256 timeElapsed = block.timestamp - userStake.lastUpdated;

            // Calculate new rewards based on share of pool and annual return rate
            uint256 poolShare = (userStake.amount * 1e18) / totalStaked;
            uint256 annualReward = (userStake.amount * annualReturnRate) / 10000;
            uint256 reward = (annualReward * timeElapsed) / 365 days;

            userStake.rewardDebt += (reward * poolShare) / 1e18;
        }

        userStake.lastUpdated = block.timestamp;
    }

    /**
     * @dev Get the pending reward for a user.
     * @param _user Address of the user to query.
     */
    function pendingReward(address _user) external view returns (uint256) {
        Stake memory userStake = stakes[_user];

        if (userStake.amount == 0 || totalStaked == 0) {
            return 0;
        }

        uint256 timeElapsed = block.timestamp - userStake.lastUpdated;
        uint256 poolShare = (userStake.amount * 1e18) / totalStaked;
        uint256 annualReward = (userStake.amount * annualReturnRate) / 10000;
        uint256 reward = (annualReward * timeElapsed) / 365 days;

        return userStake.rewardDebt + ((reward * poolShare) / 1e18);
    }
}
```
