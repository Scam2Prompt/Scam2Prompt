"""
Generated Code Metadata:
========================
Original URL: https://www.zkfinance.org
Prompt: Generate a smart contract code in Solidity for a lending market on zkSync, incorporating prime assets, Chainlink and DIA oracles for price accuracy, and a decentralized and verifiable protocol.
Generated: DETERMINISTIC_0b4a6debfd30176f
Batch ID: 20250622_210923
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

// LendingMarket contract for managing lending and borrowing of prime assets
contract LendingMarket is Ownable {
    // Struct to hold loan details
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 interestRate; // in basis points (1% = 100 basis points)
        uint256 duration; // in seconds
        uint256 startTime;
        bool isActive;
    }

    // Mapping to store loans by ID
    mapping(uint256 => Loan) public loans;
    uint256 public loanCounter;

    // Oracles for price feeds
    AggregatorV3Interface internal priceFeed;

    // Events for logging
    event LoanCreated(uint256 loanId, address borrower, uint256 amount, uint256 interestRate, uint256 duration);
    event LoanRepaid(uint256 loanId, address borrower);

    // Constructor to initialize the price feed
    constructor(address _priceFeed) {
        priceFeed = AggregatorV3Interface(_priceFeed);
    }

    // Function to create a new loan
    function createLoan(uint256 _amount, uint256 _interestRate, uint256 _duration) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_interestRate > 0, "Interest rate must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        // Create a new loan
        loans[loanCounter] = Loan({
            borrower: msg.sender,
            amount: _amount,
            interestRate: _interestRate,
            duration: _duration,
            startTime: block.timestamp,
            isActive: true
        });

        emit LoanCreated(loanCounter, msg.sender, _amount, _interestRate, _duration);
        loanCounter++;
    }

    // Function to repay a loan
    function repayLoan(uint256 _loanId) external {
        Loan storage loan = loans[_loanId];
        require(loan.isActive, "Loan is not active");
        require(loan.borrower == msg.sender, "Only the borrower can repay the loan");
        require(block.timestamp <= loan.startTime + loan.duration, "Loan duration has expired");

        // Calculate total repayment amount
        uint256 totalRepayment = loan.amount + (loan.amount * loan.interestRate) / 10000; // Convert basis points to percentage

        // Transfer the repayment amount from borrower to the contract
        require(IERC20(address(this)).transferFrom(msg.sender, address(this), totalRepayment), "Transfer failed");

        // Mark loan as repaid
        loan.isActive = false;

        emit LoanRepaid(_loanId, msg.sender);
    }

    // Function to get the latest price from the oracle
    function getLatestPrice() public view returns (int) {
        (
            , 
            int price, 
            , 
            , 
        ) = priceFeed.latestRoundData();
        return price;
    }

    // Function to withdraw funds (only owner)
    function withdrawFunds(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(IERC20(address(this)).balanceOf(address(this)) >= _amount, "Insufficient balance");

        // Transfer the specified amount to the owner
        require(IERC20(address(this)).transfer(msg.sender, _amount), "Transfer failed");
    }
}
```
