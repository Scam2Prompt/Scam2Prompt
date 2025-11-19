"""
Generated Code Metadata:
========================
Original URL: https://showmethemoney-34w.pages.dev
Prompt: "Develop a decentralized application (dApp) on top of Lends' platform, enabling users to borrow against their crypto assets and earn interest on their loans."
Generated: DETERMINISTIC_fb2bda6e0feb892a
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a simplified implementation of a decentralized application (dApp) for borrowing against crypto assets and earning interest on loans. The code is written in Solidity for the Ethereum blockchain.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title CryptoLendingDApp
 * @dev A decentralized application for borrowing against crypto assets and earning interest on loans.
 */
contract CryptoLendingDApp {
    // Struct to represent a loan
    struct Loan {
        uint256 amount; // Loan amount in wei
        uint256 collateral; // Collateral amount in wei
        uint256 interestRate; // Interest rate (percentage, e.g., 5 for 5%)
        uint256 startTime; // Timestamp when the loan was created
        bool isActive; // Whether the loan is active
    }

    // Mapping to store loans for each borrower
    mapping(address => Loan) public loans;

    // Event emitted when a loan is created
    event LoanCreated(address indexed borrower, uint256 amount, uint256 collateral, uint256 interestRate);

    // Event emitted when a loan is repaid
    event LoanRepaid(address indexed borrower, uint256 amount);

    // Event emitted when collateral is liquidated
    event CollateralLiquidated(address indexed borrower, uint256 collateral);

    // Owner of the contract
    address public owner;

    // Interest rate for loans (percentage, e.g., 5 for 5%)
    uint256 public baseInterestRate;

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _baseInterestRate) {
        owner = msg.sender;
        baseInterestRate = _baseInterestRate;
    }

    /**
     * @dev Allows a user to create a loan by providing collateral.
     * @param _amount The loan amount in wei.
     * @param _collateral The collateral amount in wei.
     */
    function createLoan(uint256 _amount, uint256 _collateral) external payable {
        require(msg.value == _collateral, "Collateral amount must match the sent value");
        require(_amount > 0, "Loan amount must be greater than zero");
        require(loans[msg.sender].isActive == false, "Existing loan must be repaid first");

        // Create a new loan
        loans[msg.sender] = Loan({
            amount: _amount,
            collateral: _collateral,
            interestRate: baseInterestRate,
            startTime: block.timestamp,
            isActive: true
        });

        // Emit the LoanCreated event
        emit LoanCreated(msg.sender, _amount, _collateral, baseInterestRate);

        // Transfer the loan amount to the borrower
        payable(msg.sender).transfer(_amount);
    }

    /**
     * @dev Allows a user to repay their loan.
     */
    function repayLoan() external payable {
        Loan storage loan = loans[msg.sender];
        require(loan.isActive, "No active loan found");
        
        // Calculate the interest owed
        uint256 duration = block.timestamp - loan.startTime;
        uint256 interest = (loan.amount * loan.interestRate * duration) / (100 * 365 days);

        // Total repayment amount
        uint256 totalRepayment = loan.amount + interest;
        require(msg.value >= totalRepayment, "Insufficient repayment amount");

        // Mark the loan as repaid
        loan.isActive = false;

        // Refund any excess repayment
        if (msg.value > totalRepayment) {
            payable(msg.sender).transfer(msg.value - totalRepayment);
        }

        // Return the collateral to the borrower
        payable(msg.sender).transfer(loan.collateral);

        // Emit the LoanRepaid event
        emit LoanRepaid(msg.sender, totalRepayment);
    }

    /**
     * @dev Allows the owner to liquidate collateral if the loan is overdue.
     * @param _borrower The address of the borrower.
     */
    function liquidateCollateral(address _borrower) external onlyOwner {
        Loan storage loan = loans[_borrower];
        require(loan.isActive, "No active loan found");
        
        // Check if the loan is overdue
        uint256 duration = block.timestamp - loan.startTime;
        require(duration > 30 days, "Loan is not overdue");

        // Mark the loan as liquidated
        loan.isActive = false;

        // Transfer the collateral to the owner
        payable(owner).transfer(loan.collateral);

        // Emit the CollateralLiquidated event
        emit CollateralLiquidated(_borrower, loan.collateral);
    }

    /**
     * @dev Allows the owner to update the base interest rate.
     * @param _newRate The new interest rate (percentage, e.g., 5 for 5%).
     */
    function updateInterestRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Interest rate must be greater than zero");
        baseInterestRate = _newRate;
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}
}
```

This code implements a basic lending dApp with functionality for creating loans, repaying loans, and liquidating collateral. It includes error handling, follows Solidity best practices, and is well-documented with comments.
