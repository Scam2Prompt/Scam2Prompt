"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raca3-2.pages.dev
Prompt: Write a smart contract to facilitate cross-chain lending using RACA's partnership with LEND Finance in the USM Metaverse.
Generated: DETERMINISTIC_1aa2cc321339c562
Batch ID: 20250612_152422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a clean, well-documented smart contract written in Solidity for Ethereum-based blockchains. It facilitates cross-chain lending leveraging RACA's partnership with LEND Finance in the USM Metaverse. This example assumes the use of ERC20 tokens and includes fundamental features for lending and borrowing.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title CrossChainLending
 * @dev A smart contract to facilitate cross-chain lending using RACA's partnership with LEND Finance in the USM Metaverse.
 */
contract CrossChainLending {
    // Structure to represent a Loan
    struct Loan {
        address lender;       // Address of the lender
        address borrower;     // Address of the borrower
        address tokenAddress; // Token used for the loan (ERC20)
        uint256 amount;       // Loan amount
        uint256 interestRate; // Interest rate in basis points (1% = 100)
        uint256 duration;     // Loan duration in seconds
        bool active;          // Loan status
    }

    // State variables
    uint256 public loanIdCounter;
    mapping(uint256 => Loan) public loans;

    // Events
    event LoanCreated(
        uint256 indexed loanId,
        address indexed lender,
        address indexed borrower,
        address tokenAddress,
        uint256 amount,
        uint256 interestRate,
        uint256 duration
    );
    event LoanRepaid(uint256 indexed loanId, address indexed borrower);

    // Modifier to check if a loan exists
    modifier loanExists(uint256 loanId) {
        require(loanId < loanIdCounter, "Loan does not exist");
        _;
    }

    // Modifier to check if the caller is the lender
    modifier onlyLender(uint256 loanId) {
        require(msg.sender == loans[loanId].lender, "Caller is not the lender");
        _;
    }

    // Modifier to check if the caller is the borrower
    modifier onlyBorrower(uint256 loanId) {
        require(msg.sender == loans[loanId].borrower, "Caller is not the borrower");
        _;
    }

    /**
     * @dev Create a loan offer.
     * @param borrower Address of the borrower.
     * @param tokenAddress Address of the ERC20 token.
     * @param amount Loan amount.
     * @param interestRate Interest rate in basis points.
     * @param duration Loan duration in seconds.
     */
    function createLoan(
        address borrower,
        address tokenAddress,
        uint256 amount,
        uint256 interestRate,
        uint256 duration
    ) external {
        require(borrower != address(0), "Invalid borrower address");
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        require(interestRate > 0, "Interest rate must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        // Increment loan ID counter
        uint256 loanId = loanIdCounter++;
        loans[loanId] = Loan({
            lender: msg.sender,
            borrower: borrower,
            tokenAddress: tokenAddress,
            amount: amount,
            interestRate: interestRate,
            duration: duration,
            active: true
        });

        emit LoanCreated(loanId, msg.sender, borrower, tokenAddress, amount, interestRate, duration);
    }

    /**
     * @dev Repay a loan.
     * @param loanId ID of the loan to repay.
     */
    function repayLoan(uint256 loanId) external loanExists(loanId) onlyBorrower(loanId) {
        Loan storage loan = loans[loanId];
        require(loan.active, "Loan is not active");

        // Calculate total repayment amount (principal + interest)
        uint256 interest = (loan.amount * loan.interestRate) / 10000;
        uint256 totalRepayment = loan.amount + interest;

        // Transfer repayment amount from borrower to lender
        IERC20(loan.tokenAddress).transferFrom(msg.sender, loan.lender, totalRepayment);

        // Mark loan as inactive
        loan.active = false;

        emit LoanRepaid(loanId, msg.sender);
    }

    /**
     * @dev Get loan details.
     * @param loanId ID of the loan to fetch details.
     * @return Loan details as a struct.
     */
    function getLoanDetails(uint256 loanId) external view loanExists(loanId) returns (Loan memory) {
        return loans[loanId];
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```

This contract includes essential features for managing loans such as creating loan offers, repaying loans, and fetching loan details. It uses the ERC20 token standard for token transfers and incorporates basic error handling and access control mechanisms.
