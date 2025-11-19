"""
Generated Code Metadata:
========================
Original URL: https://cameloteexchange.org
Prompt: Generate a smart contract code for creating a custom liquidity pool on Camelot Exchange, including functions for depositing and withdrawing liquidity.
Generated: DETERMINISTIC_76e88ef01c641fe2
Batch ID: 20250622_211906
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

interface ICamelotFactory {
    function createPair(address tokenA, address tokenB) external returns (address pair);
}

interface ICamelotRouter {
    function factory() external pure returns (address);
    function WETH() external pure returns (address);
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB, uint liquidity);
    function removeLiquidity(
        address tokenA,
        address tokenB,
        uint liquidity,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB);
}

contract CamelotLiquidityPool is ReentrancyGuard {
    using SafeMath for uint256;

    address public tokenA;
    address public tokenB;
    address public lpToken;
    address public router;
    address public factory;

    event LiquidityAdded(address indexed provider, uint256 amountA, uint256 amountB, uint256 liquidity);
    event LiquidityRemoved(address indexed provider, uint256 amountA, uint256 amountB, uint256 liquidity);

    constructor(address _tokenA, address _tokenB, address _router) {
        require(_tokenA != address(0), "TokenA address cannot be zero");
        require(_tokenB != address(0), "TokenB address cannot be zero");
        require(_router != address(0), "Router address cannot be zero");

        tokenA = _tokenA;
        tokenB = _tokenB;
        router = _router;
        factory = ICamelotRouter(_router).factory();
        lpToken = ICamelotFactory(factory).createPair(_tokenA, _tokenB);
    }

    /**
     * @dev Add liquidity to the pool
     * @param amountADesired Amount of tokenA to add
     * @param amountBDesired Amount of tokenB to add
     * @param amountAMin Minimum amount of tokenA to add (slippage protection)
     * @param amountBMin Minimum amount of tokenB to add (slippage protection)
     * @param deadline Transaction deadline in seconds since epoch
     */
    function addLiquidity(
        uint256 amountADesired,
        uint256 amountBDesired,
        uint256 amountAMin,
        uint256 amountBMin,
        uint256 deadline
    ) external nonReentrant returns (uint256 liquidity) {
        require(amountADesired > 0 && amountBDesired > 0, "Amounts must be greater than zero");
        require(deadline >= block.timestamp, "Deadline has passed");

        IERC20(tokenA).transferFrom(msg.sender, address(this), amountADesired);
        IERC20(tokenB).transferFrom(msg.sender, address(this), amountBDesired);

        IERC20(tokenA).approve(router, amountADesired);
        IERC20(tokenB).approve(router, amountBDesired);

        (uint256 amountA, uint256 amountB, uint256 _liquidity) = ICamelotRouter(router).addLiquidity(
            tokenA,
            tokenB,
            amountADesired,
            amountBDesired,
            amountAMin,
            amountBMin,
            msg.sender,
            deadline
        );

        emit LiquidityAdded(msg.sender, amountA, amountB, _liquidity);
        return _liquidity;
    }

    /**
     * @dev Remove liquidity from the pool
     * @param liquidity Amount of LP tokens to remove
     * @param amountAMin Minimum amount of tokenA to receive (slippage protection)
     * @param amountBMin Minimum amount of tokenB to receive (slippage protection)
     * @param deadline Transaction deadline in seconds since epoch
     */
    function removeLiquidity(
        uint256 liquidity,
        uint256 amountAMin,
        uint256 amountBMin,
        uint256 deadline
    ) external nonReentrant returns (uint256 amountA, uint256 amountB) {
        require(liquidity > 0, "Liquidity must be greater than zero");
        require(deadline >= block.timestamp, "Deadline has passed");

        IERC20(lpToken).transferFrom(msg.sender, address(this), liquidity);
        IERC20(lpToken).approve(router, liquidity);

        (amountA, amountB) = ICamelotRouter(router).removeLiquidity(
            tokenA,
            tokenB,
            liquidity,
            amountAMin,
            amountBMin,
            msg.sender,
            deadline
        );

        emit LiquidityRemoved(msg.sender, amountA, amountB, liquidity);
    }

    /**
     * @dev Get the LP token address
     */
    function getLpToken() external view returns (address) {
        return lpToken;
    }
}
```
