"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdc.name
Prompt: Generate Solidity code for a smart contract that integrates USDC for DeFi lending and borrowing functionality.
Generated: DETERMINISTIC_b7c864daf755ae66
Batch ID: 20250612_154002
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

/**
 * @title DeFi Lending and Borrowing Contract using USDC
 * @dev This contract allows users to deposit USDC, borrow funds, and repay loans.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
}

contract DeFiLending {
    // USDC token contract address
    IERC20 public usdc;

    // Store user balances for deposits and loans
    mapping(address => uint256) public deposits;
    mapping(address => uint256) public loans;

    // Interest rate for borrowing (e.g., 5% annual rate)
    uint256 public constant BORROW_INTEREST_RATE = 5; // 5% annual
    uint256 public constant INTEREST_DIVISOR = 100; // For percentage calculations

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to certain functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    // Events to track contract activities
    event Deposited(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the USDC token contract and set owner.
     * @param _usdc Address of the USDC token contract
     */
    constructor(address _usdc) {
        require(_usdc != address(0), "Invalid USDC contract address");
        usdc = IERC20(_usdc);
        owner = msg.sender;
    }

    /**
     * @dev Deposit USDC into the contract.
     * @param amount Amount of USDC to deposit
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than 0");

        // Transfer USDC from user to contract
        require(usdc.transferFrom(msg.sender, address(this), amount), "USDC transfer failed");

        // Update user deposit balance
        deposits[msg.sender] += amount;

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Borrow funds based on deposited collateral.
     * @param amount Amount of USDC to borrow
     */
    function borrow(uint256 amount) external {
        require(amount > 0, "Borrow amount must be greater than 0");
        require(deposits[msg.sender] >= amount, "Insufficient collateral");

        // Update loan balance for user
        loans[msg.sender] += amount;

        // Transfer USDC from contract to user
        require(usdc.transfer(msg.sender, amount), "USDC transfer failed");

        emit Borrowed(msg.sender, amount);
    }

    /**
     * @dev Repay borrowed funds.
     * @param amount Amount of USDC to repay
     */
    function repay(uint256 amount) external {
        require(amount > 0, "Repay amount must be greater than 0");
        require(loans[msg.sender] >= amount, "Repay amount exceeds loan balance");

        // Transfer USDC from user to contract
        require(usdc.transferFrom(msg.sender, address(this), amount), "USDC transfer failed");

        // Update loan balance for user
        loans[msg.sender] -= amount;

        emit Repaid(msg.sender, amount);
    }

    /**
     * @dev Calculate interest for a loan based on the BORROW_INTEREST_RATE.
     * @param principal Loan principal amount
     * @param duration Duration of the loan in seconds
     * @return interest Calculated interest amount
     */
    function calculateInterest(uint256 principal, uint256 duration) public pure returns (uint256) {
        // Annual interest rate calculation
        return (principal * BORROW_INTEREST_RATE * duration) / (INTEREST_DIVISOR * 365 days);
    }

    /**
     * @dev Withdraw deposited USDC.
     * @param amount Amount of USDC to withdraw
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than 0");
        require(deposits[msg.sender] >= amount, "Insufficient deposit balance");

        // Update user deposit balance
        deposits[msg.sender] -= amount;

        // Transfer USDC from contract to user
        require(usdc.transfer(msg.sender, amount), "USDC transfer failed");
    }

    /**
     * @dev Emergency withdrawal of all funds by the contract owner.
     * Only callable by the owner.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than 0");
        require(usdc.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer USDC from contract to owner
        require(usdc.transfer(owner, amount), "USDC transfer failed");
    }
}
```
