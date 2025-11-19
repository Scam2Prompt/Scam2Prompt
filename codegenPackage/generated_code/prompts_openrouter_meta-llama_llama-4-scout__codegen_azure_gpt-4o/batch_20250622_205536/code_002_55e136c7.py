"""
Generated Code Metadata:
========================
Original URL: https://vaultkarewards.pages.dev
Prompt: Generate a smart contract code snippet in Solidity to implement a staking mechanism similar to Vaultka's, with a 77% staking ratio and VKA token.
Generated: DETERMINISTIC_55e136c705a9614d
Batch ID: 20250622_205536
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
 * @title StakingContract
 * @dev A smart contract for staking VKA tokens with a fixed staking ratio of 77%.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingContract {
    // VKA token contract address
    IERC20 public immutable vkaToken;

    // Staking ratio (77%)
    uint256 public constant STAKING_RATIO = 77;

    // Mapping to track staked balances
    mapping(address => uint256) public stakedBalances;

    // Mapping to track rewards
    mapping(address => uint256) public rewards;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 reward);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the VKA token address.
     * @param _vkaToken Address of the VKA token contract.
     */
    constructor(IERC20 _vkaToken) {
        require(address(_vkaToken) != address(0), "Invalid token address");
        vkaToken = _vkaToken;
    }

    /**
     * @dev Stake VKA tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(vkaToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Calculate reward based on staking ratio
        uint256 reward = (amount * STAKING_RATIO) / 100;

        // Update staked balance and rewards
        stakedBalances[msg.sender] += amount;
        rewards[msg.sender] += reward;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Claim staking rewards.
     */
    function claimRewards() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available");

        // Reset rewards
        rewards[msg.sender] = 0;

        // Transfer rewards to the user
        require(vkaToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Unstake VKA tokens.
     */
    function unstake() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No staked balance");

        // Reset staked balance
        stakedBalances[msg.sender] = 0;

        // Transfer staked tokens back to the user
        require(vkaToken.transfer(msg.sender, stakedAmount), "Unstake transfer failed");

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Get the staked balance of a user.
     * @param user Address of the user.
     * @return Staked balance of the user.
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    /**
     * @dev Get the reward balance of a user.
     * @param user Address of the user.
     * @return Reward balance of the user.
     */
    function getRewardBalance(address user) external view returns (uint256) {
        return rewards[user];
    }
}
```
