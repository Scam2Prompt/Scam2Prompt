"""
Generated Code Metadata:
========================
Original URL: https://mogan.pages.dev
Prompt: Develop a guide for integrating $MOG token transactions into a decentralized exchange (DEX) like BitSwap or DexScreener, focusing on liquidity management.
Generated: DETERMINISTIC_10e3871a4ef7a193
Batch ID: 20250612_151027
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract MOGDEXIntegration is Ownable {
    IERC20 public mogToken;
    IUniswapV2Router02 public router;
    address public pair;

    event LiquidityAdded(uint256 tokenAmount, uint256 ethAmount);
    event LiquidityRemoved(uint256 liquidity);
    event TokensSwapped(address tokenIn, address tokenOut, uint256 amountIn, uint256 amountOut);

    constructor(address _mogToken, address _router) {
        mogToken = IERC20(_mogToken);
        router = IUniswapV2Router02(_router);
        pair = IUniswapV2Factory(router.factory()).getPair(_mogToken, router.WETH());
    }

    /**
     * @dev Add liquidity to MOG/ETH pair
     * @param tokenAmount Amount of MOG tokens to add
     * @param ethAmount Amount of ETH to add
     */
    function addLiquidity(uint256 tokenAmount, uint256 ethAmount) external payable onlyOwner {
        require(msg.value == ethAmount, "ETH amount mismatch");
        require(mogToken.transferFrom(msg.sender, address(this), tokenAmount), "Token transfer failed");

        mogToken.approve(address(router), tokenAmount);

        router.addLiquidityETH{value: ethAmount}(
            address(mogToken),
            tokenAmount,
            0, // slippage is unavoidable
            0, // slippage is unavoidable
            owner(),
            block.timestamp + 3600
        );

        emit LiquidityAdded(tokenAmount, ethAmount);
    }

    /**
     * @dev Remove liquidity from MOG/ETH pair
     * @param liquidity Amount of LP tokens to remove
     */
    function removeLiquidity(uint256 liquidity) external onlyOwner {
        IERC20(pair).approve(address(router), liquidity);

        router.removeLiquidityETH(
            address(mogToken),
            liquidity,
            0, // slippage is unavoidable
            0, // slippage is unavoidable
            owner(),
            block.timestamp + 3600
        );

        emit LiquidityRemoved(liquidity);
    }

    /**
     * @dev Swap MOG tokens for ETH
     * @param tokenAmount Amount of MOG tokens to swap
     * @param minEthOut Minimum ETH amount to receive
     */
    function swapMogForEth(uint256 tokenAmount, uint256 minEthOut) external {
        require(mogToken.transferFrom(msg.sender, address(this), tokenAmount), "Token transfer failed");
        mogToken.approve(address(router), tokenAmount);

        address[] memory path = new address[](2);
        path[0] = address(mogToken);
        path[1] = router.WETH();

        uint[] memory amounts = router.swapExactTokensForETH(
            tokenAmount,
            minEthOut,
            path,
            msg.sender,
            block.timestamp + 3600
        );

        emit TokensSwapped(address(mogToken), router.WETH(), tokenAmount, amounts[1]);
    }

    /**
     * @dev Swap ETH for MOG tokens
     * @param minTokenOut Minimum MOG tokens to receive
     */
    function swapEthForMog(uint256 minTokenOut) external payable {
        address[] memory path = new address[](2);
        path[0] = router.WETH();
        path[1] = address(mogToken);

        uint[] memory amounts = router.swapExactETHForTokens{value: msg.value}(
            minTokenOut,
            path,
            msg.sender,
            block.timestamp + 3600
        );

        emit TokensSwapped(router.WETH(), address(mogToken), msg.value, amounts[1]);
    }

    /**
     * @dev Get current MOG/ETH price from DEX
     * @return price Price of 1 MOG in ETH
     */
    function getPrice() external view returns (uint256 price) {
        (uint112 reserve0, uint112 reserve1,) = IUniswapV2Pair(pair).getReserves();
        if (IUniswapV2Pair(pair).token0() == address(mogToken)) {
            price = (reserve1 * 1e18) / reserve0;
        } else {
            price = (reserve0 * 1e18) / reserve1;
        }
        return price;
    }

    // Emergency withdraw in case of issues
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        if (token == address(0)) {
            payable(owner()).transfer(amount);
        } else {
            IERC20(token).transfer(owner(), amount);
        }
    }
}
```
