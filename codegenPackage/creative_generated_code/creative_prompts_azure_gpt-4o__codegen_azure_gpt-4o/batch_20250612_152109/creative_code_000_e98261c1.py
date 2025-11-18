"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-e.pages.dev
Prompt: Write an Ethereum smart contract for staking DOGE20 tokens that distributes rewards proportionally to stakers over a two-year period, as described on the Dogecoin20 website.
Generated: DETERMINISTIC_e98261c1fc748f42
Batch ID: 20250612_152109
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
 * @title Doge20 Staking Contract
 * @dev This contract allows users to stake DOGE20 tokens and receive proportional rewards
 * distributed over a two-year period.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract Doge20Staking {
    // State variables
    IERC20 public immutable doge20Token; // DOGE20 token interface
    uint256 public constant REWARD_PERIOD = 2 * 365 days; // Two-year reward distribution
    uint256 public immutable startTime; // Contract start time
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public totalRewardPool; // Total reward pool allocated to stakers

    mapping(address => uint256) public stakes; // User stakes
    mapping(address => uint256) public rewardsClaimed; // Rewards already claimed

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor initializes the contract with the DOGE20 token and starts the staking period.
     * @param _doge20Token Address of the DOGE20 token contract.
     * @param _rewardPool Total reward pool allocated for distribution.
     */
    constructor(IERC20 _doge20Token, uint256 _rewardPool) {
        require(address(_doge20Token) != address(0), "Invalid token address");
        require(_rewardPool > 0, "Reward pool must be greater than zero");

        doge20Token = _doge20Token;
        totalRewardPool = _rewardPool;
        startTime = block.timestamp;
    }

    /**
     * @dev Allows a user to stake DOGE20 tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(block.timestamp < startTime + REWARD_PERIOD, "Staking period has ended");

        // Transfer DOGE20 tokens from the user to the contract
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        stakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to unstake DOGE20 tokens.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Insufficient staked balance");

        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer DOGE20 tokens back to the user
        require(doge20Token.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to claim their proportional rewards.
     */
    function claimReward() external {
        uint256 earnedReward = calculateReward(msg.sender);
        require(earnedReward > 0, "No reward available to claim");

        rewardsClaimed[msg.sender] += earnedReward;

        // Transfer reward tokens to the user
        require(doge20Token.transfer(msg.sender, earnedReward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, earnedReward);
    }

    /**
     * @dev Calculates the proportional rewards for a user based on their staked amount.
     * @param user Address of the user.
     * @return The amount of reward tokens the user is eligible to claim.
     */
    function calculateReward(address user) public view returns (uint256) {
        if (stakes[user] == 0 || block.timestamp > startTime + REWARD_PERIOD) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - startTime;
        uint256 totalDuration = REWARD_PERIOD;

        // Proportional reward calculation
        uint256 proportionalReward = (stakes[user] * totalRewardPool * stakingDuration) / (totalStaked * totalDuration);

        // Subtract already claimed rewards
        return proportionalReward - rewardsClaimed[user];
    }

    /**
     * @dev Returns the current staking balance of a user.
     * @param user Address of the user.
     * @return The amount of DOGE20 tokens staked by the user.
     */
    function stakingBalance(address user) external view returns (uint256) {
        return stakes[user];
    }
}
```
