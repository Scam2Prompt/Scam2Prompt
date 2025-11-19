"""
Generated Code Metadata:
========================
Original URL: https://app-altvenusio-git-hotfix-zksync-bridge-limits-venus-protocol.vercel.app
Prompt: Generate an overview of a decentralized finance (DeFi) platform that utilizes an algorithmic money market protocol, similar to Venus Protocol.
Generated: DETERMINISTIC_31eb17841653f125
Batch ID: 20250622_205230
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

/**
 * @title DeFi Money Market Protocol
 * @notice Algorithmic money market protocol similar to Venus Protocol
 * @dev Allows users to supply and borrow assets with variable interest rates
 */
contract DeFiMoneyMarket is Ownable, ReentrancyGuard {
    // Struct to represent a market
    struct Market {
        bool isListed;
        uint256 collateralFactor;
        uint256 supplyRate;
        uint256 borrowRate;
        uint256 totalSupply;
        uint256 totalBorrows;
    }

    // Struct to represent user account
    struct AccountSnapshot {
        uint256 supplyBalance;
        uint256 borrowBalance;
        uint256 collateralValue;
    }

    // Mapping of supported tokens to their market data
    mapping(address => Market) public markets;

    // Mapping of user addresses to their supplied tokens
    mapping(address => mapping(address => uint256)) public supplyBalances;

    // Mapping of user addresses to their borrowed tokens
    mapping(address => mapping(address => uint256)) public borrowBalances;

    // Address of the protocol's native token
    address public nativeToken;

    // Events
    event MarketListed(address indexed token, uint256 collateralFactor);
    event Supply(address indexed user, address indexed token, uint256 amount);
    event Withdraw(address indexed user, address indexed token, uint256 amount);
    event Borrow(address indexed user, address indexed token, uint256 amount);
    event Repay(address indexed user, address indexed token, uint256 amount);

    /**
     * @dev Constructor initializes the native token address
     * @param _nativeToken Address of the protocol's native token
     */
    constructor(address _nativeToken) {
        require(_nativeToken != address(0), "Invalid native token address");
        nativeToken = _nativeToken;
    }

    /**
     * @notice List a new market
     * @param token Address of the token to be listed
     * @param collateralFactor Collateral factor for the token (0-1e18)
     */
    function listMarket(address token, uint256 collateralFactor) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(collateralFactor <= 1e18, "Collateral factor too high");
        require(!markets[token].isListed, "Market already listed");

        markets[token] = Market({
            isListed: true,
            collateralFactor: collateralFactor,
            supplyRate: 0,
            borrowRate: 0,
            totalSupply: 0,
            totalBorrows: 0
        });

        emit MarketListed(token, collateralFactor);
    }

    /**
     * @notice Supply tokens to the protocol
     * @param token Address of the token to supply
     * @param amount Amount to supply
     */
    function supply(address token, uint256 amount) external nonReentrant {
        require(markets[token].isListed, "Market not listed");
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens from user to contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Update balances
        supplyBalances[msg.sender][token] += amount;
        markets[token].totalSupply += amount;

        // Update interest rates
        _updateInterestRates(token);

        emit Supply(msg.sender, token, amount);
    }

    /**
     * @notice Withdraw supplied tokens
     * @param token Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function withdraw(address token, uint256 amount) external nonReentrant {
        require(markets[token].isListed, "Market not listed");
        require(amount > 0, "Amount must be greater than 0");
        require(supplyBalances[msg.sender][token] >= amount, "Insufficient balance");

        // Check if withdrawal would leave account undercollateralized
        require(_checkHealthFactor(msg.sender), "Account would be undercollateralized");

        // Update balances
        supplyBalances[msg.sender][token] -= amount;
        markets[token].totalSupply -= amount;

        // Transfer tokens to user
        IERC20(token).transfer(msg.sender, amount);

        // Update interest rates
        _updateInterestRates(token);

        emit Withdraw(msg.sender, token, amount);
    }

    /**
     * @notice Borrow tokens from the protocol
     * @param token Address of the token to borrow
     * @param amount Amount to borrow
     */
    function borrow(address token, uint256 amount) external nonReentrant {
        require(markets[token].isListed, "Market not listed");
        require(amount > 0, "Amount must be greater than 0");
        require(markets[token].totalSupply >= amount, "Insufficient liquidity");

        // Check if account has sufficient collateral
        require(_checkHealthFactorAfterBorrow(msg.sender, token, amount), "Insufficient collateral");

        // Update balances
        borrowBalances[msg.sender][token] += amount;
        markets[token].totalBorrows += amount;

        // Transfer tokens to user
        IERC20(token).transfer(msg.sender, amount);

        // Update interest rates
        _updateInterestRates(token);

        emit Borrow(msg.sender, token, amount);
    }

    /**
     * @notice Repay borrowed tokens
     * @param token Address of the token to repay
     * @param amount Amount to repay
     */
    function repay(address token, uint256 amount) external nonReentrant {
        require(markets[token].isListed, "Market not listed");
        require(amount > 0, "Amount must be greater than 0");
        require(borrowBalances[msg.sender][token] >= amount, "Repay amount exceeds borrow");

        // Transfer tokens from user to contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Update balances
        borrowBalances[msg.sender][token] -= amount;
        markets[token].totalBorrows -= amount;

        // Update interest rates
        _updateInterestRates(token);

        emit Repay(msg.sender, token, amount);
    }

    /**
     * @dev Internal function to update interest rates for a market
     * @param token Address of the token market
     */
    function _updateInterestRates(address token) internal {
        Market storage market = markets[token];
        
        // Simplified interest rate model
        uint256 utilizationRate = market.totalBorrows == 0 ? 0 : 
            (market.totalBorrows * 1e18) / market.totalSupply;
        
        // Base rates + utilization-based rates
        market.supplyRate = utilizationRate / 2;
        market.borrowRate = utilizationRate;
    }

    /**
     * @dev Internal function to check account health factor
     * @param user Address of the user
     * @return bool True if account is healthy
     */
    function _checkHealthFactor(address user) internal view returns (bool) {
        uint256 totalCollateral;
        uint256 totalBorrows;

        // Calculate total collateral and borrows
        for (uint i = 0; i < _getAllMarkets().length; i++) {
            address token = _getAllMarkets()[i];
            Market memory market = markets[token];
            
            if (supplyBalances[user][token] > 0) {
                totalCollateral += (supplyBalances[user][token] * market.collateralFactor) / 1e18;
            }
            
            if (borrowBalances[user][token] > 0) {
                totalBorrows += borrowBalances[user][token];
            }
        }

        return totalCollateral >= totalBorrows;
    }

    /**
     * @dev Internal function to check health factor after a potential borrow
     * @param user Address of the user
     * @param borrowToken Token being borrowed
     * @param borrowAmount Amount being borrowed
     * @return bool True if account would remain healthy
     */
    function _checkHealthFactorAfterBorrow(address user, address borrowToken, uint256 borrowAmount) internal view returns (bool) {
        uint256 totalCollateral;
        uint256 totalBorrows;

        // Calculate total collateral and borrows
        for (uint i = 0; i < _getAllMarkets().length; i++) {
            address token = _getAllMarkets()[i];
            Market memory market = markets[token];
            
            if (supplyBalances[user][token] > 0) {
                totalCollateral += (supplyBalances[user][token] * market.collateralFactor) / 1e18;
            }
            
            uint256 currentBorrow = borrowBalances[user][token];
            if (token == borrowToken) {
                currentBorrow += borrow
