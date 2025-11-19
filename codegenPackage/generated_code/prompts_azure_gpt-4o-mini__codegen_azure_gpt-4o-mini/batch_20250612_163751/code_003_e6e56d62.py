"""
Generated Code Metadata:
========================
Original URL: https://xpxpay.pages.dev
Prompt: Describe how to create a smart loan feature in a blockchain application that allows users to take interest-free loans against their asset-backed tokens, similar to the XPX model.
Generated: DETERMINISTIC_e6e56d621fc174d3
Batch ID: 20250612_163751
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

// Smart contract for the Smart Loan feature
contract SmartLoan is Ownable {
    // Struct to hold loan details
    struct Loan {
        uint256 amount; // Amount of the loan
        uint256 collateral; // Amount of collateral in asset-backed tokens
        uint256 interestRate; // Interest rate (0 for interest-free)
        uint256 duration; // Duration of the loan in seconds
        uint256 startTime; // Start time of the loan
        bool isActive; // Loan status
    }

    // Mapping to store loans for each user
    mapping(address => Loan) public loans;

    // Event emitted when a loan is created
    event LoanCreated(address indexed borrower, uint256 amount, uint256 collateral, uint256 duration);

    // Event emitted when a loan is repaid
    event LoanRepaid(address indexed borrower, uint256 amount);

    // Function to create a new loan
    function createLoan(uint256 _amount, uint256 _collateral, uint256 _duration) external {
        require(_amount > 0, "Loan amount must be greater than zero");
        require(_collateral > 0, "Collateral must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");
        require(loans[msg.sender].isActive == false, "Existing loan must be repaid first");

        // Transfer collateral tokens from borrower to contract
        IERC20 collateralToken = IERC20(address(this)); // Assuming the contract itself holds the collateral tokens
        require(collateralToken.transferFrom(msg.sender, address(this), _collateral), "Collateral transfer failed");

        // Create the loan
        loans[msg.sender] = Loan({
            amount: _amount,
            collateral: _collateral,
            interestRate: 0, // Interest-free loan
            duration: _duration,
            startTime: block.timestamp,
            isActive: true
        });

        // Emit loan creation event
        emit LoanCreated(msg.sender, _amount, _collateral, _duration);
    }

    // Function to repay the loan
    function repayLoan() external {
        Loan storage loan = loans[msg.sender];
        require(loan.isActive, "No active loan to repay");
        require(block.timestamp <= loan.startTime + loan.duration, "Loan duration has expired");

        // Transfer loan amount back to the borrower
        require(IERC20(address(this)).transfer(msg.sender, loan.amount), "Loan repayment transfer failed");

        // Transfer collateral back to the borrower
        require(IERC20(address(this)).transfer(msg.sender, loan.collateral), "Collateral transfer failed");

        // Mark loan as repaid
        loan.isActive = false;

        // Emit loan repayment event
        emit LoanRepaid(msg.sender, loan.amount);
    }

    // Function to check loan details
    function getLoanDetails(address _borrower) external view returns (Loan memory) {
        return loans[_borrower];
    }
}
```
