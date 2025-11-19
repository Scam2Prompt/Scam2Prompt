"""
Generated Code Metadata:
========================
Original URL: https://definerhodler.pages.dev
Prompt: Create a smart contract that supports configurable lending terms, including collateral and interest rates, inspired by DeFiner's lending model.
Generated: DETERMINISTIC_dfc0293f04daca89
Batch ID: 20250612_150613
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title ConfigurableLendingContract
 * @dev A smart contract for configurable lending with collateral and interest rates
 */
contract ConfigurableLendingContract is Ownable, ReentrancyGuard {
    struct LoanTerms {
        uint256 collateralRatio; // Percentage (e.g., 150 for 150%)
        uint256 interestRate;    // Annual percentage rate (e.g., 10 for 10%)
        uint256 loanTerm;        // Duration in seconds
        bool isActive;           // Whether these terms are active
    }

    struct Loan {
        address borrower;
        address collateralToken;
        address loanToken;
        uint256 collateralAmount;
        uint256 loanAmount;
        uint256 interestDue;
        uint256 startTime;
        uint256 dueTime;
        bool isRepaid;
    }

    // Mapping from token address to LoanTerms
    mapping(address => LoanTerms) public tokenLoanTerms;

    // Mapping from loan ID to Loan
    mapping(uint256 => Loan) public loans;

    // Counter for loan IDs
    uint256 public loanCounter;

    // Events
    event LoanTermsUpdated(
        address indexed token,
        uint256 collateralRatio,
        uint256 interestRate,
        uint256 loanTerm
    );
    event LoanCreated(
        uint256 indexed loanId,
        address indexed borrower,
        address collateralToken,
        address loanToken,
        uint256 collateralAmount,
        uint256 loanAmount,
        uint256 dueTime
    );
    event LoanRepaid(
        uint256 indexed loanId,
        address indexed borrower,
        uint256 amountRepaid
    );
    event CollateralClaimed(
        uint256 indexed loanId,
        address indexed borrower,
        uint256 collateralAmount
    );

    /**
     * @dev Set or update loan terms for a token
     * @param token The token address
     * @param collateralRatio The required collateral ratio (percentage)
     * @param interestRate The annual interest rate (percentage)
     * @param loanTerm The loan term in seconds
     */
    function setLoanTerms(
        address token,
        uint256 collateralRatio,
        uint256 interestRate,
        uint256 loanTerm
    ) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(collateralRatio >= 100, "Collateral ratio must be >= 100%");
        require(loanTerm > 0, "Loan term must be positive");

        tokenLoanTerms[token] = LoanTerms({
            collateralRatio: collateralRatio,
            interestRate: interestRate,
            loanTerm: loanTerm,
            isActive: true
        });

        emit LoanTermsUpdated(token, collateralRatio, interestRate, loanTerm);
    }

    /**
     * @dev Toggle loan terms activation status
     * @param token The token address
     * @param isActive Whether the terms should be active
     */
    function toggleLoanTerms(address token, bool isActive) external onlyOwner {
        require(token != address(0), "Invalid token address");
        tokenLoanTerms[token].isActive = isActive;
    }

    /**
     * @dev Create a new loan
     * @param collateralToken The token used as collateral
     * @param loanToken The token being borrowed
     * @param collateralAmount The amount of collateral
     * @param loanAmount The amount to borrow
     */
    function createLoan(
        address collateralToken,
        address loanToken,
        uint256 collateralAmount,
        uint256 loanAmount
    ) external nonReentrant {
        require(collateralToken != address(0) && loanToken != address(0), "Invalid token address");
        require(collateralAmount > 0 && loanAmount > 0, "Amounts must be positive");

        LoanTerms memory terms = tokenLoanTerms[loanToken];
        require(terms.isActive, "Loan terms not active for this token");

        // Verify collateral ratio
        uint256 requiredCollateral = (loanAmount * terms.collateralRatio) / 100;
        require(
            collateralAmount >= requiredCollateral,
            "Insufficient collateral"
        );

        // Transfer collateral from borrower to contract
        IERC20(collateralToken).transferFrom(
            msg.sender,
            address(this),
            collateralAmount
        );

        // Calculate interest
        uint256 interest = (loanAmount * terms.interestRate) / 100;

        // Create loan
        uint256 loanId = loanCounter++;
        loans[loanId] = Loan({
            borrower: msg.sender,
            collateralToken: collateralToken,
            loanToken: loanToken,
            collateralAmount: collateralAmount,
            loanAmount: loanAmount,
            interestDue: interest,
            startTime: block.timestamp,
            dueTime: block.timestamp + terms.loanTerm,
            isRepaid: false
        });

        // Transfer loan amount to borrower
        IERC20(loanToken).transfer(msg.sender, loanAmount);

        emit LoanCreated(
            loanId,
            msg.sender,
            collateralToken,
            loanToken,
            collateralAmount,
            loanAmount,
            block.timestamp + terms.loanTerm
        );
    }

    /**
     * @dev Repay a loan
     * @param loanId The ID of the loan to repay
     */
    function repayLoan(uint256 loanId) external nonReentrant {
        Loan storage loan = loans[loanId];
        require(loan.borrower == msg.sender, "Not the borrower");
        require(!loan.isRepaid, "Loan already repaid");
        require(block.timestamp <= loan.dueTime, "Loan is overdue");

        uint256 totalRepayment = loan.loanAmount + loan.interestDue;

        // Transfer repayment from borrower to contract
        IERC20(loan.loanToken).transferFrom(
            msg.sender,
            address(this),
            totalRepayment
        );

        // Transfer collateral back to borrower
        IERC20(loan.collateralToken).transfer(
            msg.sender,
            loan.collateralAmount
        );

        loan.isRepaid = true;

        emit LoanRepaid(loanId, msg.sender, totalRepayment);
    }

    /**
     * @dev Claim collateral for an overdue loan
     * @param loanId The ID of the overdue loan
     */
    function claimCollateral(uint256 loanId) external nonReentrant onlyOwner {
        Loan storage loan = loans[loanId];
        require(!loan.isRepaid, "Loan already repaid");
        require(block.timestamp > loan.dueTime, "Loan not yet overdue");

        // Transfer collateral to contract owner
        IERC20(loan.collateralToken).transfer(
            owner(),
            loan.collateralAmount
        );

        loan.isRepaid = true;

        emit CollateralClaimed(loanId, loan.borrower, loan.collateralAmount);
    }

    /**
     * @dev Get loan details
     * @param loanId The ID of the loan
     * @return Loan details
     */
    function getLoan(uint256 loanId) external view returns (Loan memory) {
        return loans[loanId];
    }

    /**
     * @dev Get current loan terms for a token
     * @param token The token address
     * @return LoanTerms for the token
     */
    function getLoanTerms(address token) external view returns (LoanTerms memory) {
        return tokenLoanTerms[token];
    }
}
```
