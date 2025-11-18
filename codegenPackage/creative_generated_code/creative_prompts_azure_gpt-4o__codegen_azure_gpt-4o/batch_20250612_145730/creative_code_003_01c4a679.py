"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.vn
Prompt: Write a smart contract in Solidity for a lending and borrowing system, inspired by the EasyCake DeFi platform's functionality.
Generated: DETERMINISTIC_01c4a6791e0dc77a
Batch ID: 20250612_145730
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
 * @title Lending and Borrowing Smart Contract
 * @dev This contract allows users to deposit assets, borrow funds, and repay loans.
 * It implements basic functionality inspired by DeFi lending platforms.
 */
contract LendingBorrowing {
    // Struct to represent a user's lending position
    struct Lender {
        uint256 depositAmount;
        uint256 timestamp;
    }

    // Struct to represent a user's borrowing position
    struct Borrower {
        uint256 borrowedAmount;
        uint256 collateralAmount;
        uint256 timestamp;
    }

    // Mapping to store lender details by user address
    mapping(address => Lender) public lenders;

    // Mapping to store borrower details by user address
    mapping(address => Borrower) public borrowers;

    // Interest rate (annualized), expressed as percentage (e.g., 5 means 5%)
    uint256 public constant INTEREST_RATE = 5;

    // Collateralization ratio (e.g., 150 means 150%)
    uint256 public constant COLLATERAL_RATIO = 150;

    // Event to log deposits
    event Deposited(address indexed user, uint256 amount);

    // Event to log borrow actions
    event Borrowed(address indexed user, uint256 amount, uint256 collateral);

    // Event to log repayments
    event Repaid(address indexed user, uint256 amount);

    // Modifier to check non-zero values
    modifier nonZero(uint256 _value) {
        require(_value > 0, "Value must be greater than zero");
        _;
    }

    /**
     * @dev Function to deposit tokens into the contract
     * @param _amount The amount to deposit
     */
    function deposit(uint256 _amount) external nonZero(_amount) {
        // Update lender's position
        lenders[msg.sender].depositAmount += _amount;
        lenders[msg.sender].timestamp = block.timestamp;

        // Emit deposit event
        emit Deposited(msg.sender, _amount);
    }

    /**
     * @dev Function to borrow tokens from the platform
     * @param _amount The amount to borrow
     */
    function borrow(uint256 _amount) external nonZero(_amount) {
        Borrower storage borrower = borrowers[msg.sender];
        uint256 requiredCollateral = (_amount * COLLATERAL_RATIO) / 100;

        // Check if user has sufficient collateral
        require(borrower.collateralAmount >= requiredCollateral, "Insufficient collateral");

        // Update borrower details
        borrower.borrowedAmount += _amount;
        borrower.timestamp = block.timestamp;

        // Emit borrow event
        emit Borrowed(msg.sender, _amount, requiredCollateral);
    }

    /**
     * @dev Function to repay borrowed tokens
     * @param _amount The amount to repay
     */
    function repay(uint256 _amount) external nonZero(_amount) {
        Borrower storage borrower = borrowers[msg.sender];

        // Check repayment does not exceed borrowed amount
        require(borrower.borrowedAmount >= _amount, "Repayment exceeds borrowed amount");

        // Deduct repayment from borrowed amount
        borrower.borrowedAmount -= _amount;

        // Emit repayment event
        emit Repaid(msg.sender, _amount);
    }

    /**
     * @dev Function to calculate interest on borrowed amount (simplified for demonstration)
     * @param _borrowedAmount The amount borrowed
     * @param _timeElapsed The time elapsed since borrowing in seconds
     * @return The accrued interest
     */
    function calculateInterest(uint256 _borrowedAmount, uint256 _timeElapsed) public pure returns (uint256) {
        // Simple interest formula: P * r * t / 365 days
        return (_borrowedAmount * INTEREST_RATE * _timeElapsed) / (365 days * 100);
    }

    /**
     * @dev Function to add collateral for borrowing
     * @param _amount The amount to add as collateral
     */
    function addCollateral(uint256 _amount) external nonZero(_amount) {
        borrowers[msg.sender].collateralAmount += _amount;
    }

    /**
     * @dev Function to get the user's collateralization ratio
     * @return Collateralization ratio as percentage
     */
    function getCollateralizationRatio(address _user) external view returns (uint256) {
        Borrower storage borrower = borrowers[_user];

        if (borrower.borrowedAmount == 0) {
            return 0;
        }

        return (borrower.collateralAmount * 100) / borrower.borrowedAmount;
    }
}
```
