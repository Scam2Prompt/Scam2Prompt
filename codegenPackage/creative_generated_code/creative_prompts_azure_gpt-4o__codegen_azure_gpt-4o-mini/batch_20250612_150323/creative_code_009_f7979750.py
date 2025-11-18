"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea-web3.pages.dev
Prompt: Create a smart contract for a decentralized finance (DeFi) application on Linea, ensuring compatibility with its zkEVM infrastructure and security standards.
Generated: DETERMINISTIC_f7979750347b4f5b
Batch ID: 20250612_150323
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for a simple DeFi lending protocol
contract DeFiLending is Ownable {
    using SafeMath for uint256;

    // Struct to hold information for each loan
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 interestRate; // Interest rate in basis points (1/100 of a percent)
        uint256 dueDate;
        bool repaid;
    }

    // Mapping to store loans by their unique identifier
    mapping(uint256 => Loan) public loans;
    uint256 public loanCount;

    IERC20 public stablecoin; // ERC20 token used for lending

    // Event emitted when a new loan is created
    event LoanCreated(uint256 indexed loanId, address borrower, uint256 amount, uint256 interestRate, uint256 dueDate);
    
    // Event emitted when a loan is repaid
    event LoanRepaid(uint256 indexed loanId);

    // Constructor to initialize the stablecoin
    constructor(address _stablecoin) {
        require(_stablecoin != address(0), "Invalid stablecoin address");
        stablecoin = IERC20(_stablecoin);
    }

    // Function to create a new loan
    function createLoan(uint256 amount, uint256 interestRate, uint256 duration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(interestRate > 0, "Interest rate must be greater than zero");
        require(duration > 0, "Loan duration must be greater than zero");

        // Transfer stablecoins from borrower to the contract
        stablecoin.transferFrom(msg.sender, address(this), amount);

        // Create a new loan
        loans[loanCount] = Loan({
            borrower: msg.sender,
            amount: amount,
            interestRate: interestRate,
            dueDate: block.timestamp.add(duration),
            repaid: false
        });

        emit LoanCreated(loanCount, msg.sender, amount, interestRate, block.timestamp.add(duration));
        loanCount++;
    }

    // Function to repay a loan
    function repayLoan(uint256 loanId) external {
        Loan storage loan = loans[loanId];

        // Validate the loan details
        require(loan.borrower == msg.sender, "Only borrower can repay the loan");
        require(!loan.repaid, "Loan already repaid");
        require(block.timestamp <= loan.dueDate, "Loan is overdue");

        // Calculate total repayment amount including interest
        uint256 totalRepayment = loan.amount.add(loan.amount.mul(loan.interestRate).div(10000));

        // Transfer stablecoins from borrower to the contract
        stablecoin.transferFrom(msg.sender, address(this), totalRepayment);

        // Mark loan as repaid
        loan.repaid = true;

        emit LoanRepaid(loanId);
    }

    // Function to withdraw stablecoins from the contract (only owner)
    function withdrawStablecoins(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(stablecoin.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer the specified amount of stablecoins to the owner
        stablecoin.transfer(msg.sender, amount);
    }

    // Function to get loan details
    function getLoanDetails(uint256 loanId) external view returns (Loan memory) {
        return loans[loanId];
    }
}
```
