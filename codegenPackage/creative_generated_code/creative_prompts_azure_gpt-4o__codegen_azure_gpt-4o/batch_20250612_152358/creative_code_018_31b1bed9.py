"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-99bitcoins.pages.dev
Prompt: Develop a smart contract to handle token rewards distribution for staking $99BTC tokens, ensuring compliance with the tokenomics percentages.
Generated: DETERMINISTIC_31b1bed9184bc768
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a `Solidity` smart contract that handles token rewards distribution for staking `$99BTC` tokens while adhering to tokenomics percentages. The contract is well-commented, includes error handling, and adheres to best practices.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TokenRewardsDistribution
 * @dev A smart contract for staking and distributing rewards based on tokenomics percentages.
 * Users stake $99BTC tokens and receive rewards proportionally.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract TokenRewardsDistribution {
    // Address of the $99BTC token
    IERC20 public immutable token;

    // Total staked amount
    uint256 public totalStaked;

    // Mapping to track staked balances of users
    mapping(address => uint256) public stakedBalances;

    // Mapping to track rewards of users
    mapping(address => uint256) public rewards;

    // Reward distribution percentages (in basis points: 1% = 100)
    uint256 public constant REWARD_PERCENTAGE = 500; // 5%

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to set the token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    /**
     * @dev Stake $99BTC tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staked balances and total staked
        stakedBalances[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake $99BTC tokens and withdraw them from the contract.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");

        // Update staked balances and total staked
        stakedBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(token.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Calculate and update rewards for a user based on their staked balance.
     * This function can be called periodically to distribute rewards.
     * @param _user Address of the user to calculate rewards for.
     */
    function calculateRewards(address _user) external {
        uint256 userStakedBalance = stakedBalances[_user];
        require(userStakedBalance > 0, "User has no staked balance");

        // Calculate rewards based on the reward percentage
        uint256 reward = (userStakedBalance * REWARD_PERCENTAGE) / 10000;
        rewards[_user] += reward;
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external {
        uint256 userRewards = rewards[msg.sender];
        require(userRewards > 0, "No rewards available to claim");

        // Reset rewards balance before transferring tokens
        rewards[msg.sender] = 0;

        // Transfer rewards to the user
        require(token.transfer(msg.sender, userRewards), "Reward transfer failed");

        emit RewardClaimed(msg.sender, userRewards);
    }

    /**
     * @dev Get the staked balance of a user.
     * @param _user Address of the user.
     * @return Staked balance of the user.
     */
    function getStakedBalance(address _user) external view returns (uint256) {
        return stakedBalances[_user];
    }

    /**
     * @dev Get the reward balance of a user.
     * @param _user Address of the user.
     * @return Reward balance of the user.
     */
    function getRewardBalance(address _user) external view returns (uint256) {
        return rewards[_user];
    }
}
```

This Solidity code defines a staking and reward distribution mechanism based on tokenomics percentages. Ensure you test and audit the contract before deploying it to a production environment.
