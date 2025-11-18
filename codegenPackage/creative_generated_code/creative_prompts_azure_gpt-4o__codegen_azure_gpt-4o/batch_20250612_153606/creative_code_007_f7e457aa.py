"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gofurs-cash.pages.dev
Prompt: Write a Solidity contract that integrates staking functionality for GOFURS tokens, allowing users to earn rewards while maintaining compatibility with the ERC404 standard.
Generated: DETERMINISTIC_f7e457aa5c148a37
Batch ID: 20250612_153606
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
 * @title GOFURS Staking Contract
 * @dev Allows users to stake GOFURS tokens and earn rewards while maintaining compatibility with ERC404 standard.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract GOFURSStaking {
    // State variables
    IERC20 public immutable token;  // ERC20-compliant GOFURS token
    uint256 public rewardRate;      // Reward rate per second
    uint256 public totalStaked;     // Total tokens staked in the contract

    struct Stake {
        uint256 amount;         // Amount of tokens staked
        uint256 timestamp;      // Timestamp when tokens were last staked
        uint256 rewardsEarned;  // Accumulated rewards
    }

    mapping(address => Stake) public stakes; // Mapping of user address to their staking data

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor
    constructor(IERC20 _token, uint256 _rewardRate) {
        require(address(_token) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        token = _token;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake GOFURS tokens to earn rewards.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Update user rewards before modifying stakes
        _updateRewards(msg.sender);

        // Transfer tokens to the contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staking data
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        // Increase the total staked amount
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and optionally claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens to unstake");

        // Update user rewards before modifying stakes
        _updateRewards(msg.sender);

        // Transfer staked tokens back to the user
        uint256 stakedAmount = userStake.amount;
        require(token.transfer(msg.sender, stakedAmount), "Token transfer failed");

        // Reset user stake
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Decrease the total staked amount
        totalStaked -= stakedAmount;

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Claim accumulated rewards without unstaking.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        Stake storage userStake = stakes[msg.sender];
        uint256 rewards = userStake.rewardsEarned;
        require(rewards > 0, "No rewards to claim");

        // Transfer rewards to the user
        require(token.transfer(msg.sender, rewards), "Rewards transfer failed");

        // Reset rewards earned
        userStake.rewardsEarned = 0;

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param user The address of the user.
     */
    function _updateRewards(address user) internal {
        Stake storage userStake = stakes[user];
        if (userStake.amount > 0) {
            // Calculate rewards based on staked amount and elapsed time
            uint256 timeElapsed = block.timestamp - userStake.timestamp;
            uint256 newRewards = (userStake.amount * rewardRate * timeElapsed) / 1e18;

            // Update rewards and timestamp
            userStake.rewardsEarned += newRewards;
            userStake.timestamp = block.timestamp;
        }
    }

    /**
     * @dev Get details of a user's stake.
     * @param user The address of the user.
     * @return amount Staked amount.
     * @return rewardsEarned Accumulated rewards.
     * @return timestamp Last staking timestamp.
     */
    function getStakeDetails(address user) external view returns (uint256 amount, uint256 rewardsEarned, uint256 timestamp) {
        Stake storage userStake = stakes[user];
        return (userStake.amount, userStake.rewardsEarned, userStake.timestamp);
    }
}
```
