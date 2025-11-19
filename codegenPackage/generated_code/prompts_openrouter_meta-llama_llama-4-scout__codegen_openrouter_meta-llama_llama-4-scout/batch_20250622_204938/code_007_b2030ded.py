"""
Generated Code Metadata:
========================
Original URL: https://copycoded.pages.dev
Prompt: Generate a Solidity smart contract that uses a Migrator and Exchange libraries to interact with Uniswap V2.
Generated: DETERMINISTIC_b2030dede90648d0
Batch ID: 20250622_204938
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

import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";

// Migrator contract for migrating liquidity to Uniswap V2
contract Migrator {
    address public immutable uniswapV2Factory;
    address public immutable weth;

    constructor(address _uniswapV2Factory, address _weth) public {
        uniswapV2Factory = _uniswapV2Factory;
        weth = _weth;
    }

    // Migrate liquidity from a given pair to Uniswap V2
    function migrate(IUniswapV2Pair _pair) public {
        // Get the pair's token addresses
        address token0 = _pair.token0();
        address token1 = _pair.token1();

        // Get the pair's liquidity
        uint256 liquidity = _pair.balanceOf(msg.sender);

        // Approve the Uniswap V2 router to spend the pair's liquidity
        _pair.approve(uniswapV2Factory, liquidity);

        // Get the Uniswap V2 pair
        IUniswapV2Pair uniswapV2Pair = IUniswapV2Pair(
            IUniswapV2Factory(uniswapV2Factory).getPair(token0, token1)
        );

        // If the Uniswap V2 pair does not exist, create it
        if (address(uniswapV2Pair) == address(0)) {
            uniswapV2Pair = IUniswapV2Pair(
                IUniswapV2Factory(uniswapV2Factory).createPair(token0, token1)
            );
        }

        // Add liquidity to the Uniswap V2 pair
        IUniswapV2Router02(IUniswapV2Factory(uniswapV2Factory).getRouter()).addLiquidity(
            token0,
            token1,
            _pair.balanceOf(msg.sender),
            0,
            0,
            msg.sender,
            block.timestamp
        );
    }
}

// Exchange contract for interacting with Uniswap V2
contract Exchange {
    IUniswapV2Router02 public immutable uniswapV2Router;

    constructor(address _uniswapV2Router) public {
        uniswapV2Router = IUniswapV2Router02(_uniswapV2Router);
    }

    // Swap tokens using Uniswap V2
    function swap(
        address _tokenIn,
        address _tokenOut,
        uint256 _amountIn,
        uint256 _amountOutMin,
        address _to
    ) public {
        // Approve the Uniswap V2 router to spend the input token
        IERC20(_tokenIn).approve(address(uniswapV2Router), _amountIn);

        // Swap the tokens
        uniswapV2Router.swapExactTokensForTokens(
            _amountIn,
            _amountOutMin,
            [_tokenIn, _tokenOut],
            _to,
            block.timestamp
        );
    }

    // Add liquidity to a Uniswap V2 pair
    function addLiquidity(
        address _token0,
        address _token1,
        uint256 _amount0,
        uint256 _amount1,
        uint256 _liquidityMin,
        address _to
    ) public {
        // Approve the Uniswap V2 router to spend the input tokens
        IERC20(_token0).approve(address(uniswapV2Router), _amount0);
        IERC20(_token1).approve(address(uniswapV2Router), _amount1);

        // Add liquidity to the pair
        uniswapV2Router.addLiquidity(
            _token0,
            _token1,
            _amount0,
            _amount1,
            _liquidityMin,
            _to,
            block.timestamp
        );
    }

    // Remove liquidity from a Uniswap V2 pair
    function removeLiquidity(
        address _token0,
        address _token1,
        uint256 _liquidity,
        uint256 _amount0Min,
        uint256 _amount1Min,
        address _to
    ) public {
        // Get the Uniswap V2 pair
        IUniswapV2Pair pair = IUniswapV2Pair(
            IUniswapV2Factory(uniswapV2Router.factory()).getPair(_token0, _token1)
        );

        // Approve the Uniswap V2 router to spend the pair's liquidity
        pair.approve(address(uniswapV2Router), _liquidity);

        // Remove liquidity from the pair
        uniswapV2Router.removeLiquidity(
            _token0,
            _token1,
            _liquidity,
            _amount0Min,
            _amount1Min,
            _to,
            block.timestamp
        );
    }
}

// Import OpenZeppelin's IERC20 contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Import OpenZeppelin's SafeMath library
import "@openzeppelin/contracts/math/SafeMath.sol";

// Use SafeMath to prevent arithmetic overflows
contract UsingSafeMath {
    using SafeMath for uint256;
}

// Combine all contracts into one
contract UniswapV2MigratorExchange is Migrator, Exchange, UsingSafeMath {
    constructor(
        address _uniswapV2Factory,
        address _weth,
        address _uniswapV2Router
    ) Migrator(_uniswapV2Factory, _weth) Exchange(_uniswapV2Router) public {}
}
```
