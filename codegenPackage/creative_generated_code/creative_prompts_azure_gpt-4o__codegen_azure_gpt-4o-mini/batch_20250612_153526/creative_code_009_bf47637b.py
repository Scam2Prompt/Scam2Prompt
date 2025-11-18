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

contract PeerToPeerLending {

    // Struct to represent a loan request
    struct LoanRequest {
        address borrower;
        uint256 amount;
        uint256 interestRate; // Interest rate in basis points (1/100th of a percent)
        uint256 duration; // Duration of the loan in seconds
        bool isActive; // To check if the loan request is active
        uint256 repaymentDeadline; // Deadline for repayment
    }

    // Mapping to store loan requests by their ID
    mapping(uint256 => LoanRequest) public loanRequests;
    uint256 public loanRequestCount;

    // Event to log loan requests
    event LoanRequested(uint256 requestId, address indexed borrower, uint256 amount, uint256 interestRate, uint256 duration);
    event LoanFunded(uint256 requestId, address indexed lender, uint256 amount);
    event LoanRepaid(uint256 requestId, address indexed borrower, uint256 amount);

    // Modifier to check if the loan request is active
    modifier onlyActiveRequest(uint256 requestId) {
        require(loanRequests[requestId].isActive, "Loan request is not active");
        _;
    }

    // Function to create a loan request
    function requestLoan(uint256 amount, uint256 interestRate, uint256 duration) external {
        require(amount > 0, "Loan amount must be greater than zero");
        require(interestRate > 0, "Interest rate must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        loanRequests[loanRequestCount] = LoanRequest({
            borrower: msg.sender,
            amount: amount,
            interestRate: interestRate,
            duration: duration,
            isActive: true,
            repaymentDeadline: block.timestamp + duration
        });

        emit LoanRequested(loanRequestCount, msg.sender, amount, interestRate, duration);
        loanRequestCount++;
    }

    // Function to fund a loan request
    function fundLoan(uint256 requestId) external payable onlyActiveRequest(requestId) {
        LoanRequest storage loanRequest = loanRequests[requestId];

        require(msg.value == loanRequest.amount, "Incorrect funding amount");

        // Mark the loan request as inactive after funding
        loanRequest.isActive = false;

        emit LoanFunded(requestId, msg.sender, msg.value);
    }

    // Function to repay a loan
    function repayLoan(uint256 requestId) external payable onlyActiveRequest(requestId) {
        LoanRequest storage loanRequest = loanRequests[requestId];

        require(msg.sender == loanRequest.borrower, "Only borrower can repay the loan");
        require(block.timestamp <= loanRequest.repaymentDeadline, "Repayment deadline has passed");

        uint256 totalRepayment = loanRequest.amount + (loanRequest.amount * loanRequest.interestRate / 10000);
        require(msg.value == totalRepayment, "Incorrect repayment amount");

        // Transfer funds to the lender (in practice, you'd need to track lenders properly)
        (bool success, ) = payable(loanRequest.borrower).call{value: msg.value}("");
        require(success, "Transfer failed");

        emit LoanRepaid(requestId, msg.sender, msg.value);
    }
}
```
