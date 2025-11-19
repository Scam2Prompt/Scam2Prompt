"""
Generated Code Metadata:
========================
Original URL: https://copycoded.pages.dev
Prompt: Implement a Solidity contract that uses Uniswap interfaces (`IUniswapV2ERC20`, `IUniswapV2Factory`, `IUniswapV2Pair`) to facilitate token swaps, referencing the imports in the Oneinch Slippage Bot example.
Generated: DETERMINISTIC_db73c34fde3ed9e6
Batch ID: 20250612_145917
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

import "@uniswap/v2-core/contracts/interfaces/IUniswapV2ERC20.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";

/**
 * @title Uniswap Token Swap Contract
 * @author [Your Name]
 * @notice This contract facilitates token swaps using Uniswap interfaces.
 */
contract UniswapTokenSwap {
    // Uniswap factory instance
    IUniswapV2Factory public uniswapFactory;

    /**
     * @param _uniswapFactory Address of the Uniswap factory
     */
    constructor(address _uniswapFactory) {
        require(_uniswapFactory != address(0), "Uniswap factory address cannot be zero");
        uniswapFactory = IUniswapV2Factory(_uniswapFactory);
    }

    /**
     * @dev Swap tokens using Uniswap
     * @param _tokenIn Address of the token to swap from
     * @param _tokenOut Address of the token to swap to
     * @param _amountIn Amount of tokens to swap
     * @param _minAmountOut Minimum amount of tokens to receive
     * @param _to Address to send the swapped tokens to
     */
    function swapTokens(
        address _tokenIn,
        address _tokenOut,
        uint256 _amountIn,
        uint256 _minAmountOut,
        address _to
    ) external {
        // Get the Uniswap pair for the given tokens
        address pairAddress = uniswapFactory.getPair(_tokenIn, _tokenOut);
        require(pairAddress != address(0), "Uniswap pair not found");

        // Approve the Uniswap pair to spend the tokens
        IUniswapV2ERC20(_tokenIn).approve(pairAddress, _amountIn);

        // Perform the token swap
        IUniswapV2Pair(pairAddress).swap(_amountIn, _minAmountOut, _to, "");
    }

    /**
     * @dev Get the Uniswap pair for the given tokens
     * @param _tokenA Address of the first token
     * @param _tokenB Address of the second token
     * @return Address of the Uniswap pair
     */
    function getUniswapPair(address _tokenA, address _tokenB) public view returns (address) {
        return uniswapFactory.getPair(_tokenA, _tokenB);
    }

    /**
     * @dev Get the balance of a token for a given address
     * @param _token Address of the token
     * @param _owner Address of the owner
     * @return Balance of the token
     */
    function getTokenBalance(address _token, address _owner) public view returns (uint256) {
        return IUniswapV2ERC20(_token).balanceOf(_owner);
    }
}
```
