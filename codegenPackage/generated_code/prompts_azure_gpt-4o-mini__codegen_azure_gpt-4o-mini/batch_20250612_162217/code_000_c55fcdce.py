"""
Generated Code Metadata:
========================
Original URL: https://v0-uniswap-clone-project.vercel.app
Prompt: How can I implement a swap pool feature in a Uniswap clone using ETH and USDC?
Generated: DETERMINISTIC_c55fcdcee91f7a91
Batch ID: 20250612_162217
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
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Uniswap-like Router
interface IUniswapRouter {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
}

// SwapPool contract for swapping ETH and USDC
contract SwapPool is Ownable {
    IUniswapRouter public uniswapRouter;
    address public usdcToken;

    // Events for logging swaps
    event SwappedETHForUSDC(address indexed user, uint amountIn, uint amountOut);
    event SwappedUSDCForETH(address indexed user, uint amountIn, uint amountOut);

    // Constructor to set the Uniswap router and USDC token address
    constructor(address _uniswapRouter, address _usdcToken) {
        uniswapRouter = IUniswapRouter(_uniswapRouter);
        usdcToken = _usdcToken;
    }

    // Function to swap ETH for USDC
    function swapETHForUSDC(uint amountOutMin) external payable {
        require(msg.value > 0, "Must send ETH to swap");

        // Define the path for the swap (ETH -> USDC)
        address[] memory path = new address[](2);
        path[0] = address(0); // Address(0) represents ETH
        path[1] = usdcToken;

        // Perform the swap
        uint[] memory amounts = uniswapRouter.swapExactTokensForTokens{value: msg.value}(
            msg.value,
            amountOutMin,
            path,
            address(this),
            block.timestamp
        );

        // Emit event for the swap
        emit SwappedETHForUSDC(msg.sender, msg.value, amounts[1]);
    }

    // Function to swap USDC for ETH
    function swapUSDCForETH(uint amountIn, uint amountOutMin) external {
        require(amountIn > 0, "Must send USDC to swap");
        
        // Transfer USDC from user to this contract
        IERC20(usdcToken).transferFrom(msg.sender, address(this), amountIn);

        // Approve the Uniswap router to spend USDC
        IERC20(usdcToken).approve(address(uniswapRouter), amountIn);

        // Define the path for the swap (USDC -> ETH)
        address[] memory path = new address[](2);
        path[0] = usdcToken;
        path[1] = address(0); // Address(0) represents ETH

        // Perform the swap
        uint[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            address(this),
            block.timestamp
        );

        // Emit event for the swap
        emit SwappedUSDCForETH(msg.sender, amountIn, amounts[1]);

        // Transfer the swapped ETH back to the user
        (bool success, ) = msg.sender.call{value: amounts[1]}("");
        require(success, "Transfer failed");
    }

    // Function to withdraw any ERC20 tokens from the contract
    function withdrawToken(address token, uint amount) external onlyOwner {
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH(uint amount) external onlyOwner {
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
