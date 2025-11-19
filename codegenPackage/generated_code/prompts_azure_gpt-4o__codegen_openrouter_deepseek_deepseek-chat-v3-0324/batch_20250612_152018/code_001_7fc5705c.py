"""
Generated Code Metadata:
========================
Original URL: https://cncrete.pages.dev
Prompt: Generate code for an appchain that improves on-chain debt and credit management, incorporating features like higher yields and liquidation protection.
Generated: DETERMINISTIC_7fc5705c1ce6f599
Batch ID: 20250612_152018
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract DebtCreditManager is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Structs
    struct Position {
        address borrower;
        address collateralToken;
        uint256 collateralAmount;
        address debtToken;
        uint256 debtAmount;
        uint256 liquidationThreshold;
        uint256 createdAt;
        uint256 lastUpdatedAt;
    }

    // State variables
    mapping(address => Position) public positions;
    mapping(address => uint256) public interestRates;
    mapping(address => bool) public supportedTokens;
    uint256 public liquidationPenalty = 5; // 5% penalty
    uint256 public minCollateralRatio = 150; // 150% minimum
    uint256 public constant PRECISION = 1e18;

    // Events
    event PositionOpened(
        address indexed borrower,
        address collateralToken,
        uint256 collateralAmount,
        address debtToken,
        uint256 debtAmount
    );
    event PositionClosed(address indexed borrower);
    event CollateralAdded(
        address indexed borrower,
        address collateralToken,
        uint256 amount
    );
    event DebtRepaid(
        address indexed borrower,
        address debtToken,
        uint256 amount
    );
    event PositionLiquidated(
        address indexed borrower,
        address liquidator,
        uint256 collateralSeized
    );
    event InterestRateUpdated(address indexed token, uint256 newRate);

    // Modifiers
    modifier onlySupportedToken(address token) {
        require(supportedTokens[token], "Token not supported");
        _;
    }

    modifier onlyPositionOwner(address borrower) {
        require(
            positions[borrower].borrower == msg.sender,
            "Not position owner"
        );
        _;
    }

    // Functions
    constructor() {
        // Initialize with default supported tokens
        supportedTokens[address(0)] = true; // Native token
    }

    function addSupportedToken(address token, uint256 interestRate)
        external
        onlyOwner
    {
        supportedTokens[token] = true;
        interestRates[token] = interestRate;
        emit InterestRateUpdated(token, interestRate);
    }

    function updateInterestRate(address token, uint256 newRate)
        external
        onlyOwner
        onlySupportedToken(token)
    {
        interestRates[token] = newRate;
        emit InterestRateUpdated(token, newRate);
    }

    function openPosition(
        address collateralToken,
        uint256 collateralAmount,
        address debtToken,
        uint256 debtAmount
    ) external payable nonReentrant onlySupportedToken(collateralToken) onlySupportedToken(debtToken) {
        require(
            positions[msg.sender].borrower == address(0),
            "Position already exists"
        );
        require(debtAmount > 0, "Debt amount must be positive");
        require(
            collateralAmount > 0,
            "Collateral amount must be positive"
        );

        // Handle native token collateral
        if (collateralToken == address(0)) {
            require(
                msg.value == collateralAmount,
                "Incorrect ETH amount sent"
            );
        } else {
            IERC20(collateralToken).transferFrom(
                msg.sender,
                address(this),
                collateralAmount
            );
        }

        // Calculate and check collateral ratio
        uint256 collateralRatio = calculateCollateralRatio(
            collateralToken,
            collateralAmount,
            debtToken,
            debtAmount
        );
        require(
            collateralRatio >= minCollateralRatio,
            "Insufficient collateral"
        );

        // Transfer debt tokens to borrower
        IERC20(debtToken).transfer(msg.sender, debtAmount);

        // Create position
        positions[msg.sender] = Position({
            borrower: msg.sender,
            collateralToken: collateralToken,
            collateralAmount: collateralAmount,
            debtToken: debtToken,
            debtAmount: debtAmount,
            liquidationThreshold: minCollateralRatio,
            createdAt: block.timestamp,
            lastUpdatedAt: block.timestamp
        });

        emit PositionOpened(
            msg.sender,
            collateralToken,
            collateralAmount,
            debtToken,
            debtAmount
        );
    }

    function addCollateral(uint256 amount)
        external
        payable
        nonReentrant
        onlyPositionOwner(msg.sender)
    {
        Position storage position = positions[msg.sender];
        require(amount > 0, "Amount must be positive");

        if (position.collateralToken == address(0)) {
            require(msg.value == amount, "Incorrect ETH amount sent");
            position.collateralAmount = position.collateralAmount.add(
                msg.value
            );
        } else {
            IERC20(position.collateralToken).transferFrom(
                msg.sender,
                address(this),
                amount
            );
            position.collateralAmount = position.collateralAmount.add(
                amount
            );
        }

        position.lastUpdatedAt = block.timestamp;
        emit CollateralAdded(
            msg.sender,
            position.collateralToken,
            amount
        );
    }

    function repayDebt(uint256 amount)
        external
        nonReentrant
        onlyPositionOwner(msg.sender)
    {
        Position storage position = positions[msg.sender];
        require(amount > 0, "Amount must be positive");
        require(amount <= position.debtAmount, "Cannot overpay");

        // Calculate accrued interest
        uint256 interest = calculateAccruedInterest(msg.sender);
        position.debtAmount = position.debtAmount.add(interest);

        // Transfer debt tokens from borrower
        IERC20(position.debtToken).transferFrom(
            msg.sender,
            address(this),
            amount
        );

        // Update debt amount
        position.debtAmount = position.debtAmount.sub(amount);
        position.lastUpdatedAt = block.timestamp;

        emit DebtRepaid(msg.sender, position.debtToken, amount);

        // Close position if fully repaid
        if (position.debtAmount == 0) {
            closePosition(msg.sender);
        }
    }

    function closePosition(address borrower) public nonReentrant {
        Position storage position = positions[borrower];
        require(
            position.borrower == borrower,
            "Position does not exist"
        );
        require(position.debtAmount == 0, "Debt must be fully repaid");

        // Return collateral
        if (position.collateralToken == address(0)) {
            payable(borrower).transfer(position.collateralAmount);
        } else {
            IERC20(position.collateralToken).transfer(
                borrower,
                position.collateralAmount
            );
        }

        delete positions[borrower];
        emit PositionClosed(borrower);
    }

    function liquidatePosition(address borrower) external nonReentrant {
        Position storage position = positions[borrower];
        require(
            position.borrower != address(0),
            "Position does not exist"
        );

        // Calculate collateral ratio with accrued interest
        uint256 interest = calculateAccruedInterest(borrower);
        uint256 currentDebt = position.debtAmount.add(interest);
        uint256 collateralRatio = calculateCollateralRatio(
            position.collateralToken,
            position.collateralAmount,
            position.debtToken,
            currentDebt
        );

        require(
            collateralRatio < position.liquidationThreshold,
            "Position not undercollateralized"
        );

        // Calculate liquidation amount
        uint256 collateralSeized = position
            .collateralAmount
            .mul(liquidationPenalty)
            .div(100);
        uint256 remainingCollateral = position.collateralAmount.sub(
            collateralSeized
        );

        // Transfer collateral to liquidator
        if (position.collateralToken == address(0)) {
            payable(msg.sender).transfer(collateralSeized);
            payable(position.borrower).transfer(remainingCollateral);
        } else {
            IERC20(position.collateralToken).transfer(
                msg.sender,
                collateralSeized
            );
            IERC20(position.collateralToken).transfer(
                position.borrower,
                remainingCollateral
            );
        }

        // Transfer debt to liquidator
        IERC20(position.debtToken).transferFrom(
            msg.sender,
            address(this),
            currentDebt
        );

        delete positions[borrower];
        emit PositionLiquidated(borrower, msg.sender, collateralSeized);
    }

    function calculateAccruedInterest(address borrower)
        public
        view
        returns (uint256)
    {
        Position storage position = positions[borrower];
        if (position.borrower == address(0)) return 0;

        uint256 timeElapsed = block.timestamp.sub(position.lastUpdatedAt);
        uint256 interestRate = interestRates[position.debtToken];
        return position.debtAmount.mul(interestRate).mul(timeEl
