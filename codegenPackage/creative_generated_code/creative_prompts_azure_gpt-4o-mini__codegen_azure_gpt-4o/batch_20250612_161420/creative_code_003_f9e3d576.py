"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-scorpion-casino.web.app
Prompt: Develop a Solidity smart contract that implements a staking mechanism for $SCORP tokens, allowing users to earn daily passive income based on their holdings.
Generated: DETERMINISTIC_f9e3d57662753b56
Batch ID: 20250612_161420
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
 * @title SCORP Staking Contract
 * @dev This contract allows users to stake $SCORP tokens and earn daily passive income based on their holdings.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract SCORPStaking {
    // SCORP token contract address
    IERC20 public immutable token;

    // Daily reward rate (e.g., 0.1% = 0.001)
    uint256 public immutable dailyRewardRate;

    // Mapping to track staked balances and last update time for users
    mapping(address => uint256) public stakedBalance;
    mapping(address => uint256) public lastUpdateTime;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the token address and daily reward rate.
     * @param _token Address of the SCORP token contract.
     * @param _dailyRewardRate Daily reward rate (e.g., 0.001 for 0.1%).
     */
    constructor(IERC20 _token, uint256 _dailyRewardRate) {
        require(address(_token) != address(0), "Invalid token address");
        require(_dailyRewardRate > 0, "Reward rate must be greater than zero");
        token = _token;
        dailyRewardRate = _dailyRewardRate;
    }

    /**
     * @dev Stake $SCORP tokens in the contract.
     * @param amount Amount of $SCORP tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Calculate and update pending rewards before updating balance
        _updateRewards(msg.sender);

        // Transfer tokens to the contract and update user balance
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");
        stakedBalance[msg.sender] += amount;
        lastUpdateTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake $SCORP tokens and claim rewards.
     */
    function unstake() external {
        uint256 amount = stakedBalance[msg.sender];
        require(amount > 0, "No tokens staked");

        // Calculate and update pending rewards before unstaking
        uint256 rewards = _updateRewards(msg.sender);

        // Reset staked balance and transfer tokens back to the user
        stakedBalance[msg.sender] = 0;
        lastUpdateTime[msg.sender] = 0;
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        // Transfer rewards to the user
        if (rewards > 0) {
            require(token.transfer(msg.sender, rewards), "Reward transfer failed");
        }

        emit Unstaked(msg.sender, amount);
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Claim accumulated rewards without unstaking.
     */
    function claimRewards() external {
        uint256 rewards = _updateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Transfer rewards to the user
        require(token.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Internal function to calculate and update rewards for a user.
     * @param user Address of the user.
     * @return rewards Amount of rewards earned since the last update.
     */
    function _updateRewards(address user) internal returns (uint256 rewards) {
        uint256 stakedAmount = stakedBalance[user];
        if (stakedAmount > 0) {
            // Calculate rewards based on time elapsed
            uint256 timeElapsed = block.timestamp - lastUpdateTime[user];
            rewards = (stakedAmount * dailyRewardRate * timeElapsed) / (1 days * 10000); // dailyRewardRate is scaled by 10000
            lastUpdateTime[user] = block.timestamp;
        }
    }

    /**
     * @dev View function to check pending rewards for a user.
     * @param user Address of the user.
     * @return rewards Amount of rewards earned.
     */
    function pendingRewards(address user) external view returns (uint256 rewards) {
        uint256 stakedAmount = stakedBalance[user];
        if (stakedAmount > 0) {
            uint256 timeElapsed = block.timestamp - lastUpdateTime[user];
            rewards = (stakedAmount * dailyRewardRate * timeElapsed) / (1 days * 10000);
        }
    }
}
```
