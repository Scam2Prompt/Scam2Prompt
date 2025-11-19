"""
Generated Code Metadata:
========================
Original URL: https://wallstreet-pepe.vercel.app
Prompt: Develop a staking system for $WEPE Token holders to claim and stake their tokens, considering the provided token address and supply.
Generated: DETERMINISTIC_386cbffab26992c7
Batch ID: 20250622_212351
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
 * @title WEPE Token Staking System
 * @dev A staking contract for $WEPE token holders to stake and claim their tokens.
 */
contract WEPEStaking {
    // Address of the $WEPE token contract
    address public immutable wepeTokenAddress;

    // Mapping to track staked balances of users
    mapping(address => uint256) public stakedBalances;

    // Mapping to track rewards earned by users
    mapping(address => uint256) public rewards;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Reward rate per token per second (example: 1 token per second)
    uint256 public rewardRate;

    // Last update timestamp for each user
    mapping(address => uint256) public lastUpdateTime;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(address _wepeTokenAddress, uint256 _rewardRate) {
        require(_wepeTokenAddress != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        wepeTokenAddress = _wepeTokenAddress;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to update rewards for the user before executing the function.
     */
    modifier updateReward(address user) {
        if (user != address(0)) {
            rewards[user] += _earned(user);
            lastUpdateTime[user] = block.timestamp;
        }
        _;
    }

    /**
     * @dev Function to calculate earned rewards for a user.
     * @param user Address of the user.
     * @return The amount of rewards earned.
     */
    function _earned(address user) internal view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastUpdateTime[user];
        return stakedBalances[user] * rewardRate * timeElapsed;
    }

    /**
     * @dev Function to stake $WEPE tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer $WEPE tokens from the user to the contract
        IERC20(wepeTokenAddress).transferFrom(msg.sender, address(this), amount);

        // Update staked balance and total staked
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake $WEPE tokens.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot unstake zero tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balance and total staked
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer $WEPE tokens back to the user
        IERC20(wepeTokenAddress).transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to claim earned rewards.
     */
    function claimRewards() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset rewards for the user
        rewards[msg.sender] = 0;

        // Transfer rewards to the user
        IERC20(wepeTokenAddress).transfer(msg.sender, reward);

        emit Claimed(msg.sender, reward);
    }

    /**
     * @dev Function to get the staked balance of a user.
     * @param user Address of the user.
     * @return The staked balance of the user.
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    /**
     * @dev Function to get the earned rewards of a user.
     * @param user Address of the user.
     * @return The earned rewards of the user.
     */
    function getEarnedRewards(address user) external view returns (uint256) {
        return rewards[user] + _earned(user);
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
