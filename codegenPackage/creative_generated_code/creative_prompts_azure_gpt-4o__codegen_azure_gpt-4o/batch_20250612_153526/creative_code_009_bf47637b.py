"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherfi-app.github.io
Prompt: Write code to implement a peer-to-peer lending system on Ethereum, ensuring the elimination of intermediaries as described in Ether Fi's lending and borrowing functionality.
Generated: DETERMINISTIC_bf47637b1c7a8e57
Batch ID: 20250612_153526
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

/**
 * @title PeerToPeerLending
 * @dev A smart contract for decentralized peer-to-peer lending on Ethereum.
 *      This contract facilitates lending and borrowing of Ether between peers 
 *      without intermediaries.
 */
contract PeerToPeerLending {
    // Struct to represent a loan request
    struct LoanRequest {
        address borrower; // Address of the borrower
        uint256 amount; // Requested loan amount in wei
        uint256 interestRate; // Interest rate in percentage (e.g., 5 for 5%)
        uint256 duration; // Loan duration in seconds
        bool fulfilled; // Whether the request has been fulfilled
    }

    // Struct to represent an active loan
    struct Loan {
        address lender; // Address of the lender
        address borrower; // Address of the borrower
        uint256 amount; // Loan amount in wei
        uint256 interestRate; // Interest rate in percentage
        uint256 startTime; // Timestamp when the loan started
        uint256 duration; // Loan duration in seconds
        bool repaid; // Whether the loan has been repaid
    }

    // Events for state changes
    event LoanRequested(
        uint256 indexed loanId,
        address indexed borrower,
        uint256 amount,
        uint256 interestRate,
        uint256 duration
    );

    event LoanFulfilled(
        uint256 indexed loanId,
        address indexed lender,
        address indexed borrower,
        uint256 amount,
        uint256 interestRate,
        uint256 duration
    );

    event LoanRepaid(
        uint256 indexed loanId,
        address indexed borrower,
        uint256 amount,
        uint256 interestPaid
    );

    // State variables
    uint256 public nextLoanId; // Unique loan identifier
    mapping(uint256 => LoanRequest) public loanRequests; // List of loan requests
    mapping(uint256 => Loan) public activeLoans; // List of active loans

    /**
     * @dev Allows a borrower to request a loan.
     * @param amount Loan amount in wei.
     * @param interestRate Interest rate in percentage.
     * @param duration Loan duration in seconds.
     */
    function requestLoan(uint256 amount, uint256 interestRate, uint256 duration) external {
        require(amount > 0, "Loan amount must be greater than zero");
        require(interestRate > 0, "Interest rate must be greater than zero");
        require(duration > 0, "Loan duration must be greater than zero");

        loanRequests[nextLoanId] = LoanRequest({
            borrower: msg.sender,
            amount: amount,
            interestRate: interestRate,
            duration: duration,
            fulfilled: false
        });

        emit LoanRequested(nextLoanId, msg.sender, amount, interestRate, duration);
        nextLoanId++;
    }

    /**
     * @dev Allows a lender to fulfill a loan request.
     * @param loanId The ID of the loan request to fulfill.
     */
    function fulfillLoan(uint256 loanId) external payable {
        LoanRequest storage request = loanRequests[loanId];
        require(!request.fulfilled, "Loan request already fulfilled");
        require(msg.value == request.amount, "Incorrect Ether value sent");

        // Mark the loan request as fulfilled
        request.fulfilled = true;

        // Create an active loan record
        activeLoans[loanId] = Loan({
            lender: msg.sender,
            borrower: request.borrower,
            amount: request.amount,
            interestRate: request.interestRate,
            startTime: block.timestamp,
            duration: request.duration,
            repaid: false
        });

        // Transfer the loan amount to the borrower
        payable(request.borrower).transfer(request.amount);

        emit LoanFulfilled(loanId, msg.sender, request.borrower, request.amount, request.interestRate, request.duration);
    }

    /**
     * @dev Allows a borrower to repay a loan.
     * @param loanId The ID of the loan to repay.
     */
    function repayLoan(uint256 loanId) external payable {
        Loan storage loan = activeLoans[loanId];
        require(!loan.repaid, "Loan already repaid");
        require(msg.sender == loan.borrower, "Only the borrower can repay the loan");

        uint256 interest = (loan.amount * loan.interestRate) / 100;
        uint256 repaymentAmount = loan.amount + interest;
        require(msg.value == repaymentAmount, "Incorrect repayment amount");

        // Mark the loan as repaid
        loan.repaid = true;

        // Transfer the repayment amount to the lender
        payable(loan.lender).transfer(repaymentAmount);

        emit LoanRepaid(loanId, msg.sender, loan.amount, interest);
    }

    /**
     * @dev Retrieves the details of a loan request.
     * @param loanId The ID of the loan request to retrieve.
     */
    function getLoanRequest(uint256 loanId) external view returns (LoanRequest memory) {
        return loanRequests[loanId];
    }

    /**
     * @dev Retrieves the details of an active loan.
     * @param loanId The ID of the active loan to retrieve.
     */
    function getActiveLoan(uint256 loanId) external view returns (Loan memory) {
        return activeLoans[loanId];
    }
}
```
