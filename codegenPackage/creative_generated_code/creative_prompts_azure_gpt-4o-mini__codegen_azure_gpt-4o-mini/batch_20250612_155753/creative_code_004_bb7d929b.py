"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerdogs.icu
Prompt: Outline a Solidity contract that includes a mechanism for tracking user commissions and withdrawals, inspired by the MinerDog platform's approach to user earnings.
Generated: DETERMINISTIC_bb7d929b27b9914c
Batch ID: 20250612_155753
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

contract UserCommissionTracker {
    // Struct to store user information
    struct User {
        uint256 totalEarnings; // Total earnings of the user
        uint256 withdrawnAmount; // Total amount withdrawn by the user
    }

    // Mapping to track user commissions by address
    mapping(address => User) private users;

    // Event to emit when a user withdraws their earnings
    event Withdraw(address indexed user, uint256 amount);

    // Event to emit when a commission is added
    event CommissionAdded(address indexed user, uint256 amount);

    // Modifier to check if the caller has sufficient earnings to withdraw
    modifier hasSufficientEarnings(address user, uint256 amount) {
        require(users[user].totalEarnings - users[user].withdrawnAmount >= amount, 
                "Insufficient earnings to withdraw");
        _;
    }

    // Function to add commission to a user
    function addCommission(address user, uint256 amount) external {
        require(amount > 0, "Commission amount must be greater than zero");
        
        // Update user's total earnings
        users[user].totalEarnings += amount;

        // Emit commission added event
        emit CommissionAdded(user, amount);
    }

    // Function to withdraw earnings by the user
    function withdraw(uint256 amount) external hasSufficientEarnings(msg.sender, amount) {
        // Update the withdrawn amount for the user
        users[msg.sender].withdrawnAmount += amount;

        // Transfer the amount to the user
        payable(msg.sender).transfer(amount);

        // Emit withdrawal event
        emit Withdraw(msg.sender, amount);
    }

    // Function to get the user's total earnings
    function getTotalEarnings(address user) external view returns (uint256) {
        return users[user].totalEarnings;
    }

    // Function to get the user's withdrawn amount
    function getWithdrawnAmount(address user) external view returns (uint256) {
        return users[user].withdrawnAmount;
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
