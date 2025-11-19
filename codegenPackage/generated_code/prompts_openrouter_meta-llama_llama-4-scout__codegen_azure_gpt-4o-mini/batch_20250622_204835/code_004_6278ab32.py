"""
Generated Code Metadata:
========================
Original URL: https://defiland-website.pages.dev
Prompt: "Design a simple smart contract for a gamified DeFi lending platform inspired by DeFi Land's model."
Generated: DETERMINISTIC_6278ab32a1bf5882
Batch ID: 20250622_204835
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for a gamified DeFi lending platform
contract GamifiedDeFiLending is Ownable {
    // Struct to hold user lending information
    struct UserLending {
        uint256 amount; // Amount lent by the user
        uint256 interestRate; // Interest rate for the lending
        uint256 startTime; // Timestamp when the lending started
    }

    // Mapping to track user lending information
    mapping(address => UserLending) public userLendings;

    // Event emitted when a user lends tokens
    event TokensLent(address indexed user, uint256 amount, uint256 interestRate);

    // Event emitted when a user withdraws tokens
    event TokensWithdrawn(address indexed user, uint256 amount);

    // The token used for lending
    IERC20 public lendingToken;

    // Constructor to initialize the lending token
    constructor(IERC20 _lendingToken) {
        lendingToken = _lendingToken;
    }

    // Function to lend tokens to the platform
    function lendTokens(uint256 amount, uint256 interestRate) external {
        require(amount > 0, "Amount must be greater than zero");
        require(interestRate > 0, "Interest rate must be greater than zero");

        // Transfer tokens from the user to the contract
        lendingToken.transferFrom(msg.sender, address(this), amount);

        // Update user lending information
        userLendings[msg.sender] = UserLending({
            amount: amount,
            interestRate: interestRate,
            startTime: block.timestamp
        });

        emit TokensLent(msg.sender, amount, interestRate);
    }

    // Function to withdraw lent tokens along with interest
    function withdrawTokens() external {
        UserLending storage userLending = userLendings[msg.sender];
        require(userLending.amount > 0, "No tokens to withdraw");

        // Calculate interest earned
        uint256 interest = calculateInterest(userLending.amount, userLending.interestRate, userLending.startTime);
        uint256 totalAmount = userLending.amount + interest;

        // Reset user lending information
        delete userLendings[msg.sender];

        // Transfer total amount back to the user
        lendingToken.transfer(msg.sender, totalAmount);

        emit TokensWithdrawn(msg.sender, totalAmount);
    }

    // Internal function to calculate interest based on time
    function calculateInterest(uint256 amount, uint256 interestRate, uint256 startTime) internal view returns (uint256) {
        uint256 timeElapsed = block.timestamp - startTime; // Time in seconds
        return (amount * interestRate * timeElapsed) / (365 days * 100); // Simple interest formula
    }

    // Function to withdraw any ERC20 tokens accidentally sent to the contract
    function withdrawERC20(IERC20 token, uint256 amount) external onlyOwner {
        require(token != lendingToken, "Cannot withdraw lending token");
        token.transfer(msg.sender, amount);
    }
}
```
