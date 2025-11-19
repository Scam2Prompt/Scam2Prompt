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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Lending and Borrowing Smart Contract
 * @author [Your Name]
 * @notice This contract enables lending and borrowing functionalities for a DeFi application.
 */
contract LendingBorrowingContract {
    using SafeMath for uint256;

    // Mapping of lenders to their provided liquidity
    mapping (address => mapping (address => uint256)) public lenderLiquidity;

    // Mapping of borrowers to their borrowed amounts
    mapping (address => mapping (address => uint256)) public borrowerAmounts;

    // Mapping of assets to their corresponding interest rates
    mapping (address => uint256) public interestRates;

    // Mapping of assets to their corresponding total liquidity
    mapping (address => uint256) public totalLiquidity;

    // Event emitted when a new loan is taken
    event NewLoan(address indexed borrower, address indexed asset, uint256 amount);

    // Event emitted when a loan is repaid
    event LoanRepaid(address indexed borrower, address indexed asset, uint256 amount);

    // Event emitted when liquidity is added
    event LiquidityAdded(address indexed lender, address indexed asset, uint256 amount);

    // Event emitted when liquidity is removed
    event LiquidityRemoved(address indexed lender, address indexed asset, uint256 amount);

    /**
     * @dev Constructor function
     */
    constructor() public {}

    /**
     * @dev Adds liquidity to the pool for a specific asset
     * @param asset The address of the asset to add liquidity for
     * @param amount The amount of liquidity to add
     */
    function addLiquidity(address asset, uint256 amount) public {
        require(amount > 0, "Invalid amount");

        // Transfer asset from lender to contract
        IERC20(asset).transferFrom(msg.sender, address(this), amount);

        // Update lender's liquidity
        lenderLiquidity[msg.sender][asset] = lenderLiquidity[msg.sender][asset].add(amount);

        // Update total liquidity for asset
        totalLiquidity[asset] = totalLiquidity[asset].add(amount);

        emit LiquidityAdded(msg.sender, asset, amount);
    }

    /**
     * @dev Removes liquidity from the pool for a specific asset
     * @param asset The address of the asset to remove liquidity for
     * @param amount The amount of liquidity to remove
     */
    function removeLiquidity(address asset, uint256 amount) public {
        require(amount > 0, "Invalid amount");
        require(lenderLiquidity[msg.sender][asset] >= amount, "Insufficient liquidity");

        // Update lender's liquidity
        lenderLiquidity[msg.sender][asset] = lenderLiquidity[msg.sender][asset].sub(amount);

        // Update total liquidity for asset
        totalLiquidity[asset] = totalLiquidity[asset].sub(amount);

        // Transfer asset from contract to lender
        IERC20(asset).transfer(msg.sender, amount);

        emit LiquidityRemoved(msg.sender, asset, amount);
    }

    /**
     * @dev Borrows an asset
     * @param asset The address of the asset to borrow
     * @param amount The amount to borrow
     */
    function borrow(address asset, uint256 amount) public {
        require(amount > 0, "Invalid amount");
        require(totalLiquidity[asset] >= amount, "Insufficient liquidity");

        // Calculate interest rate
        uint256 interestRate = interestRates[asset];

        // Update borrower's amount
        borrowerAmounts[msg.sender][asset] = borrowerAmounts[msg.sender][asset].add(amount);

        // Update total liquidity for asset
        totalLiquidity[asset] = totalLiquidity[asset].sub(amount);

        // Transfer asset from contract to borrower
        IERC20(asset).transfer(msg.sender, amount);

        emit NewLoan(msg.sender, asset, amount);
    }

    /**
     * @dev Repays a borrowed asset
     * @param asset The address of the asset to repay
     * @param amount The amount to repay
     */
    function repay(address asset, uint256 amount) public {
        require(amount > 0, "Invalid amount");
        require(borrowerAmounts[msg.sender][asset] >= amount, "Invalid repayment amount");

        // Calculate interest
        uint256 interestRate = interestRates[asset];
        uint256 interest = amount.mul(interestRate).div(100);

        // Update borrower's amount
        borrowerAmounts[msg.sender][asset] = borrowerAmounts[msg.sender][asset].sub(amount);

        // Update total liquidity for asset
        totalLiquidity[asset] = totalLiquidity[asset].add(amount).add(interest);

        // Transfer asset from borrower to contract
        IERC20(asset).transferFrom(msg.sender, address(this), amount.add(interest));

        emit LoanRepaid(msg.sender, asset, amount);
    }

    /**
     * @dev Sets the interest rate for an asset
     * @param asset The address of the asset
     * @param rate The interest rate
     */
    function setInterestRate(address asset, uint256 rate) public onlyOwner {
        interestRates[asset] = rate;
    }
}
```
