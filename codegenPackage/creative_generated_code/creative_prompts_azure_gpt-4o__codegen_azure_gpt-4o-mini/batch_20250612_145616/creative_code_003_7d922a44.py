"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binancedogxyz.pages.dev
Prompt: Create a Solidity smart contract that interacts with the Binance Dog token contract (`0x1C45366641014069114c78962bDc371F534Bc81c`) to track token holdings and earnings.
Generated: DETERMINISTIC_7d922a44a1dbeebb
Batch ID: 20250612_145616
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

// Importing the interface for ERC20 tokens
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

/**
 * @title DogTokenTracker
 * @dev This contract allows users to track their holdings and earnings of the Binance Dog token.
 */
contract DogTokenTracker {
    // Address of the Binance Dog token contract
    address public constant DOG_TOKEN_ADDRESS = 0x1C45366641014069114c78962bDc371F534Bc81c;

    // Instance of the IERC20 interface for the Dog token
    IERC20 private dogToken;

    // Event to log the earnings withdrawal
    event EarningsWithdrawn(address indexed user, uint256 amount);

    // Mapping to track user earnings
    mapping(address => uint256) private earnings;

    // Constructor to initialize the Dog token contract instance
    constructor() {
        dogToken = IERC20(DOG_TOKEN_ADDRESS);
    }

    /**
     * @dev Function to get the balance of Dog tokens for a specific user.
     * @param user The address of the user to check the balance for.
     * @return The balance of Dog tokens.
     */
    function getUserBalance(address user) external view returns (uint256) {
        return dogToken.balanceOf(user);
    }

    /**
     * @dev Function for users to withdraw their earnings.
     * @param amount The amount of earnings to withdraw.
     */
    function withdrawEarnings(uint256 amount) external {
        require(earnings[msg.sender] >= amount, "Insufficient earnings to withdraw");
        earnings[msg.sender] -= amount;

        // Transfer the specified amount of Dog tokens to the user
        require(dogToken.transfer(msg.sender, amount), "Transfer failed");

        // Emit event for the withdrawal
        emit EarningsWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Function to record earnings for a user. This function can be called by trusted entities.
     * @param user The address of the user receiving the earnings.
     * @param amount The amount of earnings to record.
     */
    function recordEarnings(address user, uint256 amount) external {
        // Only let trusted entities call this function (implement access control as needed)
        earnings[user] += amount;
    }

    /**
     * @dev Function to get the earnings of a specific user.
     * @param user The address of the user to check earnings for.
     * @return The earnings of the user.
     */
    function getEarnings(address user) external view returns (uint256) {
        return earnings[user];
    }
}
```
