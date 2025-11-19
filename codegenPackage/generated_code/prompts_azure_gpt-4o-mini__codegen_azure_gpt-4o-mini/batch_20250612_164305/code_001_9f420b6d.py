"""
Generated Code Metadata:
========================
Original URL: https://bafybeif5xdzxzkk6hpdngckqqt4qfejabreu6fkzi4rwsnuk733woz2spu.ipfs.dweb.link
Prompt: Write a smart contract that allows for permissionless borrowing and lending of crypto assets in a Silo, ensuring shared liquidity.
Generated: DETERMINISTIC_9f420b6d4f3d5bd1
Batch ID: 20250612_164305
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Silo
 * @dev A smart contract for permissionless borrowing and lending of crypto assets
 *      ensuring shared liquidity.
 */
contract Silo is Ownable {
    // Struct to hold information about each asset
    struct Asset {
        uint256 totalDeposited; // Total amount of asset deposited
        uint256 totalBorrowed;   // Total amount of asset borrowed
        mapping(address => uint256) deposits; // User deposits
        mapping(address => uint256) borrows;   // User borrows
    }

    // Mapping of asset addresses to their respective Asset structs
    mapping(address => Asset) private assets;

    // Event emitted when an asset is deposited
    event Deposited(address indexed asset, address indexed user, uint256 amount);
    
    // Event emitted when an asset is borrowed
    event Borrowed(address indexed asset, address indexed user, uint256 amount);
    
    // Event emitted when an asset is repaid
    event Repaid(address indexed asset, address indexed user, uint256 amount);

    // Event emitted when an asset is withdrawn
    event Withdrawn(address indexed asset, address indexed user, uint256 amount);

    /**
     * @dev Deposit an asset into the Silo.
     * @param asset The address of the ERC20 asset to deposit.
     * @param amount The amount of the asset to deposit.
     */
    function deposit(address asset, uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer the asset from the user to the contract
        IERC20(asset).transferFrom(msg.sender, address(this), amount);
        
        // Update the asset's total deposited and user's deposit
        assets[asset].totalDeposited += amount;
        assets[asset].deposits[msg.sender] += amount;

        emit Deposited(asset, msg.sender, amount);
    }

    /**
     * @dev Borrow an asset from the Silo.
     * @param asset The address of the ERC20 asset to borrow.
     * @param amount The amount of the asset to borrow.
     */
    function borrow(address asset, uint256 amount) external {
        require(amount > 0, "Borrow amount must be greater than zero");
        require(assets[asset].totalDeposited >= assets[asset].totalBorrowed + amount, "Insufficient liquidity");

        // Update the asset's total borrowed and user's borrow
        assets[asset].totalBorrowed += amount;
        assets[asset].borrows[msg.sender] += amount;

        // Transfer the asset to the borrower
        IERC20(asset).transfer(msg.sender, amount);

        emit Borrowed(asset, msg.sender, amount);
    }

    /**
     * @dev Repay a borrowed asset.
     * @param asset The address of the ERC20 asset to repay.
     * @param amount The amount of the asset to repay.
     */
    function repay(address asset, uint256 amount) external {
        require(amount > 0, "Repay amount must be greater than zero");
        require(assets[asset].borrows[msg.sender] >= amount, "Repay amount exceeds borrowed amount");

        // Update the asset's total borrowed and user's borrow
        assets[asset].totalBorrowed -= amount;
        assets[asset].borrows[msg.sender] -= amount;

        // Transfer the asset from the user to the contract
        IERC20(asset).transferFrom(msg.sender, address(this), amount);

        emit Repaid(asset, msg.sender, amount);
    }

    /**
     * @dev Withdraw a deposited asset.
     * @param asset The address of the ERC20 asset to withdraw.
     * @param amount The amount of the asset to withdraw.
     */
    function withdraw(address asset, uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(assets[asset].deposits[msg.sender] >= amount, "Withdraw amount exceeds deposited amount");

        // Update the asset's total deposited and user's deposit
        assets[asset].totalDeposited -= amount;
        assets[asset].deposits[msg.sender] -= amount;

        // Transfer the asset back to the user
        IERC20(asset).transfer(msg.sender, amount);

        emit Withdrawn(asset, msg.sender, amount);
    }

    /**
     * @dev Get the total deposited amount of an asset.
     * @param asset The address of the ERC20 asset.
     * @return The total deposited amount of the asset.
     */
    function totalDeposited(address asset) external view returns (uint256) {
        return assets[asset].totalDeposited;
    }

    /**
     * @dev Get the total borrowed amount of an asset.
     * @param asset The address of the ERC20 asset.
     * @return The total borrowed amount of the asset.
     */
    function totalBorrowed(address asset) external view returns (uint256) {
        return assets[asset].totalBorrowed;
    }

    /**
     * @dev Get the deposit balance of a user for a specific asset.
     * @param asset The address of the ERC20 asset.
     * @param user The address of the user.
     * @return The deposit balance of the user for the asset.
     */
    function userDepositBalance(address asset, address user) external view returns (uint256) {
        return assets[asset].deposits[user];
    }

    /**
     * @dev Get the borrow balance of a user for a specific asset.
     * @param asset The address of the ERC20 asset.
     * @param user The address of the user.
     * @return The borrow balance of the user for the asset.
     */
    function userBorrowBalance(address asset, address user) external view returns (uint256) {
        return assets[asset].borrows[user];
    }
}
```
