"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retikclaim.web.app
Prompt: Create a smart contract in Solidity to implement cashback rewards for Retik Finance's DeFi debit cards based on the tier system (Silver, Gold, Diamond) described on the website.
Generated: DETERMINISTIC_9a935876a0b41d69
Batch ID: 20250612_150848
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
 * @title CashbackRewards
 * @dev Smart contract to manage cashback rewards for Retik Finance DeFi debit cards.
 * Tier system: Silver, Gold, Diamond.
 * Cashback percentages: Silver = 1%, Gold = 2%, Diamond = 3%.
 */
contract CashbackRewards {
    // Owner of the contract
    address public owner;

    // Enum to represent card tiers
    enum CardTier { Silver, Gold, Diamond }

    // Struct to store user data
    struct User {
        uint256 totalSpent;
        uint256 cashbackEarned;
        CardTier tier;
    }

    // Mapping to store user data
    mapping(address => User) private users;

    // Event to log cashback payouts
    event CashbackPaid(address indexed user, uint256 amount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Access restricted to the contract owner.");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to set the tier of a user.
     * @param user Address of the user.
     * @param tier The tier to assign to the user (0 = Silver, 1 = Gold, 2 = Diamond).
     */
    function setUserTier(address user, CardTier tier) external onlyOwner {
        users[user].tier = tier;
    }

    /**
     * @dev Function to record a user's debit card spending and calculate cashback.
     * @param user Address of the user.
     * @param amountSpent The amount spent by the user.
     */
    function recordSpending(address user, uint256 amountSpent) external onlyOwner {
        require(amountSpent > 0, "Amount spent must be greater than zero.");

        // Update the total spent
        users[user].totalSpent += amountSpent;

        // Calculate cashback based on tier
        uint256 cashbackPercentage = getCashbackPercentage(users[user].tier);
        uint256 cashback = (amountSpent * cashbackPercentage) / 100;

        // Update cashback earned
        users[user].cashbackEarned += cashback;

        // Emit an event
        emit CashbackPaid(user, cashback);
    }

    /**
     * @dev Function to retrieve user statistics.
     * @param user Address of the user.
     * @return totalSpent Total amount spent by the user.
     * @return cashbackEarned Total cashback earned by the user.
     * @return tier Current tier of the user.
     */
    function getUserStats(address user)
        external
        view
        returns (uint256 totalSpent, uint256 cashbackEarned, CardTier tier)
    {
        User memory userData = users[user];
        return (userData.totalSpent, userData.cashbackEarned, userData.tier);
    }

    /**
     * @dev Internal function to determine cashback percentage based on tier.
     * @param tier The user's card tier.
     * @return Cashback percentage as an integer.
     */
    function getCashbackPercentage(CardTier tier) internal pure returns (uint256) {
        if (tier == CardTier.Silver) {
            return 1; // 1%
        } else if (tier == CardTier.Gold) {
            return 2; // 2%
        } else if (tier == CardTier.Diamond) {
            return 3; // 3%
        } else {
            return 0; // Default to 0% if tier is invalid
        }
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address.");
        owner = newOwner;
    }
}
```
