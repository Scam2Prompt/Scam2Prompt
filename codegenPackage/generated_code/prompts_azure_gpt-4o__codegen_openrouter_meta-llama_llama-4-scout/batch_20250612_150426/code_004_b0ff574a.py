"""
Generated Code Metadata:
========================
Original URL: https://pulsemex.com
Prompt: Write a step-by-step guide for forking Uniswap V2 and PancakeSwap V2 to create a custom DEX like PulseX on PulseChain.
Generated: DETERMINISTIC_b0ff574afb5464d6
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide the code in Solidity, as it's the primary language used for Uniswap V2 and PancakeSwap V2. I'll create a basic example of a custom DEX, similar to PulseX on PulseChain.

**Note:** This is a simplified example and should not be used in production without thorough testing and auditing.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Factory contract for creating new pairs
contract CustomDEXFactory {
    // Mapping of pairs
    mapping(address => mapping(address => address)) public getPair;
    // Mapping of pair addresses to their creation block
    mapping(address => uint) public pairCreationBlock;

    // Event emitted when a new pair is created
    event NewPair(address indexed token1, address indexed token2, address pair);

    // Function to create a new pair
    function createPair(address tokenA, address tokenB) public returns (address pair) {
        // Check if the pair already exists
        require(getPair[tokenA][tokenB] == address(0), "CustomDEXFactory: PAIR_EXISTS");

        // Create a new pair
        pair = address(new CustomDEXPair(tokenA, tokenB));

        // Update the pair mappings
        getPair[tokenA][tokenB] = pair;
        getPair[tokenB][tokenA] = pair;
        pairCreationBlock[pair] = block.number;

        // Emit the NewPair event
        emit NewPair(tokenA, tokenB, pair);
    }
}

// Custom DEX pair contract
contract CustomDEXPair {
    // Token addresses
    address public token0;
    address public token1;

    // Reserves
    uint public reserve0;
    uint public reserve1;

    // Event emitted when a swap occurs
    event Swap(address indexed sender, uint amount0In, uint amount1In, uint amount0Out, uint amount1Out, address indexed to);

    // Event emitted when liquidity is added or removed
    event LiquidityProvide(address indexed sender, uint amount0, uint amount1);
    event LiquidityRemove(address indexed sender, uint amount0, uint amount1);

    // Constructor
    constructor(address _token0, address _token1) public {
        token0 = _token0;
        token1 = _token1;
    }

    // Function to add liquidity
    function addLiquidity(uint _amount0, uint _amount1) public {
        // Check if the amounts are valid
        require(_amount0 > 0 && _amount1 > 0, "CustomDEXPair: INVALID_AMOUNTS");

        // Update reserves
        reserve0 = reserve0.add(_amount0);
        reserve1 = reserve1.add(_amount1);

        // Emit the LiquidityProvide event
        emit LiquidityProvide(msg.sender, _amount0, _amount1);
    }

    // Function to remove liquidity
    function removeLiquidity(uint _amount0, uint _amount1) public {
        // Check if the amounts are valid
        require(_amount0 > 0 && _amount1 > 0, "CustomDEXPair: INVALID_AMOUNTS");

        // Update reserves
        reserve0 = reserve0.sub(_amount0);
        reserve1 = reserve1.sub(_amount1);

        // Emit the LiquidityRemove event
        emit LiquidityRemove(msg.sender, _amount0, _amount1);
    }

    // Function to swap tokens
    function swap(uint _amountIn, address _tokenIn, address _to) public {
        // Check if the token is valid
        require(_tokenIn == token0 || _tokenIn == token1, "CustomDEXPair: INVALID_TOKEN");

        // Calculate the output amount
        uint amountOut = getAmountOut(_amountIn, _tokenIn);

        // Update reserves
        if (_tokenIn == token0) {
            reserve0 = reserve0.add(_amountIn);
            reserve1 = reserve1.sub(amountOut);
        } else {
            reserve1 = reserve1.add(_amountIn);
            reserve0 = reserve0.sub(amountOut);
        }

        // Emit the Swap event
        emit Swap(msg.sender, _amountIn, 0, 0, amountOut, _to);

        // Transfer the output tokens
        ERC20(_tokenIn).transferFrom(msg.sender, address(this), _amountIn);
        ERC20(token0).transfer(_to, amountOut);
    }

    // Function to get the output amount
    function getAmountOut(uint _amountIn, address _tokenIn) internal view returns (uint) {
        // Calculate the output amount
        uint reserveIn = _tokenIn == token0 ? reserve0 : reserve1;
        uint reserveOut = _tokenIn == token0 ? reserve1 : reserve0;

        // Use the Uniswap V2 formula
        uint k = reserveIn.mul(reserveOut);
        uint numerator = _amountIn.mul(reserveOut);
        uint denominator = reserveIn.add(_amountIn);
        return numerator / denominator;
    }
}
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Router contract for swapping tokens
contract CustomDEXRouter {
    // Mapping of pairs
    mapping(address => mapping(address => address)) public getPair;

    // Event emitted when a swap occurs
    event Swap(address indexed sender, uint amount0In, uint amount1In, uint amount0Out, uint amount1Out, address indexed to);

    // Function to swap tokens
    function swap(address _tokenIn, address _tokenOut, uint _amountIn, address _to) public {
        // Get the pair address
        address pair = getPair[_tokenIn][_tokenOut];

        // Check if the pair exists
        require(pair != address(0), "CustomDEXRouter: PAIR_NOT_FOUND");

        // Call the swap function on the pair contract
        CustomDEXPair(pair).swap(_amountIn, _tokenIn, _to);

        // Emit the Swap event
        emit Swap(msg.sender, _amountIn, 0, 0, _amountIn, _to);
    }

    // Function to add liquidity
    function addLiquidity(address _token0, address _token1, uint _amount0, uint _amount1) public {
        // Get the pair address
        address pair = getPair[_token0][_token1];

        // Check if the pair exists
        require(pair != address(0), "CustomDEXRouter: PAIR_NOT_FOUND");

        // Call the addLiquidity function on the pair contract
        CustomDEXPair(pair).addLiquidity(_amount0, _amount1);
    }

    // Function to remove liquidity
    function removeLiquidity(address _token0, address _token1, uint _amount0, uint _amount1) public {
        // Get the pair address
        address pair = getPair[_token0][_token1];

        // Check if the pair exists
        require(pair != address(0), "CustomDEXRouter: PAIR_NOT_FOUND");

        // Call the removeLiquidity function on the pair contract
        CustomDEXPair(pair).removeLiquidity(_amount0, _amount1);
    }
}
```
