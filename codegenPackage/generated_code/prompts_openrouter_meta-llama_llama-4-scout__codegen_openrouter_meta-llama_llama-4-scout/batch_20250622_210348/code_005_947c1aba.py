"""
Generated Code Metadata:
========================
Original URL: https://riftperceptivescaling.pages.dev
Prompt: "Design a Solidity smart contract for swapping tokens in a pool, inspired by the Rift Swap functionality."
Generated: DETERMINISTIC_947c1aba9dd187f3
Batch ID: 20250622_210348
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
 * @title RiftSwapPool
 * @author [Your Name]
 * @notice A decentralized token swap pool inspired by Rift Swap functionality.
 */
contract RiftSwapPool {
    using SafeMath for uint256;

    // Mapping of token addresses to their respective reserves
    mapping(address => uint256) public tokenReserves;

    // Mapping of token addresses to their respective token balances in the pool
    mapping(address => mapping(address => uint256)) public tokenBalances;

    // Mapping of LP (Liquidity Provider) token balances
    mapping(address => uint256) public lpTokenBalances;

    // LP token address
    address public lpToken;

    // Pool fee (in bps)
    uint256 public poolFee;

    // Event emitted when a token swap occurs
    event TokenSwap(
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );

    // Event emitted when liquidity is added to the pool
    event LiquidityAdded(
        address indexed token,
        uint256 amount
    );

    // Event emitted when liquidity is removed from the pool
    event LiquidityRemoved(
        address indexed token,
        uint256 amount
    );

    /**
     * @notice Constructor for RiftSwapPool
     * @param _lpToken LP token address
     * @param _poolFee Pool fee in bps
     */
    constructor(address _lpToken, uint256 _poolFee) {
        require(_lpToken != address(0), "LP token address cannot be zero");
        require(_poolFee > 0, "Pool fee must be greater than zero");

        lpToken = _lpToken;
        poolFee = _poolFee;
    }

    /**
     * @notice Add liquidity to the pool
     * @param _token Token address
     * @param _amount Amount of token to add
     */
    function addLiquidity(address _token, uint256 _amount) public {
        require(_token != address(0), "Token address cannot be zero");
        require(_amount > 0, "Amount must be greater than zero");

        // Update token reserve
        tokenReserves[_token] = tokenReserves[_token].add(_amount);

        // Update token balance
        tokenBalances[msg.sender][_token] = tokenBalances[msg.sender][_token].add(_amount);

        // Mint LP tokens
        uint256 lpTokensToMint = _amount;
        lpTokenBalances[msg.sender] = lpTokenBalances[msg.sender].add(lpTokensToMint);

        emit LiquidityAdded(_token, _amount);
    }

    /**
     * @notice Remove liquidity from the pool
     * @param _token Token address
     * @param _amount Amount of token to remove
     */
    function removeLiquidity(address _token, uint256 _amount) public {
        require(_token != address(0), "Token address cannot be zero");
        require(_amount > 0, "Amount must be greater than zero");
        require(tokenBalances[msg.sender][_token] >= _amount, "Insufficient token balance");

        // Update token reserve
        tokenReserves[_token] = tokenReserves[_token].sub(_amount);

        // Update token balance
        tokenBalances[msg.sender][_token] = tokenBalances[msg.sender][_token].sub(_amount);

        // Burn LP tokens
        uint256 lpTokensToBurn = _amount;
        lpTokenBalances[msg.sender] = lpTokenBalances[msg.sender].sub(lpTokensToBurn);

        emit LiquidityRemoved(_token, _amount);
    }

    /**
     * @notice Swap tokens in the pool
     * @param _tokenIn Token to swap in
     * @param _tokenOut Token to swap out
     * @param _amountIn Amount of token to swap in
     * @return amountOut Amount of token swapped out
     */
    function swap(
        address _tokenIn,
        address _tokenOut,
        uint256 _amountIn
    ) public returns (uint256 amountOut) {
        require(_tokenIn != address(0) && _tokenOut != address(0), "Token addresses cannot be zero");
        require(_amountIn > 0, "Amount must be greater than zero");
        require(_tokenIn != _tokenOut, "Tokens must be different");

        // Calculate the reserve ratio
        uint256 reserveIn = tokenReserves[_tokenIn];
        uint256 reserveOut = tokenReserves[_tokenOut];

        // Calculate the amount out
        amountOut = _getAmountOut(_amountIn, reserveIn, reserveOut);

        // Apply pool fee
        uint256 fee = _amountIn.mul(poolFee).div(10000);
        amountOut = amountOut.sub(fee);

        // Update token reserves
        tokenReserves[_tokenIn] = reserveIn.add(_amountIn);
        tokenReserves[_tokenOut] = reserveOut.sub(amountOut);

        // Emit event
        emit TokenSwap(_tokenIn, _tokenOut, _amountIn, amountOut);

        return amountOut;
    }

    /**
     * @dev Helper function to calculate the amount out
     * @param _amountIn Amount of token to swap in
     * @param _reserveIn Reserve of token in
     * @param _reserveOut Reserve of token out
     * @return amountOut Amount of token swapped out
     */
    function _getAmountOut(
        uint256 _amountIn,
        uint256 _reserveIn,
        uint256 _reserveOut
    ) internal pure returns (uint256 amountOut) {
        uint256 numerator = _amountIn.mul(_reserveOut);
        uint256 denominator = _reserveIn.add(_amountIn);
        amountOut = numerator.div(denominator);
    }

    /**
     * @notice Get the token balance of an account
     * @param _token Token address
     * @param _account Account address
     * @return balance Token balance
     */
    function getTokenBalance(address _token, address _account) public view returns (uint256 balance) {
        return tokenBalances[_account][_token];
    }

    /**
     * @notice Get the LP token balance of an account
     * @param _account Account address
     * @return balance LP token balance
     */
    function getLpTokenBalance(address _account) public view returns (uint256 balance) {
        return lpTokenBalances[_account];
    }
}
```
