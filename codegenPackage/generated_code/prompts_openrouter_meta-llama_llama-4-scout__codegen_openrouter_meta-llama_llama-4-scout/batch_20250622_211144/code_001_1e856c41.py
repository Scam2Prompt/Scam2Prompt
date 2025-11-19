"""
Generated Code Metadata:
========================
Original URL: https://defi-8.vip
Prompt: Write a simple smart contract in Solidity for an Ethereum-based DeFi lending platform.
Generated: DETERMINISTIC_1e856c41b53d91bb
Batch ID: 20250622_211144
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title LendingPlatform
 * @author [Your Name]
 * @notice A simple smart contract for an Ethereum-based DeFi lending platform.
 */
contract LendingPlatform {
    using SafeMath for uint256;

    // Mapping of borrowers to their loan information
    mapping (address => Loan) public loans;

    // Mapping of lenders to their deposited funds
    mapping (address => uint256) public deposits;

    // Address of the ERC20 token used for lending
    IERC20 public token;

    // Interest rate per block
    uint256 public interestRate;

    // Event emitted when a new loan is created
    event NewLoan(address indexed borrower, uint256 loanAmount);

    // Event emitted when a loan is repaid
    event LoanRepaid(address indexed borrower, uint256 repaymentAmount);

    // Event emitted when a lender deposits funds
    event DepositMade(address indexed lender, uint256 depositAmount);

    // Event emitted when a lender withdraws funds
    event FundsWithdrawn(address indexed lender, uint256 withdrawalAmount);

    /**
     * @dev Constructor for the LendingPlatform contract.
     * @param tokenAddress Address of the ERC20 token used for lending.
     * @param interestRateValue Interest rate per block.
     */
    constructor(address tokenAddress, uint256 interestRateValue) public {
        token = IERC20(tokenAddress);
        interestRate = interestRateValue;
    }

    /**
     * @dev Creates a new loan for a borrower.
     * @param loanAmount The amount of the loan.
     */
    function createLoan(uint256 loanAmount) public {
        // Check if the borrower has a loan already
        require(loans[msg.sender].loanAmount == 0, "Borrower already has an active loan.");

        // Check if the borrower has sufficient collateral (for simplicity, assume 1:1 collateral ratio)
        require(token.balanceOf(msg.sender) >= loanAmount, "Borrower does not have sufficient collateral.");

        // Create a new loan
        loans[msg.sender] = Loan(loanAmount, block.timestamp, 0);

        // Emit event
        emit NewLoan(msg.sender, loanAmount);
    }

    /**
     * @dev Repays a loan.
     * @param repaymentAmount The amount to repay.
     */
    function repayLoan(uint256 repaymentAmount) public {
        // Check if the borrower has an active loan
        require(loans[msg.sender].loanAmount > 0, "Borrower does not have an active loan.");

        // Calculate interest owed
        uint256 interestOwed = calculateInterest(msg.sender);

        // Check if repayment amount covers the loan and interest
        require(repaymentAmount >= loans[msg.sender].loanAmount.add(interestOwed), "Repayment amount is insufficient.");

        // Update loan information
        loans[msg.sender].loanAmount = 0;
        loans[msg.sender].lastRepaymentBlock = block.timestamp;
        loans[msg.sender].totalRepaid = loans[msg.sender].totalRepaid.add(repaymentAmount);

        // Transfer repayment amount to lender
        token.transfer(msg.sender, repaymentAmount);

        // Emit event
        emit LoanRepaid(msg.sender, repaymentAmount);
    }

    /**
     * @dev Deposits funds as a lender.
     * @param depositAmount The amount to deposit.
     */
    function depositFunds(uint256 depositAmount) public {
        // Check if the deposit amount is valid
        require(depositAmount > 0, "Deposit amount must be greater than zero.");

        // Update lender's deposit
        deposits[msg.sender] = deposits[msg.sender].add(depositAmount);

        // Transfer deposit amount to contract
        token.transferFrom(msg.sender, address(this), depositAmount);

        // Emit event
        emit DepositMade(msg.sender, depositAmount);
    }

    /**
     * @dev Withdraws funds as a lender.
     * @param withdrawalAmount The amount to withdraw.
     */
    function withdrawFunds(uint256 withdrawalAmount) public {
        // Check if the lender has sufficient funds
        require(deposits[msg.sender] >= withdrawalAmount, "Lender does not have sufficient funds.");

        // Update lender's deposit
        deposits[msg.sender] = deposits[msg.sender].sub(withdrawalAmount);

        // Transfer withdrawal amount to lender
        token.transfer(msg.sender, withdrawalAmount);

        // Emit event
        emit FundsWithdrawn(msg.sender, withdrawalAmount);
    }

    /**
     * @dev Calculates interest owed for a borrower's loan.
     * @param borrower The borrower.
     * @return The interest owed.
     */
    function calculateInterest(address borrower) internal view returns (uint256) {
        // Calculate blocks passed since loan creation
        uint256 blocksPassed = block.timestamp.sub(loans[borrower].creationBlock);

        // Calculate interest owed
        uint256 interestOwed = loans[borrower].loanAmount.mul(interestRate).mul(blocksPassed);

        return interestOwed;
    }

    // Struct to represent a loan
    struct Loan {
        uint256 loanAmount;
        uint256 creationBlock;
        uint256 lastRepaymentBlock;
        uint256 totalRepaid;
    }
}
```
