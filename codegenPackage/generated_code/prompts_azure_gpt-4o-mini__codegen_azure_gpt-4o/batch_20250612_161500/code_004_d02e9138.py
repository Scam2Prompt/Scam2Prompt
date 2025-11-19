"""
Generated Code Metadata:
========================
Original URL: https://claimanyinu.pages.dev
Prompt: Develop a smart contract that allows users to earn rewards for holding $AI tokens, incorporating the concept of a loyalty program similar to the Diamond Hands app.
Generated: DETERMINISTIC_d02e9138dac4e207
Batch ID: 20250612_161500
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
 * @title AI Token Loyalty Rewards Smart Contract
 * @dev This contract allows users to earn rewards for holding $AI tokens.
 *      It incorporates a loyalty program where rewards are distributed based on the duration of token holding.
 */
contract AITokenLoyaltyRewards {
    // State variables
    address public owner; // Contract owner
    IERC20 public aiToken; // $AI token contract
    uint256 public rewardRate; // Reward rate per second per token
    uint256 public totalRewardsDistributed; // Total rewards distributed

    struct HolderInfo {
        uint256 balance; // Amount of $AI tokens held
        uint256 lastClaimed; // Timestamp of the last reward claim
        uint256 pendingRewards; // Accumulated rewards not yet claimed
    }

    mapping(address => HolderInfo) public holders; // Mapping of user addresses to their holding info

    // Events
    event TokensDeposited(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event TokensWithdrawn(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier updateRewards(address user) {
        HolderInfo storage holder = holders[user];
        if (holder.balance > 0) {
            uint256 timeElapsed = block.timestamp - holder.lastClaimed;
            holder.pendingRewards += timeElapsed * holder.balance * rewardRate / 1e18;
        }
        holder.lastClaimed = block.timestamp;
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _aiToken Address of the $AI token contract.
     * @param _rewardRate Reward rate per second per token (scaled by 1e18 for precision).
     */
    constructor(address _aiToken, uint256 _rewardRate) {
        require(_aiToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        owner = msg.sender;
        aiToken = IERC20(_aiToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Deposit $AI tokens into the contract to start earning rewards.
     * @param amount Amount of $AI tokens to deposit.
     */
    function depositTokens(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Deposit amount must be greater than zero");
        require(aiToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        holders[msg.sender].balance += amount;

        emit TokensDeposited(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external updateRewards(msg.sender) {
        uint256 rewards = holders[msg.sender].pendingRewards;
        require(rewards > 0, "No rewards to claim");

        holders[msg.sender].pendingRewards = 0;
        totalRewardsDistributed += rewards;

        require(aiToken.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Withdraw $AI tokens from the contract.
     * @param amount Amount of $AI tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(holders[msg.sender].balance >= amount, "Insufficient balance");

        holders[msg.sender].balance -= amount;
        require(aiToken.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Update the reward rate. Only the owner can call this function.
     * @param newRewardRate New reward rate per second per token (scaled by 1e18 for precision).
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        require(newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = newRewardRate;
    }

    /**
     * @dev Emergency withdrawal of tokens from the contract. Only the owner can call this function.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(IERC20(token).transfer(owner, amount), "Token transfer failed");
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
