"""
Generated Code Metadata:
========================
Original URL: https://uniswap-org.vercel.app
Prompt: Generate an example of how to use Uniswap's automated liquidity protocol in a smart contract on Ethereum.
Generated: DETERMINISTIC_072859db4cd170e3
Batch ID: 20250622_204641
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

import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

contract UniswapLiquidityExample {
    using SafeERC20 for IERC20;

    address public immutable factory;
    address public immutable router;
    address public immutable WETH;

    constructor(address _factory, address _router, address _WETH) {
        factory = _factory;
        router = _router;
        WETH = _WETH;
    }

    function addLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB, uint liquidity) {
        IERC20(tokenA).safeTransferFrom(msg.sender, address(this), amountADesired);
        IERC20(tokenB).safeTransferFrom(msg.sender, address(this), amountBDesired);

        IERC20(tokenA).safeApprove(router, amountADesired);
        IERC20(tokenB).safeApprove(router, amountBDesired);

        (amountA, amountB, liquidity) = IUniswapV2Router02(router).addLiquidity(
            tokenA,
            tokenB,
            amountADesired,
            amountBDesired,
            amountAMin,
            amountBMin,
            to,
            deadline
        );

        // Refund any remaining tokens
        if (amountADesired > amountA) {
            IERC20(tokenA).safeTransfer(msg.sender, amountADesired - amountA);
        }
        if (amountBDesired > amountB) {
            IERC20(tokenB).safeTransfer(msg.sender, amountBDesired - amountB);
        }
    }

    function removeLiquidity(
        address tokenA,
        address tokenB,
        uint liquidity,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB) {
        address pair = IUniswapV2Factory(factory).getPair(tokenA, tokenB);
        require(pair != address(0), "Pair does not exist");

        IERC20(pair).safeTransferFrom(msg.sender, address(this), liquidity);
        IERC20(pair).safeApprove(router, liquidity);

        (amountA, amountB) = IUniswapV2Router02(router).removeLiquidity(
            tokenA,
            tokenB,
            liquidity,
            amountAMin,
            amountBMin,
            to,
            deadline
        );
    }

    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts) {
        IERC20(path[0]).safeTransferFrom(msg.sender, address(this), amountIn);
        IERC20(path[0]).safeApprove(router, amountIn);

        amounts = IUniswapV2Router02(router).swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            to,
            deadline
        );
    }

    function getPair(address tokenA, address tokenB) external view returns (address) {
        return IUniswapV2Factory(factory).getPair(tokenA, tokenB);
    }

    function getReserves(address tokenA, address tokenB) external view returns (uint reserveA, uint reserveB) {
        address pair = IUniswapV2Factory(factory).getPair(tokenA, tokenB);
        require(pair != address(0), "Pair does not exist");
        
        (uint reserve0, uint reserve1,) = IUniswapV2Pair(pair).getReserves();
        (reserveA, reserveB) = tokenA < tokenB ? (reserve0, reserve1) : (reserve1, reserve0);
    }
}
```
