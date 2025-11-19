"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-im.pages.dev
Prompt: Create a Solidity contract for managing DOGE20 token liquidity provision on Uniswap, ensuring compliance with the tokenomics outlined in the Dogecoin20 documentation.
Generated: DETERMINISTIC_8b4bc43ac9d6ebe2
Batch ID: 20250612_153526
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";

contract DOGE20LiquidityManager {
    using SafeERC20 for IERC20;

    // State variables
    address public owner;
    IERC20 public doge20Token;
    IUniswapV2Router02 public uniswapRouter;
    address public uniswapPair;

    // Events
    event LiquidityAdded(uint256 tokenAmount, uint256 ethAmount);
    event LiquidityRemoved(uint256 tokenAmount, uint256 ethAmount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _doge20Token, address _uniswapRouter) {
        owner = msg.sender;
        doge20Token = IERC20(_doge20Token);
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
        uniswapPair = IUniswapV2Factory(uniswapRouter.factory()).getPair(address(doge20Token), uniswapRouter.WETH());
    }

    // Function to add liquidity to Uniswap
    function addLiquidity(uint256 tokenAmount) external payable onlyOwner {
        require(tokenAmount > 0, "Token amount must be greater than 0");
        require(msg.value > 0, "ETH amount must be greater than 0");

        // Approve the Uniswap router to spend the tokens
        doge20Token.safeApprove(address(uniswapRouter), tokenAmount);

        // Add liquidity to Uniswap
        (uint256 amountToken, uint256 amountETH, uint256 liquidity) = uniswapRouter.addLiquidityETH{value: msg.value}(
            address(doge20Token),
            tokenAmount,
            0, // slippage is unavoidable
            0, // slippage is unavoidable
            owner,
            block.timestamp
        );

        emit LiquidityAdded(amountToken, amountETH);
    }

    // Function to remove liquidity from Uniswap
    function removeLiquidity(uint256 liquidity) external onlyOwner {
        require(liquidity > 0, "Liquidity amount must be greater than 0");

        // Approve the Uniswap router to spend the liquidity tokens
        IERC20(uniswapPair).safeApprove(address(uniswapRouter), liquidity);

        // Remove liquidity from Uniswap
        (uint256 amountToken, uint256 amountETH) = uniswapRouter.removeLiquidityETH(
            address(doge20Token),
            liquidity,
            0, // slippage is unavoidable
            0, // slippage is unavoidable
            owner,
            block.timestamp
        );

        emit LiquidityRemoved(amountToken, amountETH);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        payable(owner).transfer(balance);
    }

    // Function to withdraw DOGE20 tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Token amount must be greater than 0");
        doge20Token.safeTransfer(owner, amount);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
