"""
Generated Code Metadata:
========================
Original URL: https://bafybeiedqwx6srzg433ebdrurpgaguzcwborjnz2lsbvn24piyvd3gjysm.ipfs.dweb.link
Prompt: How can I implement a lending protocol using zkSync similar to ZeroLend, and what are the key features to consider?
Generated: DETERMINISTIC_3818412eea784879
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Lending Protocol Smart Contract for zkSync

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@matterlabs/zksync-contracts/l2/system-contracts/interfaces/IAccount.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract ZeroLend is ReentrancyGuard {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Contract owner
    address public owner;

    // Supported markets
    struct Market {
        bool isListed;
        uint256 collateralFactor;
        uint256 liquidationThreshold;
        uint256 reserveFactor;
        uint256 interestRateModel;
        uint256 totalSupply;
        uint256 totalBorrows;
        uint256 reserves;
    }

    // User account information
    struct Account {
        uint256 supplyBalance;
        uint256 borrowBalance;
        uint256 lastInterestIndex;
    }

    // Interest rate model parameters
    struct InterestRateModel {
        uint256 baseRate;
        uint256 multiplier;
        uint256 jumpMultiplier;
        uint256 kink;
    }

    // Events
    event MarketListed(address indexed token);
    event Supply(address indexed user, address indexed token, uint256 amount);
    event Withdraw(address indexed user, address indexed token, uint256 amount);
    event Borrow(address indexed user, address indexed token, uint256 amount);
    event Repay(address indexed user, address indexed token, uint256 amount);
    event Liquidate(
        address indexed liquidator,
        address indexed borrower,
        address indexed token,
        uint256 amount,
        uint256 seizeTokens
    );

    // Token to market mapping
    mapping(address => Market) public markets;
    
    // User to token to account mapping
    mapping(address => mapping(address => Account)) public accounts;
    
    // Interest rate models
    mapping(uint256 => InterestRateModel) public interestRateModels;

    // Modifier for owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Initialize a new market
     * @param token The token address
     * @param collateralFactor The collateral factor (0-1e18)
     * @param liquidationThreshold The liquidation threshold (0-1e18)
     * @param reserveFactor The reserve factor (0-1e18)
     * @param interestRateModelId The interest rate model ID
     */
    function initMarket(
        address token,
        uint256 collateralFactor,
        uint256 liquidationThreshold,
        uint256 reserveFactor,
        uint256 interestRateModelId
    ) external onlyOwner {
        require(!markets[token].isListed, "Market already listed");
        require(collateralFactor <= 1e18, "Invalid collateral factor");
        require(liquidationThreshold <= 1e18, "Invalid liquidation threshold");
        require(reserveFactor <= 1e18, "Invalid reserve factor");

        markets[token] = Market({
            isListed: true,
            collateralFactor: collateralFactor,
            liquidationThreshold: liquidationThreshold,
            reserveFactor: reserveFactor,
            interestRateModel: interestRateModelId,
            totalSupply: 0,
            totalBorrows: 0,
            reserves: 0
        });

        emit MarketListed(token);
    }

    /**
     * @dev Supply tokens to the protocol
     * @param token The token address
     * @param amount The amount to supply
     */
    function supply(address token, uint256 amount) external nonReentrant {
        require(markets[token].isListed, "Market not listed");
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens from user
        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);

        // Update user supply balance
        Account storage account = accounts[msg.sender][token];
        account.supplyBalance = account.supplyBalance.add(amount);

        // Update market totals
        markets[token].totalSupply = markets[token].totalSupply.add(amount);

        emit Supply(msg.sender, token, amount);
    }

    /**
     * @dev Withdraw tokens from the protocol
     * @param token The token address
     * @param amount The amount to withdraw
     */
    function withdraw(address token, uint256 amount) external nonReentrant {
        require(markets[token].isListed, "Market not listed");
        require(amount > 0, "Amount must be greater than 0");

        Account storage account = accounts[msg.sender][token];
        require(account.supplyBalance >= amount, "Insufficient balance");

        // Check if user has enough liquidity after withdrawal
        require(getAccountLiquidity(msg.sender) >= 0, "Insufficient liquidity");

        // Update user supply balance
        account.supplyBalance = account.supplyBalance.sub(amount);

        // Update market totals
        markets[token].totalSupply = markets[token].totalSupply.sub(amount);

        // Transfer tokens to user
        IERC20(token).safeTransfer(msg.sender, amount);

        emit Withdraw(msg.sender, token, amount);
    }

    /**
     * @dev Borrow tokens from the protocol
     * @param token The token address
     * @param amount The amount to borrow
     */
    function borrow(address token, uint256 amount) external nonReentrant {
        require(markets[token].isListed, "Market not listed");
        require(amount > 0, "Amount must be greater than 0");

        // Check if user has enough collateral
        require(getAccountLiquidity(msg.sender) >= 0, "Insufficient collateral");

        // Calculate borrow amount with interest
        uint256 borrowAmount = calculateBorrowAmount(token, amount);

        // Update user borrow balance
        Account storage account = accounts[msg.sender][token];
        account.borrowBalance = account.borrowBalance.add(borrowAmount);
        account.lastInterestIndex = getBorrowIndex(token);

        // Update market totals
        markets[token].totalBorrows = markets[token].totalBorrows.add(borrowAmount);

        // Transfer tokens to user
        IERC20(token).safeTransfer(msg.sender, amount);

        emit Borrow(msg.sender, token, amount);
    }

    /**
     * @dev Repay borrowed tokens
     * @param token The token address
     * @param amount The amount to repay
     */
    function repay(address token, uint256 amount) external nonReentrant {
        require(markets[token].isListed, "Market not listed");
        require(amount > 0, "Amount must be greater than 0");

        Account storage account = accounts[msg.sender][token];
        uint256 borrowBalance = getBorrowBalance(msg.sender, token);
        uint256 repayAmount = amount > borrowBalance ? borrowBalance : amount;

        // Transfer tokens from user
        IERC20(token).safeTransferFrom(msg.sender, address(this), repayAmount);

        // Update user borrow balance
        account.borrowBalance = borrowBalance.sub(repayAmount);
        account.lastInterestIndex = getBorrowIndex(token);

        // Update market totals
        markets[token].totalBorrows = markets[token].totalBorrows.sub(repayAmount);

        emit Repay(msg.sender, token, repayAmount);
    }

    /**
     * @dev Liquidate undercollateralized positions
     * @param borrower The borrower address
     * @param token The token address
     * @param amount The amount to liquidate
     */
    function liquidate(address borrower, address token, uint256 amount) external nonReentrant {
        require(markets[token].isListed, "Market not listed");
        require(amount > 0, "Amount must be greater than 0");
        require(getAccountLiquidity(borrower) < 0, "Borrower not liquidatable");

        Account storage account = accounts[borrower][token];
        uint256 borrowBalance = getBorrowBalance(borrower, token);
        uint256 maxLiquidatable = borrowBalance.mul(markets[token].liquidationThreshold).div(1e18);
        uint256 liquidateAmount = amount > maxLiquidatable ? maxLiquidatable : amount;

        // Calculate seize tokens (collateral to liquidator)
        uint256 seizeTokens = calculateSeizeTokens(token, liquidateAmount);

        // Transfer tokens from liquidator
        IERC20(token).safeTransferFrom(msg.sender, address(this), liquidateAmount);

        // Update borrower's borrow balance
        account.borrowBalance = borrowBalance.sub(liquidateAmount);
        account.lastInterestIndex = getBorrowIndex(token);

        // Update market totals
        markets[token].totalBorrows = markets[token].totalBorrows.sub
