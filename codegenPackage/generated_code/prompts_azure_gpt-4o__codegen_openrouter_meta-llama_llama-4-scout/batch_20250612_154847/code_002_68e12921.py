"""
Generated Code Metadata:
========================
Original URL: https://uniswap-clone-gray.vercel.app
Prompt: Generate code for a "Pool" feature that allows users to add liquidity to an Ethereum-based decentralized exchange, inspired by the Uniswap Clone website.
Generated: DETERMINISTIC_68e12921039ab9d1
Batch ID: 20250612_154847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title Pool Contract
 * @author [Your Name]
 * @notice This contract enables users to add liquidity to a decentralized exchange.
 */
contract Pool {
    using SafeMath for uint256;

    // Mapping of liquidity provider addresses to their corresponding liquidity information
    mapping(address => LiquidityProvider) public liquidityProviders;

    // Mapping of token addresses to their corresponding reserves
    mapping(address => mapping(address => uint256)) public reserves;

    // Mapping of token addresses to their corresponding token balances
    mapping(address => uint256) public tokenBalances;

    // Event emitted when liquidity is added
    event AddLiquidity(address indexed provider, address indexed token1, address indexed token2, uint256 amount1, uint256 amount2);

    // Event emitted when liquidity is removed
    event RemoveLiquidity(address indexed provider, address indexed token1, address indexed token2, uint256 amount1, uint256 amount2);

    // Struct to represent liquidity provider information
    struct LiquidityProvider {
        uint256 liquidity;
        mapping(address => mapping(address => uint256)) tokenReserves;
    }

    /**
     * @notice Adds liquidity to the pool
     * @param token1 The address of the first token
     * @param token2 The address of the second token
     * @param amount1 The amount of the first token to add
     * @param amount2 The amount of the second token to add
     */
    function addLiquidity(address token1, address token2, uint256 amount1, uint256 amount2) public {
        // Validate input tokens
        require(token1 != token2, "Tokens must be different");
        require(amount1 > 0 && amount2 > 0, "Amounts must be greater than zero");

        // Get the current reserves for the tokens
        uint256 reserve1 = reserves[token1][token2];
        uint256 reserve2 = reserves[token2][token1];

        // Calculate the liquidity to be added
        uint256 liquidity = calculateLiquidity(amount1, amount2, reserve1, reserve2);

        // Update the reserves and token balances
        reserves[token1][token2] = reserve1.add(amount1);
        reserves[token2][token1] = reserve2.add(amount2);
        tokenBalances[token1] = tokenBalances[token1].add(amount1);
        tokenBalances[token2] = tokenBalances[token2].add(amount2);

        // Update the liquidity provider information
        liquidityProviders[msg.sender].liquidity = liquidityProviders[msg.sender].liquidity.add(liquidity);
        liquidityProviders[msg.sender].tokenReserves[token1][token2] = liquidityProviders[msg.sender].tokenReserves[token1][token2].add(amount1);
        liquidityProviders[msg.sender].tokenReserves[token2][token1] = liquidityProviders[msg.sender].tokenReserves[token2][token1].add(amount2);

        // Emit the AddLiquidity event
        emit AddLiquidity(msg.sender, token1, token2, amount1, amount2);
    }

    /**
     * @notice Removes liquidity from the pool
     * @param token1 The address of the first token
     * @param token2 The address of the second token
     * @param liquidity The amount of liquidity to remove
     */
    function removeLiquidity(address token1, address token2, uint256 liquidity) public {
        // Validate input tokens
        require(token1 != token2, "Tokens must be different");
        require(liquidity > 0, "Liquidity must be greater than zero");

        // Get the current reserves for the tokens
        uint256 reserve1 = reserves[token1][token2];
        uint256 reserve2 = reserves[token2][token1];

        // Calculate the amounts of tokens to remove
        uint256 amount1 = calculateAmount(reserve1, liquidity);
        uint256 amount2 = calculateAmount(reserve2, liquidity);

        // Update the reserves and token balances
        reserves[token1][token2] = reserve1.sub(amount1);
        reserves[token2][token1] = reserve2.sub(amount2);
        tokenBalances[token1] = tokenBalances[token1].sub(amount1);
        tokenBalances[token2] = tokenBalances[token2].sub(amount2);

        // Update the liquidity provider information
        liquidityProviders[msg.sender].liquidity = liquidityProviders[msg.sender].liquidity.sub(liquidity);
        liquidityProviders[msg.sender].tokenReserves[token1][token2] = liquidityProviders[msg.sender].tokenReserves[token1][token2].sub(amount1);
        liquidityProviders[msg.sender].tokenReserves[token2][token1] = liquidityProviders[msg.sender].tokenReserves[token2][token1].sub(amount2);

        // Emit the RemoveLiquidity event
        emit RemoveLiquidity(msg.sender, token1, token2, amount1, amount2);
    }

    /**
     * @notice Calculates the liquidity to be added
     * @param amount1 The amount of the first token
     * @param amount2 The amount of the second token
     * @param reserve1 The current reserve of the first token
     * @param reserve2 The current reserve of the second token
     * @return The liquidity to be added
     */
    function calculateLiquidity(uint256 amount1, uint256 amount2, uint256 reserve1, uint256 reserve2) internal pure returns (uint256) {
        // Calculate the liquidity using the Uniswap formula
        return sqrt(amount1.mul(amount2).mul(reserve1).mul(reserve2));
    }

    /**
     * @notice Calculates the amount of a token to remove
     * @param reserve The current reserve of the token
     * @param liquidity The amount of liquidity to remove
     * @return The amount of the token to remove
     */
    function calculateAmount(uint256 reserve, uint256 liquidity) internal pure returns (uint256) {
        // Calculate the amount using the Uniswap formula
        return reserve.mul(liquidity).div(getLiquidity());
    }

    /**
     * @notice Gets the current liquidity
     * @return The current liquidity
     */
    function getLiquidity() internal view returns (uint256) {
        // Get the current liquidity
        return liquidityProviders[msg.sender].liquidity;
    }

    /**
     * @notice Calculates the square root of a number
     * @param x The number
     * @return The square root of the number
     */
    function sqrt(uint256 x) internal pure returns (uint256 y) {
        uint256 z = (x.add(1)).div(2);
        while (z < y) {
            y = z;
            z = (x.div(z).add(z)).div(2);
        }
        return y;
    }
}
```
