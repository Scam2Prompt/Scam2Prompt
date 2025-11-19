"""
Generated Code Metadata:
========================
Original URL: https://pancakeswap.vn
Prompt: Write a smart contract in Solidity for a lending and borrowing system, inspired by the EasyCake DeFi platform's functionality.
Generated: DETERMINISTIC_01c4a6791e0dc77a
Batch ID: 20250612_145730
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title Lending and Borrowing System Contract
 * @author [Your Name]
 * @notice Inspired by EasyCake DeFi platform's functionality
 */
contract LendingBorrowingSystem is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of lenders to their provided liquidity
    mapping(address => mapping(address => uint256)) public lenderLiquidity;

    // Mapping of borrowers to their borrowed amounts
    mapping(address => mapping(address => uint256)) public borrowerAmounts;

    // Mapping of assets to their corresponding token addresses
    mapping(address => IERC20) public assets;

    // Event emitted when a new asset is added
    event NewAssetAdded(address indexed asset, address indexed token);

    // Event emitted when a lender provides liquidity
    event LiquidityProvided(address indexed lender, address indexed asset, uint256 amount);

    // Event emitted when a borrower borrows an asset
    event Borrowed(address indexed borrower, address indexed asset, uint256 amount);

    // Event emitted when a borrower repays a loan
    event Repaid(address indexed borrower, address indexed asset, uint256 amount);

    // Event emitted when a lender withdraws liquidity
    event LiquidityWithdrawn(address indexed lender, address indexed asset, uint256 amount);

    /**
     * @notice Constructor function
     */
    constructor() public {}

    /**
     * @notice Adds a new asset to the system
     * @param asset The address of the asset
     * @param token The address of the corresponding token
     */
    function addAsset(address asset, address token) public onlyOwner {
        require(asset != address(0) && token != address(0), "Invalid asset or token address");
        assets[asset] = IERC20(token);
        emit NewAssetAdded(asset, token);
    }

    /**
     * @notice Provides liquidity to the system
     * @param asset The address of the asset to provide liquidity for
     * @param amount The amount of liquidity to provide
     */
    function provideLiquidity(address asset, uint256 amount) public {
        require(assets[asset] != IERC20(0), "Asset not found");
        require(amount > 0, "Invalid amount");

        IERC20(assets[asset]).transferFrom(msg.sender, address(this), amount);
        lenderLiquidity[msg.sender][asset] = lenderLiquidity[msg.sender][asset].add(amount);
        emit LiquidityProvided(msg.sender, asset, amount);
    }

    /**
     * @notice Borrows an asset from the system
     * @param asset The address of the asset to borrow
     * @param amount The amount of the asset to borrow
     */
    function borrow(address asset, uint256 amount) public {
        require(assets[asset] != IERC20(0), "Asset not found");
        require(amount > 0, "Invalid amount");
        require(lenderLiquidity[address(this)][asset] >= amount, "Insufficient liquidity");

        IERC20(assets[asset]).transfer(msg.sender, amount);
        borrowerAmounts[msg.sender][asset] = borrowerAmounts[msg.sender][asset].add(amount);
        lenderLiquidity[address(this)][asset] = lenderLiquidity[address(this)][asset].sub(amount);
        emit Borrowed(msg.sender, asset, amount);
    }

    /**
     * @notice Repays a loan
     * @param asset The address of the asset to repay
     * @param amount The amount to repay
     */
    function repay(address asset, uint256 amount) public {
        require(assets[asset] != IERC20(0), "Asset not found");
        require(amount > 0, "Invalid amount");
        require(borrowerAmounts[msg.sender][asset] >= amount, "Invalid repayment amount");

        IERC20(assets[asset]).transferFrom(msg.sender, address(this), amount);
        borrowerAmounts[msg.sender][asset] = borrowerAmounts[msg.sender][asset].sub(amount);
        lenderLiquidity[address(this)][asset] = lenderLiquidity[address(this)][asset].add(amount);
        emit Repaid(msg.sender, asset, amount);
    }

    /**
     * @notice Withdraws liquidity from the system
     * @param asset The address of the asset to withdraw liquidity for
     * @param amount The amount of liquidity to withdraw
     */
    function withdrawLiquidity(address asset, uint256 amount) public {
        require(assets[asset] != IERC20(0), "Asset not found");
        require(amount > 0, "Invalid amount");
        require(lenderLiquidity[msg.sender][asset] >= amount, "Insufficient liquidity");

        IERC20(assets[asset]).transfer(msg.sender, amount);
        lenderLiquidity[msg.sender][asset] = lenderLiquidity[msg.sender][asset].sub(amount);
        emit LiquidityWithdrawn(msg.sender, asset, amount);
    }

    /**
     * @notice Gets the available liquidity for an asset
     * @param asset The address of the asset
     * @return The available liquidity
     */
    function getAvailableLiquidity(address asset) public view returns (uint256) {
        return lenderLiquidity[address(this)][asset];
    }

    /**
     * @notice Gets the borrowed amount for a borrower and asset
     * @param borrower The address of the borrower
     * @param asset The address of the asset
     * @return The borrowed amount
     */
    function getBorrowedAmount(address borrower, address asset) public view returns (uint256) {
        return borrowerAmounts[borrower][asset];
    }
}
```
