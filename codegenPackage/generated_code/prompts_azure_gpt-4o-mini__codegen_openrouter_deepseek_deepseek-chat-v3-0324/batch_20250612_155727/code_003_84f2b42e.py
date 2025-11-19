"""
Generated Code Metadata:
========================
Original URL: https://meteora-ag.github.io
Prompt: Develop a smart contract for a decentralized finance (DeFi) application that enables lending and borrowing, reflecting the functionalities offered by Meteora Crypto.
Generated: DETERMINISTIC_84f2b42e43249e89
Batch ID: 20250612_155727
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract DeFiLending is ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to store user's deposit information
    struct Deposit {
        uint256 amount;
        uint256 timestamp;
    }

    // Struct to store loan information
    struct Loan {
        uint256 amount;
        uint256 collateral;
        uint256 startTime;
        uint256 interestRate;
        bool isActive;
    }

    // Token contract address
    IERC20 public token;

    // Interest rate parameters
    uint256 public baseInterestRate;
    uint256 public interestRateMultiplier;

    // Collateral ratio (e.g., 150% = 150)
    uint256 public collateralRatio;

    // Mapping of user addresses to their deposits
    mapping(address => Deposit) public deposits;

    // Mapping of user addresses to their loans
    mapping(address => Loan) public loans;

    // Total deposited amount
    uint256 public totalDeposits;

    // Total borrowed amount
    uint256 public totalBorrowed;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount, uint256 collateral);
    event Repaid(address indexed user, uint256 amount);
    event Liquidated(address indexed user, address indexed liquidator, uint256 amount);

    constructor(
        address _tokenAddress,
        uint256 _baseInterestRate,
        uint256 _interestRateMultiplier,
        uint256 _collateralRatio
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_collateralRatio >= 100, "Collateral ratio too low");

        token = IERC20(_tokenAddress);
        baseInterestRate = _baseInterestRate;
        interestRateMultiplier = _interestRateMultiplier;
        collateralRatio = _collateralRatio;
    }

    /**
     * @dev Deposit tokens into the lending pool
     * @param amount Amount of tokens to deposit
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens from user to contract
        bool success = token.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update user's deposit
        deposits[msg.sender].amount = deposits[msg.sender].amount.add(amount);
        deposits[msg.sender].timestamp = block.timestamp;

        // Update total deposits
        totalDeposits = totalDeposits.add(amount);

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw tokens from the lending pool
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(deposits[msg.sender].amount >= amount, "Insufficient balance");

        // Check if user has active loans
        require(!loans[msg.sender].isActive, "Active loan exists");

        // Update user's deposit
        deposits[msg.sender].amount = deposits[msg.sender].amount.sub(amount);

        // Update total deposits
        totalDeposits = totalDeposits.sub(amount);

        // Transfer tokens to user
        bool success = token.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Borrow tokens from the lending pool
     * @param amount Amount of tokens to borrow
     * @param collateral Amount of collateral provided
     */
    function borrow(uint256 amount, uint256 collateral) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(collateral >= amount.mul(collateralRatio).div(100), "Insufficient collateral");
        require(!loans[msg.sender].isActive, "Active loan exists");

        // Calculate interest rate based on utilization
        uint256 utilization = totalBorrowed.mul(100).div(totalDeposits);
        uint256 interestRate = baseInterestRate.add(utilization.mul(interestRateMultiplier).div(100));

        // Create new loan
        loans[msg.sender] = Loan({
            amount: amount,
            collateral: collateral,
            startTime: block.timestamp,
            interestRate: interestRate,
            isActive: true
        });

        // Update total borrowed
        totalBorrowed = totalBorrowed.add(amount);

        // Transfer borrowed tokens to user
        bool success = token.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit Borrowed(msg.sender, amount, collateral);
    }

    /**
     * @dev Repay a loan
     * @param amount Amount of tokens to repay
     */
    function repay(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(loans[msg.sender].isActive, "No active loan");

        Loan storage loan = loans[msg.sender];

        // Calculate interest
        uint256 timeElapsed = block.timestamp.sub(loan.startTime);
        uint256 interest = loan.amount.mul(loan.interestRate).mul(timeElapsed).div(365 days).div(100);

        uint256 totalRepayment = loan.amount.add(interest);
        require(amount <= totalRepayment, "Amount exceeds repayment");

        // Transfer repayment from user to contract
        bool success = token.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update loan status
        if (amount == totalRepayment) {
            loan.isActive = false;
            totalBorrowed = totalBorrowed.sub(loan.amount);
            emit Repaid(msg.sender, amount);
        } else {
            loan.amount = totalRepayment.sub(amount);
            loan.startTime = block.timestamp;
            emit Repaid(msg.sender, amount);
        }
    }

    /**
     * @dev Liquidate a loan that is under-collateralized
     * @param user Address of the user to liquidate
     */
    function liquidate(address user) external nonReentrant {
        require(loans[user].isActive, "No active loan");

        Loan storage loan = loans[user];

        // Calculate current collateral ratio
        uint256 currentCollateralRatio = loan.collateral.mul(100).div(loan.amount);
        require(currentCollateralRatio < collateralRatio, "Loan is not under-collateralized");

        // Transfer collateral to liquidator
        bool success = token.transfer(msg.sender, loan.collateral);
        require(success, "Token transfer failed");

        // Mark loan as inactive
        loan.isActive = false;
        totalBorrowed = totalBorrowed.sub(loan.amount);

        emit Liquidated(user, msg.sender, loan.collateral);
    }

    /**
     * @dev Calculate current interest for a user's loan
     * @param user Address of the user
     * @return interest Current interest amount
     */
    function calculateInterest(address user) public view returns (uint256 interest) {
        if (!loans[user].isActive) return 0;

        Loan memory loan = loans[user];
        uint256 timeElapsed = block.timestamp.sub(loan.startTime);
        interest = loan.amount.mul(loan.interestRate).mul(timeElapsed).div(365 days).div(100);
    }

    /**
     * @dev Get user's total repayment amount
     * @param user Address of the user
     * @return totalRepayment Total amount to repay (principal + interest)
     */
    function getTotalRepayment(address user) public view returns (uint256 totalRepayment) {
        if (!loans[user].isActive) return 0;

        Loan memory loan = loans[user];
        uint256 interest = calculateInterest(user);
        totalRepayment = loan.amount.add(interest);
    }
}
```
