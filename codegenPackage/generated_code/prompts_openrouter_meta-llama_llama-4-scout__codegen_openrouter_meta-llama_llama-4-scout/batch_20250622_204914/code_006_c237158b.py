"""
Generated Code Metadata:
========================
Original URL: https://codecopyed.pages.dev
Prompt: "Explain how to import and use Uniswap V2 core interfaces (IUniswapV2ERC20, IUniswapV2Factory, IUniswapV2Pair) in a Solidity contract for a project."
Generated: DETERMINISTIC_c237158b1a24ac88
Batch ID: 20250622_204914
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
 * @title UniswapV2ExampleContract
 * @author [Your Name]
 * @notice Example contract demonstrating how to use Uniswap V2 core interfaces
 */
contract UniswapV2ExampleContract {
    // Uniswap V2 Factory instance
    IUniswapV2Factory public uniswapV2Factory;

    /**
     * @notice Constructor
     * @param _uniswapV2FactoryAddress Address of the Uniswap V2 Factory
     */
    constructor(address _uniswapV2FactoryAddress) {
        // Initialize Uniswap V2 Factory instance
        uniswapV2Factory = IUniswapV2Factory(_uniswapV2FactoryAddress);
    }

    /**
     * @notice Get the address of a Uniswap V2 Pair
     * @param _tokenA Address of token A
     * @param _tokenB Address of token B
     * @return Address of the Uniswap V2 Pair
     */
    function getPairAddress(address _tokenA, address _tokenB) public view returns (address) {
        return uniswapV2Factory.getPair(_tokenA, _tokenB);
    }

    /**
     * @notice Create a new Uniswap V2 Pair
     * @param _tokenA Address of token A
     * @param _tokenB Address of token B
     */
    function createPair(address _tokenA, address _tokenB) public {
        // Check if the pair already exists
        require(uniswapV2Factory.getPair(_tokenA, _tokenB) == address(0), "Pair already exists");

        // Create a new pair
        uniswapV2Factory.createPair(_tokenA, _tokenB);
    }

    /**
     * @notice Get the token addresses of a Uniswap V2 Pair
     * @param _pairAddress Address of the Uniswap V2 Pair
     * @return Addresses of token A and token B
     */
    function getTokenAddresses(address _pairAddress) public view returns (address, address) {
        // Get the Uniswap V2 Pair instance
        IUniswapV2Pair pair = IUniswapV2Pair(_pairAddress);

        // Get the token addresses
        (address tokenA, address tokenB) = (pair.token0(), pair.token1());

        return (tokenA, tokenB);
    }

    /**
     * @notice Get the balance of a token for a given address
     * @param _tokenAddress Address of the token
     * @param _owner Address of the owner
     * @return Balance of the token
     */
    function getTokenBalance(address _tokenAddress, address _owner) public view returns (uint256) {
        // Get the token instance
        IUniswapV2ERC20 token = IUniswapV2ERC20(_tokenAddress);

        // Get the balance
        return token.balanceOf(_owner);
    }
}
```
