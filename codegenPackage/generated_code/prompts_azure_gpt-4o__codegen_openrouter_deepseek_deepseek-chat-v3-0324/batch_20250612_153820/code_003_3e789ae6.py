"""
Generated Code Metadata:
========================
Original URL: https://store-uni-app.com
Prompt: Write a Solidity smart contract that integrates with the Uniswap protocol to automate token swaps based on predefined market conditions.
Generated: DETERMINISTIC_3e789ae645f93bc8
Batch ID: 20250612_153820
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

import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract UniswapAutoSwapper is Ownable, ReentrancyGuard {
    IUniswapV2Router02 public immutable uniswapRouter;
    address public immutable WETH;

    struct SwapCondition {
        address tokenIn;
        address tokenOut;
        uint256 minAmountOut;
        uint256 priceThreshold; // price in terms of tokenOut per tokenIn (multiplied by 1e18)
        bool isAboveThreshold;
        bool isActive;
    }

    mapping(uint256 => SwapCondition) public swapConditions;
    uint256 public conditionCount;

    event SwapExecuted(
        uint256 conditionId,
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );
    event ConditionAdded(uint256 conditionId, SwapCondition condition);
    event ConditionUpdated(uint256 conditionId, SwapCondition condition);
    event ConditionRemoved(uint256 conditionId);
    event TokensWithdrawn(address indexed token, uint256 amount);

    constructor(address _router) {
        uniswapRouter = IUniswapV2Router02(_router);
        WETH = uniswapRouter.WETH();
    }

    function addSwapCondition(
        address _tokenIn,
        address _tokenOut,
        uint256 _minAmountOut,
        uint256 _priceThreshold,
        bool _isAboveThreshold
    ) external onlyOwner {
        require(_tokenIn != address(0) && _tokenOut != address(0), "Invalid token address");
        require(_priceThreshold > 0, "Price threshold must be positive");

        uint256 conditionId = conditionCount++;
        swapConditions[conditionId] = SwapCondition({
            tokenIn: _tokenIn,
            tokenOut: _tokenOut,
            minAmountOut: _minAmountOut,
            priceThreshold: _priceThreshold,
            isAboveThreshold: _isAboveThreshold,
            isActive: true
        });

        emit ConditionAdded(conditionId, swapConditions[conditionId]);
    }

    function updateSwapCondition(
        uint256 _conditionId,
        uint256 _minAmountOut,
        uint256 _priceThreshold,
        bool _isAboveThreshold,
        bool _isActive
    ) external onlyOwner {
        require(_conditionId < conditionCount, "Invalid condition ID");
        require(_priceThreshold > 0, "Price threshold must be positive");

        SwapCondition storage condition = swapConditions[_conditionId];
        condition.minAmountOut = _minAmountOut;
        condition.priceThreshold = _priceThreshold;
        condition.isAboveThreshold = _isAboveThreshold;
        condition.isActive = _isActive;

        emit ConditionUpdated(_conditionId, condition);
    }

    function removeSwapCondition(uint256 _conditionId) external onlyOwner {
        require(_conditionId < conditionCount, "Invalid condition ID");
        delete swapConditions[_conditionId];
        emit ConditionRemoved(_conditionId);
    }

    function checkAndExecuteSwaps() external nonReentrant {
        for (uint256 i = 0; i < conditionCount; i++) {
            SwapCondition memory condition = swapConditions[i];
            if (!condition.isActive) continue;

            uint256 currentPrice = getCurrentPrice(condition.tokenIn, condition.tokenOut);
            bool shouldExecute = condition.isAboveThreshold
                ? currentPrice >= condition.priceThreshold
                : currentPrice <= condition.priceThreshold;

            if (shouldExecute) {
                _executeSwap(i, condition);
            }
        }
    }

    function getCurrentPrice(address tokenIn, address tokenOut) public view returns (uint256) {
        if (tokenIn == tokenOut) return 1e18;

        address factory = uniswapRouter.factory();
        address pair = IUniswapV2Factory(factory).getPair(tokenIn, tokenOut);
        require(pair != address(0), "No pair exists");

        (uint256 reserve0, uint256 reserve1, ) = IUniswapV2Pair(pair).getReserves();
        (uint256 reserveIn, uint256 reserveOut) = tokenIn < tokenOut
            ? (reserve0, reserve1)
            : (reserve1, reserve0);

        return (reserveOut * 1e18) / reserveIn;
    }

    function _executeSwap(uint256 conditionId, SwapCondition memory condition) private {
        address tokenIn = condition.tokenIn;
        address tokenOut = condition.tokenOut;

        uint256 balance = IERC20(tokenIn).balanceOf(address(this));
        require(balance > 0, "No balance to swap");

        IERC20(tokenIn).approve(address(uniswapRouter), balance);

        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        uint256[] memory amountsOut = uniswapRouter.getAmountsOut(balance, path);
        require(
            amountsOut[amountsOut.length - 1] >= condition.minAmountOut,
            "Insufficient output amount"
        );

        uint256[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            balance,
            condition.minAmountOut,
            path,
            address(this),
            block.timestamp + 300
        );

        emit SwapExecuted(conditionId, tokenIn, tokenOut, amounts[0], amounts[1]);
    }

    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be positive");
        if (token == address(0)) {
            payable(owner()).transfer(amount);
        } else {
            IERC20(token).transfer(owner(), amount);
        }
        emit TokensWithdrawn(token, amount);
    }

    receive() external payable {}
}

interface IUniswapV2Pair {
    function getReserves() external view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast);
}
```
