"""
Generated Code Metadata:
========================
Original URL: https://memekombat-chain.pages.dev
Prompt: Generate a smart contract in Solidity for handling $MK token transactions, staking, and rewards distribution on the Binance Smart Chain (BSC).
Generated: DETERMINISTIC_f4d935863f0549f8
Batch ID: 20250622_205751
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
 * @title MKTokenStaking
 * @dev A smart contract for handling $MK token transactions, staking, and rewards distribution.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract MKTokenStaking {
    // Address of the $MK token contract
    IERC20 public mkToken;

    // Reward rate per second (e.g., 1 token per second)
    uint256 public rewardRate;

    // Mapping to track staked balances
    mapping(address => uint256) public stakedBalances;

    // Mapping to track reward balances
    mapping(address => uint256) public rewardBalances;

    // Mapping to track last staking timestamp
    mapping(address => uint256) public lastStakedTime;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _mkToken Address of the $MK token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _mkToken, uint256 _rewardRate) {
        mkToken = _mkToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake $MK tokens in the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Update rewards before staking
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        require(mkToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staked balance and timestamp
        stakedBalances[msg.sender] += amount;
        lastStakedTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake $MK tokens from the contract.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        // Update staked balance
        stakedBalances[msg.sender] -= amount;

        // Transfer tokens back to the user
        require(mkToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external {
        // Update rewards before claiming
        _updateRewards(msg.sender);

        uint256 rewards = rewardBalances[msg.sender];
        require(rewards > 0, "No rewards available");

        // Reset reward balance
        rewardBalances[msg.sender] = 0;

        // Transfer rewards to the user
        require(mkToken.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param user Address of the user.
     */
    function _updateRewards(address user) internal {
        uint256 stakedTime = block.timestamp - lastStakedTime[user];
        uint256 rewards = stakedTime * rewardRate * stakedBalances[user] / 1e18; // Adjust for decimals
        rewardBalances[user] += rewards;
        lastStakedTime[user] = block.timestamp;
    }

    /**
     * @dev View function to calculate pending rewards for a user.
     * @param user Address of the user.
     * @return Pending rewards.
     */
    function pendingRewards(address user) external view returns (uint256) {
        uint256 stakedTime = block.timestamp - lastStakedTime[user];
        uint256 rewards = stakedTime * rewardRate * stakedBalances[user] / 1e18; // Adjust for decimals
        return rewardBalances[user] + rewards;
    }
}
```
