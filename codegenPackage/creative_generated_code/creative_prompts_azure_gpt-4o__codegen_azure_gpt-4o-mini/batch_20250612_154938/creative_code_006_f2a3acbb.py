"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stadelink.com
Prompt: Write a Solidity smart contract example that aligns with the earning interest functionality described on Stadelink.
Generated: DETERMINISTIC_f2a3acbbc52acb81
Batch ID: 20250612_154938
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

contract StadelinkInterestEarning {
    // Mapping to track user's balance
    mapping(address => uint256) private balances;
    // Mapping to track user's interest rate
    mapping(address => uint256) private interestRates;
    // Mapping to track last deposit time for interest calculation
    mapping(address => uint256) private lastDepositTime;

    // Event to log deposits
    event Deposited(address indexed user, uint256 amount);
    // Event to log withdrawals
    event Withdrawn(address indexed user, uint256 amount);
    // Event to log interest earned
    event InterestPaid(address indexed user, uint256 interest);

    // Modifier to check if the sender has a positive balance
    modifier hasBalance() {
        require(balances[msg.sender] > 0, "No balance available");
        _;
    }

    // Function to deposit funds into the contract
    function deposit(uint256 amount) external payable {
        require(amount > 0, "Deposit amount must be greater than zero");
        require(msg.value == amount, "Sent value must match the specified amount");

        // Update the user's balance and last deposit time
        balances[msg.sender] += amount;
        lastDepositTime[msg.sender] = block.timestamp;

        emit Deposited(msg.sender, amount);
    }

    // Function to withdraw funds from the contract
    function withdraw(uint256 amount) external hasBalance {
        require(amount <= balances[msg.sender], "Insufficient balance");

        // Calculate and pay interest before withdrawal
        uint256 interest = calculateInterest(msg.sender);
        if (interest > 0) {
            balances[msg.sender] += interest;
            emit InterestPaid(msg.sender, interest);
        }

        // Update the user's balance and handle withdrawal
        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to set interest rate for a user
    function setInterestRate(uint256 rate) external {
        require(rate >= 0, "Interest rate must be non-negative");
        interestRates[msg.sender] = rate;
    }

    // Internal function to calculate accrued interest for a user
    function calculateInterest(address user) internal view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastDepositTime[user];
        uint256 interestRate = interestRates[user];

        // Calculate interest as (balance * rate * time) / (365 days)
        uint256 interest = (balances[user] * interestRate * timeElapsed) / (365 days * 100);
        return interest;
    }

    // Function to check the user's balance
    function getBalance() external view returns (uint256) {
        return balances[msg.sender];
    }

    // Function to check the user's interest rate
    function getInterestRate() external view returns (uint256) {
        return interestRates[msg.sender];
    }
}
```
