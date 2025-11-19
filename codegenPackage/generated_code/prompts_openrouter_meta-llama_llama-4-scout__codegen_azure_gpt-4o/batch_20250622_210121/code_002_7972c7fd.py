"""
Generated Code Metadata:
========================
Original URL: https://retik-com.pages.dev
Prompt: "Generate a smart contract code for a simple peer-to-peer lending platform using AI-powered decision-making, inspired by Retik Finance's lending solutions."
Generated: DETERMINISTIC_7972c7fd9bbb57f7
Batch ID: 20250622_210121
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
 * @dev A simple peer-to-peer lending platform with AI-powered decision-making.
 * Inspired by Retik Finance's lending solutions.
 */
contract PeerToPeerLending {
    // Struct to represent a loan request
    struct LoanRequest {
        uint256 amount; // Loan amount requested
        uint256 interestRate; // Interest rate (in basis points, e.g., 500 = 5%)
        uint256 duration; // Loan duration in seconds
        address borrower; // Address of the borrower
        bool approved; // Whether the loan is approved
        bool repaid; // Whether the loan is repaid
    }

    // Mapping to store loan requests
    mapping(uint256 => LoanRequest) public loanRequests;

    // Mapping to store lenders' balances
    mapping(address => uint256) public lenderBalances;

    // Counter for loan request IDs
    uint256 public loanRequestCounter;

    // Address of the AI decision-making oracle
    address public aiOracle;

    // Events
    event LoanRequested(uint256 indexed loanId, address indexed borrower, uint256 amount, uint256 interestRate, uint256 duration);
    event LoanApproved(uint256 indexed loanId, address indexed borrower);
    event LoanFunded(uint256 indexed loanId, address indexed lender);
    event LoanRepaid(uint256 indexed loanId, address indexed borrower);

    // Modifier to restrict access to the AI oracle
    modifier onlyAIOracle() {
        require(msg.sender == aiOracle, "Only AI oracle can perform this action");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _aiOracle) {
        require(_aiOracle != address(0), "AI oracle address cannot be zero");
        aiOracle = _aiOracle;
    }

    /**
     * @dev Allows a borrower to request a loan.
     * @param _amount The loan amount requested.
     * @param _interestRate The interest rate (in basis points).
     * @param _duration The loan duration in seconds.
     */
    function requestLoan(uint256 _amount, uint256 _interestRate, uint256 _duration) external {
        require(_amount > 0, "Loan amount must be greater than zero");
        require(_interestRate > 0, "Interest rate must be greater than zero");
        require(_duration > 0, "Loan duration must be greater than zero");

        loanRequestCounter++;
        loanRequests[loanRequestCounter] = LoanRequest({
            amount: _amount,
            interestRate: _interestRate,
            duration: _duration,
            borrower: msg.sender,
            approved: false,
            repaid: false
        });

        emit LoanRequested(loanRequestCounter, msg.sender, _amount, _interestRate, _duration);
    }

    /**
     * @dev Allows the AI oracle to approve a loan request.
     * @param _loanId The ID of the loan request to approve.
     */
    function approveLoan(uint256 _loanId) external onlyAIOracle {
        LoanRequest storage loan = loanRequests[_loanId];
        require(loan.borrower != address(0), "Loan request does not exist");
        require(!loan.approved, "Loan is already approved");

        loan.approved = true;

        emit LoanApproved(_loanId, loan.borrower);
    }

    /**
     * @dev Allows a lender to fund an approved loan request.
     * @param _loanId The ID of the loan request to fund.
     */
    function fundLoan(uint256 _loanId) external payable {
        LoanRequest storage loan = loanRequests[_loanId];
        require(loan.borrower != address(0), "Loan request does not exist");
        require(loan.approved, "Loan is not approved");
        require(!loan.repaid, "Loan is already repaid");
        require(msg.value == loan.amount, "Incorrect funding amount");

        lenderBalances[msg.sender] += msg.value;
        payable(loan.borrower).transfer(msg.value);

        emit LoanFunded(_loanId, msg.sender);
    }

    /**
     * @dev Allows a borrower to repay a loan.
     * @param _loanId The ID of the loan to repay.
     */
    function repayLoan(uint256 _loanId) external payable {
        LoanRequest storage loan = loanRequests[_loanId];
        require(loan.borrower == msg.sender, "Only the borrower can repay the loan");
        require(loan.approved, "Loan is not approved");
        require(!loan.repaid, "Loan is already repaid");

        uint256 repaymentAmount = loan.amount + (loan.amount * loan.interestRate / 10000);
        require(msg.value == repaymentAmount, "Incorrect repayment amount");

        loan.repaid = true;

        emit LoanRepaid(_loanId, msg.sender);
    }

    /**
     * @dev Allows the contract owner to update the AI oracle address.
     * @param _newAIOracle The new AI oracle address.
     */
    function updateAIOracle(address _newAIOracle) external {
        require(msg.sender == aiOracle, "Only the current AI oracle can update the address");
        require(_newAIOracle != address(0), "AI oracle address cannot be zero");
        aiOracle = _newAIOracle;
    }
}
```
