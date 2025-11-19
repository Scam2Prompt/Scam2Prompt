"""
Generated Code Metadata:
========================
Original URL: https://florencefinance.pages.dev
Prompt: "Generate a smart contract code for a DeFi platform that enables transparent and mutually beneficial lending and borrowing, similar to Florence Finance."
Generated: DETERMINISTIC_d3f0b5a30569b5a6
Batch ID: 20250622_210316
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
 * @title DeFi Lending and Borrowing Smart Contract
 * @dev This contract enables transparent and mutually beneficial lending and borrowing.
 * It allows lenders to deposit funds and borrowers to request loans with interest.
 */
contract DeFiLendingBorrowing {
    // Struct to represent a loan request
    struct LoanRequest {
        uint256 amount; // Amount requested by the borrower
        uint256 interestRate; // Interest rate (in basis points, e.g., 500 = 5%)
        uint256 duration; // Loan duration in seconds
        address borrower; // Address of the borrower
        bool isApproved; // Whether the loan is approved
        bool isRepaid; // Whether the loan is repaid
    }

    // Struct to represent a lender's deposit
    struct Deposit {
        uint256 amount; // Amount deposited by the lender
        uint256 interestEarned; // Interest earned by the lender
        address lender; // Address of the lender
    }

    // Mapping to store loan requests
    mapping(uint256 => LoanRequest) public loanRequests;
    uint256 public loanRequestCount;

    // Mapping to store lender deposits
    mapping(address => Deposit) public deposits;

    // Events
    event LoanRequested(uint256 loanId, address indexed borrower, uint256 amount, uint256 interestRate, uint256 duration);
    event LoanApproved(uint256 loanId, address indexed lender);
    event LoanRepaid(uint256 loanId, address indexed borrower);
    event FundsDeposited(address indexed lender, uint256 amount);
    event FundsWithdrawn(address indexed lender, uint256 amount);

    // Modifier to ensure only the borrower can interact with their loan
    modifier onlyBorrower(uint256 loanId) {
        require(loanRequests[loanId].borrower == msg.sender, "Not the borrower");
        _;
    }

    // Modifier to ensure only the lender can interact with their deposit
    modifier onlyLender() {
        require(deposits[msg.sender].amount > 0, "Not a lender");
        _;
    }

    /**
     * @dev Allows a borrower to request a loan.
     * @param amount The amount of the loan.
     * @param interestRate The interest rate (in basis points).
     * @param duration The duration of the loan in seconds.
     */
    function requestLoan(uint256 amount, uint256 interestRate, uint256 duration) external {
        require(amount > 0, "Loan amount must be greater than zero");
        require(interestRate > 0, "Interest rate must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        loanRequests[loanRequestCount] = LoanRequest({
            amount: amount,
            interestRate: interestRate,
            duration: duration,
            borrower: msg.sender,
            isApproved: false,
            isRepaid: false
        });

        emit LoanRequested(loanRequestCount, msg.sender, amount, interestRate, duration);
        loanRequestCount++;
    }

    /**
     * @dev Allows a lender to deposit funds into the platform.
     */
    function depositFunds() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        deposits[msg.sender].amount += msg.value;
        deposits[msg.sender].lender = msg.sender;

        emit FundsDeposited(msg.sender, msg.value);
    }

    /**
     * @dev Allows a lender to approve a loan request.
     * @param loanId The ID of the loan request to approve.
     */
    function approveLoan(uint256 loanId) external onlyLender {
        LoanRequest storage loan = loanRequests[loanId];
        require(!loan.isApproved, "Loan already approved");
        require(!loan.isRepaid, "Loan already repaid");
        require(deposits[msg.sender].amount >= loan.amount, "Insufficient funds to approve loan");

        loan.isApproved = true;
        deposits[msg.sender].amount -= loan.amount;

        // Transfer funds to the borrower
        payable(loan.borrower).transfer(loan.amount);

        emit LoanApproved(loanId, msg.sender);
    }

    /**
     * @dev Allows a borrower to repay their loan.
     * @param loanId The ID of the loan to repay.
     */
    function repayLoan(uint256 loanId) external payable onlyBorrower(loanId) {
        LoanRequest storage loan = loanRequests[loanId];
        require(loan.isApproved, "Loan not approved");
        require(!loan.isRepaid, "Loan already repaid");

        uint256 repaymentAmount = loan.amount + (loan.amount * loan.interestRate / 10000);
        require(msg.value >= repaymentAmount, "Insufficient repayment amount");

        loan.isRepaid = true;

        // Transfer repayment to the lender
        deposits[loan.borrower].interestEarned += (loan.amount * loan.interestRate / 10000);
        deposits[loan.borrower].amount += loan.amount;

        emit LoanRepaid(loanId, msg.sender);
    }

    /**
     * @dev Allows a lender to withdraw their funds and earned interest.
     */
    function withdrawFunds() external onlyLender {
        uint256 totalAmount = deposits[msg.sender].amount + deposits[msg.sender].interestEarned;
        require(totalAmount > 0, "No funds to withdraw");

        deposits[msg.sender].amount = 0;
        deposits[msg.sender].interestEarned = 0;

        payable(msg.sender).transfer(totalAmount);

        emit FundsWithdrawn(msg.sender, totalAmount);
    }
}
```
