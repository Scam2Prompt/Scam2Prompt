"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copiedcode.pages.dev
Prompt: Implement a Solidity contract that uses the Uniswap V2 ERC20 interface to interact with liquidity pools, referencing the imports and structure of the Oneinch Slippage Bot code.
Generated: DETERMINISTIC_b302f4a9c6a1d7c8
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

// Import the IERC20 interface for interacting with ERC20 tokens.
import "@uniswap/v2-periphery/contracts/interfaces/IERC20.sol";
// Import the Uniswap V2 Router interface for interacting with liquidity pools.
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract UniswapLiquidityManager {
    // State variables to store addresses for the Uniswap V2 Router and the owner of the contract.
    address public owner;
    IUniswapV2Router02 public uniswapRouter;

    // Modifier to restrict certain functions to only the owner of the contract.
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Event emitted whenever liquidity is added or removed.
    event LiquidityAdded(address tokenA, address tokenB, uint amountA, uint amountB, uint liquidity);
    event LiquidityRemoved(address tokenA, address tokenB, uint amountA, uint amountB);

    // Constructor to initialize the contract with the Uniswap V2 Router address.
    constructor(address _uniswapRouter) {
        require(_uniswapRouter != address(0), "Invalid router address");
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
        owner = msg.sender;
    }

    // Function to add liquidity to a Uniswap V2 liquidity pool.
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        uint deadline
    ) external onlyOwner {
        // Transfer tokens from the owner to this contract.
        IERC20(tokenA).transferFrom(msg.sender, address(this), amountADesired);
        IERC20(tokenB).transferFrom(msg.sender, address(this), amountBDesired);

        // Approve the Uniswap Router contract to spend the tokens.
        IERC20(tokenA).approve(address(uniswapRouter), amountADesired);
        IERC20(tokenB).approve(address(uniswapRouter), amountBDesired);

        // Add liquidity and capture returned values.
        (uint amountA, uint amountB, uint liquidity) = uniswapRouter.addLiquidity(
            tokenA,
            tokenB,
            amountADesired,
            amountBDesired,
            amountAMin,
            amountBMin,
            address(this),
            deadline
        );

        emit LiquidityAdded(tokenA, tokenB, amountA, amountB, liquidity);
    }

    // Function to remove liquidity from a Uniswap V2 liquidity pool.
    function removeLiquidity(
        address tokenA,
        address tokenB,
        uint liquidity,
        uint amountAMin,
        uint amountBMin,
        uint deadline
    ) external onlyOwner {
        // Get the pair's liquidity token address from the Uniswap factory.
        address pair = IUniswapV2Router02(uniswapRouter).factory().getPair(tokenA, tokenB);
        require(pair != address(0), "Invalid pair address");

        // Approve the Uniswap Router contract to spend the liquidity tokens.
        IERC20(pair).approve(address(uniswapRouter), liquidity);

        // Remove liquidity and capture returned values.
        (uint amountA, uint amountB) = uniswapRouter.removeLiquidity(
            tokenA,
            tokenB,
            liquidity,
            amountAMin,
            amountBMin,
            address(this),
            deadline
        );

        // Transfer the tokens back to the contract owner.
        IERC20(tokenA).transfer(msg.sender, amountA);
        IERC20(tokenB).transfer(msg.sender, amountB);

        emit LiquidityRemoved(tokenA, tokenB, amountA, amountB);
    }

    // Function to withdraw tokens from the contract (emergency use).
    function emergencyWithdraw(address token, uint amount) external onlyOwner {
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
