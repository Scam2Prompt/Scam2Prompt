"""
Generated Code Metadata:
========================
Original URL: https://mmorpho.org
Prompt: Write a smart contract function that integrates Morpho Bundler to supply wstETH as collateral, borrow USDC, and deposit it into a Spark DAI vault.
Generated: DETERMINISTIC_a84f70fae50bbe75
Batch ID: 20250612_145444
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";

contract MorphoSparkStrategy {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Morpho Bundler contract address
    address public morphoBundler;

    // Spark DAI vault contract address
    address public sparkDaiVault;

    // wstETH token contract address
    address public wstETH;

    // USDC token contract address
    address public USDC;

    // DAI token contract address
    address public DAI;

    // Mapping of users to their vaults
    mapping(address => address) public userVaults;

    /**
     * @param _morphoBundler Morpho Bundler contract address
     * @param _sparkDaiVault Spark DAI vault contract address
     * @param _wstETH wstETH token contract address
     * @param _USDC USDC token contract address
     * @param _DAI DAI token contract address
     */
    constructor(
        address _morphoBundler,
        address _sparkDaiVault,
        address _wstETH,
        address _USDC,
        address _DAI
    ) public {
        morphoBundler = _morphoBundler;
        sparkDaiVault = _sparkDaiVault;
        wstETH = _wstETH;
        USDC = _USDC;
        DAI = _DAI;
    }

    /**
     * Supplies wstETH as collateral, borrows USDC, and deposits it into a Spark DAI vault
     * @param _amount The amount of wstETH to supply as collateral
     * @return The amount of USDC borrowed
     */
    function supplyAndBorrow(uint256 _amount) public returns (uint256) {
        // Approve Morpho Bundler to spend wstETH
        IERC20(wstETH).safeApprove(morphoBundler, _amount);

        // Supply wstETH as collateral to Morpho Bundler
        uint256 collateralizedAmount = MorphoBundler(morphoBundler).supply(wstETH, _amount);

        // Borrow USDC from Morpho Bundler
        uint256 borrowAmount = collateralizedAmount.mul(5).div(10); // 50% LTV
        uint256 usdcBorrowed = MorphoBundler(morphoBundler).borrow(USDC, borrowAmount);

        // Deposit USDC into Spark DAI vault
        IERC20(USDC).safeTransfer(sparkDaiVault, usdcBorrowed);

        // Create a new vault for the user if it doesn't exist
        if (userVaults[msg.sender] == address(0)) {
            userVaults[msg.sender] = SparkDaiVault(sparkDaiVault).createVault(msg.sender);
        }

        // Deposit DAI into the user's vault (assuming DAI is received from somewhere)
        // For demonstration purposes, assume DAI is transferred from an external source
        // IERC20(DAI).safeTransfer(userVaults[msg.sender], _amount);

        return usdcBorrowed;
    }

    // Fallback function for emergency situations
    fallback() external payable {}

    // Example usage
    function exampleUsage() public {
        uint256 wstETHAmount = 10 ether;
        uint256 usdcBorrowed = supplyAndBorrow(wstETHAmount);
        // Use the borrowed USDC
    }
}

// Interfaces for external contracts
interface MorphoBundler {
    function supply(address _collateral, uint256 _amount) external returns (uint256);
    function borrow(address _borrowedToken, uint256 _amount) external returns (uint256);
}

interface SparkDaiVault {
    function createVault(address _user) external returns (address);
}
```
