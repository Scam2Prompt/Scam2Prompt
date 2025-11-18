"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starltoken.com
Prompt: Create a smart contract in Solidity to manage casino bonuses, including features like "VIP cashback" and "weekly rewards" as outlined on the STARL Token website.
Generated: DETERMINISTIC_62b7b3bc0d058e14
Batch ID: 20250612_145455
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

/// @title CasinoBonusManager
/// @dev A smart contract to manage casino bonuses such as VIP cashback and weekly rewards.
contract CasinoBonusManager {
    // Event emitted when a user receives cashback
    event CashbackGranted(address indexed user, uint256 amount);
    
    // Event emitted when a user receives a weekly reward
    event WeeklyRewardGranted(address indexed user, uint256 amount);

    // Struct to hold user information
    struct User {
        uint256 totalDeposits;     // Total deposits made by the user
        uint256 cashbackBalance;    // Cashback balance available for withdrawal
        uint256 lastRewardTimestamp; // Last time user received a weekly reward
    }

    // Mapping to store user information
    mapping(address => User) private users;

    // Constants for cashback and rewards
    uint256 public constant CASHBACK_PERCENTAGE = 5; // Cashback percentage
    uint256 public constant REWARD_AMOUNT = 1 ether;  // Weekly reward amount
    uint256 public constant REWARD_INTERVAL = 7 days; // Time interval for weekly rewards

    /// @dev Allows users to deposit their funds into the casino.
    function deposit() external payable {
        require(msg.value > 0, "Deposit must be greater than zero");
        users[msg.sender].totalDeposits += msg.value;
    }

    /// @dev Grants cashback to the user based on their deposits.
    function grantCashback() external {
        User storage user = users[msg.sender];
        require(user.totalDeposits > 0, "No deposits found for user");
        
        // Calculate cashback amount
        uint256 cashbackAmount = (user.totalDeposits * CASHBACK_PERCENTAGE) / 100;

        // Update user's cashback balance
        user.cashbackBalance += cashbackAmount;

        // Emit cashback event
        emit CashbackGranted(msg.sender, cashbackAmount);
    }

    /// @dev Grants a weekly reward to the user.
    function grantWeeklyReward() external {
        User storage user = users[msg.sender];
        require(block.timestamp >= user.lastRewardTimestamp + REWARD_INTERVAL, "Weekly reward not available yet");

        // Update last reward timestamp
        user.lastRewardTimestamp = block.timestamp;

        // Transfer the weekly reward to the user
        (bool success, ) = msg.sender.call{value: REWARD_AMOUNT}("");
        require(success, "Transfer failed");

        // Emit weekly reward event
        emit WeeklyRewardGranted(msg.sender, REWARD_AMOUNT);
    }

    /// @dev Allows users to withdraw their available cashback.
    function withdrawCashback() external {
        User storage user = users[msg.sender];
        require(user.cashbackBalance > 0, "No cashback available");

        uint256 amountToWithdraw = user.cashbackBalance;
        user.cashbackBalance = 0; // Reset balance before transferring to prevent re-entrancy

        // Transfer cashback to the user
        (bool success, ) = msg.sender.call{value: amountToWithdraw}("");
        require(success, "Transfer failed");
    }

    /// @dev Fallback function to prevent accidental ETH transfers.
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }

    /// @dev Function to retrieve user information.
    function getUserInfo(address userAddress) external view returns (uint256, uint256, uint256) {
        User storage user = users[userAddress];
        return (user.totalDeposits, user.cashbackBalance, user.lastRewardTimestamp);
    }
}
```
