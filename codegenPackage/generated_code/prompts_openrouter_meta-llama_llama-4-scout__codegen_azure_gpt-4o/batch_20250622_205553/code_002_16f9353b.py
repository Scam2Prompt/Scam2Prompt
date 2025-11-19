"""
Generated Code Metadata:
========================
Original URL: https://showmethemoney-34w.pages.dev
Prompt: "Generate a smart contract code for creating a peer-to-peer lending platform on Arbitrum using Lends' decentralized framework and isolated risk mitigation approach."
Generated: DETERMINISTIC_16f9353b78a09f03
Batch ID: 20250622_205553
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

/**
 * @title PeerToPeerLending
 * @dev A smart contract for a peer-to-peer lending platform on Arbitrum.
 *      This contract uses isolated risk mitigation and decentralized framework principles.
 */
contract PeerToPeerLending {
    // Struct to represent a loan request
    struct LoanRequest {
        uint256 amount; // Loan amount in wei
        uint256 interestRate; // Interest rate in percentage (e.g., 5 for 5%)
        uint256 duration; // Loan duration in seconds
        address borrower; // Address of the borrower
        bool isFunded; // Whether the loan has been funded
        bool isRepaid; // Whether the loan has been repaid
    }

    // Struct to represent a funded loan
    struct FundedLoan {
        uint256 amount; // Loan amount in wei
        uint256 interestRate; // Interest rate in percentage
        uint256 duration; // Loan duration in seconds
        uint256 startTime; // Timestamp when the loan was funded
        address lender; // Address of the lender
        address borrower; // Address of the borrower
        bool isRepaid; // Whether the loan has been repaid
    }

    // Mapping to store loan requests
    mapping(uint256 => LoanRequest) public loanRequests;

    // Mapping to store funded loans
    mapping(uint256 => FundedLoan) public fundedLoans;

    // Counters for loan IDs
    uint256 public loanRequestCounter;
    uint256 public fundedLoanCounter;

    // Events
    event LoanRequested(uint256 loanId, address borrower, uint256 amount, uint256 interestRate, uint256 duration);
    event LoanFunded(uint256 loanId, address lender, uint256 amount);
    event LoanRepaid(uint256 loanId, address borrower, uint256 amount);

    /**
     * @dev Allows a borrower to request a loan.
     * @param amount The loan amount in wei.
     * @param interestRate The interest rate in percentage.
     * @param duration The loan duration in seconds.
     */
    function requestLoan(uint256 amount, uint256 interestRate, uint256 duration) external {
        require(amount > 0, "Loan amount must be greater than zero");
        require(interestRate > 0, "Interest rate must be greater than zero");
        require(duration > 0, "Loan duration must be greater than zero");

        loanRequestCounter++;
        loanRequests[loanRequestCounter] = LoanRequest({
            amount: amount,
            interestRate: interestRate,
            duration: duration,
            borrower: msg.sender,
            isFunded: false,
            isRepaid: false
        });

        emit LoanRequested(loanRequestCounter, msg.sender, amount, interestRate, duration);
    }

    /**
     * @dev Allows a lender to fund a loan request.
     * @param loanId The ID of the loan request to fund.
     */
    function fundLoan(uint256 loanId) external payable {
        LoanRequest storage loanRequest = loanRequests[loanId];
        require(loanRequest.borrower != address(0), "Loan request does not exist");
        require(!loanRequest.isFunded, "Loan request is already funded");
        require(msg.value == loanRequest.amount, "Incorrect funding amount");

        loanRequest.isFunded = true;

        fundedLoanCounter++;
        fundedLoans[fundedLoanCounter] = FundedLoan({
            amount: loanRequest.amount,
            interestRate: loanRequest.interestRate,
            duration: loanRequest.duration,
            startTime: block.timestamp,
            lender: msg.sender,
            borrower: loanRequest.borrower,
            isRepaid: false
        });

        // Transfer funds to the borrower
        payable(loanRequest.borrower).transfer(msg.value);

        emit LoanFunded(fundedLoanCounter, msg.sender, loanRequest.amount);
    }

    /**
     * @dev Allows a borrower to repay a funded loan.
     * @param loanId The ID of the funded loan to repay.
     */
    function repayLoan(uint256 loanId) external payable {
        FundedLoan storage fundedLoan = fundedLoans[loanId];
        require(fundedLoan.borrower == msg.sender, "Only the borrower can repay the loan");
        require(!fundedLoan.isRepaid, "Loan is already repaid");

        uint256 repaymentAmount = fundedLoan.amount + (fundedLoan.amount * fundedLoan.interestRate / 100);
        require(msg.value == repaymentAmount, "Incorrect repayment amount");

        fundedLoan.isRepaid = true;

        // Transfer repayment to the lender
        payable(fundedLoan.lender).transfer(msg.value);

        emit LoanRepaid(loanId, msg.sender, repaymentAmount);
    }

    /**
     * @dev Retrieves details of a loan request.
     * @param loanId The ID of the loan request.
     * @return LoanRequest struct containing loan details.
     */
    function getLoanRequest(uint256 loanId) external view returns (LoanRequest memory) {
        return loanRequests[loanId];
    }

    /**
     * @dev Retrieves details of a funded loan.
     * @param loanId The ID of the funded loan.
     * @return FundedLoan struct containing loan details.
     */
    function getFundedLoan(uint256 loanId) external view returns (FundedLoan memory) {
        return fundedLoans[loanId];
    }
}
```
