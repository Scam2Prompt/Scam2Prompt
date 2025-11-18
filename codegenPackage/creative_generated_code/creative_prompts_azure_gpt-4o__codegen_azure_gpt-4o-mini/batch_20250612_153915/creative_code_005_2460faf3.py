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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title USDSBorrowing
 * @dev A contract allowing users to borrow USDS against supplied assets
 * on Spark's platform, with dynamic borrowing rates managed by Sky's governance.
 */
contract USDSBorrowing is Ownable {
    // Token used for borrowing
    IERC20 public usdsToken;

    // Mapping of user balances
    mapping(address => uint256) public collateralBalance;
    
    // Mapping of user debts
    mapping(address => uint256) public userDebt;

    // Minimum collateralization ratio for borrowing
    uint256 public constant MIN_COLLATERAL_RATIO = 150; // 150%
    
    // Current borrowing rate (in basis points)
    uint256 public borrowingRate; // rate per block in basis points

    // Event emitted when collateral is supplied
    event CollateralSupplied(address indexed user, uint256 amount);
    
    // Event emitted when USDS is borrowed
    event USDSBorrowed(address indexed user, uint256 amount);
    
    // Event emitted when borrowing rate is updated
    event BorrowingRateUpdated(uint256 newRate);
    
    constructor(address _usdsToken) {
        require(_usdsToken != address(0), "Invalid USDS token address");
        usdsToken = IERC20(_usdsToken);
        borrowingRate = 200; // Initial rate set to 2.00%
    }

    /**
     * @dev Allows users to supply collateral.
     * @param amount The amount of collateral to supply.
     */
    function supplyCollateral(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        collateralBalance[msg.sender] += amount;
        emit CollateralSupplied(msg.sender, amount);
    }

    /**
     * @dev Allows users to borrow USDS against their supplied collateral.
     * @param borrowAmount The amount of USDS to borrow.
     */
    function borrowUSDS(uint256 borrowAmount) external {
        require(borrowAmount > 0, "Borrow amount must be greater than zero");
        uint256 collateralValue = collateralBalance[msg.sender]; // Assume 1:1 for simplicity
        uint256 collateralizationRatio = (collateralValue * 100) / borrowAmount;
        
        require(collateralizationRatio >= MIN_COLLATERAL_RATIO, "Collateralization ratio too low");

        userDebt[msg.sender] += borrowAmount;
        require(usdsToken.transfer(msg.sender, borrowAmount), "Transfer failed");
        emit USDSBorrowed(msg.sender, borrowAmount);
    }

    /**
     * @dev Updates the borrowing rate. Only callable by the owner (Sky's governance).
     * @param newRate The new borrowing rate in basis points (1 basis point = 0.01%).
     */
    function updateBorrowingRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Rate must be greater than zero");
        borrowingRate = newRate;
        emit BorrowingRateUpdated(newRate);
    }

    /**
     * @dev Allows users to repay borrowed USDS.
     * @param repayAmount The amount of USDS to repay.
     */
    function repayUSDS(uint256 repayAmount) external {
        require(repayAmount > 0, "Repay amount must be greater than zero");
        require(userDebt[msg.sender] >= repayAmount, "Repay amount exceeds debt");

        userDebt[msg.sender] -= repayAmount;
        require(usdsToken.transferFrom(msg.sender, address(this), repayAmount), "Transfer failed");
    }

    /**
     * @dev Allows users to withdraw their collateral.
     * @param amount The amount of collateral to withdraw.
     */
    function withdrawCollateral(uint256 amount) external {
        require(collateralBalance[msg.sender] >= amount, "Insufficient collateral");
        require(userDebt[msg.sender] == 0, "Outstanding debt exists");

        collateralBalance[msg.sender] -= amount;
        // For simplicity, we assume collateral is an ERC20 token as well
        require(usdsToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
