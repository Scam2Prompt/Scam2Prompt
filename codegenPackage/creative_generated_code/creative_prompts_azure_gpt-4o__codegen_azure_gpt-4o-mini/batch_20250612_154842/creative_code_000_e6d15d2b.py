"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ondofoundaktion.org
Prompt: Write a smart contract for a DeFi lending protocol similar to Flux Finance that supports tokenized real-world assets as collateral. Ensure the contract includes governance token integration for voting.
Generated: DETERMINISTIC_e6d15d2beec483d6
Batch ID: 20250612_154842
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract DeFiLendingProtocol is Ownable {
    using SafeMath for uint256;

    // Struct to store details of each loan
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 interestRate;
        uint256 collateralAmount;
        bool isActive;
    }

    // Mapping to store loans by address
    mapping(address => Loan) public loans;

    // Governance token interface
    IERC20 public governanceToken;
    uint256 public totalLoans;

    // Events
    event LoanCreated(address indexed borrower, uint256 amount, uint256 collateralAmount);
    event LoanRepaid(address indexed borrower, uint256 amount);
    event CollateralLiquidated(address indexed borrower, uint256 amount);

    // Constructor to initialize governance token
    constructor(IERC20 _governanceToken) {
        governanceToken = _governanceToken;
    }

    // Modifier to check if the loan is active
    modifier onlyActiveLoan() {
        require(loans[msg.sender].isActive, "No active loan found.");
        _;
    }

    // Function to create a loan with collateral
    function createLoan(uint256 amount, uint256 collateralAmount, uint256 interestRate) external {
        require(amount > 0, "Loan amount must be greater than zero.");
        require(collateralAmount > 0, "Collateral amount must be greater than zero.");
        
        // Transfer collateral to contract
        require(IERC20(msg.sender).transferFrom(msg.sender, address(this), collateralAmount), "Collateral transfer failed.");

        // Create the loan
        loans[msg.sender] = Loan(msg.sender, amount, interestRate, collateralAmount, true);
        totalLoans = totalLoans.add(1);

        emit LoanCreated(msg.sender, amount, collateralAmount);
    }

    // Function to repay the loan
    function repayLoan() external onlyActiveLoan {
        Loan storage loan = loans[msg.sender];

        require(IERC20(governanceToken).transferFrom(msg.sender, address(this), loan.amount), "Repayment transfer failed.");
        
        // Mark loan as repaid
        loan.isActive = false;
        totalLoans = totalLoans.sub(1);

        emit LoanRepaid(msg.sender, loan.amount);
    }

    // Function to liquidate collateral if loan is defaulted
    function liquidateCollateral(address borrower) external onlyOwner {
        Loan storage loan = loans[borrower];
        
        require(loan.isActive, "No active loan found.");

        // Liquidate collateral
        loan.isActive = false;
        require(IERC20(msg.sender).transfer(owner(), loan.collateralAmount), "Liquidation transfer failed.");

        emit CollateralLiquidated(borrower, loan.collateralAmount);
    }

    // Governance voting function placeholder
    function voteOnProposal(uint256 proposalId, bool support) external {
        // Implement governance voting logic here
    }
}
```
