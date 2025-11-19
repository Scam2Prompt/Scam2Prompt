"""
Generated Code Metadata:
========================
Original URL: https://borroefinnance.web.app
Prompt: "Design a smart contract for a peer-to-peer lending platform that utilizes tokenization and AI-powered risk assessment, similar to Borroe Finance."
Generated: DETERMINISTIC_78735be0823d34a9
Batch ID: 20250622_210316
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

// Importing OpenZeppelin's ERC20 token implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the AI risk assessment service
interface IRiskAssessment {
    function assessRisk(address borrower) external view returns (uint256);
}

// Peer-to-Peer Lending Smart Contract
contract PeerToPeerLending is Ownable {
    // Token used for lending
    ERC20 public lendingToken;
    IRiskAssessment public riskAssessmentService;

    // Struct to represent a loan
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 interestRate; // in basis points (1% = 100 basis points)
        uint256 duration; // in seconds
        uint256 startTime;
        bool isRepaid;
    }

    // Mapping to store loans by ID
    mapping(uint256 => Loan) public loans;
    uint256 public loanCounter;

    // Event emitted when a loan is created
    event LoanCreated(uint256 loanId, address indexed borrower, uint256 amount, uint256 interestRate, uint256 duration);
    
    // Event emitted when a loan is repaid
    event LoanRepaid(uint256 loanId, address indexed borrower);

    // Constructor to initialize the lending token and risk assessment service
    constructor(ERC20 _lendingToken, IRiskAssessment _riskAssessmentService) {
        lendingToken = _lendingToken;
        riskAssessmentService = _riskAssessmentService;
    }

    // Function to create a new loan
    function createLoan(uint256 amount, uint256 interestRate, uint256 duration) external {
        require(amount > 0, "Loan amount must be greater than zero");
        require(interestRate > 0, "Interest rate must be greater than zero");
        require(duration > 0, "Loan duration must be greater than zero");

        // Assess the risk of the borrower
        uint256 riskScore = riskAssessmentService.assessRisk(msg.sender);
        require(riskScore < 500, "Borrower risk is too high"); // Example threshold

        // Transfer tokens from the lender to the borrower
        lendingToken.transferFrom(msg.sender, address(this), amount);

        // Create the loan
        loans[loanCounter] = Loan({
            borrower: msg.sender,
            amount: amount,
            interestRate: interestRate,
            duration: duration,
            startTime: block.timestamp,
            isRepaid: false
        });

        emit LoanCreated(loanCounter, msg.sender, amount, interestRate, duration);
        loanCounter++;
    }

    // Function to repay a loan
    function repayLoan(uint256 loanId) external {
        Loan storage loan = loans[loanId];
        require(loan.borrower == msg.sender, "Only the borrower can repay the loan");
        require(!loan.isRepaid, "Loan has already been repaid");
        require(block.timestamp <= loan.startTime + loan.duration, "Loan duration has expired");

        // Calculate total repayment amount
        uint256 totalRepayment = loan.amount + (loan.amount * loan.interestRate) / 10000; // Convert basis points to percentage

        // Transfer tokens from the borrower to the contract
        lendingToken.transferFrom(msg.sender, address(this), totalRepayment);

        // Mark the loan as repaid
        loan.isRepaid = true;

        emit LoanRepaid(loanId, msg.sender);
    }

    // Function to withdraw funds by the owner (for example, after all loans are repaid)
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(lendingToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        lendingToken.transfer(msg.sender, amount);
    }
}
```
