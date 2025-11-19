"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeia5w6ij6k5e2i3vwagaacosirdjz6kce4q3y2thlqdaqcfnictzmu.ipfs.dweb.link
Prompt: Write a code snippet to interact with the Berachain's Polaris VM for swapping tokens and providing liquidity.
Generated: DETERMINISTIC_51004f7edb3eae92
Batch ID: 20250612_160853
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

// Interface for Berachain's Polaris VM
interface IPolarisVM {
    function swapTokens(address tokenIn, address tokenOut, uint256 amountIn, uint256 minAmountOut) external returns (uint256);
    function addLiquidity(address tokenA, address tokenB, uint256 amountA, uint256 amountB) external returns (uint256 liquidity);
    function removeLiquidity(address tokenA, address tokenB, uint256 liquidity) external returns (uint256 amountA, uint256 amountB);
}

contract TokenSwapAndLiquidity {
    // Address of Polaris VM contract
    address public polarisVMAddress;

    // Event logging swap details
    event Swap(address indexed user, address tokenIn, address tokenOut, uint256 amountIn, uint256 amountOut);

    // Event logging liquidity addition details
    event LiquidityAdded(address indexed user, address tokenA, address tokenB, uint256 amountA, uint256 amountB, uint256 liquidity);

    // Constructor to initialize Polaris VM address
    constructor(address _polarisVMAddress) {
        require(_polarisVMAddress != address(0), "Invalid Polaris VM address");
        polarisVMAddress = _polarisVMAddress;
    }

    /** 
     * @dev Swap tokens using Polaris VM
     * @param tokenIn Address of the input token
     * @param tokenOut Address of the output token
     * @param amountIn Amount of input tokens
     * @param minAmountOut Minimum acceptable output tokens
     */
    function swapTokens(address tokenIn, address tokenOut, uint256 amountIn, uint256 minAmountOut) external {
        require(tokenIn != address(0) && tokenOut != address(0), "Invalid token addresses");
        require(amountIn > 0, "Amount must be greater than zero");

        // Transfer tokens to the Polaris VM contract
        IERC20(tokenIn).transferFrom(msg.sender, polarisVMAddress, amountIn);

        // Interact with the Polaris VM to swap tokens
        uint256 amountOut = IPolarisVM(polarisVMAddress).swapTokens(tokenIn, tokenOut, amountIn, minAmountOut);

        // Emit swap event
        emit Swap(msg.sender, tokenIn, tokenOut, amountIn, amountOut);

        // Return swapped tokens to user
        require(IERC20(tokenOut).transfer(msg.sender, amountOut), "Token transfer failed");
    }

    /**
     * @dev Add liquidity to the Polaris VM
     * @param tokenA Address of token A
     * @param tokenB Address of token B
     * @param amountA Amount of token A
     * @param amountB Amount of token B
     */
    function addLiquidity(address tokenA, address tokenB, uint256 amountA, uint256 amountB) external {
        require(tokenA != address(0) && tokenB != address(0), "Invalid token addresses");
        require(amountA > 0 && amountB > 0, "Amounts must be greater than zero");

        // Transfer tokens to the Polaris VM contract
        IERC20(tokenA).transferFrom(msg.sender, polarisVMAddress, amountA);
        IERC20(tokenB).transferFrom(msg.sender, polarisVMAddress, amountB);

        // Interact with Polaris VM to add liquidity
        uint256 liquidity = IPolarisVM(polarisVMAddress).addLiquidity(tokenA, tokenB, amountA, amountB);

        // Emit liquidity added event
        emit LiquidityAdded(msg.sender, tokenA, tokenB, amountA, amountB, liquidity);
    }
}

// Minimal ERC20 interface for token transfers
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
