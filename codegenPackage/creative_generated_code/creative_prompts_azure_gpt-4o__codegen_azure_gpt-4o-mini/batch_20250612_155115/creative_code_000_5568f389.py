"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starsdapps.pro
Prompt: Write a smart contract in Solidity that mimics the functionality of earning interest as described on starsdapps.pro, ensuring safety and trust features are implemented.
Generated: DETERMINISTIC_5568f38979a8189b
Batch ID: 20250612_155115
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

contract InterestEarning {
    
    // Struct to hold user information
    struct User {
        uint256 balance; // User's balance
        uint256 lastDepositTime; // Last deposit time for interest calculation
    }

    // Mapping from user address to user information
    mapping(address => User) private users;

    // Interest rate in percentage (e.g., 5 means 5%)
    uint256 public interestRate;

    // Constructor to initialize the interest rate
    constructor(uint256 _interestRate) {
        require(_interestRate > 0, "Interest rate should be greater than zero");
        interestRate = _interestRate;
    }

    // Event to log deposits
    event Deposited(address indexed user, uint256 amount);

    // Event to log withdrawals
    event Withdrawn(address indexed user, uint256 amount);

    // Modifier to check if the user has a balance
    modifier hasBalance() {
        require(users[msg.sender].balance > 0, "No balance to withdraw");
        _;
    }

    // Function to deposit funds and start earning interest
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Update user's balance and last deposit time
        User storage user = users[msg.sender];
        user.balance += msg.value;
        user.lastDepositTime = block.timestamp;

        emit Deposited(msg.sender, msg.value);
    }

    // Function to withdraw funds along with earned interest
    function withdraw() external hasBalance {
        User storage user = users[msg.sender];
        uint256 interest = calculateInterest(user.balance, user.lastDepositTime);

        // Calculate total amount to withdraw (balance + interest)
        uint256 amountToWithdraw = user.balance + interest;

        // Reset user's balance and last deposit time
        user.balance = 0;
        user.lastDepositTime = 0;

        // Transfer funds to the user
        (bool sent, ) = msg.sender.call{value: amountToWithdraw}("");
        require(sent, "Failed to send Ether");

        emit Withdrawn(msg.sender, amountToWithdraw);
    }

    // Function to calculate interest based on the user's balance and deposit time
    function calculateInterest(uint256 balance, uint256 lastDepositTime) internal view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastDepositTime; // Time elapsed since last deposit
        uint256 interest = (balance * interestRate * timeElapsed) / (365 days * 100); // Simple interest formula
        return interest;
    }

    // Function to check the user's balance
    function getUserBalance() external view returns (uint256) {
        return users[msg.sender].balance + calculateInterest(users[msg.sender].balance, users[msg.sender].lastDepositTime);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct deposits not allowed. Use the deposit function.");
    }

    // Function to update the interest rate (only owner can call this)
    function updateInterestRate(uint256 newInterestRate) external {
        // Assume only the contract owner can execute this function
        // For production, implement a proper ownership mechanism
        require(newInterestRate > 0, "Interest rate must be greater than zero");
        interestRate = newInterestRate;
    }
}
```
