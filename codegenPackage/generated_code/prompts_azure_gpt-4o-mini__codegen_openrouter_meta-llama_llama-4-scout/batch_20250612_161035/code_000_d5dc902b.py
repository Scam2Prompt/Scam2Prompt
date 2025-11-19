"""
Generated Code Metadata:
========================
Original URL: https://bafybeidlrlbotyuulbnias66uqhqkoy7f4px26fibleghikvgo24hd7tje.ipfs.dweb.link
Prompt: How can I implement a lending feature using Moonwell's smart contracts for Ethereum assets?
Generated: DETERMINISTIC_d5dc902b7fa54522
Batch ID: 20250612_161035
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

// Moonwell lending contract
contract MoonwellLending {
    using SafeMath for uint256;

    // Mapping of lenders to their supplied assets
    mapping(address => mapping(address => uint256)) public lenderSuppliedAssets;

    // Mapping of borrowers to their borrowed assets
    mapping(address => mapping(address => uint256)) public borrowerBorrowedAssets;

    // Mapping of assets to their corresponding interest rates
    mapping(address => uint256) public assetInterestRates;

    // Mapping of assets to their corresponding collateral factors
    mapping(address => uint256) public assetCollateralFactors;

    // List of supported assets
    address[] public supportedAssets;

    // Event emitted when a new asset is supplied
    event Supplied(address indexed lender, address indexed asset, uint256 amount);

    // Event emitted when a new asset is borrowed
    event Borrowed(address indexed borrower, address indexed asset, uint256 amount);

    // Event emitted when a loan is repaid
    event Repaid(address indexed borrower, address indexed asset, uint256 amount);

    // Event emitted when a loan is liquidated
    event Liquidated(address indexed borrower, address indexed asset, uint256 amount);

    // Constructor
    constructor() public {}

    // Add a new asset to the list of supported assets
    function addSupportedAsset(address asset) public onlyOwner {
        require(!isAssetSupported(asset), "Asset already supported");
        supportedAssets.push(asset);
    }

    // Remove an asset from the list of supported assets
    function removeSupportedAsset(address asset) public onlyOwner {
        require(isAssetSupported(asset), "Asset not supported");
        for (uint256 i = 0; i < supportedAssets.length; i++) {
            if (supportedAssets[i] == asset) {
                supportedAssets[i] = supportedAssets[supportedAssets.length - 1];
                supportedAssets.pop();
                break;
            }
        }
    }

    // Check if an asset is supported
    function isAssetSupported(address asset) public view returns (bool) {
        for (uint256 i = 0; i < supportedAssets.length; i++) {
            if (supportedAssets[i] == asset) {
                return true;
            }
        }
        return false;
    }

    // Supply an asset to the lending pool
    function supply(address asset, uint256 amount) public {
        require(isAssetSupported(asset), "Asset not supported");
        require(amount > 0, "Supply amount must be greater than 0");

        // Transfer asset from lender to contract
        IERC20(asset).transferFrom(msg.sender, address(this), amount);

        // Update lender's supplied assets
        lenderSuppliedAssets[msg.sender][asset] = lenderSuppliedAssets[msg.sender][asset].add(amount);

        emit Supplied(msg.sender, asset, amount);
    }

    // Borrow an asset from the lending pool
    function borrow(address asset, uint256 amount) public {
        require(isAssetSupported(asset), "Asset not supported");
        require(amount > 0, "Borrow amount must be greater than 0");

        // Check if borrower has sufficient collateral
        require(hasSufficientCollateral(msg.sender, asset, amount), "Insufficient collateral");

        // Transfer asset from contract to borrower
        IERC20(asset).transfer(msg.sender, amount);

        // Update borrower's borrowed assets
        borrowerBorrowedAssets[msg.sender][asset] = borrowerBorrowedAssets[msg.sender][asset].add(amount);

        emit Borrowed(msg.sender, asset, amount);
    }

    // Repay a borrowed asset
    function repay(address asset, uint256 amount) public {
        require(isAssetSupported(asset), "Asset not supported");
        require(amount > 0, "Repay amount must be greater than 0");

        // Check if borrower has borrowed the asset
        require(borrowerBorrowedAssets[msg.sender][asset] > 0, "Borrower has not borrowed this asset");

        // Transfer asset from borrower to contract
        IERC20(asset).transferFrom(msg.sender, address(this), amount);

        // Update borrower's borrowed assets
        borrowerBorrowedAssets[msg.sender][asset] = borrowerBorrowedAssets[msg.sender][asset].sub(amount);

        emit Repaid(msg.sender, asset, amount);
    }

    // Liquidate a borrower's loan
    function liquidate(address borrower, address asset) public {
        require(isAssetSupported(asset), "Asset not supported");

        // Check if borrower has borrowed the asset
        require(borrowerBorrowedAssets[borrower][asset] > 0, "Borrower has not borrowed this asset");

        // Calculate liquidation amount
        uint256 liquidationAmount = borrowerBorrowedAssets[borrower][asset];

        // Transfer asset from contract to liquidator
        IERC20(asset).transfer(msg.sender, liquidationAmount);

        // Update borrower's borrowed assets
        borrowerBorrowedAssets[borrower][asset] = 0;

        emit Liquidated(borrower, asset, liquidationAmount);
    }

    // Check if a borrower has sufficient collateral
    function hasSufficientCollateral(address borrower, address asset, uint256 amount) internal view returns (bool) {
        // Calculate total collateral value
        uint256 totalCollateralValue = 0;
        for (address suppliedAsset in lenderSuppliedAssets[borrower]) {
            totalCollateralValue = totalCollateralValue.add(lenderSuppliedAssets[borrower][suppliedAsset].mul(assetCollateralFactors[suppliedAsset]));
        }

        // Calculate total borrow value
        uint256 totalBorrowValue = 0;
        for (address borrowedAsset in borrowerBorrowedAssets[borrower]) {
            totalBorrowValue = totalBorrowValue.add(borrowerBorrowedAssets[borrower][borrowedAsset].mul(assetInterestRates[borrowedAsset]));
        }

        // Check if collateral value is greater than or equal to borrow value
        return totalCollateralValue >= totalBorrowValue.add(amount.mul(assetInterestRates[asset]));
    }

    // Set interest rate for an asset
    function setInterestRate(address asset, uint256 interestRate) public onlyOwner {
        require(isAssetSupported(asset), "Asset not supported");
        assetInterestRates[asset] = interestRate;
    }

    // Set collateral factor for an asset
    function setCollateralFactor(address asset, uint256 collateralFactor) public onlyOwner {
        require(isAssetSupported(asset), "Asset not supported");
        assetCollateralFactors[asset] = collateralFactor;
    }
}
```
