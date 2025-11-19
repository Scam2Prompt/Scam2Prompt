"""
Generated Code Metadata:
========================
Original URL: https://stadelink.com
Prompt: Write a Solidity smart contract example that aligns with the earning interest functionality described on Stadelink.
Generated: DETERMINISTIC_f2a3acbbc52acb81
Batch ID: 20250612_154938
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

/// @title Stadelink Interest Earning Contract
/// @notice This contract allows users to deposit funds and earn interest over time.
/// @dev Interest is calculated based on a fixed annual rate and is compounded daily.

contract StadelinkInterest {
    // State variables
    address public owner;
    uint256 public interestRate; // Annual interest rate in basis points (1% = 100 basis points)
    uint256 public constant SECONDS_IN_A_YEAR = 31536000; // Number of seconds in a year

    // Struct to hold user information
    struct User {
        uint256 balance; // User's balance
        uint256 lastDepositTime; // Last time the user deposited funds
    }

    // Mapping to store user information
    mapping(address => User) private users;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event InterestRateUpdated(uint256 newRate);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _interestRate) {
        require(_interestRate > 0, "Interest rate must be positive");
        owner = msg.sender;
        interestRate = _interestRate;
    }

    /// @notice Allows users to deposit funds into the contract
    /// @dev Updates the user's balance and last deposit time
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Calculate interest before updating balance
        uint256 interest = calculateInterest(msg.sender);
        users[msg.sender].balance += msg.value + interest;
        users[msg.sender].lastDepositTime = block.timestamp;

        emit Deposited(msg.sender, msg.value);
    }

    /// @notice Allows users to withdraw their funds along with earned interest
    /// @dev Transfers the total balance to the user and resets their balance
    function withdraw() external {
        uint256 totalBalance = getTotalBalance(msg.sender);
        require(totalBalance > 0, "No balance to withdraw");

        // Reset user's balance before transferring to prevent reentrancy attacks
        users[msg.sender].balance = 0;

        // Transfer funds to the user
        (bool success, ) = msg.sender.call{value: totalBalance}("");
        require(success, "Transfer failed");

        emit Withdrawn(msg.sender, totalBalance);
    }

    /// @notice Calculates the total balance including interest for a user
    /// @param user The address of the user
    /// @return The total balance including interest
    function getTotalBalance(address user) public view returns (uint256) {
        uint256 interest = calculateInterest(user);
        return users[user].balance + interest;
    }

    /// @notice Calculates the interest earned by a user since their last deposit
    /// @param user The address of the user
    /// @return The calculated interest
    function calculateInterest(address user) internal view returns (uint256) {
        User storage userInfo = users[user];
        if (userInfo.lastDepositTime == 0) {
            return 0; // No deposits made
        }

        uint256 timeElapsed = block.timestamp - userInfo.lastDepositTime;
        uint256 interest = (userInfo.balance * interestRate * timeElapsed) / (SECONDS_IN_A_YEAR * 10000); // Convert basis points to percentage
        return interest;
    }

    /// @notice Allows the owner to update the interest rate
    /// @param newRate The new interest rate in basis points
    function updateInterestRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Interest rate must be positive");
        interestRate = newRate;
        emit InterestRateUpdated(newRate);
    }

    /// @notice Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
