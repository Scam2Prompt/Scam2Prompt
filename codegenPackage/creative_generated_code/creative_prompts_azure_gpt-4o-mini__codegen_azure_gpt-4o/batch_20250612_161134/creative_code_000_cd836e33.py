"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-slippagebot.pages.dev
Prompt: Write a Solidity function for a Uniswap slippage bot that can handle mainnet transactions, referencing the contract structure provided in the UniswapSlippageBot example.
Generated: DETERMINISTIC_cd836e33226a3b63
Batch ID: 20250612_161134
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

// Import necessary interfaces from Uniswap
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IERC20.sol";

contract UniswapSlippageBot {
    address private owner;
    IUniswapV2Router02 private uniswapRouter;

    // Constants for slippage tolerance
    uint256 private constant SLIPPAGE_TOLERANCE = 5; // 5% slippage

    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    constructor(address _uniswapRouter) {
        require(_uniswapRouter != address(0), "Invalid router address");
        owner = msg.sender;
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
    }

    /**
     * @dev Execute a token swap on Uniswap with slippage control.
     * @param tokenIn The address of the token to sell.
     * @param tokenOut The address of the token to buy.
     * @param amountIn The amount of tokenIn to swap.
     * @param minAmountOut The minimum amount of tokenOut to receive after slippage.
     */
    function executeSwap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut
    ) external onlyOwner {
        require(tokenIn != address(0) && tokenOut != address(0), "Invalid token addresses");
        require(amountIn > 0, "Amount in must be greater than zero");
        require(minAmountOut > 0, "Min amount out must be greater than zero");

        // Approve the Uniswap router to spend tokenIn
        IERC20(tokenIn).approve(address(uniswapRouter), amountIn);

        // Get the current timestamp
        uint256 deadline = block.timestamp + 300; // 5-minute deadline for transaction execution

        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        try uniswapRouter.swapExactTokensForTokens(
            amountIn,
            minAmountOut,
            path,
            address(this),
            deadline
        ) {
            // Successful swap
        } catch {
            revert("Uniswap swap failed");
        }
    }

    /**
     * @dev Withdraw tokens from the contract.
     * @param token The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20(token).transfer(owner, amount);
    }

    /**
     * @dev Withdraw Ether from the contract.
     * @param amount The amount of Ether to withdraw.
     */
    function withdrawEther(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        payable(owner).transfer(amount);
    }

    // Fallback function to accept Ether deposits
    receive() external payable {}

    // Function to update the router address (if needed)
    function updateRouter(address _uniswapRouter) external onlyOwner {
        require(_uniswapRouter != address(0), "Invalid router address");
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
    }
}
```
