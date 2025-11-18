"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-de.web.app
Prompt: Develop a staking pool smart contract in Solidity that allows users to stake $MGLS tokens and earn rewards based on their share of the pool.
Generated: DETERMINISTIC_2429d41ecd2e9e55
Batch ID: 20250612_152739
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
 * @title StakingPool
 * @dev A contract for staking $MGLS tokens and distributing rewards based on the share of the pool.
 */
contract StakingPool {
    // ERC20 token interface
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // The $MGLS token contract address
    IERC20 public immutable mglsToken;
    
    // Total staked tokens in the pool
    uint256 public totalStaked;

    // Accumulated rewards per token (scaled to avoid precision issues)
    uint256 public rewardPerToken;

    // Last updated timestamp for reward calculation
    uint256 public lastUpdateTime;

    // Reward rate per second (defined as reward tokens per second)
    uint256 public rewardRate;

    // Mapping to track user stakes
    mapping(address => uint256) public userStakes;

    // Mapping to track rewards owed to each user
    mapping(address => uint256) public userRewards;

    // Mapping to track rewards claimed by each user
    mapping(address => uint256) public userRewardDebt;

    /**
     * @dev Initializes the staking pool contract.
     * @param _mglsToken Address of the $MGLS token contract.
     * @param _rewardRate Reward rate per second (in reward tokens).
     */
    constructor(address _mglsToken, uint256 _rewardRate) {
        require(_mglsToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be nonzero");

        mglsToken = IERC20(_mglsToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to update rewards for the staking pool and user.
     * Ensures rewards are properly accounted for before any state-changing actions.
     */
    modifier updateRewards(address user) {
        _updatePool();
        if (user != address(0)) {
            userRewards[user] = pendingRewards(user);
            userRewardDebt[user] = userStakes[user] * rewardPerToken / 1e18;
        }
        _;
    }

    /**
     * @dev Allows a user to stake $MGLS tokens into the pool.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer $MGLS tokens from user to contract
        require(mglsToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user stake and total staked amount
        userStakes[msg.sender] += amount;
        totalStaked += amount;
    }

    /**
     * @dev Allows a user to withdraw their staked tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Cannot withdraw zero tokens");
        require(userStakes[msg.sender] >= amount, "Insufficient stake");

        // Update user stake and total staked amount
        userStakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        require(mglsToken.transfer(msg.sender, amount), "Token transfer failed");
    }

    /**
     * @dev Allows a user to claim their earned rewards.
     */
    function claimRewards() external updateRewards(msg.sender) {
        uint256 rewards = userRewards[msg.sender];
        require(rewards > 0, "No rewards to claim");

        userRewards[msg.sender] = 0;

        // Transfer rewards to user
        require(mglsToken.transfer(msg.sender, rewards), "Reward transfer failed");
    }

    /**
     * @dev Calculates the pending rewards for a user.
     * @param user Address of the user.
     * @return Pending reward amount.
     */
    function pendingRewards(address user) public view returns (uint256) {
        uint256 accumulatedRewardPerToken = rewardPerToken;
        if (totalStaked > 0) {
            accumulatedRewardPerToken += rewardRate * (block.timestamp - lastUpdateTime) * 1e18 / totalStaked;
        }
        return userStakes[user] * accumulatedRewardPerToken / 1e18 - userRewardDebt[user];
    }

    /**
     * @dev Internal function to update the pool's reward calculations.
     */
    function _updatePool() internal {
        if (totalStaked > 0) {
            rewardPerToken += rewardRate * (block.timestamp - lastUpdateTime) * 1e18 / totalStaked;
        }
        lastUpdateTime = block.timestamp;
    }
}
```
