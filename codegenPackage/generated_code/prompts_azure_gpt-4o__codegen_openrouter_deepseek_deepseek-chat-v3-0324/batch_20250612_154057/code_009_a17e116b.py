"""
Generated Code Metadata:
========================
Original URL: https://morpho.orgmorpho.org
Prompt: Write a smart contract to leverage Morpho's zero-fee borrowing feature and calculate interest rates based on collateral and risk levels.
Generated: DETERMINISTIC_a17e116bfcd489ee
Batch ID: 20250612_154057
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@morpho-dao/morpho-core-v1/contracts/interfaces/IMorpho.sol";
import "@morpho-dao/morpho-core-v1/contracts/interfaces/ILendingPool.sol";

/**
 * @title MorphoZeroFeeBorrower
 * @dev A smart contract to leverage Morpho's zero-fee borrowing feature
 * with dynamic interest rate calculation based on collateral and risk levels.
 */
contract MorphoZeroFeeBorrower is Ownable {
    IMorpho public immutable morpho;
    
    // Risk parameters
    uint256 public constant MAX_LTV = 8000; // 80% in basis points
    uint256 public constant LIQUIDATION_THRESHOLD = 8500; // 85% in basis points
    uint256 public constant RISK_FREE_RATE = 200; // 2% in basis points
    uint256 public constant RISK_PREMIUM_BASE = 100; // 1% in basis points
    
    // Mapping to track user positions
    mapping(address => mapping(address => uint256)) public collateralBalances;
    mapping(address => mapping(address => uint256)) public borrowedAmounts;

    event Borrowed(
        address indexed user,
        address indexed collateralToken,
        address indexed borrowToken,
        uint256 collateralAmount,
        uint256 borrowAmount,
        uint256 interestRate
    );
    
    event Repaid(
        address indexed user,
        address indexed collateralToken,
        address indexed borrowToken,
        uint256 repayAmount,
        uint256 collateralReleased
    );

    /**
     * @dev Initializes the contract with Morpho's core address
     * @param _morpho Address of the Morpho protocol
     */
    constructor(address _morpho) {
        require(_morpho != address(0), "Invalid Morpho address");
        morpho = IMorpho(_morpho);
    }

    /**
     * @dev Borrow assets using collateral with zero fees
     * @param collateralToken The token to be used as collateral
     * @param borrowToken The token to borrow
     * @param collateralAmount The amount of collateral to deposit
     * @param borrowAmount The amount to borrow
     */
    function borrow(
        address collateralToken,
        address borrowToken,
        uint256 collateralAmount,
        uint256 borrowAmount
    ) external {
        require(collateralToken != address(0), "Invalid collateral token");
        require(borrowToken != address(0), "Invalid borrow token");
        require(collateralAmount > 0, "Collateral amount must be > 0");
        require(borrowAmount > 0, "Borrow amount must be > 0");

        // Transfer collateral from user
        IERC20(collateralToken).transferFrom(msg.sender, address(this), collateralAmount);

        // Approve Morpho to spend collateral
        IERC20(collateralToken).approve(address(morpho), collateralAmount);

        // Supply collateral to Morpho
        morpho.supply(collateralToken, collateralAmount);

        // Calculate dynamic interest rate based on collateral and risk
        uint256 interestRate = calculateInterestRate(collateralToken, borrowToken, collateralAmount, borrowAmount);

        // Borrow with zero fees
        morpho.borrow(borrowToken, borrowAmount);

        // Update user position
        collateralBalances[msg.sender][collateralToken] += collateralAmount;
        borrowedAmounts[msg.sender][borrowToken] += borrowAmount;

        // Transfer borrowed tokens to user
        IERC20(borrowToken).transfer(msg.sender, borrowAmount);

        emit Borrowed(
            msg.sender,
            collateralToken,
            borrowToken,
            collateralAmount,
            borrowAmount,
            interestRate
        );
    }

    /**
     * @dev Repay borrowed amount and release collateral
     * @param collateralToken The collateral token to withdraw
     * @param borrowToken The borrowed token to repay
     * @param repayAmount The amount to repay
     */
    function repay(
        address collateralToken,
        address borrowToken,
        uint256 repayAmount
    ) external {
        require(collateralToken != address(0), "Invalid collateral token");
        require(borrowToken != address(0), "Invalid borrow token");
        require(repayAmount > 0, "Repay amount must be > 0");

        uint256 borrowed = borrowedAmounts[msg.sender][borrowToken];
        uint256 collateral = collateralBalances[msg.sender][collateralToken];
        
        require(borrowed >= repayAmount, "Repay amount exceeds borrowed");

        // Transfer repay amount from user
        IERC20(borrowToken).transferFrom(msg.sender, address(this), repayAmount);

        // Approve Morpho to spend repay amount
        IERC20(borrowToken).approve(address(morpho), repayAmount);

        // Repay borrow
        morpho.repay(borrowToken, repayAmount);

        // Calculate collateral to withdraw (proportional to repayment)
        uint256 collateralToWithdraw = (collateral * repayAmount) / borrowed;

        // Withdraw collateral
        morpho.withdraw(collateralToken, collateralToWithdraw);

        // Transfer collateral back to user
        IERC20(collateralToken).transfer(msg.sender, collateralToWithdraw);

        // Update user position
        borrowedAmounts[msg.sender][borrowToken] -= repayAmount;
        collateralBalances[msg.sender][collateralToken] -= collateralToWithdraw;

        emit Repaid(
            msg.sender,
            collateralToken,
            borrowToken,
            repayAmount,
            collateralToWithdraw
        );
    }

    /**
     * @dev Calculate dynamic interest rate based on collateral and risk
     * @param collateralToken The collateral token
     * @param borrowToken The borrowed token
     * @param collateralAmount The collateral amount
     * @param borrowAmount The borrow amount
     * @return The calculated interest rate in basis points
     */
    function calculateInterestRate(
        address collateralToken,
        address borrowToken,
        uint256 collateralAmount,
        uint256 borrowAmount
    ) public view returns (uint256) {
        // Get token prices from Morpho's oracle
        uint256 collateralPrice = morpho.getPrice(collateralToken);
        uint256 borrowPrice = morpho.getPrice(borrowToken);

        // Calculate collateral value in borrow token terms
        uint256 collateralValue = (collateralAmount * collateralPrice) / borrowPrice;

        // Calculate loan-to-value ratio
        uint256 ltv = (borrowAmount * 1e4) / collateralValue;
        require(ltv < MAX_LTV, "LTV too high");

        // Calculate risk premium based on LTV
        uint256 riskPremium = RISK_PREMIUM_BASE * (ltv * ltv) / (MAX_LTV * MAX_LTV);

        // Total interest rate = risk-free rate + risk premium
        return RISK_FREE_RATE + riskPremium;
    }

    /**
     * @dev Emergency function to withdraw any ERC20 tokens
     * @param token The token to withdraw
     * @param amount The amount to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner(), amount);
    }
}
```
