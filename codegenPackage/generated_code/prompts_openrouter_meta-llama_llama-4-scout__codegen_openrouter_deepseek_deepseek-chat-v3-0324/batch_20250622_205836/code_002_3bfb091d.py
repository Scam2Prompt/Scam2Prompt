"""
Generated Code Metadata:
========================
Original URL: https://pepe-unchaineds.pages.dev
Prompt: Develop a smart contract code for a decentralized exchange (DEX) on Pepe Unchained's Layer 2 blockchain, utilizing the tokenomics system and 7.5% liquidity allocation.
Generated: DETERMINISTIC_3bfb091ddf7ea024
Batch ID: 20250622_205836
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract PepeDEX is ReentrancyGuard {
    using SafeMath for uint256;

    address public feeCollector;
    uint256 public constant LIQUIDITY_FEE = 75; // 7.5% represented as 75 basis points
    uint256 public constant FEE_DENOMINATOR = 1000;

    struct Pool {
        uint256 reserve0;
        uint256 reserve1;
        uint256 totalLiquidity;
        mapping(address => uint256) liquidity;
    }

    mapping(address => mapping(address => Pool)) public pools;
    mapping(address => bool) public supportedTokens;

    event LiquidityAdded(
        address indexed provider,
        address indexed token0,
        address indexed token1,
        uint256 amount0,
        uint256 amount1,
        uint256 liquidity
    );
    event LiquidityRemoved(
        address indexed provider,
        address indexed token0,
        address indexed token1,
        uint256 amount0,
        uint256 amount1,
        uint256 liquidity
    );
    event TokensSwapped(
        address indexed sender,
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );

    constructor(address _feeCollector) {
        require(_feeCollector != address(0), "Invalid fee collector address");
        feeCollector = _feeCollector;
    }

    function addLiquidity(
        address token0,
        address token1,
        uint256 amount0,
        uint256 amount1
    ) external nonReentrant {
        require(token0 != token1, "Identical tokens");
        require(amount0 > 0 && amount1 > 0, "Amount must be greater than 0");
        require(supportedTokens[token0] && supportedTokens[token1], "Token not supported");

        Pool storage pool = pools[token0][token1];
        uint256 liquidity;

        if (pool.totalLiquidity == 0) {
            liquidity = sqrt(amount0.mul(amount1));
        } else {
            liquidity = min(
                amount0.mul(pool.totalLiquidity) / pool.reserve0,
                amount1.mul(pool.totalLiquidity) / pool.reserve1
            );
        }

        require(liquidity > 0, "Insufficient liquidity");

        IERC20(token0).transferFrom(msg.sender, address(this), amount0);
        IERC20(token1).transferFrom(msg.sender, address(this), amount1);

        pool.reserve0 = pool.reserve0.add(amount0);
        pool.reserve1 = pool.reserve1.add(amount1);
        pool.totalLiquidity = pool.totalLiquidity.add(liquidity);
        pool.liquidity[msg.sender] = pool.liquidity[msg.sender].add(liquidity);

        emit LiquidityAdded(msg.sender, token0, token1, amount0, amount1, liquidity);
    }

    function removeLiquidity(
        address token0,
        address token1,
        uint256 liquidity
    ) external nonReentrant {
        require(token0 != token1, "Identical tokens");
        require(liquidity > 0, "Amount must be greater than 0");

        Pool storage pool = pools[token0][token1];
        require(pool.liquidity[msg.sender] >= liquidity, "Insufficient liquidity");

        uint256 amount0 = liquidity.mul(pool.reserve0) / pool.totalLiquidity;
        uint256 amount1 = liquidity.mul(pool.reserve1) / pool.totalLiquidity;

        pool.reserve0 = pool.reserve0.sub(amount0);
        pool.reserve1 = pool.reserve1.sub(amount1);
        pool.totalLiquidity = pool.totalLiquidity.sub(liquidity);
        pool.liquidity[msg.sender] = pool.liquidity[msg.sender].sub(liquidity);

        IERC20(token0).transfer(msg.sender, amount0);
        IERC20(token1).transfer(msg.sender, amount1);

        emit LiquidityRemoved(msg.sender, token0, token1, amount0, amount1, liquidity);
    }

    function swap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn
    ) external nonReentrant {
        require(tokenIn != tokenOut, "Identical tokens");
        require(amountIn > 0, "Amount must be greater than 0");
        require(supportedTokens[tokenIn] && supportedTokens[tokenOut], "Token not supported");

        Pool storage pool = pools[tokenIn][tokenOut];
        require(pool.totalLiquidity > 0, "No liquidity pool");

        uint256 feeAmount = amountIn.mul(LIQUIDITY_FEE) / FEE_DENOMINATOR;
        uint256 amountInAfterFee = amountIn.sub(feeAmount);

        uint256 amountOut = getAmountOut(amountInAfterFee, pool.reserve0, pool.reserve1);
        require(amountOut > 0, "Insufficient output amount");

        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        IERC20(tokenIn).transfer(feeCollector, feeAmount);

        pool.reserve0 = pool.reserve0.add(amountInAfterFee);
        pool.reserve1 = pool.reserve1.sub(amountOut);

        IERC20(tokenOut).transfer(msg.sender, amountOut);

        emit TokensSwapped(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    function getAmountOut(
        uint256 amountIn,
        uint256 reserveIn,
        uint256 reserveOut
    ) public pure returns (uint256) {
        require(amountIn > 0, "Insufficient input amount");
        require(reserveIn > 0 && reserveOut > 0, "Insufficient liquidity");
        uint256 amountInWithFee = amountIn.mul(FEE_DENOMINATOR.sub(LIQUIDITY_FEE));
        uint256 numerator = amountInWithFee.mul(reserveOut);
        uint256 denominator = reserveIn.mul(FEE_DENOMINATOR).add(amountInWithFee);
        return numerator / denominator;
    }

    function addSupportedToken(address token) external {
        require(msg.sender == feeCollector, "Only fee collector can add tokens");
        supportedTokens[token] = true;
    }

    function sqrt(uint256 y) internal pure returns (uint256 z) {
        if (y > 3) {
            z = y;
            uint256 x = y / 2 + 1;
            while (x < z) {
                z = x;
                x = (y / x + x) / 2;
            }
        } else if (y != 0) {
            z = 1;
        }
    }

    function min(uint256 a, uint256 b) internal pure returns (uint256) {
        return a < b ? a : b;
    }
}
```
