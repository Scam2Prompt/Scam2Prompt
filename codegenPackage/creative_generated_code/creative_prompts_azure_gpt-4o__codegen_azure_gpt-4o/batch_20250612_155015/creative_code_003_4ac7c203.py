"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-uni-infos.com
Prompt: Write a Solidity smart contract that interacts with Uniswap V2 to execute token swaps directly from the contract.
Generated: DETERMINISTIC_4ac7c203445b9f82
Batch ID: 20250612_155015
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

// Interface for Uniswap V2 Router
interface IUniswapV2Router {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);

    function getAmountsOut(
        uint amountIn,
        address[] calldata path
    ) external view returns (uint[] memory amounts);
}

// Interface for ERC20 token standard
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract UniswapInteraction {
    address public owner; // Owner of the contract
    IUniswapV2Router public uniswapRouter; // Uniswap V2 Router address

    // Constructor to initialize the contract
    constructor(address _uniswapRouter) {
        owner = msg.sender;
        uniswapRouter = IUniswapV2Router(_uniswapRouter);
    }

    // Modifier to restrict access to owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /**
     * @notice Executes a token swap on Uniswap V2
     * @param tokenIn Address of the input token
     * @param tokenOut Address of the output token
     * @param amountIn Amount of tokens to swap
     * @param amountOutMin Minimum amount of output tokens expected
     * @param to Address to receive the output tokens
     * @param deadline Unix timestamp by which the transaction must be completed
     */
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint amountIn,
        uint amountOutMin,
        address to,
        uint deadline
    ) external onlyOwner {
        // Ensure the contract has sufficient allowance to spend the input tokens
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        IERC20(tokenIn).approve(address(uniswapRouter), amountIn);

        // Define the token swap path (from tokenIn to tokenOut)
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        // Execute the swap
        uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            to,
            deadline
        );
    }

    /**
     * @notice Fetches the estimated output amount for a token swap
     * @param tokenIn Address of the input token
     * @param tokenOut Address of the output token
     * @param amountIn Amount of tokens to swap
     * @return amounts Array containing the output token amount
     */
    function getEstimatedOutput(
        address tokenIn,
        address tokenOut,
        uint amountIn
    ) external view returns (uint[] memory amounts) {
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        return uniswapRouter.getAmountsOut(amountIn, path);
    }

    /**
     * @notice Allows the owner to withdraw tokens accidentally sent to the contract
     * @param token Address of the token to withdraw
     * @param to Address to receive the withdrawn tokens
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(address token, address to, uint amount) external onlyOwner {
        IERC20(token).transferFrom(address(this), to, amount);
    }
}
```
