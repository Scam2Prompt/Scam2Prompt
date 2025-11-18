"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spark.fiddler-pkg.com
Prompt: Develop a Solidity contract to borrow USDS against supplied assets on Spark's platform. Include functionality to calculate borrowing rates based on Sky's governance and ensure transparent rate adjustments.
Generated: DETERMINISTIC_2460faf363c5a3cc
Batch ID: 20250612_153915
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
 * @title SparkBorrowingContract
 * @notice This contract allows users to borrow USDS against supplied assets on Spark's platform.
 * It calculates borrowing rates based on governance rules and ensures rate adjustments are transparent.
 */
contract SparkBorrowingContract {
    // Events
    event Borrow(address indexed borrower, uint256 amount, uint256 rate);
    event RateAdjusted(uint256 oldRate, uint256 newRate);

    // Governance address for rate adjustment
    address public governance;

    // Borrowing rate in basis points (1 basis point = 0.01%)
    uint256 public borrowingRate;

    // Maximum allowable borrowing rate (for safety)
    uint256 public constant MAX_BORROWING_RATE = 2000; // 20%

    // Mapping of borrower to their borrowed balance
    mapping(address => uint256) public borrowedBalances;

    // Constructor to initialize the contract
    constructor(address _governance, uint256 _initialRate) {
        require(_governance != address(0), "Invalid governance address");
        require(_initialRate <= MAX_BORROWING_RATE, "Initial rate exceeds max rate");

        governance = _governance;
        borrowingRate = _initialRate;
    }

    /**
     * @notice Borrow USDS against supplied assets.
     * @param _amount The amount of USDS to borrow.
     */
    function borrow(uint256 _amount) external {
        require(_amount > 0, "Borrow amount must be greater than zero");

        // Example implementation of borrowing logic:
        // In production, this function would interact with Spark's platform to verify collateral and execute the loan.

        borrowedBalances[msg.sender] += _amount;

        // Emit the borrow event
        emit Borrow(msg.sender, _amount, borrowingRate);
    }

    /**
     * @notice Adjust the borrowing rate. Can only be called by governance.
     * @param _newRate The new borrowing rate in basis points.
     */
    function adjustRate(uint256 _newRate) external {
        require(msg.sender == governance, "Caller is not governance");
        require(_newRate <= MAX_BORROWING_RATE, "New rate exceeds max rate");

        uint256 oldRate = borrowingRate;
        borrowingRate = _newRate;

        // Emit the rate adjustment event
        emit RateAdjusted(oldRate, _newRate);
    }

    /**
     * @notice Get the current borrowing rate.
     * @return The current borrowing rate in basis points.
     */
    function getBorrowingRate() external view returns (uint256) {
        return borrowingRate;
    }

    /**
     * @notice Get the borrowed balance of a user.
     * @param _borrower The address of the borrower.
     * @return The borrowed balance of the borrower.
     */
    function getBorrowedBalance(address _borrower) external view returns (uint256) {
        return borrowedBalances[_borrower];
    }
}
```
