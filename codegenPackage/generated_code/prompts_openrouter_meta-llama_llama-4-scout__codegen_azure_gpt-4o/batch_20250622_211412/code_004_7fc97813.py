"""
Generated Code Metadata:
========================
Original URL: https://ercsz.com
Prompt: "Design a basic DeFi lending platform using ERC-20 tokens and smart contracts on Ethereum."
Generated: DETERMINISTIC_7fc97813c68a655f
Batch ID: 20250622_211412
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

/**
 * @title DeFi Lending Platform
 * @dev A basic decentralized finance (DeFi) lending platform using ERC-20 tokens.
 * Users can deposit ERC-20 tokens, borrow against their collateral, and repay loans.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract DeFiLendingPlatform {
    // Struct to store user balances
    struct User {
        uint256 collateralBalance; // Collateral deposited by the user
        uint256 loanBalance;       // Loan taken by the user
    }

    // Mapping of user addresses to their balances
    mapping(address => User) public users;

    // ERC-20 token used for collateral and loans
    IERC20 public token;

    // Interest rate for loans (e.g., 5% annual interest rate)
    uint256 public interestRate = 5;

    // Owner of the contract
    address public owner;

    // Events
    event CollateralDeposited(address indexed user, uint256 amount);
    event LoanTaken(address indexed user, uint256 amount);
    event LoanRepaid(address indexed user, uint256 amount);
    event CollateralWithdrawn(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to initialize the contract
    constructor(IERC20 _token) {
        token = _token;
        owner = msg.sender;
    }

    /**
     * @dev Deposit collateral into the platform.
     * @param amount The amount of tokens to deposit.
     */
    function depositCollateral(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user collateral balance
        users[msg.sender].collateralBalance += amount;

        emit CollateralDeposited(msg.sender, amount);
    }

    /**
     * @dev Take a loan against the deposited collateral.
     * @param amount The amount of tokens to borrow.
     */
    function takeLoan(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Ensure the user has enough collateral to borrow
        uint256 maxLoanAmount = users[msg.sender].collateralBalance / 2; // 50% collateralization ratio
        require(amount <= maxLoanAmount, "Insufficient collateral");

        // Update user loan balance
        users[msg.sender].loanBalance += amount;

        // Transfer loan tokens to the user
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit LoanTaken(msg.sender, amount);
    }

    /**
     * @dev Repay a loan.
     * @param amount The amount of tokens to repay.
     */
    function repayLoan(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(users[msg.sender].loanBalance >= amount, "Repayment amount exceeds loan balance");

        // Transfer tokens from the user to the contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user loan balance
        users[msg.sender].loanBalance -= amount;

        emit LoanRepaid(msg.sender, amount);
    }

    /**
     * @dev Withdraw collateral after repaying the loan.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawCollateral(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(users[msg.sender].collateralBalance >= amount, "Insufficient collateral");
        require(users[msg.sender].loanBalance == 0, "Loan must be repaid before withdrawing collateral");

        // Update user collateral balance
        users[msg.sender].collateralBalance -= amount;

        // Transfer tokens back to the user
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit CollateralWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Update the interest rate (only owner can call this function).
     * @param newRate The new interest rate (in percentage).
     */
    function updateInterestRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Interest rate must be greater than zero");
        interestRate = newRate;
    }

    /**
     * @dev Get the user's collateral and loan balances.
     * @param user The address of the user.
     * @return collateralBalance The collateral balance of the user.
     * @return loanBalance The loan balance of the user.
     */
    function getUserBalances(address user) external view returns (uint256 collateralBalance, uint256 loanBalance) {
        collateralBalance = users[user].collateralBalance;
        loanBalance = users[user].loanBalance;
    }
}
```
