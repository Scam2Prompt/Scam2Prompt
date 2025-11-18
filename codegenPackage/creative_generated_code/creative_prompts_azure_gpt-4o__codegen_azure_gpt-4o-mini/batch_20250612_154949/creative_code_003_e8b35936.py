"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chaindapps.pages.dev
Prompt: Create a dApp prototype that integrates blockchain protocols to solve DeFi-related problems, referencing the features discussed on Decentralised Connect.
Generated: DETERMINISTIC_e8b359364c1b8bf9
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import necessary libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// A simple DeFi protocol for lending and borrowing ERC20 tokens
contract DeFiLending is Ownable {
    // Struct to hold loan information
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 interestRate; // in basis points (1% = 100)
        uint256 duration; // loan duration in seconds
        uint256 startTime;
        bool isActive;
    }

    // Events for logging actions
    event LoanCreated(uint256 loanId, address indexed borrower, uint256 amount, uint256 duration);
    event LoanRepaid(uint256 loanId, address indexed borrower, uint256 amount);
    event LoanDefaulted(uint256 loanId, address indexed borrower);

    // Mapping of loan IDs to Loan structs
    mapping(uint256 => Loan) public loans;
    uint256 public loanCounter; // to keep track of loan IDs

    // ERC20 token used for lending
    IERC20 public token;

    // Constructor to set the token address
    constructor(address _tokenAddress) {
        token = IERC20(_tokenAddress);
    }

    // Function to create a new loan
    function createLoan(uint256 amount, uint256 interestRate, uint256 duration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        loanCounter++;
        loans[loanCounter] = Loan({
            borrower: msg.sender,
            amount: amount,
            interestRate: interestRate,
            duration: duration,
            startTime: block.timestamp,
            isActive: true
        });

        emit LoanCreated(loanCounter, msg.sender, amount, duration);
    }

    // Function to repay the loan
    function repayLoan(uint256 loanId) external {
        Loan storage loan = loans[loanId];
        require(loan.isActive, "Loan is not active");
        require(loan.borrower == msg.sender, "Only borrower can repay the loan");

        uint256 interest = (loan.amount * loan.interestRate * (block.timestamp - loan.startTime)) / (10000 * loan.duration);
        uint256 totalRepayment = loan.amount + interest;

        require(token.transferFrom(msg.sender, address(this), totalRepayment), "Token transfer failed");

        loan.isActive = false; // Mark loan as repaid

        emit LoanRepaid(loanId, msg.sender, totalRepayment);
    }

    // Function to check for loan defaults
    function checkForDefault(uint256 loanId) external {
        Loan storage loan = loans[loanId];
        require(loan.isActive, "Loan is not active");
        require(block.timestamp >= loan.startTime + loan.duration, "Loan is not defaulted yet");

        loan.isActive = false; // Mark loan as defaulted

        emit LoanDefaulted(loanId, loan.borrower);
    }
}
```

### Instructions:
1. Deploy this contract to a blockchain that supports Solidity (e.g., Ethereum).
2. Ensure that your contract is tested adequately before deploying to a main network to avoid any loss of funds.
3. Integrate with a front-end application as needed to create a complete dApp experience for users.
