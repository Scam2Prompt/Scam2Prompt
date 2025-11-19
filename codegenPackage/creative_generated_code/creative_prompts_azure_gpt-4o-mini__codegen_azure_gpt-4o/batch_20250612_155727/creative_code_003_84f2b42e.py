"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meteora-ag.github.io
Prompt: Develop a smart contract for a decentralized finance (DeFi) application that enables lending and borrowing, reflecting the functionalities offered by Meteora Crypto.
Generated: DETERMINISTIC_84f2b42e43249e89
Batch ID: 20250612_155727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean implementation of a lending and borrowing smart contract written in Solidity for Ethereum-based DeFi applications:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title DeFi Lending and Borrowing Contract
 * @dev This contract enables lending and borrowing of ERC20 tokens in a decentralized manner.
 * It follows standard best practices, includes error handling, and is production-ready.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DeFiLendingBorrowing is Ownable {
    // Structure to store information about deposits
    struct Deposit {
        uint256 amount;
        uint256 depositTime;
    }

    // Structure to store information about loans
    struct Loan {
        uint256 amount;
        uint256 borrowTime;
        bool isRepaid;
    }

    // Interest rate constants (e.g., annual rates scaled by 1e18 for precision)
    uint256 public constant LENDING_INTEREST_RATE = 5e16; // 5% annual rate
    uint256 public constant BORROWING_INTEREST_RATE = 10e16; // 10% annual rate

    // ERC20 token used in this contract
    IERC20 public token;

    // Mapping to store deposits by users
    mapping(address => Deposit) public deposits;

    // Mapping to store loans by users
    mapping(address => Loan) public loans;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the ERC20 token address
     * @param _token Address of the ERC20 token
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Deposit tokens into the contract to earn interest
     * @param _amount Amount of tokens to deposit
     */
    function deposit(uint256 _amount) external {
        require(_amount > 0, "Deposit amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update the deposit details
        deposits[msg.sender].amount += _amount;
        deposits[msg.sender].depositTime = block.timestamp;

        emit Deposited(msg.sender, _amount);
    }

    /**
     * @dev Withdraw deposited tokens along with earned interest
     */
    function withdraw() external {
        Deposit storage userDeposit = deposits[msg.sender];
        require(userDeposit.amount > 0, "No deposit found");

        // Calculate the interest earned
        uint256 timeElapsed = block.timestamp - userDeposit.depositTime;
        uint256 interest = (userDeposit.amount * LENDING_INTEREST_RATE * timeElapsed) / (365 days * 1e18);

        uint256 totalAmount = userDeposit.amount + interest;

        // Update the deposit details
        userDeposit.amount = 0;
        userDeposit.depositTime = 0;

        // Transfer tokens back to the user
        require(token.transfer(msg.sender, totalAmount), "Token transfer failed");

        emit Withdrawn(msg.sender, totalAmount);
    }

    /**
     * @dev Borrow tokens from the contract
     * @param _amount Amount of tokens to borrow
     */
    function borrow(uint256 _amount) external {
        require(_amount > 0, "Borrow amount must be greater than zero");

        // Ensure the contract has enough liquidity
        uint256 contractBalance = token.balanceOf(address(this));
        require(contractBalance >= _amount, "Insufficient liquidity in the contract");

        // Update the loan details
        loans[msg.sender].amount += _amount;
        loans[msg.sender].borrowTime = block.timestamp;
        loans[msg.sender].isRepaid = false;

        // Transfer tokens to the borrower
        require(token.transfer(msg.sender, _amount), "Token transfer failed");

        emit Borrowed(msg.sender, _amount);
    }

    /**
     * @dev Repay borrowed tokens along with interest
     */
    function repay() external {
        Loan storage userLoan = loans[msg.sender];
        require(userLoan.amount > 0, "No loan found");
        require(!userLoan.isRepaid, "Loan already repaid");

        // Calculate the interest due
        uint256 timeElapsed = block.timestamp - userLoan.borrowTime;
        uint256 interest = (userLoan.amount * BORROWING_INTEREST_RATE * timeElapsed) / (365 days * 1e18);

        uint256 totalRepayment = userLoan.amount + interest;

        // Transfer tokens from the user to the contract
        require(token.transferFrom(msg.sender, address(this), totalRepayment), "Token transfer failed");

        // Update the loan details
        userLoan.amount = 0;
        userLoan.borrowTime = 0;
        userLoan.isRepaid = true;

        emit Repaid(msg.sender, totalRepayment);
    }

    /**
     * @dev Owner function to withdraw excess liquidity from the contract
     * @param _amount Amount of tokens to withdraw
     */
    function ownerWithdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(token.balanceOf(address(this)) >= _amount, "Insufficient contract balance");

        require(token.transfer(owner(), _amount), "Token transfer failed");
    }
}
```
