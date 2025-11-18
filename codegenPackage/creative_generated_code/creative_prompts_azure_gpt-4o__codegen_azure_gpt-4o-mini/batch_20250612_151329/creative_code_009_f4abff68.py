"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftcap.pages.dev
Prompt: Create a Solidity function to calculate interest on NFT-backed loans, ensuring compatibility with the permissionless smart contract infrastructure described on NFTfi.com.
Generated: DETERMINISTIC_f4abff68c967fece
Batch ID: 20250612_151329
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

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract NFTLoan {
    // Struct to hold loan information
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 nftId;
        uint256 interestRate; // Interest rate in basis points (1% = 100)
        uint256 duration; // Duration in seconds
        uint256 startTime;
        bool isActive;
    }
    
    // Mapping from loan ID to Loan struct
    mapping(uint256 => Loan) public loans;
    uint256 public nextLoanId = 1; // Counter for loan IDs

    // Event emitted when a loan is created
    event LoanCreated(uint256 loanId, address indexed borrower, uint256 amount, uint256 nftId);

    // Function to create a loan
    function createLoan(uint256 _amount, uint256 _nftId, uint256 _interestRate, uint256 _duration) external {
        require(_amount > 0, "Loan amount must be greater than zero");
        require(_interestRate > 0, "Interest rate must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        // Create new loan
        loans[nextLoanId] = Loan({
            borrower: msg.sender,
            amount: _amount,
            nftId: _nftId,
            interestRate: _interestRate,
            duration: _duration,
            startTime: block.timestamp,
            isActive: true
        });

        emit LoanCreated(nextLoanId, msg.sender, _amount, _nftId);
        
        nextLoanId++;
    }

    // Function to calculate interest for a given loan ID
    function calculateInterest(uint256 _loanId) public view returns (uint256) {
        Loan memory loan = loans[_loanId];
        require(loan.isActive, "Loan is not active");

        // Calculate the elapsed time
        uint256 elapsedTime = block.timestamp - loan.startTime;
        require(elapsedTime <= loan.duration, "Loan duration exceeded");

        // Calculate interest
        uint256 interest = (loan.amount * loan.interestRate * elapsedTime) / (10000 * loan.duration);
        return interest;
    }

    // Function to close the loan
    function closeLoan(uint256 _loanId) external {
        Loan storage loan = loans[_loanId];
        require(loan.isActive, "Loan is not active");
        require(msg.sender == loan.borrower, "Only the borrower can close the loan");

        // Mark loan as inactive
        loan.isActive = false;
    }
}
```
