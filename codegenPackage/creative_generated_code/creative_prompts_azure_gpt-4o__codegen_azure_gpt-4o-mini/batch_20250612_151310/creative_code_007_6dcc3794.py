"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koi-finance.pages.dev
Prompt: Write a smart contract to implement a farming pool with fixed APY, similar to Koi Finance's model, ensuring guaranteed reward payouts without lockups.
Generated: DETERMINISTIC_6dcc3794a7dfaecc
Batch ID: 20250612_151310
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FarmingPool
 * @dev A smart contract for a farming pool with fixed APY.
 */
contract FarmingPool is Ownable {
    // Struct to hold information about each user's stake
    struct UserInfo {
        uint256 amount;     // Amount of tokens the user has staked
        uint256 rewardDebt; // Amount of rewards the user has accumulated
    }

    // Token being staked
    IERC20 public stakingToken;

    // Fixed Annual Percentage Yield (APY) in basis points (i.e., 100 = 1%)
    uint256 public apyBasisPoints;

    // Total staked amount
    uint256 public totalStaked;

    // Mapping of user addresses to their staking information
    mapping(address => UserInfo) public userInfo;

    // Event for when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event for when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Event for when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking token and APY.
     * @param _stakingToken Address of the token being staked.
     * @param _apyBasisPoints Fixed APY in basis points.
     */
    constructor(IERC20 _stakingToken, uint256 _apyBasisPoints) {
        require(_apyBasisPoints > 0, "APY must be greater than 0");
        stakingToken = _stakingToken;
        apyBasisPoints = _apyBasisPoints;
    }

    /**
     * @dev Stake tokens into the pool.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from user to this contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user and total staked amount
        UserInfo storage user = userInfo[msg.sender];
        user.amount += amount;
        totalStaked += amount;

        // Emit the Staked event
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens from the pool.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= amount, "Insufficient staked amount");

        // Update total staked amount
        totalStaked -= amount;

        // Update user's staked amount
        user.amount -= amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        // Emit the Withdrawn event
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Calculate the pending rewards for a user.
     * @param user Address of the user.
     * @return Pending rewards in tokens.
     */
    function pendingRewards(address user) external view returns (uint256) {
        UserInfo storage userInfo = userInfo[user];
        // Calculate the rewards based on the amount staked and the APY
        return (userInfo.amount * apyBasisPoints / 10000);
    }

    /**
     * @dev Claim rewards for the user.
     */
    function claimRewards() external {
        UserInfo storage user = userInfo[msg.sender];
        uint256 reward = pendingRewards(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update reward debt
        user.rewardDebt += reward;

        // Transfer the reward to the user (assuming the contract has enough balance)
        stakingToken.transfer(msg.sender, reward);

        // Emit the RewardsClaimed event
        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Emergency function to withdraw tokens from the contract.
     * @param token Address of the token to withdraw.
     */
    function emergencyWithdraw(IERC20 token) external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No balance to withdraw");
        token.transfer(owner(), balance);
    }
}
```
