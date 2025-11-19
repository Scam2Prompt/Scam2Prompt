"""
Generated Code Metadata:
========================
Original URL: https://copycoded.pages.dev
Prompt: Develop a Solidity contract that uses the Uniswap V2 factory and pair interfaces to interact with the Uniswap Exchange.
Generated: DETERMINISTIC_cbaabf8b771b9fea
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

import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";

/**
 * @title UniswapV2ExchangeContract
 * @author [Your Name]
 * @notice This contract interacts with the Uniswap Exchange using the Uniswap V2 factory and pair interfaces.
 */
contract UniswapV2ExchangeContract {
    // Uniswap V2 factory instance
    IUniswapV2Factory public immutable uniswapV2Factory;

    /**
     * @dev Constructor
     * @param _uniswapV2FactoryAddress Address of the Uniswap V2 factory
     */
    constructor(address _uniswapV2FactoryAddress) {
        require(_uniswapV2FactoryAddress != address(0), "UniswapV2ExchangeContract: Invalid factory address");
        uniswapV2Factory = IUniswapV2Factory(_uniswapV2FactoryAddress);
    }

    /**
     * @dev Get the address of a Uniswap V2 pair
     * @param _tokenA Address of token A
     * @param _tokenB Address of token B
     * @return Address of the Uniswap V2 pair
     */
    function getPairAddress(address _tokenA, address _tokenB) public view returns (address) {
        return uniswapV2Factory.getPair(_tokenA, _tokenB);
    }

    /**
     * @dev Create a new Uniswap V2 pair
     * @param _tokenA Address of token A
     * @param _tokenB Address of token B
     */
    function createPair(address _tokenA, address _tokenB) public {
        uniswapV2Factory.createPair(_tokenA, _tokenB);
    }

    /**
     * @dev Get the reserves of a Uniswap V2 pair
     * @param _pairAddress Address of the Uniswap V2 pair
     * @return Reserves of the Uniswap V2 pair (reserve0, reserve1)
     */
    function getReserves(address _pairAddress) public view returns (uint112, uint112) {
        IUniswapV2Pair pair = IUniswapV2Pair(_pairAddress);
        (uint112 reserve0, uint112 reserve1, ) = pair.getReserves();
        return (reserve0, reserve1);
    }

    /**
     * @dev Swap tokens on Uniswap V2
     * @param _pairAddress Address of the Uniswap V2 pair
     * @param _amountIn Amount of tokens to swap
     * @param _tokenIn Address of token to swap
     * @param _tokenOut Address of token to receive
     * @param _to Address to send tokens to
     */
    function swap(
        address _pairAddress,
        uint256 _amountIn,
        address _tokenIn,
        address _tokenOut,
        address _to
    ) public {
        IUniswapV2Pair pair = IUniswapV2Pair(_pairAddress);
        require(pair.token0() == _tokenIn || pair.token1() == _tokenIn, "UniswapV2ExchangeContract: Invalid token in");
        require(pair.token0() == _tokenOut || pair.token1() == _tokenOut, "UniswapV2ExchangeContract: Invalid token out");

        // Approve the pair to spend tokens
        IERC20(_tokenIn).approve(_pairAddress, _amountIn);

        // Perform the swap
        if (pair.token0() == _tokenIn) {
            pair.swap(_amountIn, 0, _to, "");
        } else {
            pair.swap(0, _amountIn, _to, "");
        }
    }
}

// Import IERC20 for token interactions
interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
}
```
