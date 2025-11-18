"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycodegpt.pages.dev
Prompt: Generate a Solidity contract that imports `IUniswapV2ERC20`, `IUniswapV2Factory`, and `IUniswapV2Pair` interfaces and implements a method for exploring new liquidity pools on Uniswap, as demonstrated in the Oneinch Slippage Bot.
Generated: DETERMINISTIC_cec611d1decee529
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import necessary Uniswap interfaces
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2ERC20.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";

/**
 * @title LiquidityPoolExplorer
 * @dev A contract for exploring new liquidity pools on Uniswap, inspired by the Oneinch Slippage Bot.
 */
contract LiquidityPoolExplorer {
    IUniswapV2Factory public uniswapFactory;

    /**
     * @dev Sets the Uniswap factory address.
     * @param _factoryAddress Address of the Uniswap V2 factory contract.
     */
    constructor(address _factoryAddress) {
        require(_factoryAddress != address(0), "Factory address cannot be zero");
        uniswapFactory = IUniswapV2Factory(_factoryAddress);
    }

    /**
     * @dev Fetches and returns information about a liquidity pool given two tokens.
     * @param tokenA Address of the first token in the pair.
     * @param tokenB Address of the second token in the pair.
     * @return pair Address of the liquidity pool (pair) contract.
     * @return reserveA Reserve of tokenA in the pair.
     * @return reserveB Reserve of tokenB in the pair.
     */
    function exploreLiquidityPool(address tokenA, address tokenB)
        external
        view
        returns (
            address pair,
            uint256 reserveA,
            uint256 reserveB
        )
    {
        // Validate input
        require(tokenA != address(0), "TokenA address cannot be zero");
        require(tokenB != address(0), "TokenB address cannot be zero");

        // Fetch the pair address from the factory
        pair = uniswapFactory.getPair(tokenA, tokenB);
        require(pair != address(0), "Liquidity pool does not exist");

        // Fetch reserve information from the pair
        (uint112 _reserveA, uint112 _reserveB, ) = IUniswapV2Pair(pair).getReserves();

        reserveA = uint256(_reserveA);
        reserveB = uint256(_reserveB);

        return (pair, reserveA, reserveB);
    }

    /**
     * @dev Checks whether a liquidity pool exists for the given token pair.
     * @param tokenA Address of the first token in the pair.
     * @param tokenB Address of the second token in the pair.
     * @return exists Boolean indicating whether the pool exists.
     */
    function doesPoolExist(address tokenA, address tokenB) external view returns (bool exists) {
        require(tokenA != address(0), "TokenA address cannot be zero");
        require(tokenB != address(0), "TokenB address cannot be zero");

        address pair = uniswapFactory.getPair(tokenA, tokenB);
        exists = (pair != address(0));

        return exists;
    }
}
```
