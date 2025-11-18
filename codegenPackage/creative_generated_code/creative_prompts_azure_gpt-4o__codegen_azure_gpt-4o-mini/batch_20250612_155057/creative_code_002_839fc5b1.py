"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://malpe.finance
Prompt: Create a smart contract in Solidity to manage risk for lending to premium institutions, incorporating transparent terms and security features inspired by Maple Finance.
Generated: DETERMINISTIC_839fc5b164aaa095
Batch ID: 20250612_155057
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
 * @title RiskManagedLending
 * @dev Smart contract for managing risk in lending to premium institutions.
 * Inspired by Maple Finance, incorporates transparent terms and security features.
 */
contract RiskManagedLending {
    // Struct to store borrower information
    struct Borrower {
        address borrowerAddress;
        uint256 loanAmount;
        uint256 interestRate; // Interest rate in basis points
        uint256 loanTerm; // Loan term in seconds
        uint256 collateralAmount; // Amount of collateral provided
        bool isActive; // Indicates if the loan is active
    }

    // Mapping from borrower address to Borrower details
    mapping(address => Borrower) public borrowers;

    // Event emitted when a loan is created
    event LoanCreated(
        address indexed borrower,
        uint256 loanAmount,
        uint256 interestRate,
        uint256 loanTerm,
        uint256 collateralAmount
    );

    // Event emitted when a loan is repaid
    event LoanRepaid(address indexed borrower, uint256 amount);

    // Event emitted when a loan is defaulted
    event LoanDefaulted(address indexed borrower);

    // Modifier to check if the caller is the borrower
    modifier onlyBorrower(address _borrower) {
        require(msg.sender == _borrower, "Caller is not the borrower");
        _;
    }

    /**
     * @dev Function to create a new loan for a borrower.
     * @param _loanAmount The amount of the loan.
     * @param _interestRate The interest rate (in basis points).
     * @param _loanTerm The duration of the loan (in seconds).
     * @param _collateralAmount The collateral amount provided.
     */
    function createLoan(
        uint256 _loanAmount,
        uint256 _interestRate,
        uint256 _loanTerm,
        uint256 _collateralAmount
    ) external {
        require(borrowers[msg.sender].loanAmount == 0, "Existing loan must be repaid first");
        require(_loanAmount > 0, "Loan amount must be greater than zero");
        require(_interestRate > 0, "Interest rate must be greater than zero");
        require(_collateralAmount >= _loanAmount, "Insufficient collateral");

        borrowers[msg.sender] = Borrower({
            borrowerAddress: msg.sender,
            loanAmount: _loanAmount,
            interestRate: _interestRate,
            loanTerm: _loanTerm,
            collateralAmount: _collateralAmount,
            isActive: true
        });

        emit LoanCreated(msg.sender, _loanAmount, _interestRate, _loanTerm, _collateralAmount);
    }

    /**
     * @dev Function to repay the loan.
     * @param _amount The amount to repay.
     */
    function repayLoan(uint256 _amount) external onlyBorrower(msg.sender) {
        Borrower storage borrower = borrowers[msg.sender];
        require(borrower.isActive, "No active loan");
        require(_amount > 0 && _amount <= borrower.loanAmount, "Invalid repayment amount");

        borrower.loanAmount -= _amount;

        if (borrower.loanAmount == 0) {
            borrower.isActive = false;
            emit LoanRepaid(msg.sender, _amount);
        }
    }

    /**
     * @dev Function to handle defaulted loans.
     */
    function handleDefault() external onlyBorrower(msg.sender) {
        Borrower storage borrower = borrowers[msg.sender];
        require(borrower.isActive, "No active loan");
        
        // Logic to determine if the loan is in default (e.g., based on time)
        // For simplicity, assume default if the loan term is exceeded
        require(block.timestamp > borrower.loanTerm, "Loan is not in default");

        borrower.isActive = false;
        emit LoanDefaulted(msg.sender);
        
        // TODO: Implement collateral liquidation logic
    }

    /**
     * @dev Function to get the details of a borrower's loan.
     * @param _borrower The address of the borrower.
     * @return Borrower details.
     */
    function getBorrowerDetails(address _borrower) external view returns (Borrower memory) {
        return borrowers[_borrower];
    }
}
```
