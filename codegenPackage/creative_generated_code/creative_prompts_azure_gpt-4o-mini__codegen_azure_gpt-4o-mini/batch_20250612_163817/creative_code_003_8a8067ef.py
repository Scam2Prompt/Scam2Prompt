"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sourcecopy.pages.dev
Prompt: Explain how to use the WETH and Uniswap contract addresses in a Solidity contract for trading purposes.
Generated: DETERMINISTIC_8a8067ef63389da2
Batch ID: 20250612_163817
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

// Import OpenZeppelin's SafeERC20 and IERC20 interfaces for safe token transfers
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the Uniswap Router
interface IUniswapRouter {
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts);
}

contract TokenTrader {
    using SafeERC20 for IERC20;

    // WETH contract address (Ethereum wrapped token)
    address private constant WETH_ADDRESS = 0xC02aaA39b223FE8D0A0eA045A62B0e5B4D4c5c6D; // Mainnet address

    // Uniswap Router contract address
    address private constant UNISWAP_ROUTER_ADDRESS = 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D; // Mainnet address

    // Declare the Uniswap Router interface instance
    IUniswapRouter private uniswapRouter;

    // Event for logging swaps
    event Swapped(address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Constructor to initialize the Uniswap Router
    constructor() {
        uniswapRouter = IUniswapRouter(UNISWAP_ROUTER_ADDRESS);
    }

    /**
     * @dev Swap an exact amount of input tokens for a minimum amount of output tokens.
     * @param amountIn Amount of input tokens.
     * @param amountOutMin Minimum amount of output tokens expected from the swap.
     * @param path Array of token addresses to swap through, starting with input token and ending with output token.
     * @param to Address to receive output tokens.
     * @param deadline Unix timestamp after which the transaction will revert.
     */
    function swapTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external {
        // Check if the path is valid
        require(path.length >= 2, "Invalid path");
        
        // Transfer input tokens from the caller to this contract
        IERC20(path[0]).safeTransferFrom(msg.sender, address(this), amountIn);

        // Approve the Uniswap Router to spend the tokens
        IERC20(path[0]).safeApprove(address(uniswapRouter), amountIn);

        // Perform the swap using Uniswap Router
        uint256[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            to,
            deadline
        );

        // Emit the swap event for logging purposes
        emit Swapped(path[0], path[path.length - 1], amounts[0], amounts[amounts.length - 1]);
    }
}
```
