"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://points-orangefinance-airdrop.pages.dev
Prompt: Provide an example of implementing liquidity vaults in a decentralized finance application, referencing the Orange Finance use case.
Generated: DETERMINISTIC_7ce10b77678d8b8b
Batch ID: 20250612_152240
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
 * @title LiquidityVault
 * @notice A smart contract to manage liquidity vaults for a decentralized finance (DeFi) application.
 * Similar to the Orange Finance use case, it enables users to deposit assets, earn yield, and withdraw liquidity.
 */
contract LiquidityVault {
    // Events for logging actions
    event Deposit(address indexed user, uint256 amount, uint256 timestamp);
    event Withdraw(address indexed user, uint256 amount, uint256 timestamp);
    event RewardsClaimed(address indexed user, uint256 amount, uint256 timestamp);

    // State variables
    address public immutable owner; // Contract owner
    mapping(address => uint256) private userBalances; // Tracks user balances
    uint256 public totalLiquidity; // Total liquidity in the vault
    uint256 public rewardPool; // Reward pool for users
    uint256 public constant REWARD_RATE = 5; // Reward rate (5% per unit of liquidity)

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @notice Allows users to deposit liquidity into the vault
     * @param _amount The amount of liquidity to deposit
     */
    function deposit(uint256 _amount) external payable {
        require(_amount > 0, "Deposit amount must be greater than zero");
        require(msg.value == _amount, "Sent value must match deposit amount");

        // Update balances
        userBalances[msg.sender] += _amount;
        totalLiquidity += _amount;

        emit Deposit(msg.sender, _amount, block.timestamp);
    }

    /**
     * @notice Allows users to withdraw liquidity from the vault
     * @param _amount The amount of liquidity to withdraw
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(userBalances[msg.sender] >= _amount, "Insufficient balance");

        // Update balances
        userBalances[msg.sender] -= _amount;
        totalLiquidity -= _amount;

        // Transfer funds back to the user
        (bool success, ) = msg.sender.call{value: _amount}("");
        require(success, "Transfer failed");

        emit Withdraw(msg.sender, _amount, block.timestamp);
    }

    /**
     * @notice Allows users to claim rewards based on their liquidity
     */
    function claimRewards() external {
        uint256 userBalance = userBalances[msg.sender];
        require(userBalance > 0, "No liquidity to claim rewards");

        // Calculate rewards based on the reward rate
        uint256 rewards = (userBalance * REWARD_RATE) / 100;
        require(rewards <= rewardPool, "Not enough rewards in the pool");

        // Transfer rewards to the user
        rewardPool -= rewards;
        (bool success, ) = msg.sender.call{value: rewards}("");
        require(success, "Claim reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards, block.timestamp);
    }

    /**
     * @notice Allows the owner to add funds to the reward pool
     * @param _amount The amount to add to the reward pool
     */
    function addRewards(uint256 _amount) external payable onlyOwner {
        require(_amount > 0, "Reward amount must be greater than zero");
        require(msg.value == _amount, "Sent value must match reward amount");

        rewardPool += _amount;
    }

    /**
     * @notice Returns the balance of a specific user
     * @param _user The address of the user
     * @return The user's liquidity balance
     */
    function getUserBalance(address _user) external view returns (uint256) {
        return userBalances[_user];
    }

    /**
     * @notice Returns the total liquidity in the vault
     * @return The total liquidity
     */
    function getTotalLiquidity() external view returns (uint256) {
        return totalLiquidity;
    }

    /**
     * @notice Returns the current reward pool amount
     * @return The reward pool
     */
    function getRewardPool() external view returns (uint256) {
        return rewardPool;
    }
}
```
