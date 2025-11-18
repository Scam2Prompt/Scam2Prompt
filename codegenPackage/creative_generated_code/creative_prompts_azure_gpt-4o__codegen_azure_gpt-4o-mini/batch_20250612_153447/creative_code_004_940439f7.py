"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-site.pages.dev
Prompt: Write a tutorial for deploying a decentralized exchange (DEX) on the Pepe Unchained Layer 2 blockchain, including token swapping functionality.
Generated: DETERMINISTIC_940439f70a586f6b
Batch ID: 20250612_153447
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Defining the DEX contract
contract PepeUnchainedDEX is Ownable {
    // Event emitted when a swap occurs
    event TokenSwapped(address indexed swapper, address tokenIn, address tokenOut, uint256 amountIn, uint256 amountOut);

    // Function to swap tokens between two ERC20 tokens
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut
    ) external {
        // Ensure that the amount in is greater than zero
        require(amountIn > 0, "Amount in must be greater than zero");

        // Transfer tokens from the user to the contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Calculate the amount to send based on a simple price model
        uint256 amountOut = getAmountOut(amountIn, tokenIn, tokenOut);
        
        // Ensure the output amount meets the minimum amount specified
        require(amountOut >= minAmountOut, "Insufficient output amount");

        // Transfer output tokens to the user
        IERC20(tokenOut).transfer(msg.sender, amountOut);

        // Emit event for the swap
        emit TokenSwapped(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    // Mock function to determine amount out based on input amount
    function getAmountOut(uint256 amountIn, address tokenIn, address tokenOut) internal view returns (uint256) {
        // For simplicity, assume a 1:1 swap rate; replace with actual liquidity calculations
        return amountIn;
    }

    // Function to withdraw tokens from the contract (admin only)
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Function to withdraw Ether from the contract (admin only)
    function withdrawEther(uint256 amount) external onlyOwner {
        payable(msg.sender).transfer(amount);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```

**Note:** This code provides a basic structure for a decentralized exchange (DEX) with simple token swapping functionality and withdrawal capabilities. This is a simplified version and does not include advanced features such as price oracles, liquidity pools, or slippage handling, which are essential for a production-ready DEX. Further enhancements and security audits are recommended before deployment.
