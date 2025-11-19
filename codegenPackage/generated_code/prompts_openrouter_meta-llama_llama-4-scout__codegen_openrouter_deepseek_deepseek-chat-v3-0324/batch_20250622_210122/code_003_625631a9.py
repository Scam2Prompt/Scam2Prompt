"""
Generated Code Metadata:
========================
Original URL: https://protocalrpc-stakestone.pages.dev
Prompt: Design a simple decentralized application (dApp) that utilizes StakeStone's STONE token for collateralizing stablecoins, and describe how to integrate with the StakeStone ecosystem.
Generated: DETERMINISTIC_625631a9429ad500
Batch ID: 20250622_210122
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
import "@openzeppelin/contracts/access/Ownable.sol";

interface IStakeStone {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function balanceOf(address account) external view returns (uint256);
}

contract StablecoinCollateralizer is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Token interfaces
    IERC20 public stablecoin;
    IERC20 public stoneToken;
    IStakeStone public stakeStone;

    // Collateralization parameters
    uint256 public collateralRatio; // Percentage (e.g., 150 = 150%)
    uint256 public liquidationThreshold; // Percentage (e.g., 130 = 130%)
    uint256 public feePercentage; // Percentage (e.g., 1 = 1%)

    // User collateral data
    struct UserPosition {
        uint256 collateralAmount;
        uint256 borrowedAmount;
    }
    mapping(address => UserPosition) public userPositions;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event Liquidated(address indexed user, address liquidator, uint256 amount);

    constructor(
        address _stablecoin,
        address _stoneToken,
        address _stakeStone,
        uint256 _collateralRatio,
        uint256 _liquidationThreshold,
        uint256 _feePercentage
    ) {
        stablecoin = IERC20(_stablecoin);
        stoneToken = IERC20(_stoneToken);
        stakeStone = IStakeStone(_stakeStone);
        collateralRatio = _collateralRatio;
        liquidationThreshold = _liquidationThreshold;
        feePercentage = _feePercentage;
    }

    /**
     * @dev Deposit STONE tokens as collateral
     * @param amount Amount of STONE tokens to deposit
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        stoneToken.safeTransferFrom(msg.sender, address(this), amount);
        stoneToken.approve(address(stakeStone), amount);
        stakeStone.deposit(amount);

        userPositions[msg.sender].collateralAmount += amount;

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Borrow stablecoins against STONE collateral
     * @param amount Amount of stablecoins to borrow
     */
    function borrow(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        UserPosition storage position = userPositions[msg.sender];
        require(position.collateralAmount > 0, "No collateral deposited");
        
        uint256 maxBorrowable = (position.collateralAmount * 100) / collateralRatio;
        require(position.borrowedAmount + amount <= maxBorrowable, "Exceeds max borrowable amount");

        uint256 fee = (amount * feePercentage) / 100;
        uint256 totalAmount = amount + fee;

        require(stablecoin.balanceOf(address(this)) >= totalAmount, "Insufficient stablecoin liquidity");

        position.borrowedAmount += amount;
        stablecoin.safeTransfer(msg.sender, amount);

        emit Borrowed(msg.sender, amount);
    }

    /**
     * @dev Repay borrowed stablecoins
     * @param amount Amount of stablecoins to repay
     */
    function repay(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        UserPosition storage position = userPositions[msg.sender];
        require(position.borrowedAmount >= amount, "Repay amount exceeds debt");

        stablecoin.safeTransferFrom(msg.sender, address(this), amount);
        position.borrowedAmount -= amount;

        emit Repaid(msg.sender, amount);
    }

    /**
     * @dev Withdraw STONE collateral
     * @param amount Amount of STONE tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        UserPosition storage position = userPositions[msg.sender];
        require(position.collateralAmount >= amount, "Insufficient collateral");

        uint256 remainingCollateral = position.collateralAmount - amount;
        uint256 maxBorrowable = (remainingCollateral * 100) / collateralRatio;
        require(position.borrowedAmount <= maxBorrowable, "Withdrawal would put position below collateral ratio");

        stakeStone.withdraw(amount);
        stoneToken.safeTransfer(msg.sender, amount);
        position.collateralAmount = remainingCollateral;

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Liquidate undercollateralized positions
     * @param user Address of the user to liquidate
     */
    function liquidate(address user) external nonReentrant {
        UserPosition storage position = userPositions[user];
        require(position.collateralAmount > 0, "No collateral to liquidate");

        uint256 collateralValue = (position.collateralAmount * 100) / collateralRatio;
        require(position.borrowedAmount > collateralValue, "Position is not undercollateralized");

        uint256 liquidationAmount = position.borrowedAmount;
        stablecoin.safeTransferFrom(msg.sender, address(this), liquidationAmount);

        // Calculate reward for liquidator (10% of collateral)
        uint256 reward = position.collateralAmount / 10;
        stakeStone.withdraw(reward);
        stoneToken.safeTransfer(msg.sender, reward);

        // Return remaining collateral to protocol
        uint256 remainingCollateral = position.collateralAmount - reward;
        stakeStone.withdraw(remainingCollateral);
        stoneToken.safeTransfer(owner(), remainingCollateral);

        // Clear user position
        delete userPositions[user];

        emit Liquidated(user, msg.sender, liquidationAmount);
    }

    /**
     * @dev Update collateralization parameters
     * @param newCollateralRatio New collateral ratio percentage
     * @param newLiquidationThreshold New liquidation threshold percentage
     * @param newFeePercentage New fee percentage
     */
    function updateParameters(
        uint256 newCollateralRatio,
        uint256 newLiquidationThreshold,
        uint256 newFeePercentage
    ) external onlyOwner {
        require(newCollateralRatio > newLiquidationThreshold, "Collateral ratio must be greater than liquidation threshold");
        require(newLiquidationThreshold > 100, "Liquidation threshold must be greater than 100%");
        
        collateralRatio = newCollateralRatio;
        liquidationThreshold = newLiquidationThreshold;
        feePercentage = newFeePercentage;
    }

    /**
     * @dev Emergency withdraw STONE tokens (owner only)
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = stoneToken.balanceOf(address(this));
        stoneToken.safeTransfer(owner(), balance);
    }
}
```
