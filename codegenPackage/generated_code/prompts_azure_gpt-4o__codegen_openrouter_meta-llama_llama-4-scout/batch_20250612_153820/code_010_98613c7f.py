"""
Generated Code Metadata:
========================
Original URL: https://store-uni-app.com
Prompt: Develop a smart contract that integrates with Uniswap to facilitate trustless token exchanges while prioritizing security and transparency.
Generated: DETERMINISTIC_98613c7f1249edd7
Batch ID: 20250612_153820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Uniswap Smart Contract**
==========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";

/**
 * @title Uniswap Smart Contract
 * @author [Your Name]
 * @notice This contract facilitates trustless token exchanges using Uniswap.
 */
contract UniswapExchange {
    using SafeMath for uint256;

    // Uniswap router address
    address public immutable ROUTER_ADDRESS;

    // Uniswap factory address
    address public immutable FACTORY_ADDRESS;

    // Mapping of token addresses to their respective reserves
    mapping(address => uint256) public tokenReserves;

    /**
     * @param _routerAddress Uniswap router address
     * @param _factoryAddress Uniswap factory address
     */
    constructor(address _routerAddress, address _factoryAddress) public {
        require(_routerAddress != address(0), "Invalid router address");
        require(_factoryAddress != address(0), "Invalid factory address");

        ROUTER_ADDRESS = _routerAddress;
        FACTORY_ADDRESS = _factoryAddress;
    }

    /**
     * @notice Add liquidity to a token pair
     * @param _token1 Address of the first token
     * @param _token2 Address of the second token
     * @param _amount1 Amount of the first token to add
     * @param _amount2 Amount of the second token to add
     */
    function addLiquidity(
        address _token1,
        address _token2,
        uint256 _amount1,
        uint256 _amount2
    ) public {
        // Approve tokens for the router
        IERC20(_token1).approve(ROUTER_ADDRESS, _amount1);
        IERC20(_token2).approve(ROUTER_ADDRESS, _amount2);

        // Get the token pair address
        address pairAddress = IUniswapV2Factory(FACTORY_ADDRESS).getPair(_token1, _token2);

        // If the pair doesn't exist, create it
        if (pairAddress == address(0)) {
            IUniswapV2Router02(ROUTER_ADDRESS).createPair(_token1, _token2);
            pairAddress = IUniswapV2Factory(FACTORY_ADDRESS).getPair(_token1, _token2);
        }

        // Add liquidity to the pair
        IUniswapV2Router02(ROUTER_ADDRESS).addLiquidity(
            _token1,
            _token2,
            _amount1,
            _amount2,
            0,
            0,
            msg.sender,
            block.timestamp
        );

        // Update token reserves
        tokenReserves[_token1] = tokenReserves[_token1].add(_amount1);
        tokenReserves[_token2] = tokenReserves[_token2].add(_amount2);
    }

    /**
     * @notice Swap tokens using Uniswap
     * @param _tokenIn Address of the token to swap in
     * @param _tokenOut Address of the token to swap out
     * @param _amountIn Amount of the token to swap in
     * @param _amountOutMin Minimum amount of the token to swap out
     */
    function swapTokens(
        address _tokenIn,
        address _tokenOut,
        uint256 _amountIn,
        uint256 _amountOutMin
    ) public {
        // Approve tokens for the router
        IERC20(_tokenIn).approve(ROUTER_ADDRESS, _amountIn);

        // Get the token pair address
        address pairAddress = IUniswapV2Factory(FACTORY_ADDRESS).getPair(_tokenIn, _tokenOut);

        require(pairAddress != address(0), "Token pair does not exist");

        // Swap tokens
        IUniswapV2Router02(ROUTER_ADDRESS).swapExactTokensForTokens(
            _amountIn,
            _amountOutMin,
            [_tokenIn, _tokenOut],
            msg.sender,
            block.timestamp
        );
    }

    /**
     * @notice Get the token reserves
     * @param _token Address of the token
     * @return The token reserve
     */
    function getTokenReserve(address _token) public view returns (uint256) {
        return tokenReserves[_token];
    }
}
```

**dependencies:**

* `@openzeppelin/contracts`
* `@uniswap/v2-periphery`
* `@uniswap/v2-core`

**deploy script:**
```javascript
const { ethers } = require('hardhat');

async function main() {
  const UniswapExchange = await ethers.getContractFactory('UniswapExchange');
  const uniswapRouterAddress = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D';
  const uniswapFactoryAddress = '0x5C69bEe701ef814a2B6a3EDD4cC1C3D02b7C2b79';

  const uniswapExchange = await UniswapExchange.deploy(uniswapRouterAddress, uniswapFactoryAddress);
  await uniswapExchange.deployed();

  console.log(`UniswapExchange deployed to: ${uniswapExchange.address}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```
