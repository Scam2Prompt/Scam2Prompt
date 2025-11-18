"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://feg-chain.pages.dev
Prompt: Develop a smart contract that utilizes SmartDeFi™ features for asset-backing and interest-free lending, allowing users to secure a 30-day loan against the token's underlying value.
Generated: DETERMINISTIC_bea70f97b265afb0
Batch ID: 20250612_152249
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for token management and ownership control
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SmartDeFiLoan
 * @dev A smart contract for asset-backed, interest-free lending
 *      that allows users to secure a 30-day loan against the token's underlying value.
 */
contract SmartDeFiLoan is Ownable {
    // Defining a structure to hold loan information
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 collateralAmount;
        uint256 loanStartTime;
        bool isActive;
    }

    // Mapping to store active loans by borrower's address
    mapping(address => Loan) public loans;

    // ERC20 token used for collateral
    IERC20 public collateralToken;

    // Event emitted when a loan is created
    event LoanCreated(address indexed borrower, uint256 amount, uint256 collateralAmount);
    
    // Event emitted when a loan is repaid
    event LoanRepaid(address indexed borrower);
    
    // Event emitted when a loan is defaulted
    event LoanDefaulted(address indexed borrower);

    // Constructor to initialize the contract with the collateral token address
    constructor(address _collateralToken) {
        collateralToken = IERC20(_collateralToken);
    }

    /**
     * @dev Creates a new loan against the specified collateral.
     * @param amount The amount of the loan.
     * @param collateralAmount The amount of collateral provided.
     */
    function createLoan(uint256 amount, uint256 collateralAmount) external {
        require(amount > 0, "Loan amount must be greater than zero");
        require(collateralAmount > 0, "Collateral amount must be greater than zero");
        require(loans[msg.sender].isActive == false, "Existing loan must be repaid first");

        // Transfer collateral from borrower to the contract
        collateralToken.transferFrom(msg.sender, address(this), collateralAmount);

        // Create a new loan
        loans[msg.sender] = Loan({
            borrower: msg.sender,
            amount: amount,
            collateralAmount: collateralAmount,
            loanStartTime: block.timestamp,
            isActive: true
        });

        // Emit loan creation event
        emit LoanCreated(msg.sender, amount, collateralAmount);
    }

    /**
     * @dev Repays an active loan and releases collateral.
     */
    function repayLoan() external {
        Loan storage loan = loans[msg.sender];
        
        require(loan.isActive, "No active loan to repay");
        
        // Transfer the loan amount back to the borrower
        // Note: In a real-world scenario, you would have a mechanism to fund the loan amount.
        // This is a simplified example.
        
        // Reset loan details
        uint256 collateralAmount = loan.collateralAmount;
        delete loans[msg.sender];

        // Transfer collateral back to the borrower
        collateralToken.transfer(msg.sender, collateralAmount);
        
        // Emit loan repayment event
        emit LoanRepaid(msg.sender);
    }

    /**
     * @dev Checks for loan expiration and handles defaults.
     */
    function checkLoanStatus() external {
        Loan storage loan = loans[msg.sender];

        require(loan.isActive, "No active loan to check");
        
        // Check if the loan has expired
        if (block.timestamp >= loan.loanStartTime + 30 days) {
            // Mark loan as inactive
            loan.isActive = false;

            // Emit loan default event
            emit LoanDefaulted(msg.sender);
        }
    }

    /**
     * @dev Allows the owner to withdraw any collateral in case of default.
     * @param borrower Address of the borrower whose collateral is to be withdrawn.
     */
    function withdrawCollateral(address borrower) external onlyOwner {
        Loan storage loan = loans[borrower];
        require(!loan.isActive, "Loan must be inactive to withdraw collateral");

        // Transfer collateral to the owner
        uint256 collateralAmount = loan.collateralAmount;
        delete loans[borrower];
        collateralToken.transfer(owner(), collateralAmount);
    }
}
```
