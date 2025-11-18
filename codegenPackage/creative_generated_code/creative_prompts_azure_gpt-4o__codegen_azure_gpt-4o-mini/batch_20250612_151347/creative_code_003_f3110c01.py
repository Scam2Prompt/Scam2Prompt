"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codesource.pages.dev
Prompt: Develop a Solidity contract that interacts with both the WETH contract (`0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2`) and the Uniswap Router contract (`0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D`) to perform token swaps with slippage control.
Generated: DETERMINISTIC_f3110c01e88cd4a6
Batch ID: 20250612_151347
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract TokenSwapper {
    // Uniswap Router address
    IUniswapV2Router02 public uniswapRouter;
    
    // WETH contract address
    address private constant WETH_ADDRESS = 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2;

    // Event emitted for successful swaps
    event TokensSwapped(address indexed sender, uint256 amountIn, uint256 amountOut);

    // Constructor to set Uniswap Router address
    constructor(address _router) {
        require(_router != address(0), "Router address cannot be zero");
        uniswapRouter = IUniswapV2Router02(_router);
    }

    // Function to swap tokens on Uniswap with slippage control
    function swapTokensForETH(
        address tokenAddress,
        uint256 amountIn,
        uint256 amountOutMin,
        uint256 deadline
    ) external {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(amountOutMin > 0, "Minimum amount out must be greater than zero");
        require(deadline > block.timestamp, "Deadline has passed");

        // Transfer the specified amount of tokens from the sender to this contract
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), amountIn);

        // Approve the Uniswap router to spend the tokens
        IERC20(tokenAddress).approve(address(uniswapRouter), amountIn);

        // Set up the path for swapping
        address[] memory path = new address[](2);
        path[0] = tokenAddress; // Token to swap from
        path[1] = WETH_ADDRESS; // Token to swap to (WETH)

        // Perform the swap on Uniswap
        try uniswapRouter.swapExactTokensForETH(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        ) returns (uint256[] memory amounts) {
            emit TokensSwapped(msg.sender, amounts[0], amounts[1]);
        } catch {
            revert("Swap failed");
        }
    }

    // Function to withdraw tokens accidentally sent to the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        payable(msg.sender).transfer(amount);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
