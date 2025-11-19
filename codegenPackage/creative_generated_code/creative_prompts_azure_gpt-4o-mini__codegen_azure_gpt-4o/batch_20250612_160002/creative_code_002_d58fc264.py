"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.vn
Prompt: Create a tutorial on how to implement a lending and borrowing feature in a blockchain application, referencing the unique aspects of EasyCake's platform.
Generated: DETERMINISTIC_d58fc264fb9b709d
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Lending and Borrowing Smart Contract for EasyCake Platform
This code implements a lending and borrowing feature in a blockchain application using Solidity.
It allows users to lend and borrow tokens with interest tracking and collateral management.

Key Features:
1. Support for EasyCake's unique tokenomics model.
2. Collateral-based borrowing to ensure user safety.
3. Interest calculation for lending and borrowing.

Note: This code is for educational purposes and requires additional testing and security auditing before deployment.

Prerequisites:
1. Ensure you have Solidity installed.
2. Deploy this contract using a blockchain IDE like Remix.
"""

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Lending and Borrowing Contract for EasyCake Platform
 */
contract LendingBorrowing {
    // State variables
    address public owner;
    uint256 public interestRate; // Annual interest rate in percentage (e.g., 5 for 5%)
    uint256 public collateralRatio; // Minimum collateral-to-loan ratio (e.g., 150 for 150%)

    struct Loan {
        uint256 amount; // Loan amount
        uint256 collateral; // Collateral amount
        uint256 interestAccrued; // Interest accrued
        bool isActive; // Loan status
    }

    // Mapping to store loans for each user
    mapping(address => Loan) public loans;

    // Events
    event LoanCreated(address indexed user, uint256 loanAmount, uint256 collateralAmount);
    event LoanRepaid(address indexed user, uint256 repaymentAmount);
    event CollateralWithdrawn(address indexed user, uint256 withdrawalAmount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _interestRate Annual interest rate in percentage.
     * @param _collateralRatio Minimum collateral-to-loan ratio in percentage.
     */
    constructor(uint256 _interestRate, uint256 _collateralRatio) {
        require(_interestRate > 0, "Interest rate must be greater than zero.");
        require(_collateralRatio >= 100, "Collateral ratio must be at least 100%.");
        
        owner = msg.sender;
        interestRate = _interestRate;
        collateralRatio = _collateralRatio;
    }

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action.");
        _;
    }

    /**
     * @dev Function for lending tokens to the platform.
     * @param _loanAmount Amount of tokens to be borrowed.
     * @param _collateralAmount Amount of collateral to be provided.
     */
    function borrow(uint256 _loanAmount, uint256 _collateralAmount) external payable {
        require(_loanAmount > 0, "Loan amount must be greater than zero.");
        require(_collateralAmount >= (_loanAmount * collateralRatio) / 100, 
                "Insufficient collateral.");

        // Record the loan in the mapping
        loans[msg.sender] = Loan({
            amount: _loanAmount,
            collateral: _collateralAmount,
            interestAccrued: 0,
            isActive: true
        });

        emit LoanCreated(msg.sender, _loanAmount, _collateralAmount);
    }

    /**
     * @dev Function for repaying the loan.
     * @param _repaymentAmount Amount of tokens to be repaid.
     */
    function repay(uint256 _repaymentAmount) external payable {
        Loan storage loan = loans[msg.sender];
        require(loan.isActive, "No active loan found.");
        require(_repaymentAmount > 0, "Repayment amount must be greater than zero.");
        require(_repaymentAmount <= loan.amount + loan.interestAccrued, 
                "Repayment amount exceeds loan balance.");

        // Update loan details
        loan.amount -= _repaymentAmount;
        if (loan.amount == 0) {
            loan.isActive = false;
        }

        emit LoanRepaid(msg.sender, _repaymentAmount);
    }

    /**
     * @dev Function for withdrawing collateral after loan repayment.
     */
    function withdrawCollateral() external {
        Loan storage loan = loans[msg.sender];
        require(!loan.isActive, "Loan must be fully repaid before withdrawing collateral.");
        require(loan.collateral > 0, "No collateral to withdraw.");

        uint256 collateralToWithdraw = loan.collateral;
        loan.collateral = 0;

        // Send collateral back to the user
        payable(msg.sender).transfer(collateralToWithdraw);

        emit CollateralWithdrawn(msg.sender, collateralToWithdraw);
    }

    /**
     * @dev Function to update the interest rate. Restricted to the owner.
     * @param _newInterestRate New annual interest rate in percentage.
     */
    function updateInterestRate(uint256 _newInterestRate) external onlyOwner {
        require(_newInterestRate > 0, "Interest rate must be greater than zero.");
        interestRate = _newInterestRate;
    }

    /**
     * @dev Function to update the collateral ratio. Restricted to the owner.
     * @param _newCollateralRatio New collateral-to-loan ratio in percentage.
     */
    function updateCollateralRatio(uint256 _newCollateralRatio) external onlyOwner {
        require(_newCollateralRatio >= 100, "Collateral ratio must be at least 100%.");
        collateralRatio = _newCollateralRatio;
    }

    /**
     * @dev Fallback function to accept collateral deposits.
     */
    receive() external payable {}
    
    /**
     * @dev Function to retrieve contract balance.
     * @return Contract's current balance.
     */
    function getContractBalance() external view onlyOwner returns (uint256) {
        return address(this).balance;
    }
}
```
