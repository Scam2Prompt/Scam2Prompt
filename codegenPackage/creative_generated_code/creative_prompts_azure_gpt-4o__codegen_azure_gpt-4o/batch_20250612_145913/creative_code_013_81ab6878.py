"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tenderize.xyz
Prompt: Write a tutorial for integrating ERC-20 compliant tenderized tokens into a DeFi lending protocol, allowing users to leverage their staked assets.
Generated: DETERMINISTIC_81ab68781f6eff0f
Batch ID: 20250612_145913
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
 * @title ERC-20 Tenderized Token Integration for DeFi Lending Protocol
 * @dev This contract demonstrates integrating ERC-20 compliant staked tokens into a DeFi lending system.
 * Users can deposit tenderized tokens, borrow against them, and withdraw their assets.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract DeFiLendingWithTenderizedTokens is ReentrancyGuard {
    // Event declarations for logging
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event Borrow(address indexed user, uint256 borrowAmount);
    event Repay(address indexed user, uint256 repayAmount);

    // State variables
    IERC20 public tenderizedToken; // ERC-20 compliant tenderized token contract
    uint256 public collateralFactor = 75; // Collateral factor (percentage, e.g., 75%)
    uint256 public interestRate = 5; // Interest rate percentage per borrow
    address public admin; // Admin address

    struct UserAccount {
        uint256 depositedAmount; // Amount of tenderized tokens deposited
        uint256 borrowedAmount;  // Amount borrowed by the user
        uint256 accruedInterest; // Interest accrued over time
    }

    mapping(address => UserAccount) public userAccounts;

    // Modifier to restrict access to admin functions
    modifier onlyAdmin() {
        require(msg.sender == admin, "Caller is not admin");
        _;
    }

    // Constructor to initialize contract with tenderized token and admin address
    constructor(address _tenderizedToken) {
        require(_tenderizedToken != address(0), "Invalid token address");
        tenderizedToken = IERC20(_tenderizedToken);
        admin = msg.sender;
    }

    /**
     * @dev Deposit tenderized tokens into the lending protocol.
     * @param _amount Amount of tokens to deposit.
     */
    function deposit(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Deposit amount must be greater than zero");

        // Transfer tokens from user to contract
        require(
            tenderizedToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update user's deposited balance
        userAccounts[msg.sender].depositedAmount += _amount;

        emit Deposit(msg.sender, _amount);
    }

    /**
     * @dev Borrow against deposited tenderized tokens.
     * @param _borrowAmount Amount to borrow.
     */
    function borrow(uint256 _borrowAmount) external nonReentrant {
        require(_borrowAmount > 0, "Borrow amount must be greater than zero");

        UserAccount storage account = userAccounts[msg.sender];

        // Calculate maximum borrowable amount
        uint256 maxBorrowable = (account.depositedAmount * collateralFactor) / 100;
        require(
            account.borrowedAmount + _borrowAmount <= maxBorrowable,
            "Borrow amount exceeds collateral limit"
        );

        // Update user's borrowed balance and interest
        account.borrowedAmount += _borrowAmount;
        account.accruedInterest += (_borrowAmount * interestRate) / 100;

        // Transfer borrowed amount to user
        require(
            tenderizedToken.transfer(msg.sender, _borrowAmount),
            "Token transfer failed"
        );

        emit Borrow(msg.sender, _borrowAmount);
    }

    /**
     * @dev Repay borrowed amount with accrued interest.
     * @param _repayAmount Amount to repay.
     */
    function repay(uint256 _repayAmount) external nonReentrant {
        require(_repayAmount > 0, "Repay amount must be greater than zero");

        UserAccount storage account = userAccounts[msg.sender];
        require(
            _repayAmount <= account.borrowedAmount + account.accruedInterest,
            "Repay amount exceeds borrowed balance"
        );

        // Transfer repayment amount from user to contract
        require(
            tenderizedToken.transferFrom(msg.sender, address(this), _repayAmount),
            "Token transfer failed"
        );

        // Update user's borrowed balance and accrued interest
        if (_repayAmount >= account.accruedInterest) {
            _repayAmount -= account.accruedInterest;
            account.accruedInterest = 0;
        } else {
            account.accruedInterest -= _repayAmount;
            _repayAmount = 0;
        }

        account.borrowedAmount -= _repayAmount;

        emit Repay(msg.sender, _repayAmount);
    }

    /**
     * @dev Withdraw tenderized tokens from the lending protocol.
     * @param _withdrawAmount Amount to withdraw.
     */
    function withdraw(uint256 _withdrawAmount) external nonReentrant {
        require(_withdrawAmount > 0, "Withdraw amount must be greater than zero");

        UserAccount storage account = userAccounts[msg.sender];
        require(
            _withdrawAmount <= account.depositedAmount - account.borrowedAmount,
            "Withdraw amount exceeds available balance"
        );

        // Update user's deposited balance
        account.depositedAmount -= _withdrawAmount;

        // Transfer tokens back to user
        require(
            tenderizedToken.transfer(msg.sender, _withdrawAmount),
            "Token transfer failed"
        );

        emit Withdraw(msg.sender, _withdrawAmount);
    }

    /**
     * @dev Admin function to update collateral factor.
     * @param _newCollateralFactor New collateral factor (percentage).
     */
    function updateCollateralFactor(uint256 _newCollateralFactor) external onlyAdmin {
        require(_newCollateralFactor > 0 && _newCollateralFactor <= 100, "Invalid collateral factor");
        collateralFactor = _newCollateralFactor;
    }

    /**
     * @dev Admin function to update interest rate.
     * @param _newInterestRate New interest rate (percentage).
     */
    function updateInterestRate(uint256 _newInterestRate) external onlyAdmin {
        require(_newInterestRate > 0, "Invalid interest rate");
        interestRate = _newInterestRate;
    }
}
```
