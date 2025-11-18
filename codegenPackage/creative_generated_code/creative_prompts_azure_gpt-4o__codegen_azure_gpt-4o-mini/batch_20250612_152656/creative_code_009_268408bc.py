"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celsius-network-en.pages.dev
Prompt: Develop a smart contract that mimics Celsius Network's lending platform, incorporating features like collateral management and interest calculation.
Generated: DETERMINISTIC_268408bc97082676
Batch ID: 20250612_152656
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

// Import the necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LendingPlatform is ReentrancyGuard, Ownable {
    // Struct to represent a user's loan
    struct Loan {
        uint256 amount;         // Amount borrowed
        uint256 collateral;     // Amount of collateral locked
        uint256 interestRate;   // Interest rate for the loan
        uint256 startTime;      // Timestamp when the loan was taken
        bool isActive;          // Whether the loan is active
    }

    // Mapping of user addresses to their loans
    mapping(address => Loan) public loans;

    // ERC20 token used for collateral and lending
    IERC20 public collateralToken;

    // Event emitted when a loan is created
    event LoanCreated(address indexed borrower, uint256 amount, uint256 collateral, uint256 interestRate);

    // Event emitted when a loan is repaid
    event LoanRepaid(address indexed borrower, uint256 amount);

    // Constructor to initialize the lending platform
    constructor(IERC20 _collateralToken) {
        collateralToken = _collateralToken;
    }

    // Function to create a new loan
    function createLoan(uint256 _amount, uint256 _collateral, uint256 _interestRate) external nonReentrant {
        require(_amount > 0, "Loan amount must be greater than zero");
        require(_collateral > 0, "Collateral must be greater than zero");
        require(_interestRate > 0, "Interest rate must be positive");
        require(loans[msg.sender].isActive == false, "Existing loan must be repaid first");

        // Transfer collateral from borrower to the contract
        require(collateralToken.transferFrom(msg.sender, address(this), _collateral), "Collateral transfer failed");

        // Create a new loan for the borrower
        loans[msg.sender] = Loan({
            amount: _amount,
            collateral: _collateral,
            interestRate: _interestRate,
            startTime: block.timestamp,
            isActive: true
        });

        emit LoanCreated(msg.sender, _amount, _collateral, _interestRate);
    }

    // Function to calculate the total amount to be repaid
    function calculateRepayment(address _borrower) public view returns (uint256) {
        Loan memory loan = loans[_borrower];
        require(loan.isActive, "No active loan found");

        // Calculate total interest accrued
        uint256 interest = (loan.amount * loan.interestRate * (block.timestamp - loan.startTime)) / (365 days * 100);
        return loan.amount + interest;
    }

    // Function to repay a loan
    function repayLoan() external nonReentrant {
        Loan storage loan = loans[msg.sender];
        require(loan.isActive, "No active loan to repay");

        // Calculate total repayment amount
        uint256 totalRepayment = calculateRepayment(msg.sender);
        require(totalRepayment > 0, "Repayment amount must be greater than zero");

        // Transfer repayment amount from borrower to the contract
        require(collateralToken.transferFrom(msg.sender, address(this), totalRepayment), "Repayment transfer failed");

        // Release collateral back to the borrower
        require(collateralToken.transfer(msg.sender, loan.collateral), "Collateral transfer failed");

        // Mark loan as repaid
        loan.isActive = false;

        emit LoanRepaid(msg.sender, totalRepayment);
    }

    // Function to get loan details
    function getLoanDetails(address _borrower) external view returns (Loan memory) {
        return loans[_borrower];
    }

    // Function to withdraw collateral (only callable by the owner)
    function emergencyWithdrawCollateral(address _to, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(collateralToken.balanceOf(address(this)) >= _amount, "Insufficient balance");

        // Transfer collateral to the specified address
        collateralToken.transfer(_to, _amount);
    }
}
```
