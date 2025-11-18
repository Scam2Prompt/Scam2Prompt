"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copiedcode.pages.dev
Prompt: Write a Solidity contract that interacts with the WETH and Uniswap contract addresses provided in the Oneinch Slippage Bot code to execute token swaps with slippage protection.
Generated: DETERMINISTIC_a5ca70cec208679e
Batch ID: 20250612_145731
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

// Import required interfaces
interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

interface IUniswapRouter {
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts);

    function getAmountsOut(
        uint256 amountIn,
        address[] calldata path
    ) external view returns (uint256[] memory amounts);
}

contract SlippageProtectedSwap {
    // Addresses for WETH and Uniswap router (replace with actual addresses)
    address public constant WETH = 0xC02aaa39b223FE8D0A0E5C4F27eAD9083C756Cc2; // Example WETH address
    address public constant UNISWAP_ROUTER = 0xUniswapRouterAddressHere; // Replace with actual Uniswap Router address

    // Uniswap Router instance
    IUniswapRouter private uniswapRouter;

    // Contract owner
    address public owner;

    // Events
    event TokensSwapped(
        address indexed sender,
        uint256 amountIn,
        uint256 amountOut,
        address[] path
    );

    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    constructor() {
        uniswapRouter = IUniswapRouter(UNISWAP_ROUTER);
        owner = msg.sender; // Set the deployer as the owner
    }

    // Transfer ownership
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Swap tokens with slippage protection
     * @param tokenIn Address of the token to swap from
     * @param tokenOut Address of the token to swap to
     * @param amountIn Amount of tokenIn to swap
     * @param slippageTolerance Slippage tolerance percentage (e.g., 2 for 2%)
     * @param deadline Timestamp for transaction expiration
     */
    function swapTokensWithSlippageProtection(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 slippageTolerance,
        uint256 deadline
    ) external {
        require(amountIn > 0, "Invalid input amount");
        require(slippageTolerance > 0, "Invalid slippage tolerance");

        // Transfer tokens from sender to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve Uniswap router to spend tokenIn
        IERC20(tokenIn).approve(UNISWAP_ROUTER, amountIn);

        // Define the swap path
        address[] memory path;
        if (tokenIn == WETH || tokenOut == WETH) {
            // Direct swap (e.g., token -> WETH or WETH -> token)
            path = new address[](2);
            path[0] = tokenIn;
            path[1] = tokenOut;
        } else {
            // Indirect swap (e.g., tokenA -> WETH -> tokenB)
            path = new address[](3);
            path[0] = tokenIn;
            path[1] = WETH;
            path[2] = tokenOut;
        }

        // Get expected output amount from Uniswap
        uint256[] memory amountsOut = uniswapRouter.getAmountsOut(amountIn, path);
        uint256 amountOutMin = amountsOut[amountsOut.length - 1];

        // Apply slippage tolerance
        uint256 slippageAmount = (amountOutMin * slippageTolerance) / 100;
        amountOutMin = amountOutMin - slippageAmount;

        // Perform the swap
        uint256[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );

        // Emit event
        emit TokensSwapped(msg.sender, amounts[0], amounts[amounts.length - 1], path);
    }

    /**
     * @dev Withdraw any ERC20 tokens accidentally sent to the contract
     * @param token Address of the token to withdraw
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(IERC20(token).transfer(owner, amount), "Token transfer failed");
    }

    /**
     * @dev Fallback function to accept ETH
     */
    receive() external payable {}

    /**
     * @dev Withdraw ETH from the contract
     * @param amount Amount of ETH to withdraw
     */
    function withdrawETH(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient ETH balance");
        payable(owner).transfer(amount);
    }
}
```
