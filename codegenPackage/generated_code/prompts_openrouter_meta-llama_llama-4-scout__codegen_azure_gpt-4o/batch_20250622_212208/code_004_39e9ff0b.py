"""
Generated Code Metadata:
========================
Original URL: https://clewx.cn
Prompt: "Design a smart contract on the OKC (OKX Chain) platform for a DeFi application, focusing on security and programmability."
Generated: DETERMINISTIC_39e9ff0b75500dfe
Batch ID: 20250622_212208
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

/**
 * @title DeFi Smart Contract for OKC (OKX Chain)
 * @dev This contract allows users to deposit, withdraw, and earn interest on their funds.
 * It is designed with security and programmability in mind.
 */
contract DeFiApp {
    // State variables
    address public owner; // Contract owner
    uint256 public totalDeposits; // Total deposits in the contract

    // Mapping to track user balances
    mapping(address => uint256) private balances;

    // Events
    event Deposit(address indexed user, uint256 amount);
    event Withdrawal(address indexed user, uint256 amount);
    event InterestPaid(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    /**
     * @dev Allows users to deposit funds into the contract.
     * Emits a Deposit event.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Update user balance and total deposits
        balances[msg.sender] += msg.value;
        totalDeposits += msg.value;

        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Allows users to withdraw their funds from the contract.
     * Emits a Withdrawal event.
     * @param amount The amount to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update user balance and total deposits
        balances[msg.sender] -= amount;
        totalDeposits -= amount;

        // Transfer the funds to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        emit Withdrawal(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to pay interest to users based on their balances.
     * Emits an InterestPaid event for each user.
     * @param interestRate The interest rate (e.g., 5 for 5%).
     */
    function payInterest(uint256 interestRate) external onlyOwner {
        require(interestRate > 0, "Interest rate must be greater than zero");

        // Iterate through all users and pay interest
        for (uint256 i = 0; i < totalDeposits; i++) {
            address user = address(uint160(i)); // Simulated user address
            uint256 userBalance = balances[user];
            if (userBalance > 0) {
                uint256 interest = (userBalance * interestRate) / 100;

                // Update user balance and total deposits
                balances[user] += interest;
                totalDeposits += interest;

                emit InterestPaid(user, interest);
            }
        }
    }

    /**
     * @dev Returns the balance of a specific user.
     * @param user The address of the user.
     * @return The balance of the user.
     */
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct transfers are not allowed");
    }

    /**
     * @dev Receive function to handle Ether transfers.
     */
    receive() external payable {
        revert("Direct transfers are not allowed");
    }
}
```
