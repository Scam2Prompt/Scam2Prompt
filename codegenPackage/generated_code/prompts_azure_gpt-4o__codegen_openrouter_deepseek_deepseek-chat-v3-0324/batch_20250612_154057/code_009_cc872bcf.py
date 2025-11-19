"""
Generated Code Metadata:
========================
Original URL: https://hyperswap.tech
Prompt: Recommend best practices for securing transactions on the HyperEVM Native Dex and write code to implement these practices in a blockchain application.
Generated: DETERMINISTIC_cc872bcfbede13ab
Batch ID: 20250612_154057
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
 * @title SecureDEX
 * @dev Implements best practices for securing transactions on HyperEVM Native DEX
 */
contract SecureDEX is Ownable, ReentrancyGuard {
    // Token addresses
    address public tokenA;
    address public tokenB;

    // Exchange rate tracking
    uint256 public exchangeRate;
    uint256 public lastUpdate;

    // Minimum and maximum trade amounts
    uint256 public minTradeAmount;
    uint256 public maxTradeAmount;

    // Trade fee percentage (basis points)
    uint256 public tradeFeeBps = 30; // 0.3%

    // Events
    event TokensSwapped(
        address indexed user,
        address fromToken,
        address toToken,
        uint256 fromAmount,
        uint256 toAmount,
        uint256 fee
    );
    event ExchangeRateUpdated(uint256 newRate);
    event TradeLimitsUpdated(uint256 min, uint256 max);

    /**
     * @dev Constructor initializes the DEX with token pairs
     * @param _tokenA Address of first token
     * @param _tokenB Address of second token
     * @param initialRate Initial exchange rate (tokenA per tokenB)
     */
    constructor(
        address _tokenA,
        address _tokenB,
        uint256 initialRate
    ) {
        require(_tokenA != address(0) && _tokenB != address(0), "Invalid token address");
        require(_tokenA != _tokenB, "Tokens must be different");
        require(initialRate > 0, "Exchange rate must be positive");

        tokenA = _tokenA;
        tokenB = _tokenB;
        exchangeRate = initialRate;
        lastUpdate = block.timestamp;
    }

    /**
     * @dev Set trade amount limits
     * @param min Minimum trade amount
     * @param max Maximum trade amount
     */
    function setTradeLimits(uint256 min, uint256 max) external onlyOwner {
        require(min < max, "Min must be less than max");
        minTradeAmount = min;
        maxTradeAmount = max;
        emit TradeLimitsUpdated(min, max);
    }

    /**
     * @dev Update exchange rate (only owner)
     * @param newRate New exchange rate (tokenA per tokenB)
     */
    function updateExchangeRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Exchange rate must be positive");
        require(block.timestamp > lastUpdate + 1 hours, "Rate can't be updated more than once per hour");

        exchangeRate = newRate;
        lastUpdate = block.timestamp;
        emit ExchangeRateUpdated(newRate);
    }

    /**
     * @dev Swap tokens with security checks
     * @param fromToken Token to swap from
     * @param toToken Token to swap to
     * @param amount Amount to swap
     */
    function swapTokens(
        address fromToken,
        address toToken,
        uint256 amount
    ) external nonReentrant {
        // Validate input parameters
        require(
            (fromToken == tokenA && toToken == tokenB) || (fromToken == tokenB && toToken == tokenA),
            "Invalid token pair"
        );
        require(amount >= minTradeAmount, "Amount below minimum");
        require(amount <= maxTradeAmount, "Amount exceeds maximum");

        // Calculate expected amount with fee
        uint256 expectedAmount = calculateExpectedAmount(fromToken, toToken, amount);
        uint256 fee = (amount * tradeFeeBps) / 10000;

        // Transfer tokens from user
        IERC20(fromToken).transferFrom(msg.sender, address(this), amount);

        // Verify token balances
        uint256 balanceBefore = IERC20(toToken).balanceOf(address(this));
        require(balanceBefore >= expectedAmount, "Insufficient liquidity");

        // Transfer tokens to user
        IERC20(toToken).transfer(msg.sender, expectedAmount);

        // Verify transfer was successful
        uint256 balanceAfter = IERC20(toToken).balanceOf(address(this));
        require(balanceBefore - balanceAfter == expectedAmount, "Transfer verification failed");

        emit TokensSwapped(msg.sender, fromToken, toToken, amount, expectedAmount, fee);
    }

    /**
     * @dev Calculate expected amount after exchange rate and fee
     * @param fromToken Token to swap from
     * @param toToken Token to swap to
     * @param amount Amount to swap
     * @return Expected amount of toToken
     */
    function calculateExpectedAmount(
        address fromToken,
        address toToken,
        uint256 amount
    ) public view returns (uint256) {
        uint256 rate = (fromToken == tokenA) ? exchangeRate : (1e18 * 1e18) / exchangeRate;
        uint256 amountAfterFee = amount - ((amount * tradeFeeBps) / 10000);
        return (amountAfterFee * rate) / 1e18;
    }

    /**
     * @dev Emergency withdraw tokens (only owner)
     * @param token Address of token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner(), amount);
    }

    /**
     * @dev Get current liquidity for a token
     * @param token Address of token to check
     * @return Current balance of token in contract
     */
    function getLiquidity(address token) external view returns (uint256) {
        return IERC20(token).balanceOf(address(this));
    }
}
```
