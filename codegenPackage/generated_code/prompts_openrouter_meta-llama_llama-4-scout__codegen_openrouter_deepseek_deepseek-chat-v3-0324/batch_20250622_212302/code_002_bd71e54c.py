"""
Generated Code Metadata:
========================
Original URL: https://visionsblog.ru
Prompt: "Explain how to use Honeyswap for providing liquidity to token pools and earning a share of transaction fees."
Generated: DETERMINISTIC_bd71e54c34823850
Batch ID: 20250622_212302
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
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract HoneyswapLiquidityProvider {
    IUniswapV2Router02 public honeyswapRouter;
    IUniswapV2Factory public honeyswapFactory;
    
    address public constant HONEYSWAP_ROUTER = 0x1C232F01118CB8B424793ae03F870aa7D0ac7f77;
    address public constant HONEYSWAP_FACTORY = 0x03DaA61d8007443a6584e3d8f85105096543C19c;
    
    constructor() {
        honeyswapRouter = IUniswapV2Router02(HONEYSWAP_ROUTER);
        honeyswapFactory = IUniswapV2Factory(HONEYSWAP_FACTORY);
    }
    
    /**
     * @notice Adds liquidity to a Honeyswap pool
     * @param tokenA Address of first token in the pair
     * @param tokenB Address of second token in the pair
     * @param amountADesired Amount of tokenA to add
     * @param amountBDesired Amount of tokenB to add
     * @param amountAMin Minimum amount of tokenA to add (slippage protection)
     * @param amountBMin Minimum amount of tokenB to add (slippage protection)
     * @param to Address that will receive the liquidity tokens
     * @param deadline Unix timestamp after which the transaction will revert
     */
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
        // Transfer tokens from sender to this contract
        IERC20(tokenA).transferFrom(msg.sender, address(this), amountADesired);
        IERC20(tokenB).transferFrom(msg.sender, address(this), amountBDesired);
        
        // Approve router to spend tokens
        IERC20(tokenA).approve(address(honeyswapRouter), amountADesired);
        IERC20(tokenB).approve(address(honeyswapRouter), amountBDesired);
        
        // Add liquidity
        (amountA, amountB, liquidity) = honeyswapRouter.addLiquidity(
            tokenA,
            tokenB,
            amountADesired,
            amountBDesired,
            amountAMin,
            amountBMin,
            to,
            deadline
        );
        
        // Refund any leftover tokens
        if (amountADesired > amountA) {
            IERC20(tokenA).transfer(msg.sender, amountADesired - amountA);
        }
        if (amountBDesired > amountB) {
            IERC20(tokenB).transfer(msg.sender, amountBDesired - amountB);
        }
    }
    
    /**
     * @notice Removes liquidity from a Honeyswap pool
     * @param tokenA Address of first token in the pair
     * @param tokenB Address of second token in the pair
     * @param liquidity Amount of liquidity tokens to remove
     * @param amountAMin Minimum amount of tokenA to receive (slippage protection)
     * @param amountBMin Minimum amount of tokenB to receive (slippage protection)
     * @param to Address that will receive the underlying tokens
     * @param deadline Unix timestamp after which the transaction will revert
     */
    function removeLiquidity(
        address tokenA,
        address tokenB,
        uint liquidity,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB) {
        // Get the pair address
        address pair = honeyswapFactory.getPair(tokenA, tokenB);
        require(pair != address(0), "Pair does not exist");
        
        // Transfer liquidity tokens from sender to this contract
        IERC20(pair).transferFrom(msg.sender, address(this), liquidity);
        
        // Approve router to spend liquidity tokens
        IERC20(pair).approve(address(honeyswapRouter), liquidity);
        
        // Remove liquidity
        (amountA, amountB) = honeyswapRouter.removeLiquidity(
            tokenA,
            tokenB,
            liquidity,
            amountAMin,
            amountBMin,
            to,
            deadline
        );
    }
    
    /**
     * @notice Checks the reserves of a token pair
     * @param tokenA Address of first token in the pair
     * @param tokenB Address of second token in the pair
     * @return reserveA Reserve amount of tokenA
     * @return reserveB Reserve amount of tokenB
     */
    function getReserves(address tokenA, address tokenB) external view returns (uint reserveA, uint reserveB) {
        address pair = honeyswapFactory.getPair(tokenA, tokenB);
        require(pair != address(0), "Pair does not exist");
        
        (reserveA, reserveB, ) = IUniswapV2Pair(pair).getReserves();
    }
    
    /**
     * @notice Calculates the expected LP token amount for given token amounts
     * @param tokenA Address of first token in the pair
     * @param tokenB Address of second token in the pair
     * @param amountADesired Amount of tokenA to add
     * @param amountBDesired Amount of tokenB to add
     * @return amountA Optimal amount of tokenA to add
     * @return amountB Optimal amount of tokenB to add
     * @return liquidity Expected amount of LP tokens to receive
     */
    function quoteLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired
    ) external view returns (uint amountA, uint amountB, uint liquidity) {
        address pair = honeyswapFactory.getPair(tokenA, tokenB);
        require(pair != address(0), "Pair does not exist");
        
        (uint reserveA, uint reserveB) = this.getReserves(tokenA, tokenB);
        
        if (reserveA == 0 && reserveB == 0) {
            // New pool - liquidity is sqrt(amountA * amountB)
            amountA = amountADesired;
            amountB = amountBDesired;
            liquidity = sqrt(amountA * amountB);
        } else {
            // Existing pool - calculate optimal amounts
            uint amountBOptimal = honeyswapRouter.quote(amountADesired, reserveA, reserveB);
            if (amountBOptimal <= amountBDesired) {
                amountA = amountADesired;
                amountB = amountBOptimal;
                liquidity = (amountADesired * IERC20(pair).totalSupply()) / reserveA;
            } else {
                uint amountAOptimal = honeyswapRouter.quote(amountBDesired, reserveB, reserveA);
                amountA = amountAOptimal;
                amountB = amountBDesired;
                liquidity = (amountBDesired * IERC20(pair).totalSupply()) / reserveB;
            }
        }
    }
    
    /**
     * @notice Internal function to calculate square root
     * @param y Number to calculate square root of
     * @return z Square root of y
     */
    function sqrt(uint y) internal pure returns (uint z) {
        if (y > 3) {
            z = y;
            uint x = y / 2 + 1;
            while (x < z) {
                z = x;
                x = (y / x + x) / 2;
            }
        } else if (y != 0) {
            z = 1;
        }
    }
}
```
