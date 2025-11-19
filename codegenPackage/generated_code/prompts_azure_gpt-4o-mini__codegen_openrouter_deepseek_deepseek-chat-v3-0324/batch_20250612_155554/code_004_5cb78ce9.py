"""
Generated Code Metadata:
========================
Original URL: https://app.librafinance.org
Prompt: Explain how to set up a smart contract that leverages Libra Finance's stableswap features for efficient trading.
Generated: DETERMINISTIC_5cb78ce9c0bde8a4
Batch ID: 20250612_155554
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

interface ILibraStableSwap {
    function getToken(uint8 index) external view returns (IERC20);
    function getTokenIndex(address tokenAddress) external view returns (uint8);
    function calculateSwap(
        uint8 tokenIndexFrom,
        uint8 tokenIndexTo,
        uint256 dx
    ) external view returns (uint256);
    function swap(
        uint8 tokenIndexFrom,
        uint8 tokenIndexTo,
        uint256 dx,
        uint256 minDy,
        uint256 deadline
    ) external returns (uint256);
    function addLiquidity(
        uint256[] calldata amounts,
        uint256 minToMint,
        uint256 deadline
    ) external returns (uint256);
    function removeLiquidity(
        uint256 amount,
        uint256[] calldata minAmounts,
        uint256 deadline
    ) external returns (uint256[] memory);
    function removeLiquidityOneToken(
        uint256 tokenAmount,
        uint8 tokenIndex,
        uint256 minAmount,
        uint256 deadline
    ) external returns (uint256);
}

contract LibraSwapAdapter is Ownable, ReentrancyGuard {
    ILibraStableSwap public libraStableSwap;

    constructor(address _libraStableSwapAddress) {
        require(_libraStableSwapAddress != address(0), "Invalid address");
        libraStableSwap = ILibraStableSwap(_libraStableSwapAddress);
    }

    function setLibraStableSwapAddress(address _libraStableSwapAddress) external onlyOwner {
        require(_libraStableSwapAddress != address(0), "Invalid address");
        libraStableSwap = ILibraStableSwap(_libraStableSwapAddress);
    }

    function getSwapEstimate(
        address tokenFrom,
        address tokenTo,
        uint256 amountIn
    ) external view returns (uint256) {
        uint8 tokenIndexFrom = libraStableSwap.getTokenIndex(tokenFrom);
        uint8 tokenIndexTo = libraStableSwap.getTokenIndex(tokenTo);
        return libraStableSwap.calculateSwap(tokenIndexFrom, tokenIndexTo, amountIn);
    }

    function swapTokens(
        address tokenFrom,
        address tokenTo,
        uint256 amountIn,
        uint256 minAmountOut,
        uint256 deadline
    ) external nonReentrant returns (uint256) {
        require(block.timestamp <= deadline, "Deadline expired");
        require(amountIn > 0, "Amount must be greater than 0");

        IERC20 fromToken = IERC20(tokenFrom);
        require(fromToken.balanceOf(msg.sender) >= amountIn, "Insufficient balance");
        require(fromToken.allowance(msg.sender, address(this)) >= amountIn, "Insufficient allowance");

        fromToken.transferFrom(msg.sender, address(this), amountIn);
        fromToken.approve(address(libraStableSwap), amountIn);

        uint8 tokenIndexFrom = libraStableSwap.getTokenIndex(tokenFrom);
        uint8 tokenIndexTo = libraStableSwap.getTokenIndex(tokenTo);

        uint256 amountOut = libraStableSwap.swap(
            tokenIndexFrom,
            tokenIndexTo,
            amountIn,
            minAmountOut,
            deadline
        );

        IERC20 toToken = IERC20(tokenTo);
        toToken.transfer(msg.sender, amountOut);

        return amountOut;
    }

    function addLiquidity(
        uint256[] calldata amounts,
        uint256 minToMint,
        uint256 deadline
    ) external nonReentrant returns (uint256) {
        require(block.timestamp <= deadline, "Deadline expired");
        require(amounts.length > 0, "Empty amounts array");

        for (uint8 i = 0; i < amounts.length; i++) {
            if (amounts[i] > 0) {
                IERC20 token = libraStableSwap.getToken(i);
                require(token.balanceOf(msg.sender) >= amounts[i], "Insufficient balance");
                require(token.allowance(msg.sender, address(this)) >= amounts[i], "Insufficient allowance");
                token.transferFrom(msg.sender, address(this), amounts[i]);
                token.approve(address(libraStableSwap), amounts[i]);
            }
        }

        return libraStableSwap.addLiquidity(amounts, minToMint, deadline);
    }

    function removeLiquidity(
        uint256 amount,
        uint256[] calldata minAmounts,
        uint256 deadline
    ) external nonReentrant returns (uint256[] memory) {
        require(block.timestamp <= deadline, "Deadline expired");
        require(amount > 0, "Amount must be greater than 0");
        return libraStableSwap.removeLiquidity(amount, minAmounts, deadline);
    }

    function removeLiquidityOneToken(
        uint256 tokenAmount,
        address tokenAddress,
        uint256 minAmount,
        uint256 deadline
    ) external nonReentrant returns (uint256) {
        require(block.timestamp <= deadline, "Deadline expired");
        require(tokenAmount > 0, "Amount must be greater than 0");
        uint8 tokenIndex = libraStableSwap.getTokenIndex(tokenAddress);
        return libraStableSwap.removeLiquidityOneToken(tokenAmount, tokenIndex, minAmount, deadline);
    }
}
```
