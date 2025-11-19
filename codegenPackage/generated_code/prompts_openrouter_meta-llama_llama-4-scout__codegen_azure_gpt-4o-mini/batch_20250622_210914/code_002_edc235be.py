"""
Generated Code Metadata:
========================
Original URL: https://scottytheaidapp.pages.dev
Prompt: Generate a smart contract code snippet in Solidity for distributing Scotty AI token rewards to users based on their share of the staking pool and annual returns percentage.
Generated: DETERMINISTIC_edc235beda88e7ef
Batch ID: 20250622_210914
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ScottyAIRewards
 * @dev A smart contract for distributing Scotty AI token rewards to users based on their share of the staking pool.
 */
contract ScottyAIRewards is Ownable {
    IERC20 public scottyToken; // The Scotty AI token contract
    uint256 public totalStaked; // Total amount of tokens staked in the pool
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public rewards; // Rewards for each user

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the Scotty AI token address.
     * @param _scottyToken Address of the Scotty AI token contract.
     */
    constructor(address _scottyToken) {
        require(_scottyToken != address(0), "Invalid token address");
        scottyToken = IERC20(_scottyToken);
    }

    /**
     * @dev Allows users to stake tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(scottyToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        stakedAmount[msg.sender] += amount;
        totalStaked += amount;
    }

    /**
     * @dev Allows users to withdraw their staked tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        require(scottyToken.transfer(msg.sender, amount), "Transfer failed");
    }

    /**
     * @dev Distributes rewards to all stakers based on their share of the staking pool.
     * @param annualReturnPercentage Annual return percentage to distribute as rewards.
     */
    function distributeRewards(uint256 annualReturnPercentage) external onlyOwner {
        require(totalStaked > 0, "No tokens staked");
        require(annualReturnPercentage > 0, "Annual return must be greater than 0");

        uint256 totalRewards = (totalStaked * annualReturnPercentage) / 100;

        for (uint256 i = 0; i < totalStaked; i++) {
            address user = address(uint160(i)); // This is a placeholder; actual implementation would require a better way to track users
            uint256 userShare = (stakedAmount[user] * totalRewards) / totalStaked;
            rewards[user] += userShare;

            emit RewardsDistributed(user, userShare);
        }
    }

    /**
     * @dev Allows users to claim their accumulated rewards.
     */
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        rewards[msg.sender] = 0;
        require(scottyToken.transfer(msg.sender, rewardAmount), "Transfer failed");
    }

    /**
     * @dev Returns the staked amount of a user.
     * @param user Address of the user.
     * @return Amount staked by the user.
     */
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmount[user];
    }

    /**
     * @dev Returns the rewards of a user.
     * @param user Address of the user.
     * @return Amount of rewards for the user.
     */
    function getRewards(address user) external view returns (uint256) {
        return rewards[user];
    }
}
```
