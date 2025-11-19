"""
Generated Code Metadata:
========================
Original URL: https://updatedcode.pages.dev
Prompt: Write a Solidity smart contract that replicates the functionality of the "Oneinch Slippage Bot" described on the webpage, including the ability to find newly deployed contracts on Uniswap with specific liquidity requirements.
Generated: DETERMINISTIC_921c72fe84fc91ea
Batch ID: 20250612_150902
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract OneInchSlippageBot is Ownable {
    IUniswapV2Factory public immutable uniswapFactory;
    IUniswapV2Router02 public immutable uniswapRouter;
    address public immutable WETH;

    struct TokenPair {
        address token;
        address pair;
        uint256 liquidity;
    }

    event NewPairDetected(address indexed token, address indexed pair, uint256 liquidity);
    event SlippageTradeExecuted(address indexed token, uint256 amountIn, uint256 amountOut);

    constructor(address _factory, address _router, address _weth) {
        uniswapFactory = IUniswapV2Factory(_factory);
        uniswapRouter = IUniswapV2Router02(_router);
        WETH = _weth;
    }

    /**
     * @dev Scan for new token pairs with minimum liquidity
     * @param minLiquidity Minimum liquidity threshold in ETH
     * @param maxPairs Maximum number of pairs to return
     * @return TokenPair[] Array of token pairs meeting criteria
     */
    function scanNewPairs(uint256 minLiquidity, uint256 maxPairs) external returns (TokenPair[] memory) {
        uint256 pairCount = uniswapFactory.allPairsLength();
        TokenPair[] memory foundPairs = new TokenPair[](maxPairs);
        uint256 foundCount = 0;

        for (uint256 i = pairCount > 100 ? pairCount - 100 : 0; i < pairCount && foundCount < maxPairs; i++) {
            address pairAddress = uniswapFactory.allPairs(i);
            IUniswapV2Pair pair = IUniswapV2Pair(pairAddress);

            if (pair.totalSupply() == 0) continue; // Skip empty pairs

            address token0 = pair.token0();
            address token1 = pair.token1();
            address token = token0 == WETH ? token1 : (token1 == WETH ? token0 : address(0));

            if (token == address(0)) continue; // Skip non-WETH pairs

            (uint112 reserve0, uint112 reserve1,) = pair.getReserves();
            uint256 liquidity = token0 == WETH ? 
                uint256(reserve0) * 2 : 
                uint256(reserve1) * 2;

            if (liquidity >= minLiquidity) {
                foundPairs[foundCount] = TokenPair(token, pairAddress, liquidity);
                foundCount++;
                emit NewPairDetected(token, pairAddress, liquidity);
            }
        }

        // Resize array to actual found count
        TokenPair[] memory result = new TokenPair[](foundCount);
        for (uint256 i = 0; i < foundCount; i++) {
            result[i] = foundPairs[i];
        }

        return result;
    }

    /**
     * @dev Execute trade with slippage protection
     * @param tokenIn Input token address
     * @param tokenOut Output token address
     * @param amountIn Amount of input tokens
     * @param minAmountOut Minimum acceptable amount of output tokens
     * @param deadline Transaction deadline
     */
    function executeTrade(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        uint256 deadline
    ) external onlyOwner {
        require(deadline >= block.timestamp, "Deadline expired");
        require(amountIn > 0, "Invalid amount");

        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        IERC20(tokenIn).approve(address(uniswapRouter), amountIn);

        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        uint256[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            minAmountOut,
            path,
            address(this),
            deadline
        );

        emit SlippageTradeExecuted(tokenOut, amountIn, amounts[1]);
    }

    /**
     * @dev Withdraw tokens from contract
     * @param token Token address to withdraw
     * @param amount Amount to withdraw
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(msg.sender, amount);
    }

    /**
     * @dev Withdraw ETH from contract
     * @param amount Amount to withdraw
     */
    function withdrawETH(uint256 amount) external onlyOwner {
        payable(msg.sender).transfer(amount);
    }

    receive() external payable {}
}
```
