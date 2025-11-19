"""
Generated Code Metadata:
========================
Original URL: https://feg-chain.pages.dev
Prompt: Develop a smart contract that utilizes SmartDeFi™ features for asset-backing and interest-free lending, allowing users to secure a 30-day loan against the token's underlying value.
Generated: DETERMINISTIC_bea70f97b265afb0
Batch ID: 20250612_152249
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// SmartDeFiLoan contract allows users to secure a 30-day loan against their token's underlying value
contract SmartDeFiLoan is Ownable {
    // Struct to hold loan details
    struct Loan {
        uint256 amount;        // Amount of the loan
        uint256 collateral;    // Amount of collateral provided
        uint256 dueDate;       // Due date for the loan repayment
        bool isActive;         // Status of the loan
    }

    // Mapping to track loans by user address
    mapping(address => Loan) public loans;

    // Event emitted when a loan is created
    event LoanCreated(address indexed borrower, uint256 amount, uint256 collateral, uint256 dueDate);
    
    // Event emitted when a loan is repaid
    event LoanRepaid(address indexed borrower, uint256 amount);

    // Event emitted when a loan is liquidated
    event LoanLiquidated(address indexed borrower, uint256 collateral);

    // ERC20 token used for collateral
    IERC20 public collateralToken;

    // Constructor to set the collateral token address
    constructor(address _collateralToken) {
        collateralToken = IERC20(_collateralToken);
    }

    // Function to create a loan
    function createLoan(uint256 _amount, uint256 _collateral) external {
        require(_amount > 0, "Loan amount must be greater than zero");
        require(_collateral > 0, "Collateral must be greater than zero");
        require(loans[msg.sender].isActive == false, "Existing loan must be repaid first");

        // Transfer collateral from borrower to contract
        require(collateralToken.transferFrom(msg.sender, address(this), _collateral), "Collateral transfer failed");

        // Create the loan
        loans[msg.sender] = Loan({
            amount: _amount,
            collateral: _collateral,
            dueDate: block.timestamp + 30 days,
            isActive: true
        });

        // Emit loan creation event
        emit LoanCreated(msg.sender, _amount, _collateral, loans[msg.sender].dueDate);
    }

    // Function to repay the loan
    function repayLoan() external {
        Loan storage loan = loans[msg.sender];
        require(loan.isActive, "No active loan to repay");
        require(block.timestamp <= loan.dueDate, "Loan is overdue");

        // Repay the loan amount (in this case, we assume the loan amount is transferred back)
        // In a real scenario, you would need to handle the loan amount transfer logic
        // For simplicity, we assume the loan amount is zero for this example

        // Transfer collateral back to borrower
        require(collateralToken.transfer(msg.sender, loan.collateral), "Collateral transfer failed");

        // Mark loan as repaid
        loan.isActive = false;

        // Emit loan repayment event
        emit LoanRepaid(msg.sender, loan.amount);
    }

    // Function to liquidate the loan if overdue
    function liquidateLoan() external {
        Loan storage loan = loans[msg.sender];
        require(loan.isActive, "No active loan to liquidate");
        require(block.timestamp > loan.dueDate, "Loan is not overdue");

        // Mark loan as inactive
        loan.isActive = false;

        // Transfer collateral to the owner (or a liquidation address)
        require(collateralToken.transfer(owner(), loan.collateral), "Collateral transfer failed");

        // Emit loan liquidation event
        emit LoanLiquidated(msg.sender, loan.collateral);
    }

    // Function to check loan status
    function getLoanStatus(address _borrower) external view returns (Loan memory) {
        return loans[_borrower];
    }
}
```
