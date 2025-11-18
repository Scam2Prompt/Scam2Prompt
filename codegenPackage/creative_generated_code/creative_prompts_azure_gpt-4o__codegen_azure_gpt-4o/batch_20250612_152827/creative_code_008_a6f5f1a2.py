"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xuirin-io.web.app
Prompt: Write a Solidity smart contract to facilitate AI-driven peer-to-peer lending, incorporating features described in XUIRIN Finance's offerings.
Generated: DETERMINISTIC_a6f5f1a22995d076
Batch ID: 20250612_152827
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

/**
 * @title AI-Powered Peer-to-Peer Lending Contract
 * @dev This contract facilitates AI-driven lending between peers.
 * Inspired by XUIRIN Finance's offerings, it incorporates lending, borrowing, and repayment functionality.
 * The contract ensures transparency and security for borrowers and lenders.
 */

contract AILending {
    // State variables
    address public owner; // Owner of the contract
    uint256 public loanCounter; // Counter for loan IDs

    enum LoanStatus { Pending, Funded, Active, Repaid, Defaulted }

    struct Loan {
        uint256 id;
        address borrower;
        address lender;
        uint256 amount;
        uint256 interestRate; // Interest rate in percentage (e.g., 5 for 5%)
        uint256 duration; // Loan duration in seconds
        LoanStatus status;
        uint256 createdAt;
        uint256 fundedAt;
    }

    // Mappings to store loans and lenders/borrowers
    mapping(uint256 => Loan) public loans;
    mapping(address => uint256[]) public borrowerLoans;
    mapping(address => uint256[]) public lenderLoans;

    // Events for transparency
    event LoanCreated(uint256 loanId, address borrower, uint256 amount);
    event LoanFunded(uint256 loanId, address lender);
    event LoanRepaid(uint256 loanId, address borrower);
    event LoanDefaulted(uint256 loanId, address borrower);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Create a loan request.
     * @param amount The loan amount.
     * @param interestRate The interest rate (percentage).
     * @param duration The loan duration in seconds.
     */
    function createLoan(uint256 amount, uint256 interestRate, uint256 duration) external {
        require(amount > 0, "Loan amount must be greater than 0");
        require(interestRate > 0, "Interest rate must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");

        loanCounter++;
        uint256 loanId = loanCounter;

        loans[loanId] = Loan({
            id: loanId,
            borrower: msg.sender,
            lender: address(0),
            amount: amount,
            interestRate: interestRate,
            duration: duration,
            status: LoanStatus.Pending,
            createdAt: block.timestamp,
            fundedAt: 0
        });

        borrowerLoans[msg.sender].push(loanId);

        emit LoanCreated(loanId, msg.sender, amount);
    }

    /**
     * @dev Fund a loan request as a lender.
     * @param loanId The ID of the loan to fund.
     */
    function fundLoan(uint256 loanId) external payable {
        Loan storage loan = loans[loanId];
        require(loan.status == LoanStatus.Pending, "Loan is not available for funding");
        require(msg.value == loan.amount, "Incorrect funding amount");

        loan.lender = msg.sender;
        loan.status = LoanStatus.Funded;
        loan.fundedAt = block.timestamp;

        lenderLoans[msg.sender].push(loanId);

        // Transfer funds to borrower
        payable(loan.borrower).transfer(msg.value);

        emit LoanFunded(loanId, msg.sender);
    }

    /**
     * @dev Repay a loan.
     * @param loanId The ID of the loan to repay.
     */
    function repayLoan(uint256 loanId) external payable {
        Loan storage loan = loans[loanId];
        require(loan.status == LoanStatus.Funded, "Loan is not active");
        require(msg.sender == loan.borrower, "Only the borrower can repay the loan");

        uint256 repaymentAmount = loan.amount + ((loan.amount * loan.interestRate) / 100);
        require(msg.value == repaymentAmount, "Incorrect repayment amount");

        loan.status = LoanStatus.Repaid;

        // Transfer repayment to lender
        payable(loan.lender).transfer(msg.value);

        emit LoanRepaid(loanId, msg.sender);
    }

    /**
     * @dev Check for loan default based on duration and status.
     * @param loanId The ID of the loan to check.
     */
    function checkDefault(uint256 loanId) external {
        Loan storage loan = loans[loanId];
        require(loan.status == LoanStatus.Funded, "Loan is not active");

        // If the duration has passed without repayment, mark it as defaulted
        if (block.timestamp > loan.fundedAt + loan.duration) {
            loan.status = LoanStatus.Defaulted;
            emit LoanDefaulted(loanId, loan.borrower);
        }
    }

    /**
     * @dev Retrieve loans created by a borrower.
     * @param borrower The address of the borrower.
     * @return An array of loan IDs.
     */
    function getBorrowerLoans(address borrower) external view returns (uint256[] memory) {
        return borrowerLoans[borrower];
    }

    /**
     * @dev Retrieve loans funded by a lender.
     * @param lender The address of the lender.
     * @return An array of loan IDs.
     */
    function getLenderLoans(address lender) external view returns (uint256[] memory) {
        return lenderLoans[lender];
    }
}
```
