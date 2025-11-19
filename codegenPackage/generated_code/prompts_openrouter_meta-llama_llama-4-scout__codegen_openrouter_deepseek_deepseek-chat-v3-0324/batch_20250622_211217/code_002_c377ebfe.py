"""
Generated Code Metadata:
========================
Original URL: https://web-extra.fi
Prompt: Design a smart contract for a new DeFi lending platform inspired by Extra Finance's lending solutions.
Generated: DETERMINISTIC_c377ebfedc92f71a
Batch ID: 20250622_211217
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DeFi Lending Platform
 * @dev Inspired by Extra Finance's lending solutions
 * Features:
 * - Deposit/Withdraw assets
 * - Borrow assets with collateral
 * - Interest rate calculation
 * - Liquidation mechanism
 */
contract DeFiLendingPlatform is ReentrancyGuard {
    using SafeMath for uint256;

    // Structs
    struct UserInfo {
        uint256 collateralBalance; // Collateral deposited by user
        uint256 borrowedBalance;   // Amount borrowed by user
        uint256 lastUpdated;       // Timestamp of last interaction
    }

    struct AssetInfo {
        uint256 totalDeposits;     // Total deposits of this asset
        uint256 totalBorrows;      // Total borrows of this asset
        uint256 interestRate;      // Current interest rate (APY)
        uint256 utilizationRate;   // Current utilization rate
        uint256 lastUpdated;       // Timestamp of last update
        bool isActive;             // Whether asset is active
    }

    // Constants
    uint256 public constant LIQUIDATION_THRESHOLD = 80; // 80% collateralization threshold
    uint256 public constant LIQUIDATION_BONUS = 5;      // 5% liquidation bonus
    uint256 public constant INTEREST_RATE_SLOPE1 = 2;   // Base interest rate (2%)
    uint256 public constant INTEREST_RATE_SLOPE2 = 20;  // High utilization interest rate (20%)
    uint256 public constant UTILIZATION_OPTIMAL = 80;   // Optimal utilization rate (80%)

    // State variables
    mapping(address => mapping(address => UserInfo)) public users; // user => asset => info
    mapping(address => AssetInfo) public assets;                   // asset => info
    address[] public supportedAssets;                              // List of supported assets

    // Events
    event Deposit(address indexed user, address indexed asset, uint256 amount);
    event Withdraw(address indexed user, address indexed asset, uint256 amount);
    event Borrow(address indexed user, address indexed asset, uint256 amount);
    event Repay(address indexed user, address indexed asset, uint256 amount);
    event Liquidate(
        address indexed liquidator,
        address indexed user,
        address indexed asset,
        uint256 amount,
        uint256 bonus
    );
    event AssetAdded(address indexed asset);
    event AssetRemoved(address indexed asset);

    // Modifiers
    modifier onlyActiveAsset(address _asset) {
        require(assets[_asset].isActive, "Asset not supported");
        _;
    }

    modifier updateInterest(address _asset) {
        _updateInterest(_asset);
        _;
    }

    /**
     * @dev Add a new supported asset
     * @param _asset Address of the ERC20 token
     */
    function addAsset(address _asset) external {
        require(!assets[_asset].isActive, "Asset already added");
        assets[_asset] = AssetInfo({
            totalDeposits: 0,
            totalBorrows: 0,
            interestRate: INTEREST_RATE_SLOPE1,
            utilizationRate: 0,
            lastUpdated: block.timestamp,
            isActive: true
        });
        supportedAssets.push(_asset);
        emit AssetAdded(_asset);
    }

    /**
     * @dev Remove an asset from support
     * @param _asset Address of the ERC20 token
     */
    function removeAsset(address _asset) external onlyActiveAsset(_asset) {
        require(
            assets[_asset].totalDeposits == 0 && assets[_asset].totalBorrows == 0,
            "Asset has active deposits/borrows"
        );
        assets[_asset].isActive = false;
        emit AssetRemoved(_asset);
    }

    /**
     * @dev Deposit assets to use as collateral or earn interest
     * @param _asset Address of the ERC20 token
     * @param _amount Amount to deposit
     */
    function deposit(address _asset, uint256 _amount) external nonReentrant onlyActiveAsset(_asset) updateInterest(_asset) {
        require(_amount > 0, "Amount must be greater than 0");

        // Transfer tokens from user
        IERC20(_asset).transferFrom(msg.sender, address(this), _amount);

        // Update user and asset info
        UserInfo storage user = users[msg.sender][_asset];
        AssetInfo storage asset = assets[_asset];

        user.collateralBalance = user.collateralBalance.add(_amount);
        asset.totalDeposits = asset.totalDeposits.add(_amount);
        user.lastUpdated = block.timestamp;

        emit Deposit(msg.sender, _asset, _amount);
    }

    /**
     * @dev Withdraw deposited assets
     * @param _asset Address of the ERC20 token
     * @param _amount Amount to withdraw
     */
    function withdraw(address _asset, uint256 _amount) external nonReentrant onlyActiveAsset(_asset) updateInterest(_asset) {
        require(_amount > 0, "Amount must be greater than 0");

        UserInfo storage user = users[msg.sender][_asset];
        AssetInfo storage asset = assets[_asset];

        require(user.collateralBalance >= _amount, "Insufficient balance");
        require(
            _getCollateralRatio(msg.sender, _asset) >= LIQUIDATION_THRESHOLD,
            "Collateral ratio below threshold"
        );

        user.collateralBalance = user.collateralBalance.sub(_amount);
        asset.totalDeposits = asset.totalDeposits.sub(_amount);
        user.lastUpdated = block.timestamp;

        // Transfer tokens to user
        IERC20(_asset).transfer(msg.sender, _amount);

        emit Withdraw(msg.sender, _asset, _amount);
    }

    /**
     * @dev Borrow assets against collateral
     * @param _asset Address of the ERC20 token
     * @param _amount Amount to borrow
     */
    function borrow(address _asset, uint256 _amount) external nonReentrant onlyActiveAsset(_asset) updateInterest(_asset) {
        require(_amount > 0, "Amount must be greater than 0");

        UserInfo storage user = users[msg.sender][_asset];
        AssetInfo storage asset = assets[_asset];

        require(asset.totalDeposits >= _amount, "Insufficient liquidity");
        require(
            _getCollateralRatio(msg.sender, _asset) >= LIQUIDATION_THRESHOLD,
            "Collateral ratio below threshold"
        );

        user.borrowedBalance = user.borrowedBalance.add(_amount);
        asset.totalBorrows = asset.totalBorrows.add(_amount);
        user.lastUpdated = block.timestamp;

        // Transfer tokens to user
        IERC20(_asset).transfer(msg.sender, _amount);

        emit Borrow(msg.sender, _asset, _amount);
    }

    /**
     * @dev Repay borrowed assets
     * @param _asset Address of the ERC20 token
     * @param _amount Amount to repay
     */
    function repay(address _asset, uint256 _amount) external nonReentrant onlyActiveAsset(_asset) updateInterest(_asset) {
        require(_amount > 0, "Amount must be greater than 0");

        UserInfo storage user = users[msg.sender][_asset];
        AssetInfo storage asset = assets[_asset];

        require(user.borrowedBalance >= _amount, "Repay amount exceeds debt");

        // Transfer tokens from user
        IERC20(_asset).transferFrom(msg.sender, address(this), _amount);

        user.borrowedBalance = user.borrowedBalance.sub(_amount);
        asset.totalBorrows = asset.totalBorrows.sub(_amount);
        user.lastUpdated = block.timestamp;

        emit Repay(msg.sender, _asset, _amount);
    }

    /**
     * @dev Liquidate undercollateralized positions
     * @param _user Address of the user to liquidate
     * @param _asset Address of the borrowed asset
     */
    function liquidate(address _user, address _asset) external nonReentrant onlyActiveAsset(_asset) updateInterest(_asset) {
        UserInfo storage user = users[_user][_asset];
        require(
            _getCollateralRatio(_user, _asset) < LIQUIDATION_THRESHOLD,
            "Position not liquidatable"
        );

        uint256 debt = user.borrowedBalance;
        uint256 collateralValue = user.collateralBalance;
        uint256 bonus = collateralValue.mul(LIQUIDATION_BONUS).div(100);

        // Clear user's debt and collateral
        user.borrowedBalance = 0;
        user.collateralBalance = 0;

        // Update asset totals
        AssetInfo storage asset = assets[_asset];
        asset.totalBorrows
