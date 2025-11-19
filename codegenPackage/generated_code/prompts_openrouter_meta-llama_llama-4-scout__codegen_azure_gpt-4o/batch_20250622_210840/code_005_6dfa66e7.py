"""
Generated Code Metadata:
========================
Original URL: https://symbioticfinance.xyz
Prompt: "Design a smart contract function to automate the creation and management of asset-backed loans on Symbiotic Finance, considering factors like loan duration and interest rates."
Generated: DETERMINISTIC_6dfa66e7c8535748
Batch ID: 20250622_210840
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
 * @title AssetBackedLoan
 * @dev A smart contract to automate the creation and management of asset-backed loans.
 *      This contract allows lenders and borrowers to interact securely, considering loan duration and interest rates.
 */
contract AssetBackedLoan {
    // Struct to represent a loan
    struct Loan {
        uint256 loanId;
        address borrower;
        address lender;
        uint256 collateralAmount;
        uint256 loanAmount;
        uint256 interestRate; // Annual interest rate in basis points (e.g., 500 = 5%)
        uint256 duration; // Loan duration in seconds
        uint256 startTime; // Timestamp when the loan starts
        bool isActive; // Whether the loan is active
    }

    // State variables
    uint256 public nextLoanId; // Counter for loan IDs
    mapping(uint256 => Loan) public loans; // Mapping of loan IDs to Loan structs
    mapping(address => uint256[]) public borrowerLoans; // Mapping of borrower addresses to their loan IDs
    mapping(address => uint256[]) public lenderLoans; // Mapping of lender addresses to their loan IDs

    // Events
    event LoanCreated(
        uint256 loanId,
        address indexed borrower,
        address indexed lender,
        uint256 collateralAmount,
        uint256 loanAmount,
        uint256 interestRate,
        uint256 duration
    );
    event LoanRepaid(uint256 loanId, address indexed borrower, address indexed lender);

    // Modifier to check if the loan exists
    modifier loanExists(uint256 loanId) {
        require(loans[loanId].loanId == loanId, "Loan does not exist");
        _;
    }

    // Modifier to check if the loan is active
    modifier loanIsActive(uint256 loanId) {
        require(loans[loanId].isActive, "Loan is not active");
        _;
    }

    /**
     * @dev Create a new asset-backed loan.
     * @param lender The address of the lender.
     * @param collateralAmount The amount of collateral provided by the borrower.
     * @param loanAmount The amount of the loan provided by the lender.
     * @param interestRate The annual interest rate in basis points.
     * @param duration The loan duration in seconds.
     */
    function createLoan(
        address lender,
        uint256 collateralAmount,
        uint256 loanAmount,
        uint256 interestRate,
        uint256 duration
    ) external payable {
        require(msg.value == collateralAmount, "Collateral amount mismatch");
        require(lender != address(0), "Invalid lender address");
        require(loanAmount > 0, "Loan amount must be greater than zero");
        require(duration > 0, "Loan duration must be greater than zero");

        // Create a new loan
        Loan memory newLoan = Loan({
            loanId: nextLoanId,
            borrower: msg.sender,
            lender: lender,
            collateralAmount: collateralAmount,
            loanAmount: loanAmount,
            interestRate: interestRate,
            duration: duration,
            startTime: block.timestamp,
            isActive: true
        });

        // Store the loan in the mapping
        loans[nextLoanId] = newLoan;
        borrowerLoans[msg.sender].push(nextLoanId);
        lenderLoans[lender].push(nextLoanId);

        // Increment the loan ID counter
        nextLoanId++;

        // Transfer the loan amount to the borrower
        (bool success, ) = msg.sender.call{value: loanAmount}("");
        require(success, "Failed to transfer loan amount");

        // Emit the LoanCreated event
        emit LoanCreated(
            newLoan.loanId,
            newLoan.borrower,
            newLoan.lender,
            newLoan.collateralAmount,
            newLoan.loanAmount,
            newLoan.interestRate,
            newLoan.duration
        );
    }

    /**
     * @dev Repay an active loan.
     * @param loanId The ID of the loan to repay.
     */
    function repayLoan(uint256 loanId) external payable loanExists(loanId) loanIsActive(loanId) {
        Loan storage loan = loans[loanId];
        require(msg.sender == loan.borrower, "Only the borrower can repay the loan");

        // Calculate the total repayment amount (loan amount + interest)
        uint256 interest = (loan.loanAmount * loan.interestRate * loan.duration) / (365 days * 10000);
        uint256 totalRepayment = loan.loanAmount + interest;
        require(msg.value == totalRepayment, "Repayment amount mismatch");

        // Transfer repayment to the lender
        (bool success, ) = loan.lender.call{value: totalRepayment}("");
        require(success, "Failed to transfer repayment to lender");

        // Mark the loan as inactive
        loan.isActive = false;

        // Return the collateral to the borrower
        (success, ) = loan.borrower.call{value: loan.collateralAmount}("");
        require(success, "Failed to return collateral to borrower");

        // Emit the LoanRepaid event
        emit LoanRepaid(loanId, loan.borrower, loan.lender);
    }

    /**
     * @dev Get the details of a loan.
     * @param loanId The ID of the loan to retrieve.
     * @return The details of the loan.
     */
    function getLoanDetails(uint256 loanId)
        external
        view
        loanExists(loanId)
        returns (
            address borrower,
            address lender,
            uint256 collateralAmount,
            uint256 loanAmount,
            uint256 interestRate,
            uint256 duration,
            uint256 startTime,
            bool isActive
        )
    {
        Loan storage loan = loans[loanId];
        return (
            loan.borrower,
            loan.lender,
            loan.collateralAmount,
            loan.loanAmount,
            loan.interestRate,
            loan.duration,
            loan.startTime,
            loan.isActive
        );
    }
}
```
