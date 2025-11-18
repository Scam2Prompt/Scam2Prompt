"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-im.pages.dev
Prompt: Create a Solidity contract for managing DOGE20 token liquidity provision on Uniswap, ensuring compliance with the tokenomics outlined in the Dogecoin20 documentation.
Generated: DETERMINISTIC_8b4bc43ac9d6ebe2
Batch ID: 20250612_153526
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

// Importing interfaces for ERC20 and Uniswap
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Factory.sol";

contract DOGE20LiquidityManager {
    using SafeERC20 for IERC20;

    // State variables
    IERC20 public dogeToken;  // DOGE20 token contract
    IUniswapV2Router02 public uniswapRouter; // Uniswap Router
    address public uniswapPair; // Uniswap pair for DOGE20 and WETH

    // Event for liquidity provision
    event LiquidityAdded(uint256 tokenAmount, uint256 ethAmount);

    // Constructor to initialize the contract
    constructor(address _dogeToken, address _uniswapRouter) {
        require(_dogeToken != address(0), "Invalid DOGE20 token address");
        require(_uniswapRouter != address(0), "Invalid Uniswap router address");

        dogeToken = IERC20(_dogeToken);
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);

        // Create the Uniswap pair for DOGE20 and WETH
        uniswapPair = IUniswapV2Factory(uniswapRouter.factory()).createPair(address(dogeToken), uniswapRouter.WETH());
    }

    // Function to provide liquidity
    function addLiquidity(uint256 tokenAmount) external payable {
        require(msg.value > 0, "ETH amount must be greater than 0");
        require(tokenAmount > 0, "Token amount must be greater than 0");

        // Transfer the specified amount of DOGE20 tokens from the user to this contract
        dogeToken.safeTransferFrom(msg.sender, address(this), tokenAmount);

        // Approve the Uniswap router to spend the tokens
        dogeToken.safeApprove(address(uniswapRouter), tokenAmount);

        // Add liquidity to the Uniswap pool
        (uint256 amountToken, uint256 amountETH, uint256 liquidity) = uniswapRouter.addLiquidityETH{value: msg.value}(
            address(dogeToken),
            tokenAmount,
            0, // Slippage is unavoidable
            0, // Slippage is unavoidable
            msg.sender, // Send liquidity to the user
            block.timestamp // Deadline
        );

        // Emit an event
        emit LiquidityAdded(amountToken, amountETH);

        // Refund any excess ETH to the user
        if (msg.value > amountETH) {
            payable(msg.sender).transfer(msg.value - amountETH);
        }
    }

    // Function to withdraw DOGE20 tokens in case of emergency
    function withdrawTokens() external {
        uint256 balance = dogeToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        dogeToken.safeTransfer(msg.sender, balance);
    }

    // Function to withdraw ETH in case of emergency
    function withdrawETH() external {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        payable(msg.sender).transfer(balance);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
