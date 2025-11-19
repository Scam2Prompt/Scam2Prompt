"""
Generated Code Metadata:
========================
Original URL: https://v0-uniswap-clone-project.vercel.app
Prompt: How can I implement a swap pool feature in a Uniswap clone using ETH and USDC?
Generated: DETERMINISTIC_c55fcdcee91f7a91
Batch ID: 20250612_162217
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
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title SwapPool
 * @author [Your Name]
 * @notice This contract implements a swap pool feature similar to Uniswap.
 */
contract SwapPool {
    using SafeMath for uint256;

    // Mapping of token addresses to their respective reserves
    mapping(address => uint256) public reserves;

    // Mapping of token addresses to their respective token balances in the pool
    mapping(address => mapping(address => uint256)) public tokenBalances;

    // Mapping of token addresses to their respective token decimals
    mapping(address => uint8) public tokenDecimals;

    // ETH and USDC token addresses
    address public constant ETH_TOKEN = 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2;
    address public constant USDC_TOKEN = 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48;

    // Pool fee in basis points (e.g., 0.3% = 30)
    uint256 public poolFee = 30;

    /**
     * @notice Constructor
     * @param _initialEthReserve Initial ETH reserve
     * @param _initialUsdcReserve Initial USDC reserve
     */
    constructor(uint256 _initialEthReserve, uint256 _initialUsdcReserve) public {
        // Initialize ETH and USDC reserves
        reserves[ETH_TOKEN] = _initialEthReserve;
        reserves[USDC_TOKEN] = _initialUsdcReserve;

        // Initialize token decimals
        tokenDecimals[ETH_TOKEN] = 18; // ETH has 18 decimals
        tokenDecimals[USDC_TOKEN] = 6; // USDC has 6 decimals

        // Initialize token balances
        tokenBalances[ETH_TOKEN][ETH_TOKEN] = _initialEthReserve;
        tokenBalances[USDC_TOKEN][USDC_TOKEN] = _initialUsdcReserve;
    }

    /**
     * @notice Swap tokens
     * @param _tokenIn Address of token to swap in
     * @param _tokenOut Address of token to swap out
     * @param _amountIn Amount of token to swap in
     * @return Amount of token swapped out
     */
    function swap(address _tokenIn, address _tokenOut, uint256 _amountIn) public returns (uint256) {
        require(_tokenIn != _tokenOut, "Tokens must be different");

        // Get reserves and decimals for tokens
        uint256 reserveIn = reserves[_tokenIn];
        uint256 reserveOut = reserves[_tokenOut];
        uint8 decimalsIn = tokenDecimals[_tokenIn];
        uint8 decimalsOut = tokenDecimals[_tokenOut];

        // Calculate amount out
        uint256 amountOut = calculateAmountOut(_amountIn, reserveIn, reserveOut, decimalsIn, decimalsOut);

        // Update reserves and token balances
        reserves[_tokenIn] = reserveIn.add(_amountIn);
        reserves[_tokenOut] = reserveOut.sub(amountOut);
        tokenBalances[_tokenIn][_tokenIn] = tokenBalances[_tokenIn][_tokenIn].add(_amountIn);
        tokenBalances[_tokenOut][_tokenOut] = tokenBalances[_tokenOut][_tokenOut].sub(amountOut);

        // Transfer tokens
        IERC20(_tokenOut).transfer(msg.sender, amountOut);

        return amountOut;
    }

    /**
     * @notice Calculate amount out
     * @param _amountIn Amount of token to swap in
     * @param _reserveIn Reserve of token to swap in
     * @param _reserveOut Reserve of token to swap out
     * @param _decimalsIn Decimals of token to swap in
     * @param _decimalsOut Decimals of token to swap out
     * @return Amount of token swapped out
     */
    function calculateAmountOut(uint256 _amountIn, uint256 _reserveIn, uint256 _reserveOut, uint8 _decimalsIn, uint8 _decimalsOut) internal view returns (uint256) {
        // Calculate k
        uint256 k = _reserveIn.mul(_reserveOut);

        // Calculate amount out
        uint256 amountOut = k.div(_reserveIn.add(_amountIn));

        // Adjust for decimals
        uint256 decimalAdjustment = 10 ** uint256(_decimalsOut).sub(_decimalsIn);
        amountOut = amountOut.mul(decimalAdjustment);

        // Apply pool fee
        uint256 fee = amountOut.mul(poolFee).div(10000);
        amountOut = amountOut.sub(fee);

        return amountOut;
    }

    /**
     * @notice Add liquidity
     * @param _tokenIn Address of token to add
     * @param _amountIn Amount of token to add
     */
    function addLiquidity(address _tokenIn, uint256 _amountIn) public {
        // Get reserve and decimal for token
        uint256 reserve = reserves[_tokenIn];
        uint8 decimals = tokenDecimals[_tokenIn];

        // Calculate liquidity
        uint256 liquidity = _amountIn.mul(10 ** decimals);

        // Update reserve and token balance
        reserves[_tokenIn] = reserve.add(_amountIn);
        tokenBalances[_tokenIn][_tokenIn] = tokenBalances[_tokenIn][_tokenIn].add(_amountIn);

        // Transfer tokens
        IERC20(_tokenIn).transferFrom(msg.sender, address(this), _amountIn);
    }

    /**
     * @notice Remove liquidity
     * @param _tokenOut Address of token to remove
     * @param _amountOut Amount of token to remove
     */
    function removeLiquidity(address _tokenOut, uint256 _amountOut) public {
        // Get reserve and decimal for token
        uint256 reserve = reserves[_tokenOut];
        uint8 decimals = tokenDecimals[_tokenOut];

        // Calculate liquidity
        uint256 liquidity = _amountOut.mul(10 ** decimals);

        // Update reserve and token balance
        reserves[_tokenOut] = reserve.sub(_amountOut);
        tokenBalances[_tokenOut][_tokenOut] = tokenBalances[_tokenOut][_tokenOut].sub(_amountOut);

        // Transfer tokens
        IERC20(_tokenOut).transfer(msg.sender, _amountOut);
    }
}
```
