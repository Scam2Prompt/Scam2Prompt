"""
Generated Code Metadata:
========================
Original URL: https://ondofoundaktion.org
Prompt: Write a Solidity contract for a decentralized treasury management system that aligns with the Ondo Foundation’s focus on strategic ecosystem growth.
Generated: DETERMINISTIC_e80f5c412bd6b9ac
Batch ID: 20250612_154842
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
 * @title TreasuryManagementSystem
 * @author [Your Name]
 * @notice A decentralized treasury management system for strategic ecosystem growth.
 */
contract TreasuryManagementSystem is Ownable {
    using SafeMath for uint256;

    // Mapping of assets to their respective balances
    mapping(address => uint256) public assetBalances;

    // Mapping of asset addresses to their respective allowance amounts
    mapping(address => mapping(address => uint256)) public assetAllowances;

    // Event emitted when an asset is deposited into the treasury
    event AssetDeposited(address indexed asset, uint256 amount);

    // Event emitted when an asset is withdrawn from the treasury
    event AssetWithdrawn(address indexed asset, uint256 amount);

    // Event emitted when an asset's allowance is updated
    event AssetAllowanceUpdated(address indexed asset, address indexed spender, uint256 amount);

    /**
     * @dev Deposits an asset into the treasury.
     * @param asset The address of the asset to deposit.
     * @param amount The amount of the asset to deposit.
     */
    function depositAsset(address asset, uint256 amount) public {
        require(amount > 0, "Invalid deposit amount");
        require(IERC20(asset).transferFrom(msg.sender, address(this), amount), "Deposit failed");

        assetBalances[asset] = assetBalances[asset].add(amount);

        emit AssetDeposited(asset, amount);
    }

    /**
     * @dev Withdraws an asset from the treasury.
     * @param asset The address of the asset to withdraw.
     * @param amount The amount of the asset to withdraw.
     */
    function withdrawAsset(address asset, uint256 amount) public {
        require(assetBalances[asset] >= amount, "Insufficient balance");
        require(IERC20(asset).transfer(msg.sender, amount), "Withdrawal failed");

        assetBalances[asset] = assetBalances[asset].sub(amount);

        emit AssetWithdrawn(asset, amount);
    }

    /**
     * @dev Approves a spender to spend a specific amount of an asset.
     * @param asset The address of the asset.
     * @param spender The address of the spender.
     * @param amount The amount of the asset to approve.
     */
    function approveAssetSpender(address asset, address spender, uint256 amount) public {
        require(amount > 0, "Invalid approval amount");

        assetAllowances[asset][spender] = amount;

        emit AssetAllowanceUpdated(asset, spender, amount);
    }

    /**
     * @dev Transfers an asset from the treasury to a spender.
     * @param asset The address of the asset.
     * @param spender The address of the spender.
     * @param amount The amount of the asset to transfer.
     */
    function transferAsset(address asset, address spender, uint256 amount) public {
        require(assetAllowances[asset][spender] >= amount, "Insufficient allowance");
        require(assetBalances[asset] >= amount, "Insufficient balance");

        assetAllowances[asset][spender] = assetAllowances[asset][spender].sub(amount);
        assetBalances[asset] = assetBalances[asset].sub(amount);

        IERC20(asset).transfer(spender, amount);
    }

    /**
     * @dev Updates the treasury's asset balance.
     * @param asset The address of the asset.
     * @param amount The new balance of the asset.
     */
    function updateAssetBalance(address asset, uint256 amount) public onlyOwner {
        assetBalances[asset] = amount;
    }

    /**
     * @dev Updates the asset allowance.
     * @param asset The address of the asset.
     * @param spender The address of the spender.
     * @param amount The new allowance amount.
     */
    function updateAssetAllowance(address asset, address spender, uint256 amount) public onlyOwner {
        assetAllowances[asset][spender] = amount;

        emit AssetAllowanceUpdated(asset, spender, amount);
    }
}
```
