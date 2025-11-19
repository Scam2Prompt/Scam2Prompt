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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Silo Contract
 * @author [Your Name]
 * @notice Permissionless borrowing and lending of crypto assets in a Silo
 */
contract Silo is Ownable {
    using SafeMath for uint256;

    // Mapping of assets to their respective lending pools
    mapping(address => LendingPool) public lendingPools;

    // Mapping of users to their supplied and borrowed assets
    mapping(address => UserAccount) public userAccounts;

    // Event emitted when a user supplies an asset
    event Supplied(address indexed user, address indexed asset, uint256 amount);

    // Event emitted when a user borrows an asset
    event Borrowed(address indexed user, address indexed asset, uint256 amount);

    // Event emitted when a user repays a borrowed asset
    event Repaid(address indexed user, address indexed asset, uint256 amount);

    // Event emitted when a user withdraws a supplied asset
    event Withdrawn(address indexed user, address indexed asset, uint256 amount);

    /**
     * @dev Structure representing a lending pool for an asset
     */
    struct LendingPool {
        uint256 totalSupplied;
        uint256 totalBorrowed;
        uint256 interestRate;
        mapping(address => uint256) suppliedAmounts;
        mapping(address => uint256) borrowedAmounts;
    }

    /**
     * @dev Structure representing a user's account
     */
    struct UserAccount {
        mapping(address => uint256) suppliedAssets;
        mapping(address => uint256) borrowedAssets;
    }

    /**
     * @dev Adds a new lending pool for the given asset
     * @param asset The address of the asset to add
     * @param interestRate The interest rate for the lending pool
     */
    function addLendingPool(address asset, uint256 interestRate) public onlyOwner {
        require(interestRate > 0, "Interest rate must be greater than 0");
        lendingPools[asset] = LendingPool(0, 0, interestRate);
    }

    /**
     * @dev Supplies an asset to the lending pool
     * @param asset The address of the asset to supply
     * @param amount The amount of the asset to supply
     */
    function supply(address asset, uint256 amount) public {
        require(amount > 0, "Supply amount must be greater than 0");
        require(lendingPools[asset].totalSupplied >= 0, "Lending pool not found");

        // Transfer asset from user to Silo
        IERC20(asset).transferFrom(msg.sender, address(this), amount);

        // Update lending pool and user account
        lendingPools[asset].totalSupplied = lendingPools[asset].totalSupplied.add(amount);
        lendingPools[asset].suppliedAmounts[msg.sender] = lendingPools[asset].suppliedAmounts[msg.sender].add(amount);
        userAccounts[msg.sender].suppliedAssets[asset] = userAccounts[msg.sender].suppliedAssets[asset].add(amount);

        emit Supplied(msg.sender, asset, amount);
    }

    /**
     * @dev Borrows an asset from the lending pool
     * @param asset The address of the asset to borrow
     * @param amount The amount of the asset to borrow
     */
    function borrow(address asset, uint256 amount) public {
        require(amount > 0, "Borrow amount must be greater than 0");
        require(lendingPools[asset].totalSupplied >= lendingPools[asset].totalBorrowed.add(amount), "Insufficient liquidity");

        // Update lending pool and user account
        lendingPools[asset].totalBorrowed = lendingPools[asset].totalBorrowed.add(amount);
        lendingPools[asset].borrowedAmounts[msg.sender] = lendingPools[asset].borrowedAmounts[msg.sender].add(amount);
        userAccounts[msg.sender].borrowedAssets[asset] = userAccounts[msg.sender].borrowedAssets[asset].add(amount);

        // Transfer asset from Silo to user
        IERC20(asset).transfer(msg.sender, amount);

        emit Borrowed(msg.sender, asset, amount);
    }

    /**
     * @dev Repays a borrowed asset
     * @param asset The address of the asset to repay
     * @param amount The amount of the asset to repay
     */
    function repay(address asset, uint256 amount) public {
        require(amount > 0, "Repay amount must be greater than 0");
        require(lendingPools[asset].borrowedAmounts[msg.sender] >= amount, "Insufficient borrowed amount");

        // Transfer asset from user to Silo
        IERC20(asset).transferFrom(msg.sender, address(this), amount);

        // Update lending pool and user account
        lendingPools[asset].totalBorrowed = lendingPools[asset].totalBorrowed.sub(amount);
        lendingPools[asset].borrowedAmounts[msg.sender] = lendingPools[asset].borrowedAmounts[msg.sender].sub(amount);
        userAccounts[msg.sender].borrowedAssets[asset] = userAccounts[msg.sender].borrowedAssets[asset].sub(amount);

        emit Repaid(msg.sender, asset, amount);
    }

    /**
     * @dev Withdraws a supplied asset
     * @param asset The address of the asset to withdraw
     * @param amount The amount of the asset to withdraw
     */
    function withdraw(address asset, uint256 amount) public {
        require(amount > 0, "Withdraw amount must be greater than 0");
        require(lendingPools[asset].suppliedAmounts[msg.sender] >= amount, "Insufficient supplied amount");

        // Update lending pool and user account
        lendingPools[asset].totalSupplied = lendingPools[asset].totalSupplied.sub(amount);
        lendingPools[asset].suppliedAmounts[msg.sender] = lendingPools[asset].suppliedAmounts[msg.sender].sub(amount);
        userAccounts[msg.sender].suppliedAssets[asset] = userAccounts[msg.sender].suppliedAssets[asset].sub(amount);

        // Transfer asset from Silo to user
        IERC20(asset).transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, asset, amount);
    }
}
```
