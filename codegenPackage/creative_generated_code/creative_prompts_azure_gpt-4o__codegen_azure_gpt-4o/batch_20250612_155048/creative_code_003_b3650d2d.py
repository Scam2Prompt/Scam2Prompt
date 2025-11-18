"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cbridge-site.github.io
Prompt: Create a smart contract that enables staking of LP tokens on cBridge for yield farming rewards, ensuring compatibility with Layer 2 solutions like Arbitrum and Optimism.
Generated: DETERMINISTIC_b3650d2d59c81057
Batch ID: 20250612_155048
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
 * @title LPTokenStaking
 * @dev A smart contract for staking LP tokens to earn yield farming rewards.
 * Compatible with Layer 2 solutions like Arbitrum and Optimism.
 */
contract LPTokenStaking {
    // Address of the LP token contract
    IERC20 public lpToken;

    // Address where reward tokens are issued from
    IERC20 public rewardToken;

    // Total amount of LP tokens staked
    uint256 public totalStaked;

    // Rewards rate per second
    uint256 public rewardsRate;

    // Last timestamp when rewards were updated
    uint256 public lastRewardTime;

    // Rewards accrued per token
    uint256 public rewardPerTokenStored;

    // Track user balances and rewards
    mapping(address => uint256) public balances;
    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract.
     * @param _lpToken Address of the LP token contract.
     * @param _rewardToken Address of the reward token contract.
     * @param _rewardsRate Reward rate per second.
     */
    constructor(IERC20 _lpToken, IERC20 _rewardToken, uint256 _rewardsRate) {
        lpToken = _lpToken;
        rewardToken = _rewardToken;
        rewardsRate = _rewardsRate;
    }

    /**
     * @dev Modifier to update rewards before executing a function.
     * Automatically updates the contract state for rewards.
     */
    modifier updateReward(address account) {
        rewardPerTokenStored = _rewardPerToken();
        lastRewardTime = block.timestamp;

        if (account != address(0)) {
            rewards[account] = _earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    /**
     * @dev Function to stake LP tokens into the contract.
     * @param amount The amount of LP tokens to stake.
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer LP tokens from the user to this contract
        require(lpToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user and total balances
        balances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw staked LP tokens.
     * @param amount The amount of LP tokens to withdraw.
     */
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw zero tokens");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update user and total balances
        balances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer LP tokens from the contract to the user
        require(lpToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Function to claim accumulated rewards.
     */
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = 0;

        // Transfer reward tokens from the contract to the user
        require(rewardToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to calculate rewards per token.
     * @return The rewards per token value.
     */
    function _rewardPerToken() internal view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }

        return
            rewardPerTokenStored +
            ((block.timestamp - lastRewardTime) * rewardsRate * 1e18) /
            totalStaked;
    }

    /**
     * @dev Internal function to calculate earned rewards for an account.
     * @param account The address of the account.
     * @return The earned rewards for the account.
     */
    function _earned(address account) internal view returns (uint256) {
        return
            (balances[account] * (_rewardPerToken() - userRewardPerTokenPaid[account])) /
            1e18 +
            rewards[account];
    }

    /**
     * @dev Function to get the current rewards for an account.
     * @param account The address of the account.
     * @return The earned rewards for the account.
     */
    function earned(address account) external view returns (uint256) {
        return _earned(account);
    }
}

/**
 * @dev Interface for ERC20 functions.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
