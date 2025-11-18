"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://s-targatefinance.github.io
Prompt: Create a smart contract for decentralized lending and borrowing on the Cosmos blockchain, implementing the automated processes highlighted in Stargate Finance's lending services.
Generated: DETERMINISTIC_c7e1989420cf4a9a
Batch ID: 20250612_153424
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

// Importing OpenZeppelin's ReentrancyGuard for secure handling of loans
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract DecentralizedLending is ReentrancyGuard {
    // Struct to hold loan details
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 interestRate; // in basis points (1/100 of a percent)
        uint256 duration; // in seconds
        uint256 startTime;
        bool isRepaid;
    }

    // Mapping to track loans by unique ID
    mapping(uint256 => Loan) public loans;
    uint256 public loanCounter; // Incrementing loan ID counter

    // Event emitted when a new loan is created
    event LoanCreated(uint256 loanId, address borrower, uint256 amount, uint256 interestRate, uint256 duration);
    
    // Event emitted when a loan is repaid
    event LoanRepaid(uint256 loanId, address borrower);

    // The asset being lent
    IERC20 public token;

    // Constructor to set the token address
    constructor(address _token) {
        token = IERC20(_token);
    }

    // Function to create a new loan
    function createLoan(uint256 amount, uint256 interestRate, uint256 duration) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(interestRate > 0, "Interest rate must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        // Transfer the amount from the borrower to the contract
        token.transferFrom(msg.sender, address(this), amount);

        // Create a new loan
        loans[loanCounter] = Loan({
            borrower: msg.sender,
            amount: amount,
            interestRate: interestRate,
            duration: duration,
            startTime: block.timestamp,
            isRepaid: false
        });

        emit LoanCreated(loanCounter, msg.sender, amount, interestRate, duration);
        loanCounter++;
    }

    // Function to repay a loan
    function repayLoan(uint256 loanId) external nonReentrant {
        Loan storage loan = loans[loanId];
        
        // Ensure the loan exists and is not repaid
        require(loan.borrower == msg.sender, "Only the borrower can repay the loan");
        require(!loan.isRepaid, "Loan has already been repaid");

        // Calculate total amount due (principal + interest)
        uint256 interest = (loan.amount * loan.interestRate * (block.timestamp - loan.startTime)) / (10000 * loan.duration);
        uint256 totalDue = loan.amount + interest;

        // Transfer the total due amount from the borrower to the contract
        token.transferFrom(msg.sender, address(this), totalDue);

        // Mark the loan as repaid
        loan.isRepaid = true;

        emit LoanRepaid(loanId, msg.sender);
    }

    // Function to withdraw funds by the contract owner (for security)
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer the specified amount to the owner
        token.transfer(msg.sender, amount);
    }

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Address of the contract owner
    address private owner;

    // Constructor to set the owner
    constructor() {
        owner = msg.sender;
    }
}
```
