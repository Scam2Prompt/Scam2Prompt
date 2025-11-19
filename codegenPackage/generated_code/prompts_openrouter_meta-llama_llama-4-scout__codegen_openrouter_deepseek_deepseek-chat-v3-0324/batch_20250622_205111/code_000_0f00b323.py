"""
Generated Code Metadata:
========================
Original URL: https://bafybeif5xdzxzkk6hpdngckqqt4qfejabreu6fkzi4rwsnuk733woz2spu.ipfs.dweb.link
Prompt: "Write a smart contract in Solidity for a lending protocol that isolates risk to a single asset, similar to Silo Finance's Silo design."
Generated: DETERMINISTIC_0f00b32345560af7
Batch ID: 20250622_205111
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title IsolatedLendingProtocol
 * @dev A lending protocol that isolates risk to a single asset
 */
contract IsolatedLendingProtocol is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    struct AssetConfig {
        uint256 collateralFactor; // Basis points (e.g., 7500 = 75%)
        uint256 interestRate;    // Annual interest rate in basis points
        bool isActive;           // Whether the asset is active for lending/borrowing
    }

    struct UserPosition {
        uint256 collateralAmount;
        uint256 borrowedAmount;
    }

    // Mapping from asset address to its configuration
    mapping(address => AssetConfig) public assetConfigs;

    // Mapping from user address to asset address to their position
    mapping(address => mapping(address => UserPosition)) public userPositions;

    // Events
    event AssetAdded(address indexed asset, uint256 collateralFactor, uint256 interestRate);
    event AssetRemoved(address indexed asset);
    event CollateralDeposited(address indexed user, address indexed asset, uint256 amount);
    event CollateralWithdrawn(address indexed user, address indexed asset, uint256 amount);
    event Borrowed(address indexed user, address indexed asset, uint256 amount);
    event Repaid(address indexed user, address indexed asset, uint256 amount);

    /**
     * @dev Add a new asset to the protocol
     * @param asset The address of the ERC20 token
     * @param collateralFactor The collateral factor in basis points (e.g., 7500 = 75%)
     * @param interestRate The annual interest rate in basis points
     */
    function addAsset(address asset, uint256 collateralFactor, uint256 interestRate) external {
        require(asset != address(0), "Invalid asset address");
        require(collateralFactor <= 10000, "Collateral factor cannot exceed 100%");
        require(!assetConfigs[asset].isActive, "Asset already added");

        assetConfigs[asset] = AssetConfig({
            collateralFactor: collateralFactor,
            interestRate: interestRate,
            isActive: true
        });

        emit AssetAdded(asset, collateralFactor, interestRate);
    }

    /**
     * @dev Remove an asset from the protocol
     * @param asset The address of the ERC20 token
     */
    function removeAsset(address asset) external {
        require(assetConfigs[asset].isActive, "Asset not active");
        assetConfigs[asset].isActive = false;
        emit AssetRemoved(asset);
    }

    /**
     * @dev Deposit collateral
     * @param asset The address of the ERC20 token
     * @param amount The amount to deposit
     */
    function depositCollateral(address asset, uint256 amount) external nonReentrant {
        require(assetConfigs[asset].isActive, "Asset not active");
        require(amount > 0, "Amount must be greater than 0");

        IERC20(asset).safeTransferFrom(msg.sender, address(this), amount);
        userPositions[msg.sender][asset].collateralAmount = userPositions[msg.sender][asset].collateralAmount.add(amount);

        emit CollateralDeposited(msg.sender, asset, amount);
    }

    /**
     * @dev Withdraw collateral
     * @param asset The address of the ERC20 token
     * @param amount The amount to withdraw
     */
    function withdrawCollateral(address asset, uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        UserPosition storage position = userPositions[msg.sender][asset];
        require(position.collateralAmount >= amount, "Insufficient collateral");

        uint256 maxWithdrawable = calculateMaxWithdrawable(msg.sender, asset);
        require(amount <= maxWithdrawable, "Withdrawal exceeds safe limit");

        position.collateralAmount = position.collateralAmount.sub(amount);
        IERC20(asset).safeTransfer(msg.sender, amount);

        emit CollateralWithdrawn(msg.sender, asset, amount);
    }

    /**
     * @dev Borrow against collateral
     * @param asset The address of the ERC20 token
     * @param amount The amount to borrow
     */
    function borrow(address asset, uint256 amount) external nonReentrant {
        require(assetConfigs[asset].isActive, "Asset not active");
        require(amount > 0, "Amount must be greater than 0");

        UserPosition storage position = userPositions[msg.sender][asset];
        uint256 maxBorrowable = calculateMaxBorrowable(msg.sender, asset);
        require(amount <= maxBorrowable, "Borrow amount exceeds limit");

        position.borrowedAmount = position.borrowedAmount.add(amount);
        IERC20(asset).safeTransfer(msg.sender, amount);

        emit Borrowed(msg.sender, asset, amount);
    }

    /**
     * @dev Repay borrowed amount
     * @param asset The address of the ERC20 token
     * @param amount The amount to repay
     */
    function repay(address asset, uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        UserPosition storage position = userPositions[msg.sender][asset];
        require(position.borrowedAmount >= amount, "Repay amount exceeds debt");

        IERC20(asset).safeTransferFrom(msg.sender, address(this), amount);
        position.borrowedAmount = position.borrowedAmount.sub(amount);

        emit Repaid(msg.sender, asset, amount);
    }

    /**
     * @dev Calculate maximum borrowable amount for a user
     * @param user The address of the user
     * @param asset The address of the ERC20 token
     * @return The maximum borrowable amount
     */
    function calculateMaxBorrowable(address user, address asset) public view returns (uint256) {
        UserPosition storage position = userPositions[user][asset];
        AssetConfig storage config = assetConfigs[asset];

        uint256 collateralValue = position.collateralAmount;
        uint256 maxBorrowValue = collateralValue.mul(config.collateralFactor).div(10000);
        uint256 currentBorrowValue = position.borrowedAmount;

        if (currentBorrowValue >= maxBorrowValue) {
            return 0;
        }
        return maxBorrowValue.sub(currentBorrowValue);
    }

    /**
     * @dev Calculate maximum withdrawable collateral for a user
     * @param user The address of the user
     * @param asset The address of the ERC20 token
     * @return The maximum withdrawable amount
     */
    function calculateMaxWithdrawable(address user, address asset) public view returns (uint256) {
        UserPosition storage position = userPositions[user][asset];
        AssetConfig storage config = assetConfigs[asset];

        if (position.borrowedAmount == 0) {
            return position.collateralAmount;
        }

        uint256 minRequiredCollateral = position.borrowedAmount.mul(10000).div(config.collateralFactor);
        if (position.collateralAmount <= minRequiredCollateral) {
            return 0;
        }
        return position.collateralAmount.sub(minRequiredCollateral);
    }

    /**
     * @dev Get user's health factor (collateral / borrowed)
     * @param user The address of the user
     * @param asset The address of the ERC20 token
     * @return The health factor in basis points
     */
    function getHealthFactor(address user, address asset) public view returns (uint256) {
        UserPosition storage position = userPositions[user][asset];
        if (position.borrowedAmount == 0) return type(uint256).max;

        uint256 collateralValue = position.collateralAmount;
        uint256 borrowedValue = position.borrowedAmount;
        return collateralValue.mul(10000).div(borrowedValue);
    }
}
```
