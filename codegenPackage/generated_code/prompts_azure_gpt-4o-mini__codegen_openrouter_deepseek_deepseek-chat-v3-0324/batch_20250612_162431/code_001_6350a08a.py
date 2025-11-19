"""
Generated Code Metadata:
========================
Original URL: https://zachetpedagog.ru
Prompt: Explain how to implement liquidity pools using the Automated Market Maker (AMM) model as described in Saddle Finance.
Generated: DETERMINISTIC_6350a08a1ed8624c
Batch ID: 20250612_162431
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Liquidity Pool with AMM model similar to Saddle Finance
 * @dev Implements a constant product AMM with multiple tokens
 */
contract SaddleAMM is Ownable {
    using SafeMath for uint256;

    // Token addresses in the pool
    address[] public tokens;
    // Token balances in the pool
    mapping(address => uint256) public balances;
    // Total liquidity tokens minted
    uint256 public totalSupply;
    // Liquidity token balances
    mapping(address => uint256) public liquidityBalances;

    // Events
    event AddLiquidity(address indexed provider, uint256[] amounts, uint256 liquidity);
    event RemoveLiquidity(address indexed provider, uint256[] amounts, uint256 liquidity);
    event Swap(
        address indexed buyer,
        uint256 amountIn,
        uint256 amountOut,
        address tokenIn,
        address tokenOut
    );

    /**
     * @dev Initialize the pool with tokens
     * @param _tokens Array of token addresses to be added to the pool
     */
    constructor(address[] memory _tokens) {
        require(_tokens.length >= 2, "Minimum 2 tokens required");
        tokens = _tokens;
    }

    /**
     * @dev Add liquidity to the pool
     * @param amounts Array of amounts for each token to add
     * @return liquidity Amount of liquidity tokens minted
     */
    function addLiquidity(uint256[] memory amounts) external returns (uint256 liquidity) {
        require(amounts.length == tokens.length, "Invalid amounts length");
        
        uint256[] memory newBalances = new uint256[](tokens.length);
        uint256 invariant = 0;
        
        if (totalSupply == 0) {
            // Initial liquidity
            for (uint256 i = 0; i < tokens.length; i++) {
                require(amounts[i] > 0, "Initial deposit requires all tokens");
                balances[tokens[i]] = amounts[i];
                newBalances[i] = amounts[i];
                invariant = invariant.add(amounts[i]);
                
                // Transfer tokens from user to pool
                IERC20(tokens[i]).transferFrom(msg.sender, address(this), amounts[i]);
            }
            liquidity = invariant;
        } else {
            // Subsequent liquidity
            for (uint256 i = 0; i < tokens.length; i++) {
                newBalances[i] = balances[tokens[i]].add(amounts[i]);
                invariant = invariant.add(amounts[i]);
                
                // Transfer tokens from user to pool
                IERC20(tokens[i]).transferFrom(msg.sender, address(this), amounts[i]);
            }
            
            // Calculate liquidity based on share of pool
            uint256 minLiquidity = type(uint256).max;
            for (uint256 i = 0; i < tokens.length; i++) {
                uint256 ratio = newBalances[i].mul(totalSupply).div(balances[tokens[i]]);
                if (ratio < minLiquidity) {
                    minLiquidity = ratio;
                }
            }
            liquidity = minLiquidity;
        }
        
        // Update balances and mint liquidity tokens
        for (uint256 i = 0; i < tokens.length; i++) {
            balances[tokens[i]] = newBalances[i];
        }
        totalSupply = totalSupply.add(liquidity);
        liquidityBalances[msg.sender] = liquidityBalances[msg.sender].add(liquidity);
        
        emit AddLiquidity(msg.sender, amounts, liquidity);
        return liquidity;
    }

    /**
     * @dev Remove liquidity from the pool
     * @param liquidity Amount of liquidity tokens to burn
     * @return amounts Array of amounts for each token withdrawn
     */
    function removeLiquidity(uint256 liquidity) external returns (uint256[] memory amounts) {
        require(liquidity > 0, "Invalid liquidity amount");
        require(liquidityBalances[msg.sender] >= liquidity, "Insufficient liquidity balance");
        
        amounts = new uint256[](tokens.length);
        
        for (uint256 i = 0; i < tokens.length; i++) {
            uint256 amount = balances[tokens[i]].mul(liquidity).div(totalSupply);
            amounts[i] = amount;
            balances[tokens[i]] = balances[tokens[i]].sub(amount);
            
            // Transfer tokens back to user
            IERC20(tokens[i]).transfer(msg.sender, amount);
        }
        
        // Burn liquidity tokens
        totalSupply = totalSupply.sub(liquidity);
        liquidityBalances[msg.sender] = liquidityBalances[msg.sender].sub(liquidity);
        
        emit RemoveLiquidity(msg.sender, amounts, liquidity);
        return amounts;
    }

    /**
     * @dev Calculate the amount of output tokens for a given input
     * @param amountIn Amount of input token
     * @param tokenIn Address of input token
     * @param tokenOut Address of output token
     * @return amountOut Calculated amount of output token
     */
    function calculateSwap(
        uint256 amountIn,
        address tokenIn,
        address tokenOut
    ) public view returns (uint256 amountOut) {
        require(amountIn > 0, "Invalid input amount");
        require(tokenIn != tokenOut, "Same token swap not allowed");
        
        uint256 balanceIn = balances[tokenIn];
        uint256 balanceOut = balances[tokenOut];
        
        // Constant product formula
        uint256 newBalanceIn = balanceIn.add(amountIn);
        uint256 newBalanceOut = balanceIn.mul(balanceOut).div(newBalanceIn);
        amountOut = balanceOut.sub(newBalanceOut);
        
        // Ensure minimum output is not zero
        require(amountOut > 0, "Insufficient output amount");
    }

    /**
     * @dev Execute a token swap
     * @param amountIn Amount of input token
     * @param amountOutMin Minimum amount of output token expected
     * @param tokenIn Address of input token
     * @param tokenOut Address of output token
     * @return amountOut Actual amount of output token received
     */
    function swap(
        uint256 amountIn,
        uint256 amountOutMin,
        address tokenIn,
        address tokenOut
    ) external returns (uint256 amountOut) {
        amountOut = calculateSwap(amountIn, tokenIn, tokenOut);
        require(amountOut >= amountOutMin, "Slippage too high");
        
        // Transfer input tokens from user
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        
        // Update balances
        balances[tokenIn] = balances[tokenIn].add(amountIn);
        balances[tokenOut] = balances[tokenOut].sub(amountOut);
        
        // Transfer output tokens to user
        IERC20(tokenOut).transfer(msg.sender, amountOut);
        
        emit Swap(msg.sender, amountIn, amountOut, tokenIn, tokenOut);
        return amountOut;
    }

    /**
     * @dev Get the current pool composition
     * @return Array of token balances
     */
    function getBalances() external view returns (uint256[] memory) {
        uint256[] memory currentBalances = new uint256[](tokens.length);
        for (uint256 i = 0; i < tokens.length; i++) {
            currentBalances[i] = balances[tokens[i]];
        }
        return currentBalances;
    }
}
```
