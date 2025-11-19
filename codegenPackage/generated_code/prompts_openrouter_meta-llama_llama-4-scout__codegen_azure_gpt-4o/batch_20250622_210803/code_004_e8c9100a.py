"""
Generated Code Metadata:
========================
Original URL: https://claim-dogecoin20-io.pages.dev
Prompt: Design a basic smart contract in Solidity for distributing staking rewards to DOGE20 token holders over a period of two years, similar to the one described in the Dogecoin20 project.
Generated: DETERMINISTIC_e8c9100aa7ba66f2
Batch ID: 20250622_210803
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
 * @title StakingRewards
 * @dev A smart contract for distributing staking rewards to DOGE20 token holders over a period of two years.
 */
contract StakingRewards {
    // Address of the DOGE20 token contract
    IERC20 public immutable doge20Token;

    // Total rewards to be distributed over two years
    uint256 public immutable totalRewards;

    // Duration of the reward distribution (2 years in seconds)
    uint256 public constant REWARD_DURATION = 2 * 365 * 24 * 60 * 60;

    // Timestamp when rewards distribution starts
    uint256 public immutable startTime;

    // Timestamp when rewards distribution ends
    uint256 public immutable endTime;

    // Mapping to track user stakes
    mapping(address => uint256) public stakes;

    // Mapping to track user reward claims
    mapping(address => uint256) public rewardsClaimed;

    // Total staked amount
    uint256 public totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _doge20Token Address of the DOGE20 token contract.
     * @param _totalRewards Total rewards to be distributed over two years.
     */
    constructor(IERC20 _doge20Token, uint256 _totalRewards) {
        require(address(_doge20Token) != address(0), "Invalid token address");
        require(_totalRewards > 0, "Total rewards must be greater than zero");

        doge20Token = _doge20Token;
        totalRewards = _totalRewards;
        startTime = block.timestamp;
        endTime = block.timestamp + REWARD_DURATION;
    }

    /**
     * @dev Allows users to stake DOGE20 tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(block.timestamp < endTime, "Staking period has ended");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user stake and total staked amount
        stakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to unstake their tokens.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Insufficient staked balance");

        // Update user stake and total staked amount
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(doge20Token.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their staking rewards.
     */
    function claimRewards() external {
        require(block.timestamp > startTime, "Rewards distribution has not started");
        require(stakes[msg.sender] > 0, "No staked tokens");

        // Calculate the user's reward based on their stake and elapsed time
        uint256 elapsedTime = block.timestamp > endTime ? endTime - startTime : block.timestamp - startTime;
        uint256 userReward = (stakes[msg.sender] * totalRewards * elapsedTime) / (totalStaked * REWARD_DURATION);

        // Subtract already claimed rewards
        userReward -= rewardsClaimed[msg.sender];

        require(userReward > 0, "No rewards available to claim");

        // Update claimed rewards
        rewardsClaimed[msg.sender] += userReward;

        // Transfer rewards to the user
        require(doge20Token.transfer(msg.sender, userReward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, userReward);
    }

    /**
     * @dev Returns the pending rewards for a user.
     * @param user Address of the user.
     * @return Pending rewards for the user.
     */
    function pendingRewards(address user) external view returns (uint256) {
        if (stakes[user] == 0 || block.timestamp <= startTime) {
            return 0;
        }

        uint256 elapsedTime = block.timestamp > endTime ? endTime - startTime : block.timestamp - startTime;
        uint256 userReward = (stakes[user] * totalRewards * elapsedTime) / (totalStaked * REWARD_DURATION);

        return userReward - rewardsClaimed[user];
    }
}

/**
 * @dev Interface for the ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
