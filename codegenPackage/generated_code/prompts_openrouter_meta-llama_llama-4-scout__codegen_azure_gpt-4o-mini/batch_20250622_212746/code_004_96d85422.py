"""
Generated Code Metadata:
========================
Original URL: https://quecko.com
Prompt: Develop a DeFi solution using Quecko's Web3 development services, including a decentralized exchange (DEX) and a lending protocol, with a focus on security and scalability.
Generated: DETERMINISTIC_96d85422f76b229e
Batch ID: 20250622_212746
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

// Importing necessary OpenZeppelin contracts for security
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Decentralized Exchange (DEX) contract
contract DecentralizedExchange is Ownable, ReentrancyGuard {
    // Event emitted when a trade occurs
    event Trade(address indexed buyer, address indexed seller, uint256 amount, uint256 price);

    // Mapping to store token balances of users
    mapping(address => mapping(address => uint256)) public balances;

    // Function to deposit tokens into the DEX
    function deposit(address token, uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        balances[msg.sender][token] += amount;
    }

    // Function to withdraw tokens from the DEX
    function withdraw(address token, uint256 amount) external nonReentrant {
        require(balances[msg.sender][token] >= amount, "Insufficient balance");
        balances[msg.sender][token] -= amount;
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to execute a trade
    function trade(address tokenToBuy, address tokenToSell, uint256 amountToSell, uint256 price) external nonReentrant {
        require(balances[msg.sender][tokenToSell] >= amountToSell, "Insufficient balance to sell");
        uint256 amountToBuy = amountToSell * price;

        // Transfer tokens
        balances[msg.sender][tokenToSell] -= amountToSell;
        balances[msg.sender][tokenToBuy] += amountToBuy;

        emit Trade(msg.sender, address(this), amountToSell, price);
    }
}

// Lending Protocol contract
contract LendingProtocol is Ownable, ReentrancyGuard {
    // Event emitted when a loan is taken
    event LoanTaken(address indexed borrower, uint256 amount, uint256 interestRate);

    // Struct to represent a loan
    struct Loan {
        uint256 amount;
        uint256 interestRate;
        uint256 dueDate;
        bool isPaid;
    }

    // Mapping to store loans for each borrower
    mapping(address => Loan) public loans;

    // Function to take a loan
    function takeLoan(uint256 amount, uint256 interestRate, uint256 duration) external nonReentrant {
        require(amount > 0, "Loan amount must be greater than zero");
        require(loans[msg.sender].amount == 0, "Existing loan must be paid off first");

        loans[msg.sender] = Loan({
            amount: amount,
            interestRate: interestRate,
            dueDate: block.timestamp + duration,
            isPaid: false
        });

        // Transfer loan amount to borrower
        payable(msg.sender).transfer(amount);
        emit LoanTaken(msg.sender, amount, interestRate);
    }

    // Function to repay a loan
    function repayLoan() external payable nonReentrant {
        Loan storage loan = loans[msg.sender];
        require(loan.amount > 0, "No active loan found");
        require(!loan.isPaid, "Loan already paid");
        require(msg.value >= loan.amount + (loan.amount * loan.interestRate / 100), "Insufficient repayment amount");

        loan.isPaid = true;
        // Transfer the loan amount back to the contract
        emit LoanTaken(msg.sender, loan.amount, loan.interestRate);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
