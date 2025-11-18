"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retik-claims.pages.dev
Prompt: Develop a smart contract in Solidity for implementing an AI-powered P2P lending system, inspired by Retik Finance's lending model.
Generated: DETERMINISTIC_b85a5c6370572719
Batch ID: 20250612_153713
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
 * @title AIP2PLending
 * @notice A smart contract for AI-powered P2P lending inspired by Retik Finance's model.
 * @dev This contract is designed to facilitate peer-to-peer lending with AI-based credit scoring.
 */
contract AIP2PLending {
    // Struct to hold loan details
    struct Loan {
        uint256 loanId;
        uint256 amount;
        uint256 interestRate; // Interest rate in percentage (e.g., 5 for 5%)
        uint256 duration; // Duration in seconds
        address borrower;
        address lender;
        bool isActive;
        bool isRepaid;
    }

    // Events
    event LoanRequested(
        uint256 loanId,
        address indexed borrower,
        uint256 amount,
        uint256 interestRate,
        uint256 duration
    );
    event LoanFunded(uint256 loanId, address indexed lender);
    event LoanRepaid(uint256 loanId, address indexed borrower);

    // State variables
    uint256 private nextLoanId = 1;
    mapping(uint256 => Loan) private loans;
    mapping(address => uint256[]) private borrowerLoans;
    mapping(address => uint256[]) private lenderLoans;

    /**
     * @notice Request a loan as a borrower.
     * @param amount The amount of the loan requested.
     * @param interestRate The interest rate for the loan (percentage).
     * @param duration The duration of the loan in seconds.
     */
    function requestLoan(
        uint256 amount,
        uint256 interestRate,
        uint256 duration
    ) external {
        require(amount > 0, "Loan amount must be greater than zero.");
        require(interestRate > 0, "Interest rate must be greater than zero.");
        require(duration > 0, "Loan duration must be greater than zero.");

        // Create the loan request
        Loan memory newLoan = Loan({
            loanId: nextLoanId,
            amount: amount,
            interestRate: interestRate,
            duration: duration,
            borrower: msg.sender,
            lender: address(0),
            isActive: false,
            isRepaid: false
        });

        loans[nextLoanId] = newLoan;
        borrowerLoans[msg.sender].push(nextLoanId);

        emit LoanRequested(nextLoanId, msg.sender, amount, interestRate, duration);

        nextLoanId++;
    }

    /**
     * @notice Fund a loan as a lender.
     * @param loanId The ID of the loan to fund.
     */
    function fundLoan(uint256 loanId) external payable {
        Loan storage loan = loans[loanId];
        require(loan.loanId != 0, "Loan does not exist.");
        require(!loan.isActive, "Loan is already active.");
        require(msg.value == loan.amount, "Incorrect funding amount.");

        loan.lender = msg.sender;
        loan.isActive = true;

        lenderLoans[msg.sender].push(loanId);

        // Transfer funds to the borrower
        payable(loan.borrower).transfer(loan.amount);

        emit LoanFunded(loanId, msg.sender);
    }

    /**
     * @notice Repay a loan as a borrower.
     * @param loanId The ID of the loan to repay.
     */
    function repayLoan(uint256 loanId) external payable {
        Loan storage loan = loans[loanId];
        require(loan.loanId != 0, "Loan does not exist.");
        require(loan.isActive, "Loan is not active.");
        require(!loan.isRepaid, "Loan is already repaid.");
        require(loan.borrower == msg.sender, "Only the borrower can repay the loan.");

        uint256 repaymentAmount = loan.amount + (loan.amount * loan.interestRate / 100);
        require(msg.value == repaymentAmount, "Incorrect repayment amount.");

        loan.isRepaid = true;

        // Transfer repayment to the lender
        payable(loan.lender).transfer(repaymentAmount);

        emit LoanRepaid(loanId, msg.sender);
    }

    /**
     * @notice Get the details of a loan.
     * @param loanId The ID of the loan.
     * @return The details of the loan.
     */
    function getLoanDetails(uint256 loanId) external view returns (Loan memory) {
        require(loans[loanId].loanId != 0, "Loan does not exist.");
        return loans[loanId];
    }

    /**
     * @notice Get all loan IDs for a borrower.
     * @return The loan IDs associated with the borrower.
     */
    function getBorrowerLoans() external view returns (uint256[] memory) {
        return borrowerLoans[msg.sender];
    }

    /**
     * @notice Get all loan IDs for a lender.
     * @return The loan IDs associated with the lender.
     */
    function getLenderLoans() external view returns (uint256[] memory) {
        return lenderLoans[msg.sender];
    }
}
```
