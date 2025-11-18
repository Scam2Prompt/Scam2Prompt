"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xuirin-com.pages.dev
Prompt: Write a Solidity smart contract for handling cashback rewards based on the tiered structure (Silver, Gold, Diamond) described in xuirin Finance's DeFi Debit Card program.
Generated: DETERMINISTIC_5cbf6eae5db442f8
Batch ID: 20250612_153606
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
 * @dev A smart contract to handle cashback rewards for a tiered structure.
 */
contract CashbackRewards {
    // Enum to represent different reward tiers
    enum Tier { Silver, Gold, Diamond }

    // Struct to hold user information
    struct User {
        Tier tier;            // Current tier of the user
        uint256 totalSpent;   // Total amount spent by the user
        uint256 cashbackEarned;  // Total cashback earned by the user
    }

    // Mapping from user address to User struct
    mapping(address => User) private users;

    // Events for logging actions
    event UserRegistered(address indexed user);
    event CashbackClaimed(address indexed user, uint256 amount);
    event TierUpdated(address indexed user, Tier newTier);

    // Modifiers to check user existence
    modifier onlyRegisteredUser() {
        require(users[msg.sender].totalSpent > 0, "User not registered.");
        _;
    }

    /**
     * @dev Register a new user with initial spend of zero.
     */
    function registerUser() external {
        require(users[msg.sender].totalSpent == 0, "User already registered.");
        
        // Register user with Silver tier
        users[msg.sender] = User({
            tier: Tier.Silver,
            totalSpent: 0,
            cashbackEarned: 0
        });
        
        emit UserRegistered(msg.sender);
    }

    /**
     * @dev Update user's total spent and determine tier.
     * @param amount The amount spent by the user.
     */
    function updateSpend(uint256 amount) external onlyRegisteredUser {
        require(amount > 0, "Amount must be greater than zero.");

        // Update total spent
        User storage user = users[msg.sender];
        user.totalSpent += amount;

        // Determine and update tier based on total spent
        if (user.totalSpent >= 5000 ether) {
            user.tier = Tier.Diamond;
        } else if (user.totalSpent >= 1000 ether) {
            user.tier = Tier.Gold;
        } else {
            user.tier = Tier.Silver;
        }

        // Emit an event if the tier changes
        emit TierUpdated(msg.sender, user.tier);
    }

    /**
     * @dev Calculate and distribute cashback based on the user's tier.
     */
    function claimCashback() external onlyRegisteredUser {
        User storage user = users[msg.sender];
        uint256 cashbackAmount = calculateCashback(user.totalSpent, user.tier);

        // Update cashback earned
        user.cashbackEarned += cashbackAmount;

        // Normally, you would send the cashback to the user here
        // For demonstration, we log an event instead
        emit CashbackClaimed(msg.sender, cashbackAmount);
    }

    /**
     * @dev Calculate cashback based on spending and tier.
     * @param totalSpent The total amount spent by the user.
     * @param tier The current tier of the user.
     * @return The amount of cashback to be awarded.
     */
    function calculateCashback(uint256 totalSpent, Tier tier) internal pure returns (uint256) {
        uint256 cashbackRate;

        // Define cashback rates based on the tier
        if (tier == Tier.Diamond) {
            cashbackRate = 5; // 5% cashback for Diamond tier
        } else if (tier == Tier.Gold) {
            cashbackRate = 3; // 3% cashback for Gold tier
        } else {
            cashbackRate = 1; // 1% cashback for Silver tier
        }

        // Calculate and return cashback
        return (totalSpent * cashbackRate) / 100;
    }

    /**
     * @dev Get user information.
     * @param userAddress The address of the user.
     * @return tier The user's current tier.
     * @return totalSpent The total amount spent by the user.
     * @return cashbackEarned The total cashback earned by the user.
     */
    function getUserInfo(address userAddress) external view returns (Tier tier, uint256 totalSpent, uint256 cashbackEarned) {
        User memory user = users[userAddress];
        return (user.tier, user.totalSpent, user.cashbackEarned);
    }
}
```
