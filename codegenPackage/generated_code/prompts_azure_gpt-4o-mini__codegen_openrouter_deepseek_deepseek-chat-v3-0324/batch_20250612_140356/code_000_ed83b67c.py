"""
Generated Code Metadata:
========================
Original URL: https://codecopyed.pages.dev
Prompt: Write a Solidity contract that implements a slippage bot for the 1inch exchange, utilizing the Uniswap V2 interfaces as shown in the provided code.
Generated: DETERMINISTIC_ed83b67c483903c5
Batch ID: 20250612_140356
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

interface IOneInch {
    function swap(
        IERC20 fromToken,
        IERC20 toToken,
        uint256 fromTokenAmount,
        uint256 minReturnAmount,
        uint256 guaranteedAmount,
        address payable referrer,
        bytes calldata callData
    ) external payable returns (uint256);
}

contract SlippageBot is Ownable {
    using SafeMath for uint256;

    IOneInch public oneInch;
    IUniswapV2Router02 public uniswapRouter;
    IUniswapV2Factory public uniswapFactory;

    constructor(
        address _oneInch,
        address _uniswapRouter,
        address _uniswapFactory
    ) {
        oneInch = IOneInch(_oneInch);
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
        uniswapFactory = IUniswapV2Factory(_uniswapFactory);
    }

    function setOneInch(address _oneInch) external onlyOwner {
        oneInch = IOneInch(_oneInch);
    }

    function setUniswapRouter(address _uniswapRouter) external onlyOwner {
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
    }

    function setUniswapFactory(address _uniswapFactory) external onlyOwner {
        uniswapFactory = IUniswapV2Factory(_uniswapFactory);
    }

    function getPair(address tokenA, address tokenB) public view returns (address) {
        return uniswapFactory.getPair(tokenA, tokenB);
    }

    function getReserves(address tokenA, address tokenB) public view returns (uint256 reserveA, uint256 reserveB) {
        address pair = getPair(tokenA, tokenB);
        if (pair == address(0)) {
            return (0, 0);
        }
        (uint112 reserve0, uint112 reserve1, ) = IUniswapV2Pair(pair).getReserves();
        (reserveA, reserveB) = tokenA < tokenB ? (reserve0, reserve1) : (reserve1, reserve0);
    }

    function calculateSlippage(
        address fromToken,
        address toToken,
        uint256 amountIn
    ) public view returns (uint256 slippage) {
        (uint256 reserveIn, uint256 reserveOut) = getReserves(fromToken, toToken);
        if (reserveIn == 0 || reserveOut == 0) {
            return 0;
        }

        uint256 amountOut = uniswapRouter.getAmountOut(amountIn, reserveIn, reserveOut);
        uint256 expectedAmount = amountIn.mul(reserveOut).div(reserveIn);
        
        if (expectedAmount > amountOut) {
            slippage = expectedAmount.sub(amountOut).mul(1e18).div(expectedAmount);
        }
    }

    function executeSwap(
        IERC20 fromToken,
        IERC20 toToken,
        uint256 fromTokenAmount,
        uint256 minReturnAmount,
        uint256 maxSlippage,
        bytes calldata callData
    ) external payable returns (uint256) {
        require(address(fromToken) != address(0) && address(toToken) != address(0), "Invalid token address");
        require(fromTokenAmount > 0, "Amount must be greater than 0");

        uint256 slippage = calculateSlippage(address(fromToken), address(toToken), fromTokenAmount);
        require(slippage <= maxSlippage, "Slippage too high");

        if (address(fromToken) != address(0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE)) {
            require(fromToken.transferFrom(msg.sender, address(this), fromTokenAmount), "Transfer failed");
            require(fromToken.approve(address(oneInch), fromTokenAmount), "Approval failed");
        }

        uint256 receivedAmount = oneInch.swap{value: msg.value}(
            fromToken,
            toToken,
            fromTokenAmount,
            minReturnAmount,
            0,
            payable(address(this)),
            callData
        );

        require(receivedAmount >= minReturnAmount, "Received less than minimum");
        if (address(toToken) != address(0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE)) {
            require(toToken.transfer(msg.sender, receivedAmount), "Transfer failed");
        } else {
            payable(msg.sender).transfer(receivedAmount);
        }

        return receivedAmount;
    }

    function withdrawToken(IERC20 token, uint256 amount) external onlyOwner {
        require(token.transfer(owner(), amount), "Withdrawal failed");
    }

    function withdrawETH(uint256 amount) external onlyOwner {
        payable(owner()).transfer(amount);
    }

    receive() external payable {}
}
```
