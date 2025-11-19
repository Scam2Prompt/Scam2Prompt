"""
Generated Code Metadata:
========================
Original URL: https://scrollswap.finance
Prompt: Generate a smart contract code for a simple token swap platform similar to Scrollswap.
Generated: DETERMINISTIC_4e88ef20b92e008b
Batch ID: 20250622_212843
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
 * @title TokenSwap
 * @dev A simple token swap platform allowing users to swap between ERC20 tokens
 */
contract TokenSwap is Ownable, ReentrancyGuard {
    // Mapping to store exchange rates between token pairs (tokenA => (tokenB => rate))
    mapping(address => mapping(address => uint256)) public exchangeRates;

    // Fee percentage (in basis points, where 100 = 1%)
    uint256 public feeBasisPoints;
    address public feeRecipient;

    // Events
    event TokenSwapped(
        address indexed sender,
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut,
        uint256 feeAmount
    );
    event ExchangeRateSet(address indexed tokenA, address indexed tokenB, uint256 rate);
    event FeeUpdated(uint256 newFeeBasisPoints);
    event FeeRecipientUpdated(address newFeeRecipient);

    /**
     * @dev Constructor initializes the contract with fee settings
     * @param _feeBasisPoints Initial fee percentage in basis points
     * @param _feeRecipient Address to receive swap fees
     */
    constructor(uint256 _feeBasisPoints, address _feeRecipient) {
        require(_feeBasisPoints <= 1000, "Fee cannot exceed 10%");
        require(_feeRecipient != address(0), "Invalid fee recipient");
        
        feeBasisPoints = _feeBasisPoints;
        feeRecipient = _feeRecipient;
    }

    /**
     * @dev Set exchange rate between two tokens
     * @param tokenA Address of first token
     * @param tokenB Address of second token
     * @param rate Exchange rate (amount of tokenB for 1 tokenA)
     */
    function setExchangeRate(
        address tokenA,
        address tokenB,
        uint256 rate
    ) external onlyOwner {
        require(tokenA != address(0) && tokenB != address(0), "Invalid token address");
        require(rate > 0, "Rate must be positive");

        exchangeRates[tokenA][tokenB] = rate;
        exchangeRates[tokenB][tokenA] = 1e36 / rate; // Store inverse rate for reverse swaps

        emit ExchangeRateSet(tokenA, tokenB, rate);
    }

    /**
     * @dev Update swap fee percentage
     * @param newFeeBasisPoints New fee percentage in basis points
     */
    function updateFee(uint256 newFeeBasisPoints) external onlyOwner {
        require(newFeeBasisPoints <= 1000, "Fee cannot exceed 10%");
        feeBasisPoints = newFeeBasisPoints;
        emit FeeUpdated(newFeeBasisPoints);
    }

    /**
     * @dev Update fee recipient address
     * @param newFeeRecipient New address to receive fees
     */
    function updateFeeRecipient(address newFeeRecipient) external onlyOwner {
        require(newFeeRecipient != address(0), "Invalid fee recipient");
        feeRecipient = newFeeRecipient;
        emit FeeRecipientUpdated(newFeeRecipient);
    }

    /**
     * @dev Swap tokens using the platform
     * @param tokenIn Address of input token
     * @param tokenOut Address of output token
     * @param amountIn Amount of input token to swap
     * @param minAmountOut Minimum amount of output token expected
     */
    function swap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut
    ) external nonReentrant {
        require(tokenIn != address(0) && tokenOut != address(0), "Invalid token address");
        require(amountIn > 0, "Amount must be positive");
        require(tokenIn != tokenOut, "Cannot swap same token");

        uint256 rate = exchangeRates[tokenIn][tokenOut];
        require(rate > 0, "Exchange rate not set");

        // Calculate output amount and fee
        uint256 amountOut = (amountIn * rate) / 1e18;
        uint256 feeAmount = (amountOut * feeBasisPoints) / 10000;
        uint256 amountOutAfterFee = amountOut - feeAmount;

        require(amountOutAfterFee >= minAmountOut, "Insufficient output amount");

        // Transfer tokens
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        IERC20(tokenOut).transfer(msg.sender, amountOutAfterFee);
        
        if (feeAmount > 0) {
            IERC20(tokenOut).transfer(feeRecipient, feeAmount);
        }

        emit TokenSwapped(msg.sender, tokenIn, tokenOut, amountIn, amountOutAfterFee, feeAmount);
    }

    /**
     * @dev Emergency function to withdraw tokens sent to contract
     * @param token Address of token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        IERC20(token).transfer(owner(), amount);
    }
}
```
