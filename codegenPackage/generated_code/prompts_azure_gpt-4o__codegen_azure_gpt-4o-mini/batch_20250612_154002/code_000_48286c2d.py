"""
Generated Code Metadata:
========================
Original URL: https://dcqep.com
Prompt: Write a smart contract in Solidity for a DeFi application that interacts with Ethereum-based protocols, ensuring compatibility with JavaScript-based frontends.
Generated: DETERMINISTIC_48286c2dcaa7d1c5
Batch ID: 20250612_154002
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

// Smart contract for a DeFi application
contract DeFiApplication is Ownable {
    // State variables
    IERC20 public token; // ERC20 token to interact with
    uint256 public interestRate; // Interest rate for lending
    mapping(address => uint256) public deposits; // User deposits
    mapping(address => uint256) public loans; // User loans

    // Events for logging
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event LoanTaken(address indexed user, uint256 amount);
    event LoanRepaid(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the token address and interest rate
    constructor(IERC20 _token, uint256 _interestRate) {
        token = _token;
        interestRate = _interestRate;
    }

    // Function to deposit tokens into the contract
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        deposits[msg.sender] += amount;

        emit Deposited(msg.sender, amount);
    }

    // Function to withdraw tokens from the contract
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(deposits[msg.sender] >= amount, "Insufficient balance");

        deposits[msg.sender] -= amount;
        require(token.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to take a loan
    function takeLoan(uint256 amount) external {
        require(amount > 0, "Loan amount must be greater than zero");
        require(deposits[msg.sender] > 0, "No deposits found");

        loans[msg.sender] += amount;
        require(token.transfer(msg.sender, amount), "Transfer failed");

        emit LoanTaken(msg.sender, amount);
    }

    // Function to repay a loan
    function repayLoan(uint256 amount) external {
        require(amount > 0, "Repayment amount must be greater than zero");
        require(loans[msg.sender] >= amount, "Repayment exceeds loan amount");

        loans[msg.sender] -= amount;
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        emit LoanRepaid(msg.sender, amount);
    }

    // Function to set a new interest rate (only owner)
    function setInterestRate(uint256 newRate) external onlyOwner {
        interestRate = newRate;
    }

    // Function to get the user's deposit balance
    function getDepositBalance(address user) external view returns (uint256) {
        return deposits[user];
    }

    // Function to get the user's loan balance
    function getLoanBalance(address user) external view returns (uint256) {
        return loans[user];
    }
}
```
