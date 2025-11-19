"""
Generated Code Metadata:
========================
Original URL: https://sourcecopy.pages.dev
Prompt: Explain how to use the WETH and Uniswap contract addresses in a Solidity contract for trading purposes.
Generated: DETERMINISTIC_8a8067ef63389da2
Batch ID: 20250612_163817
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

/**
 * @title UniswapTrading
 * @dev A contract for trading tokens using Uniswap and WETH.
 */
contract UniswapTrading {
    // Address of the WETH token contract
    address public constant WETH_ADDRESS = 0xC02aaA39b223FE8D0a0e5C4F27eAD9083C756Cc2; // Mainnet WETH address

    // Address of the Uniswap V2 Router contract
    address public constant UNISWAP_ROUTER_ADDRESS = 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D; // Mainnet Uniswap V2 Router address

    // Interface for interacting with the Uniswap V2 Router
    IUniswapV2Router public uniswapRouter;

    // Constructor to initialize the Uniswap Router
    constructor() {
        uniswapRouter = IUniswapV2Router(UNISWAP_ROUTER_ADDRESS);
    }

    /**
     * @dev Swaps ETH for a specified ERC20 token using Uniswap.
     * @param tokenAddress The address of the ERC20 token to swap for.
     * @param amountOutMin The minimum amount of tokens to receive.
     */
    function swapETHForTokens(address tokenAddress, uint256 amountOutMin) external payable {
        require(msg.value > 0, "Must send ETH to swap");

        // Path for the swap: ETH -> WETH -> Token
        address[] memory path = new address[](2);
        path[0] = WETH_ADDRESS;
        path[1] = tokenAddress;

        // Perform the swap
        uniswapRouter.swapExactETHForTokens{value: msg.value}(
            amountOutMin, // Minimum amount of tokens to receive
            path,         // Path for the swap
            msg.sender,   // Recipient of the tokens
            block.timestamp // Deadline for the transaction
        );
    }

    /**
     * @dev Swaps a specified ERC20 token for ETH using Uniswap.
     * @param tokenAddress The address of the ERC20 token to swap.
     * @param tokenAmount The amount of tokens to swap.
     * @param amountOutMin The minimum amount of ETH to receive.
     */
    function swapTokensForETH(address tokenAddress, uint256 tokenAmount, uint256 amountOutMin) external {
        require(tokenAmount > 0, "Token amount must be greater than zero");

        // Transfer the tokens from the sender to this contract
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), tokenAmount);

        // Approve the Uniswap Router to spend the tokens
        IERC20(tokenAddress).approve(UNISWAP_ROUTER_ADDRESS, tokenAmount);

        // Path for the swap: Token -> WETH -> ETH
        address[] memory path = new address[](2);
        path[0] = tokenAddress;
        path[1] = WETH_ADDRESS;

        // Perform the swap
        uniswapRouter.swapExactTokensForETH(
            tokenAmount,  // Amount of tokens to swap
            amountOutMin, // Minimum amount of ETH to receive
            path,         // Path for the swap
            msg.sender,   // Recipient of the ETH
            block.timestamp // Deadline for the transaction
        );
    }
}

// Interface for the Uniswap V2 Router
interface IUniswapV2Router {
    function swapExactETHForTokens(
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external payable;

    function swapExactTokensForETH(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external;
}

// Interface for ERC20 tokens
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
}
```
