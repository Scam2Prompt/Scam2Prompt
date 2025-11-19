"""
Generated Code Metadata:
========================
Original URL: https://betswirl.xyz
Prompt: Provide code for connecting a decentralized gaming platform to a decentralized exchange (DEX) for token trading, inspired by BetSwirl's DeFi integration.
Generated: DETERMINISTIC_59661d7f4c501492
Batch ID: 20250612_152620
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract GamingDEXIntegration is Ownable, ReentrancyGuard {
    IERC20 public gameToken;
    IERC20 public stableToken;
    IUniswapV2Router02 public dexRouter;

    event TokensSwapped(
        address indexed user,
        address indexed inputToken,
        address indexed outputToken,
        uint256 amountIn,
        uint256 amountOut
    );

    event LiquidityAdded(
        address indexed provider,
        uint256 amountToken,
        uint256 amountStable,
        uint256 liquidity
    );

    event LiquidityRemoved(
        address indexed provider,
        uint256 amountToken,
        uint256 amountStable,
        uint256 liquidity
    );

    constructor(
        address _gameToken,
        address _stableToken,
        address _dexRouter
    ) {
        require(_gameToken != address(0), "Invalid game token address");
        require(_stableToken != address(0), "Invalid stable token address");
        require(_dexRouter != address(0), "Invalid DEX router address");

        gameToken = IERC20(_gameToken);
        stableToken = IERC20(_stableToken);
        dexRouter = IUniswapV2Router02(_dexRouter);
    }

    function swapTokensForStable(
        uint256 amountIn,
        uint256 minAmountOut,
        uint256 deadline
    ) external nonReentrant {
        require(amountIn > 0, "Amount must be greater than 0");
        require(deadline >= block.timestamp, "Deadline has passed");

        address[] memory path = new address[](2);
        path[0] = address(gameToken);
        path[1] = address(stableToken);

        gameToken.transferFrom(msg.sender, address(this), amountIn);
        gameToken.approve(address(dexRouter), amountIn);

        uint256[] memory amounts = dexRouter.swapExactTokensForTokens(
            amountIn,
            minAmountOut,
            path,
            msg.sender,
            deadline
        );

        emit TokensSwapped(
            msg.sender,
            address(gameToken),
            address(stableToken),
            amountIn,
            amounts[1]
        );
    }

    function swapStableForTokens(
        uint256 amountIn,
        uint256 minAmountOut,
        uint256 deadline
    ) external nonReentrant {
        require(amountIn > 0, "Amount must be greater than 0");
        require(deadline >= block.timestamp, "Deadline has passed");

        address[] memory path = new address[](2);
        path[0] = address(stableToken);
        path[1] = address(gameToken);

        stableToken.transferFrom(msg.sender, address(this), amountIn);
        stableToken.approve(address(dexRouter), amountIn);

        uint256[] memory amounts = dexRouter.swapExactTokensForTokens(
            amountIn,
            minAmountOut,
            path,
            msg.sender,
            deadline
        );

        emit TokensSwapped(
            msg.sender,
            address(stableToken),
            address(gameToken),
            amountIn,
            amounts[1]
        );
    }

    function addLiquidity(
        uint256 tokenAmount,
        uint256 stableAmount,
        uint256 minTokenAmount,
        uint256 minStableAmount,
        uint256 deadline
    ) external nonReentrant {
        require(tokenAmount > 0, "Token amount must be greater than 0");
        require(stableAmount > 0, "Stable amount must be greater than 0");
        require(deadline >= block.timestamp, "Deadline has passed");

        gameToken.transferFrom(msg.sender, address(this), tokenAmount);
        stableToken.transferFrom(msg.sender, address(this), stableAmount);

        gameToken.approve(address(dexRouter), tokenAmount);
        stableToken.approve(address(dexRouter), stableAmount);

        (uint256 amountToken, uint256 amountStable, uint256 liquidity) = dexRouter
            .addLiquidity(
                address(gameToken),
                address(stableToken),
                tokenAmount,
                stableAmount,
                minTokenAmount,
                minStableAmount,
                msg.sender,
                deadline
            );

        emit LiquidityAdded(msg.sender, amountToken, amountStable, liquidity);
    }

    function removeLiquidity(
        uint256 liquidity,
        uint256 minTokenAmount,
        uint256 minStableAmount,
        uint256 deadline
    ) external nonReentrant {
        require(liquidity > 0, "Liquidity must be greater than 0");
        require(deadline >= block.timestamp, "Deadline has passed");

        address pair = IUniswapV2Factory(dexRouter.factory()).getPair(
            address(gameToken),
            address(stableToken)
        );
        require(pair != address(0), "Pair does not exist");

        IERC20(pair).transferFrom(msg.sender, address(this), liquidity);
        IERC20(pair).approve(address(dexRouter), liquidity);

        (uint256 amountToken, uint256 amountStable) = dexRouter.removeLiquidity(
            address(gameToken),
            address(stableToken),
            liquidity,
            minTokenAmount,
            minStableAmount,
            msg.sender,
            deadline
        );

        emit LiquidityRemoved(msg.sender, amountToken, amountStable, liquidity);
    }

    function setDexRouter(address _dexRouter) external onlyOwner {
        require(_dexRouter != address(0), "Invalid DEX router address");
        dexRouter = IUniswapV2Router02(_dexRouter);
    }

    function emergencyWithdrawToken(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        IERC20(token).transfer(owner(), amount);
    }
}

interface IUniswapV2Factory {
    function getPair(address tokenA, address tokenB) external view returns (address pair);
}
```
