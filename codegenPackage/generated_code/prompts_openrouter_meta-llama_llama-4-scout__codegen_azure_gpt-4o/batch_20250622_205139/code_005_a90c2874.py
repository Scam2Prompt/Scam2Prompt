"""
Generated Code Metadata:
========================
Original URL: https://walletconnect.network
Prompt: Design a smart contract for staking and rewarding WCT tokens on the WalletConnect Network, considering scalability and decentralization.
Generated: DETERMINISTIC_a90c28741c0714d9
Batch ID: 20250622_205139
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
 * @title WCT Staking and Reward Smart Contract
 * @dev This contract allows users to stake WCT tokens and earn rewards over time.
 * It is designed for scalability and decentralization.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract WCTStaking {
    // Address of the WCT token contract
    IERC20 public immutable wctToken;

    // Reward rate per second (e.g., 1 WCT token per second)
    uint256 public rewardRate;

    // Total staked amount
    uint256 public totalStaked;

    // Mapping of user address to their staked amount
    mapping(address => uint256) public stakedBalances;

    // Mapping of user address to their last update timestamp
    mapping(address => uint256) public lastUpdateTime;

    // Mapping of user address to their accumulated rewards
    mapping(address => uint256) public rewards;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract with the WCT token address and reward rate.
     * @param _wctToken Address of the WCT token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _wctToken, uint256 _rewardRate) {
        require(address(_wctToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        wctToken = _wctToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to update rewards for the user before executing the function.
     * @param user Address of the user.
     */
    modifier updateReward(address user) {
        if (user != address(0)) {
            rewards[user] += earned(user);
            lastUpdateTime[user] = block.timestamp;
        }
        _;
    }

    /**
     * @dev Function to calculate the earned rewards for a user.
     * @param user Address of the user.
     * @return The amount of rewards earned.
     */
    function earned(address user) public view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastUpdateTime[user];
        return (stakedBalances[user] * rewardRate * timeElapsed) / 1e18;
    }

    /**
     * @dev Function to stake WCT tokens.
     * @param amount Amount of WCT tokens to stake.
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer WCT tokens from the user to the contract
        require(wctToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staked balances and total staked amount
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw staked WCT tokens.
     * @param amount Amount of WCT tokens to withdraw.
     */
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw zero tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balances and total staked amount
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer WCT tokens back to the user
        require(wctToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Function to claim earned rewards.
     */
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset the user's rewards
        rewards[msg.sender] = 0;

        // Transfer rewards to the user
        require(wctToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Function to get the total staked balance of the contract.
     * @return Total staked balance.
     */
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    /**
     * @dev Function to get the staked balance of a user.
     * @param user Address of the user.
     * @return Staked balance of the user.
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    /**
     * @dev Function to get the earned rewards of a user.
     * @param user Address of the user.
     * @return Earned rewards of the user.
     */
    function getEarnedRewards(address user) external view returns (uint256) {
        return earned(user) + rewards[user];
    }
}
```
