"""
Generated Code Metadata:
========================
Original URL: https://claimalvara.pages.dev
Prompt: Implement a function in Solidity to integrate the Uniswap V2 Router for buying and selling underlying tokens during the creation and withdrawal of ERC-7621 Basket Tokens.
Generated: DETERMINISTIC_7098329d1e83eeaf
Batch ID: 20250612_154820
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
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BasketToken is Ownable {
    // Uniswap V2 Router address
    IUniswapV2Router02 public uniswapRouter;

    // Event emitted when tokens are bought or sold
    event TokensBought(address indexed buyer, uint256 amountIn, uint256 amountOut);
    event TokensSold(address indexed seller, uint256 amountIn, uint256 amountOut);

    // Constructor to set the Uniswap Router address
    constructor(address _router) {
        require(_router != address(0), "Invalid router address");
        uniswapRouter = IUniswapV2Router02(_router);
    }

    // Function to buy tokens using Uniswap
    function buyTokens(address token, uint256 amountIn, uint256 minAmountOut) external payable {
        require(amountIn > 0, "Amount must be greater than 0");
        require(msg.value > 0, "Ether value must be greater than 0");

        // Approve the Uniswap router to spend the specified amount of ETH
        // Note: This is not needed for ETH, but included for consistency
        // IERC20(token).approve(address(uniswapRouter), amountIn);

        // Define the path for the swap (ETH -> Token)
        address[] memory path = new address[](2);
        path[0] = uniswapRouter.WETH();
        path[1] = token;

        // Execute the swap
        uint256[] memory amounts = uniswapRouter.swapExactETHForTokens{value: msg.value}(
            minAmountOut,
            path,
            msg.sender,
            block.timestamp
        );

        emit TokensBought(msg.sender, msg.value, amounts[1]);
    }

    // Function to sell tokens using Uniswap
    function sellTokens(address token, uint256 amountIn, uint256 minAmountOut) external {
        require(amountIn > 0, "Amount must be greater than 0");

        // Transfer tokens from the seller to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amountIn);

        // Approve the Uniswap router to spend the specified amount of tokens
        IERC20(token).approve(address(uniswapRouter), amountIn);

        // Define the path for the swap (Token -> ETH)
        address[] memory path = new address[](2);
        path[0] = token;
        path[1] = uniswapRouter.WETH();

        // Execute the swap
        uint256[] memory amounts = uniswapRouter.swapExactTokensForETH(
            amountIn,
            minAmountOut,
            path,
            msg.sender,
            block.timestamp
        );

        emit TokensSold(msg.sender, amountIn, amounts[1]);
    }

    // Function to withdraw any ETH from the contract (only owner)
    function withdrawETH() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw any ERC20 tokens from the contract (only owner)
    function withdrawTokens(address token) external onlyOwner {
        uint256 balance = IERC20(token).balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        IERC20(token).transfer(owner(), balance);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
