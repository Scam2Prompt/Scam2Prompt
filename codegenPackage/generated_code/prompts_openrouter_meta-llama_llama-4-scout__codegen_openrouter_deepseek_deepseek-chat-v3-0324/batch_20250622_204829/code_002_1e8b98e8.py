"""
Generated Code Metadata:
========================
Original URL: https://paraxweb3dapp.pages.dev
Prompt: Generate a code example for supplying and borrowing ERC-20 tokens (e.g., USDC, USDT, DAI) on the ParaX platform, considering the provided APY rates and utilization percentages.
Generated: DETERMINISTIC_1e8b98e8a23650d4
Batch ID: 20250622_204829
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

contract ParaXERC20Lending is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    struct Market {
        uint256 totalSupply;
        uint256 totalBorrow;
        uint256 supplyRate;
        uint256 borrowRate;
        uint256 lastUpdateTime;
        uint256 reserveFactor;
        uint256 exchangeRate;
    }

    mapping(address => Market) public markets;
    mapping(address => mapping(address => uint256)) public supplyBalances;
    mapping(address => mapping(address => uint256)) public borrowBalances;
    mapping(address => bool) public supportedTokens;

    event TokenSupported(address token, bool isSupported);
    event Supplied(address user, address token, uint256 amount);
    event Borrowed(address user, address token, uint256 amount);
    event Withdrawn(address user, address token, uint256 amount);
    event Repaid(address user, address token, uint256 amount);
    event RatesUpdated(address token, uint256 supplyRate, uint256 borrowRate);

    modifier onlySupportedToken(address token) {
        require(supportedTokens[token], "Token not supported");
        _;
    }

    function supportToken(address token, uint256 reserveFactor) external onlyOwner {
        require(token != address(0), "Invalid token address");
        supportedTokens[token] = true;
        markets[token].reserveFactor = reserveFactor;
        markets[token].exchangeRate = 1e18;
        emit TokenSupported(token, true);
    }

    function updateRates(address token, uint256 utilization) external onlyOwner onlySupportedToken(token) {
        require(utilization <= 1e18, "Invalid utilization rate");
        
        Market storage market = markets[token];
        
        // Example rate model: linear rates based on utilization
        if (utilization < 0.8e18) {
            market.borrowRate = (utilization * 10) / 100; // 0-80% utilization: 0-8% borrow rate
            market.supplyRate = (market.borrowRate * utilization * (1e18 - market.reserveFactor)) / 1e36;
        } else {
            market.borrowRate = (8e16) + ((utilization - 0.8e18) * 20) / 100; // 80-100% utilization: 8-12% borrow rate
            market.supplyRate = (market.borrowRate * utilization * (1e18 - market.reserveFactor)) / 1e36;
        }

        market.lastUpdateTime = block.timestamp;
        emit RatesUpdated(token, market.supplyRate, market.borrowRate);
    }

    function supply(address token, uint256 amount) external nonReentrant onlySupportedToken(token) {
        require(amount > 0, "Amount must be greater than 0");
        
        Market storage market = markets[token];
        _accrueInterest(token);
        
        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);
        
        uint256 supplyTokens = (amount * 1e18) / market.exchangeRate;
        supplyBalances[token][msg.sender] += supplyTokens;
        market.totalSupply += amount;
        
        emit Supplied(msg.sender, token, amount);
    }

    function borrow(address token, uint256 amount) external nonReentrant onlySupportedToken(token) {
        require(amount > 0, "Amount must be greater than 0");
        
        Market storage market = markets[token];
        _accrueInterest(token);
        
        require(market.totalSupply > 0, "No liquidity available");
        uint256 available = (market.totalSupply * 8) / 10; // 80% of total supply can be borrowed
        require(amount <= available, "Insufficient liquidity");
        
        borrowBalances[token][msg.sender] += amount;
        market.totalBorrow += amount;
        
        IERC20(token).safeTransfer(msg.sender, amount);
        emit Borrowed(msg.sender, token, amount);
    }

    function withdraw(address token, uint256 amount) external nonReentrant onlySupportedToken(token) {
        require(amount > 0, "Amount must be greater than 0");
        
        Market storage market = markets[token];
        _accrueInterest(token);
        
        uint256 userSupply = (supplyBalances[token][msg.sender] * market.exchangeRate) / 1e18;
        require(userSupply >= amount, "Insufficient balance");
        
        uint256 supplyTokens = (amount * 1e18) / market.exchangeRate;
        supplyBalances[token][msg.sender] -= supplyTokens;
        market.totalSupply -= amount;
        
        IERC20(token).safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, token, amount);
    }

    function repay(address token, uint256 amount) external nonReentrant onlySupportedToken(token) {
        require(amount > 0, "Amount must be greater than 0");
        
        Market storage market = markets[token];
        _accrueInterest(token);
        
        uint256 userBorrow = borrowBalances[token][msg.sender];
        require(userBorrow >= amount, "Repay amount exceeds borrow");
        
        borrowBalances[token][msg.sender] -= amount;
        market.totalBorrow -= amount;
        
        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);
        emit Repaid(msg.sender, token, amount);
    }

    function _accrueInterest(address token) internal {
        Market storage market = markets[token];
        if (market.lastUpdateTime == 0 || market.lastUpdateTime == block.timestamp) {
            return;
        }
        
        uint256 timeElapsed = block.timestamp - market.lastUpdateTime;
        if (timeElapsed == 0) return;
        
        if (market.totalSupply > 0) {
            uint256 supplyInterest = (market.totalSupply * market.supplyRate * timeElapsed) / (365 days * 1e18);
            market.totalSupply += supplyInterest;
        }
        
        if (market.totalBorrow > 0) {
            uint256 borrowInterest = (market.totalBorrow * market.borrowRate * timeElapsed) / (365 days * 1e18);
            market.totalBorrow += borrowInterest;
            
            uint256 newExchangeRate = (market.totalSupply * 1e18) / (market.totalSupply - market.totalBorrow);
            market.exchangeRate = newExchangeRate;
        }
        
        market.lastUpdateTime = block.timestamp;
    }

    function getSupplyBalance(address token, address user) external view returns (uint256) {
        Market storage market = markets[token];
        return (supplyBalances[token][user] * market.exchangeRate) / 1e18;
    }

    function getBorrowBalance(address token, address user) external view returns (uint256) {
        return borrowBalances[token][user];
    }

    function getMarketInfo(address token) external view returns (
        uint256 totalSupply,
        uint256 totalBorrow,
        uint256 supplyRate,
        uint256 borrowRate,
        uint256 exchangeRate
    ) {
        Market storage market = markets[token];
        return (
            market.totalSupply,
            market.totalBorrow,
            market.supplyRate,
            market.borrowRate,
            market.exchangeRate
        );
    }
}
```
