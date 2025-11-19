"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-org.vercel.app
Prompt: What are the steps to build oracles using Uniswap's reliable on-chain price feeds?
Generated: DETERMINISTIC_3c145c8f65b999fc
Batch ID: 20250612_135409
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract UniswapOracle is Ownable {
    using SafeMath for uint256;

    // Address of the Uniswap V2 Router
    IUniswapV2Router02 public uniswapRouter;

    // Event to emit when price is updated
    event PriceUpdated(address indexed tokenPair, uint256 price);

    // Mapping to store price feeds
    mapping(address => uint256) public priceFeeds;

    // Constructor to set the Uniswap Router address
    constructor(address _router) {
        require(_router != address(0), "Invalid router address");
        uniswapRouter = IUniswapV2Router02(_router);
    }

    // Function to fetch the price of a token pair from Uniswap
    function updatePrice(address tokenA, address tokenB) external onlyOwner {
        address pair = IUniswapV2Factory(uniswapRouter.factory()).getPair(tokenA, tokenB);
        require(pair != address(0), "Pair does not exist");

        IUniswapV2Pair uniswapPair = IUniswapV2Pair(pair);
        (uint112 reserve0, uint112 reserve1, ) = uniswapPair.getReserves();

        // Calculate price based on reserves
        uint256 price;
        if (tokenA < tokenB) {
            price = reserve1.mul(1e18).div(reserve0); // Price of tokenB in terms of tokenA
        } else {
            price = reserve0.mul(1e18).div(reserve1); // Price of tokenA in terms of tokenB
        }

        // Update the price feed
        priceFeeds[pair] = price;

        emit PriceUpdated(pair, price);
    }

    // Getter for prices
    function getPrice(address tokenA, address tokenB) external view returns (uint256) {
        address pair = IUniswapV2Factory(uniswapRouter.factory()).getPair(tokenA, tokenB);
        require(pair != address(0), "Pair does not exist");
        return priceFeeds[pair];
    }

    // Function to set new Uniswap Router (if required)
    function setRouter(address _router) external onlyOwner {
        require(_router != address(0), "Invalid router address");
        uniswapRouter = IUniswapV2Router02(_router);
    }
}
```
