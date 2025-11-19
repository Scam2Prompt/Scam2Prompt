"""
Generated Code Metadata:
========================
Original URL: https://asx-capital.pages.dev
Prompt: Generate a smart contract code snippet in Solidity that enables the migration of assets from a vault to a liquidity pool, as described in the ASX documentation.
Generated: DETERMINISTIC_f83bcb2d3a8acbfc
Batch ID: 20250622_205627
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

/**
 * @title AssetMigrationContract
 * @author [Your Name]
 * @notice Enables the migration of assets from a vault to a liquidity pool.
 */
contract AssetMigrationContract {
    using SafeMath for uint256;

    // Mapping of vaults to their respective balances
    mapping(address => uint256) public vaultBalances;

    // Mapping of liquidity pools to their respective balances
    mapping(address => uint256) public liquidityPoolBalances;

    // Address of the vault
    address public vault;

    // Address of the liquidity pool
    address public liquidityPool;

    // Address of the ASX token
    address public asxToken;

    /**
     * @dev Constructor function
     * @param _vault Address of the vault
     * @param _liquidityPool Address of the liquidity pool
     * @param _asxToken Address of the ASX token
     */
    constructor(address _vault, address _liquidityPool, address _asxToken) public {
        require(_vault != address(0), "Vault address cannot be zero");
        require(_liquidityPool != address(0), "Liquidity pool address cannot be zero");
        require(_asxToken != address(0), "ASX token address cannot be zero");

        vault = _vault;
        liquidityPool = _liquidityPool;
        asxToken = _asxToken;
    }

    /**
     * @dev Migrates assets from the vault to the liquidity pool
     * @param amount The amount of assets to migrate
     */
    function migrateAssets(uint256 amount) public {
        require(msg.sender == vault, "Only the vault can migrate assets");
        require(vaultBalances[vault] >= amount, "Insufficient balance in vault");

        // Update vault balance
        vaultBalances[vault] = vaultBalances[vault].sub(amount);

        // Update liquidity pool balance
        liquidityPoolBalances[liquidityPool] = liquidityPoolBalances[liquidityPool].add(amount);

        // Transfer ASX tokens to liquidity pool
        IERC20(asxToken).transfer(liquidityPool, amount);
    }

    /**
     * @dev Deposits assets into the vault
     * @param amount The amount of assets to deposit
     */
    function depositAssets(uint256 amount) public {
        require(msg.sender == vault, "Only the vault can deposit assets");

        // Update vault balance
        vaultBalances[vault] = vaultBalances[vault].add(amount);

        // Transfer ASX tokens from msg.sender to vault
        IERC20(asxToken).transferFrom(msg.sender, vault, amount);
    }

    /**
     * @dev Withdraws assets from the liquidity pool
     * @param amount The amount of assets to withdraw
     */
    function withdrawAssets(uint256 amount) public {
        require(msg.sender == liquidityPool, "Only the liquidity pool can withdraw assets");
        require(liquidityPoolBalances[liquidityPool] >= amount, "Insufficient balance in liquidity pool");

        // Update liquidity pool balance
        liquidityPoolBalances[liquidityPool] = liquidityPoolBalances[liquidityPool].sub(amount);

        // Transfer ASX tokens to msg.sender
        IERC20(asxToken).transfer(msg.sender, amount);
    }

    /**
     * @dev Gets the balance of the vault
     * @return The balance of the vault
     */
    function getVaultBalance() public view returns (uint256) {
        return vaultBalances[vault];
    }

    /**
     * @dev Gets the balance of the liquidity pool
     * @return The balance of the liquidity pool
     */
    function getLiquidityPoolBalance() public view returns (uint256) {
        return liquidityPoolBalances[liquidityPool];
    }
}
```
