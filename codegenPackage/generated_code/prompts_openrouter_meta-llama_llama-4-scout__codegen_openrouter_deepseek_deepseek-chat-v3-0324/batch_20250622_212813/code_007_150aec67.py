"""
Generated Code Metadata:
========================
Original URL: https://ondofoundkation.com
Prompt: Design a smart contract for a DeFi protocol that utilizes Ondo's tokenized RWAs as collateral, written in Solidity.
Generated: DETERMINISTIC_150aec67576e014c
Batch ID: 20250622_212813
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

interface IOndoRWA {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function getUnderlyingValue(uint256 amount) external view returns (uint256);
}

contract DeFiProtocol is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user collateral and debt information
    struct UserPosition {
        uint256 collateralAmount;
        uint256 debtAmount;
        uint256 lastUpdated;
    }

    // Token contracts
    IOndoRWA public immutable ondoRWAToken;
    IERC20 public immutable stablecoin;

    // Protocol parameters
    uint256 public collateralizationRatio; // Minimum collateralization ratio (in basis points, e.g. 15000 = 150%)
    uint256 public liquidationThreshold; // Liquidation threshold (in basis points)
    uint256 public interestRate; // Annual interest rate (in basis points)
    uint256 public liquidationPenalty; // Penalty for liquidation (in basis points)

    // Mapping of user positions
    mapping(address => UserPosition) public positions;

    // Events
    event DepositCollateral(address indexed user, uint256 amount);
    event WithdrawCollateral(address indexed user, uint256 amount);
    event Borrow(address indexed user, uint256 amount);
    event Repay(address indexed user, uint256 amount);
    event Liquidate(address indexed user, address liquidator, uint256 collateralSeized, uint256 debtRepaid);

    constructor(
        address _ondoRWAToken,
        address _stablecoin,
        uint256 _collateralizationRatio,
        uint256 _liquidationThreshold,
        uint256 _interestRate,
        uint256 _liquidationPenalty
    ) {
        require(_ondoRWAToken != address(0), "Invalid Ondo RWA token address");
        require(_stablecoin != address(0), "Invalid stablecoin address");
        require(_collateralizationRatio > _liquidationThreshold, "Invalid ratio parameters");
        require(_liquidationThreshold > 0, "Liquidation threshold must be positive");
        require(_interestRate > 0, "Interest rate must be positive");
        require(_liquidationPenalty > 0, "Liquidation penalty must be positive");

        ondoRWAToken = IOndoRWA(_ondoRWAToken);
        stablecoin = IERC20(_stablecoin);
        collateralizationRatio = _collateralizationRatio;
        liquidationThreshold = _liquidationThreshold;
        interestRate = _interestRate;
        liquidationPenalty = _liquidationPenalty;
    }

    /**
     * @dev Deposit Ondo RWA tokens as collateral
     * @param amount Amount of Ondo RWA tokens to deposit
     */
    function depositCollateral(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        // Update user's accrued interest before modifying position
        _updateInterest(msg.sender);

        // Transfer tokens from user to contract
        ondoRWAToken.transferFrom(msg.sender, address(this), amount);

        // Update user's collateral balance
        positions[msg.sender].collateralAmount += amount;

        emit DepositCollateral(msg.sender, amount);
    }

    /**
     * @dev Withdraw collateral from the protocol
     * @param amount Amount of Ondo RWA tokens to withdraw
     */
    function withdrawCollateral(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        UserPosition storage position = positions[msg.sender];
        
        // Update user's accrued interest before modifying position
        _updateInterest(msg.sender);

        require(position.collateralAmount >= amount, "Insufficient collateral");

        // Check collateralization ratio after withdrawal
        uint256 newCollateral = position.collateralAmount - amount;
        uint256 collateralValue = ondoRWAToken.getUnderlyingValue(newCollateral);
        require(
            collateralValue * 10000 >= position.debtAmount * collateralizationRatio,
            "Withdrawal would violate collateralization ratio"
        );

        // Update user's collateral balance
        position.collateralAmount = newCollateral;

        // Transfer tokens back to user
        ondoRWAToken.transfer(msg.sender, amount);

        emit WithdrawCollateral(msg.sender, amount);
    }

    /**
     * @dev Borrow stablecoins against deposited collateral
     * @param amount Amount of stablecoins to borrow
     */
    function borrow(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        UserPosition storage position = positions[msg.sender];

        // Update user's accrued interest before modifying position
        _updateInterest(msg.sender);

        // Calculate collateral value
        uint256 collateralValue = ondoRWAToken.getUnderlyingValue(position.collateralAmount);
        uint256 newDebt = position.debtAmount + amount;

        // Check collateralization ratio
        require(
            collateralValue * 10000 >= newDebt * collateralizationRatio,
            "Borrow would violate collateralization ratio"
        );

        // Update user's debt balance
        position.debtAmount = newDebt;

        // Transfer stablecoins to user
        stablecoin.safeTransfer(msg.sender, amount);

        emit Borrow(msg.sender, amount);
    }

    /**
     * @dev Repay borrowed stablecoins
     * @param amount Amount of stablecoins to repay
     */
    function repay(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        UserPosition storage position = positions[msg.sender];

        // Update user's accrued interest before modifying position
        _updateInterest(msg.sender);

        require(position.debtAmount >= amount, "Repay amount exceeds debt");

        // Transfer stablecoins from user to contract
        stablecoin.safeTransferFrom(msg.sender, address(this), amount);

        // Update user's debt balance
        position.debtAmount -= amount;

        emit Repay(msg.sender, amount);
    }

    /**
     * @dev Liquidate an undercollateralized position
     * @param user Address of the user to liquidate
     */
    function liquidate(address user) external nonReentrant {
        UserPosition storage position = positions[user];
        
        // Update user's accrued interest before checking position
        _updateInterest(user);

        // Calculate collateral value
        uint256 collateralValue = ondoRWAToken.getUnderlyingValue(position.collateralAmount);

        // Check if position is undercollateralized
        require(
            collateralValue * 10000 < position.debtAmount * liquidationThreshold,
            "Position is not undercollateralized"
        );

        // Calculate amount to liquidate (up to full debt)
        uint256 debtToRepay = position.debtAmount;
        uint256 collateralToSeize = (debtToRepay * (10000 + liquidationPenalty)) / 10000;
        
        // Ensure we don't seize more collateral than available
        if (collateralToSeize > position.collateralAmount) {
            collateralToSeize = position.collateralAmount;
            debtToRepay = (collateralToSeize * 10000) / (10000 + liquidationPenalty);
        }

        // Transfer stablecoins from liquidator to protocol
        stablecoin.safeTransferFrom(msg.sender, address(this), debtToRepay);

        // Update user's position
        position.debtAmount -= debtToRepay;
        position.collateralAmount -= collateralToSeize;

        // Transfer seized collateral to liquidator
        ondoRWAToken.transfer(msg.sender, collateralToSeize);

        emit Liquidate(user, msg.sender, collateralToSeize, debtToRepay);
    }

    /**
     * @dev Update the accrued interest for a user's position
     * @param user Address of the user to update
     */
    function _updateInterest(address user) internal {
        UserPosition storage position = positions[user];
        if (position.debtAmount == 0) return;

        uint256 timeElapsed = block.timestamp - position.lastUpdated;
        if (timeElapsed == 0) return;

        // Calculate interest (simple interest)
        uint256 interest = (position.debtAmount * interestRate * timeElapsed) / (365 days * 10000);
        
        // Update debt and timestamp
        position.debtAmount += interest;
        position.lastUpdated = block.timestamp;
    }

    /**
     * @dev Update protocol parameters (owner only)
     */
    function updateProtocolParameters(
