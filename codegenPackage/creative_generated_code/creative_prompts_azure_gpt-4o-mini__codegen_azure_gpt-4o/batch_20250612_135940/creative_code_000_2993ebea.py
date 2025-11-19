"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defiethereum.com
Prompt: Write a smart contract in Solidity for a decentralized lending platform on Ethereum.
Generated: DETERMINISTIC_2993ebeae66cd860
Batch ID: 20250612_135940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title Decentralized Lending Platform
 * @dev A smart contract for borrowing and lending ERC20 tokens on Ethereum blockchain.
 */
contract LendingPlatform {
    // Struct to represent a loan
    struct Loan {
        uint256 amount;        // Loan amount in tokens
        uint256 interestRate;  // Annual interest rate (in percentage, e.g., 5 for 5%)
        uint256 duration;      // Loan duration in seconds
        address borrower;      // Address of the borrower
        bool isRepaid;         // Status of loan repayment
    }

    // Mapping to store loans (loanId => Loan)
    mapping(uint256 => Loan) public loans;

    // Token address used for lending and borrowing
    address public immutable tokenAddress;

    // Unique ID for loans
    uint256 public loanCounter;

    // Events
    event LoanCreated(uint256 loanId, address borrower, uint256 amount, uint256 interestRate, uint256 duration);
    event LoanRepaid(uint256 loanId, address borrower);

    // Constructor to initialize the token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
    }

    /**
     * @notice Creates a new loan.
     * @param _amount Loan amount in tokens.
     * @param _interestRate Annual interest rate (percentage).
     * @param _duration Loan duration in seconds.
     */
    function createLoan(uint256 _amount, uint256 _interestRate, uint256 _duration) external {
        require(_amount > 0, "Loan amount must be greater than zero");
        require(_interestRate > 0, "Interest rate must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        // Increment loan ID
        loanCounter++;

        // Create a new loan
        loans[loanCounter] = Loan({
            amount: _amount,
            interestRate: _interestRate,
            duration: _duration,
            borrower: msg.sender,
            isRepaid: false
        });

        // Emit event
        emit LoanCreated(loanCounter, msg.sender, _amount, _interestRate, _duration);

        // Transfer tokens from borrower to contract
        require(
            IERC20(tokenAddress).transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );
    }

    /**
     * @notice Repays an existing loan.
     * @param _loanId ID of the loan to repay.
     */
    function repayLoan(uint256 _loanId) external {
        Loan storage loan = loans[_loanId];

        require(loan.borrower == msg.sender, "Only the borrower can repay the loan");
        require(!loan.isRepaid, "Loan is already repaid");

        // Calculate repayment amount (principal + interest)
        uint256 repaymentAmount = loan.amount + ((loan.amount * loan.interestRate * loan.duration) / (365 days * 100));

        // Mark the loan as repaid
        loan.isRepaid = true;

        // Emit event
        emit LoanRepaid(_loanId, msg.sender);

        // Transfer tokens from borrower to contract
        require(
            IERC20(tokenAddress).transferFrom(msg.sender, address(this), repaymentAmount),
            "Token transfer failed"
        );
    }

    /**
     * @notice Withdraws tokens from contract balance.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(
            IERC20(tokenAddress).balanceOf(address(this)) >= _amount,
            "Insufficient contract balance"
        );

        // Transfer tokens to caller
        require(
            IERC20(tokenAddress).transfer(msg.sender, _amount),
            "Token transfer failed"
        );
    }
}

// Interface for interaction with ERC20 token contract
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
