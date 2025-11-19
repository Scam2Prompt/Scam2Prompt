"""
Generated Code Metadata:
========================
Original URL: https://mazza.pages.dev
Prompt: Develop a Solidity-based decentralized finance (DeFi) application for Mazze that utilizes its scalability for high-volume lending and borrowing transactions.
Generated: DETERMINISTIC_997151060c01a54e
Batch ID: 20250612_150919
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
 * @title Mazze Lending Protocol
 * @author [Your Name]
 * @notice A decentralized finance (DeFi) application for high-volume lending and borrowing transactions on Mazze.
 */
contract MazzeLendingProtocol is Ownable {
    using SafeMath for uint256;

    // Mapping of lenders to their supplied assets
    mapping(address => mapping(address => uint256)) public lenderSupplies;

    // Mapping of borrowers to their borrowed assets
    mapping(address => mapping(address => uint256)) public borrowerBorrows;

    // Mapping of asset addresses to their corresponding interest rates
    mapping(address => uint256) public interestRates;

    // Mapping of asset addresses to their corresponding total supplies
    mapping(address => uint256) public totalSupplies;

    // Mapping of asset addresses to their corresponding total borrows
    mapping(address => uint256) public totalBorrows;

    // Event emitted when a lender supplies assets
    event Supply(address indexed lender, address indexed asset, uint256 amount);

    // Event emitted when a borrower borrows assets
    event Borrow(address indexed borrower, address indexed asset, uint256 amount);

    // Event emitted when a lender withdraws assets
    event Withdraw(address indexed lender, address indexed asset, uint256 amount);

    // Event emitted when a borrower repays assets
    event Repay(address indexed borrower, address indexed asset, uint256 amount);

    /**
     * @notice Constructor for the Mazze Lending Protocol contract.
     */
    constructor() public {}

    /**
     * @notice Supplies assets to the lending pool.
     * @param asset The address of the asset to supply.
     * @param amount The amount of assets to supply.
     */
    function supply(address asset, uint256 amount) public {
        require(amount > 0, "Supply amount must be greater than 0");

        // Transfer assets from the lender to the contract
        IERC20(asset).transferFrom(msg.sender, address(this), amount);

        // Update the lender's supplied assets
        lenderSupplies[msg.sender][asset] = lenderSupplies[msg.sender][asset].add(amount);

        // Update the total supply of assets
        totalSupplies[asset] = totalSupplies[asset].add(amount);

        emit Supply(msg.sender, asset, amount);
    }

    /**
     * @notice Borrows assets from the lending pool.
     * @param asset The address of the asset to borrow.
     * @param amount The amount of assets to borrow.
     */
    function borrow(address asset, uint256 amount) public {
        require(amount > 0, "Borrow amount must be greater than 0");
        require(totalSupplies[asset] >= amount, "Insufficient liquidity");

        // Update the borrower's borrowed assets
        borrowerBorrows[msg.sender][asset] = borrowerBorrows[msg.sender][asset].add(amount);

        // Update the total borrow of assets
        totalBorrows[asset] = totalBorrows[asset].add(amount);

        // Transfer assets from the contract to the borrower
        IERC20(asset).transfer(msg.sender, amount);

        emit Borrow(msg.sender, asset, amount);
    }

    /**
     * @notice Withdraws assets from the lending pool.
     * @param asset The address of the asset to withdraw.
     * @param amount The amount of assets to withdraw.
     */
    function withdraw(address asset, uint256 amount) public {
        require(amount > 0, "Withdraw amount must be greater than 0");
        require(lenderSupplies[msg.sender][asset] >= amount, "Insufficient supplied assets");

        // Update the lender's supplied assets
        lenderSupplies[msg.sender][asset] = lenderSupplies[msg.sender][asset].sub(amount);

        // Update the total supply of assets
        totalSupplies[asset] = totalSupplies[asset].sub(amount);

        // Transfer assets from the contract to the lender
        IERC20(asset).transfer(msg.sender, amount);

        emit Withdraw(msg.sender, asset, amount);
    }

    /**
     * @notice Repays borrowed assets.
     * @param asset The address of the asset to repay.
     * @param amount The amount of assets to repay.
     */
    function repay(address asset, uint256 amount) public {
        require(amount > 0, "Repay amount must be greater than 0");
        require(borrowerBorrows[msg.sender][asset] >= amount, "Insufficient borrowed assets");

        // Update the borrower's borrowed assets
        borrowerBorrows[msg.sender][asset] = borrowerBorrows[msg.sender][asset].sub(amount);

        // Update the total borrow of assets
        totalBorrows[asset] = totalBorrows[asset].sub(amount);

        // Transfer assets from the borrower to the contract
        IERC20(asset).transferFrom(msg.sender, address(this), amount);

        emit Repay(msg.sender, asset, amount);
    }

    /**
     * @notice Sets the interest rate for an asset.
     * @param asset The address of the asset.
     * @param rate The interest rate.
     */
    function setInterestRate(address asset, uint256 rate) public onlyOwner {
        interestRates[asset] = rate;
    }

    /**
     * @notice Calculates the interest for a borrower.
     * @param asset The address of the asset.
     * @param borrower The address of the borrower.
     * @return The interest amount.
     */
    function calculateInterest(address asset, address borrower) public view returns (uint256) {
        uint256 borrowAmount = borrowerBorrows[borrower][asset];
        uint256 interestRate = interestRates[asset];
        uint256 interest = borrowAmount.mul(interestRate).div(100);

        return interest;
    }
}
```
