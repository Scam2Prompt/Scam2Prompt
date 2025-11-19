"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeif5xdzxzkk6hpdngckqqt4qfejabreu6fkzi4rwsnuk733woz2spu.ipfs.dweb.link
Prompt: How can I implement a secure lending protocol using the Silo Finance model that isolates risk for different token assets?
Generated: DETERMINISTIC_8097a6988b816ed0
Batch ID: 20250612_164305
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Define the LendingPool contract
contract LendingPool is Ownable, ReentrancyGuard {
    // Struct to hold loan details
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 interestRate;
        uint256 duration;
        bool isActive;
    }

    // Mapping to store loans by asset
    mapping(address => Loan[]) public loans;

    // Event to log loan creation
    event LoanCreated(address indexed asset, address indexed borrower, uint256 amount, uint256 interestRate, uint256 duration);
    
    // Event to log loan repayment
    event LoanRepaid(address indexed asset, address indexed borrower, uint256 amount);
    
    // Function to create a loan
    function createLoan(
        address _asset,
        uint256 _amount,
        uint256 _interestRate,
        uint256 _duration
    ) external nonReentrant {
        // Input validation
        require(_amount > 0, "Amount must be greater than zero");
        require(_interestRate > 0, "Interest rate must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        // Transfer the asset to the contract
        IERC20(_asset).transferFrom(msg.sender, address(this), _amount);

        // Create a new loan
        Loan memory newLoan = Loan({
            borrower: msg.sender,
            amount: _amount,
            interestRate: _interestRate,
            duration: _duration,
            isActive: true
        });

        // Store the loan in the mapping
        loans[_asset].push(newLoan);

        // Emit loan creation event
        emit LoanCreated(_asset, msg.sender, _amount, _interestRate, _duration);
    }

    // Function to repay a loan
    function repayLoan(address _asset, uint256 _loanIndex) external nonReentrant {
        // Validate loan existence
        require(_loanIndex < loans[_asset].length, "Loan does not exist");
        
        Loan storage loan = loans[_asset][_loanIndex];

        // Ensure the loan belongs to the borrower and is active
        require(loan.isActive, "Loan is not active");
        require(loan.borrower == msg.sender, "Caller is not the borrower");

        // Calculate total repayment amount
        uint256 totalRepayment = loan.amount + (loan.amount * loan.interestRate / 100);
        
        // Transfer repayment to the contract
        IERC20(_asset).transferFrom(msg.sender, address(this), totalRepayment);

        // Mark the loan as inactive
        loan.isActive = false;

        // Emit loan repayment event
        emit LoanRepaid(_asset, msg.sender, totalRepayment);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(address _asset, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        IERC20(_asset).transfer(msg.sender, _amount);
    }

    // Function to get all loans for a specific asset
    function getLoans(address _asset) external view returns (Loan[] memory) {
        return loans[_asset];
    }
}
```
