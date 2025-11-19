"""
Generated Code Metadata:
========================
Original URL: https://copiedcode.pages.dev
Prompt: Write a Solidity contract that interacts with the WETH and Uniswap contract addresses provided in the Oneinch Slippage Bot code to execute token swaps with slippage protection.
Generated: DETERMINISTIC_a5ca70cec208679e
Batch ID: 20250612_145731
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

// Importing necessary interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract SlippageProtectedSwap {
    // State variables
    address private owner;
    IUniswapV2Router02 public uniswapRouter;
    IERC20 public weth;

    // Events
    event SwapExecuted(address indexed user, uint256 amountIn, uint256 amountOutMin, address[] path);

    // Constructor to initialize the contract with Uniswap router and WETH address
    constructor(address _uniswapRouter, address _weth) {
        require(_uniswapRouter != address(0), "Invalid Uniswap router address");
        require(_weth != address(0), "Invalid WETH address");
        
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
        weth = IERC20(_weth);
        owner = msg.sender;
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Function to execute a token swap with slippage protection
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        uint256 deadline
    ) external {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(amountOutMin > 0, "Amount out minimum must be greater than zero");
        require(deadline > block.timestamp, "Deadline has passed");

        // Transfer the input tokens from the user to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the Uniswap router to spend the tokens
        IERC20(tokenIn).approve(address(uniswapRouter), amountIn);

        // Define the path for the swap
        address[] memory path;
        if (tokenIn == address(weth) || tokenOut == address(weth)) {
            path = new address[](2);
            path[0] = tokenIn;
            path[1] = tokenOut;
        } else {
            revert("Token swap must involve WETH");
        }

        // Execute the swap
        uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );

        // Emit an event for the swap execution
        emit SwapExecuted(msg.sender, amountIn, amountOutMin, path);
    }

    // Function to withdraw tokens from the contract (for emergency purposes)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(owner, amount);
    }

    // Function to withdraw ETH from the contract (if any)
    function withdrawETH(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        payable(owner).transfer(amount);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
