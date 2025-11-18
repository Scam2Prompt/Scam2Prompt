"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thorchain.pages.dev
Prompt: Provide an example of how to implement THORChain’s lending functionality in a decentralized finance (DeFi) application. Include references to synthetic assets and incentive pendulum.
Generated: DETERMINISTIC_40d41fbc919b823e
Batch ID: 20250612_152924
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title THORChainLending
 * @dev A simple implementation of lending functionality for THORChain using synthetic assets.
 */
contract THORChainLending is ReentrancyGuard, Ownable {
    // Define a struct to represent a loan
    struct Loan {
        uint256 amount;         // Amount of synthetic asset lent
        uint256 interest;       // Interest amount to be paid
        uint256 duration;       // Loan duration in seconds
        address borrower;       // Borrower's address
        bool isActive;          // Status of the loan
    }

    // Mapping from loan ID to Loan struct
    mapping(uint256 => Loan) public loans;
    uint256 public loanCount;  // Counter for the number of loans

    // Event emitted when a loan is created
    event LoanCreated(uint256 loanId, address borrower, uint256 amount, uint256 interest, uint256 duration);
    
    // Event emitted when a loan is repaid
    event LoanRepaid(uint256 loanId, address borrower);

    // Reference to synthetic asset contract (e.g., a stablecoin)
    IERC20 public syntheticAsset;

    // Constructor to initialize the synthetic asset
    constructor(address _syntheticAsset) {
        require(_syntheticAsset != address(0), "Invalid synthetic asset address");
        syntheticAsset = IERC20(_syntheticAsset);
    }

    /**
     * @dev Allows a user to lend synthetic assets.
     * @param amount The amount of synthetic assets to lend.
     * @param interest The interest for the loan.
     * @param duration The duration of the loan in seconds.
     */
    function lend(uint256 amount, uint256 interest, uint256 duration) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(interest > 0, "Interest must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        // Transfer synthetic assets from the borrower to the contract
        require(syntheticAsset.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Create a new loan
        loans[loanCount] = Loan(amount, interest, duration, msg.sender, true);
        emit LoanCreated(loanCount, msg.sender, amount, interest, duration);
        
        // Increment loan count
        loanCount++;
    }

    /**
     * @dev Allows a borrower to repay a loan.
     * @param loanId The ID of the loan to repay.
     */
    function repayLoan(uint256 loanId) external nonReentrant {
        Loan storage loan = loans[loanId];
        
        require(loan.isActive, "Loan is not active");
        require(msg.sender == loan.borrower, "Only the borrower can repay the loan");

        uint256 totalRepayment = loan.amount + loan.interest;

        // Transfer synthetic assets back to the contract for repayment
        require(syntheticAsset.transferFrom(msg.sender, address(this), totalRepayment), "Repayment transfer failed");

        // Mark the loan as inactive
        loan.isActive = false;
        emit LoanRepaid(loanId, msg.sender);
    }

    /**
     * @dev Allows the owner to withdraw synthetic assets from the contract.
     * @param amount The amount of synthetic assets to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(syntheticAsset.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer synthetic assets to the owner
        require(syntheticAsset.transfer(msg.sender, amount), "Withdraw failed");
    }

    // Additional functions for incentive mechanisms can be added here.
}
```
