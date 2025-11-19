"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defilellama.com
Prompt: Explain how to integrate Swap Llama's smart contract features for secure token swaps in a decentralized application.
Generated: DETERMINISTIC_0a2e87f9f7123a8e
Batch ID: 20250612_160726
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

// Import required interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define a contract for the token swap integration
contract SwapLlamaIntegration is Ownable {
    // Event emitted when a token swap occurs
    event TokenSwapped(address indexed user, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Address of the Swap Llama contract
    address public swapLlamaAddress;

    // Modifier to ensure that the caller is the Swap Llama contract
    modifier onlySwapLlama() {
        require(msg.sender == swapLlamaAddress, "Caller is not Swap Llama");
        _;
    }

    // Constructor to set the Swap Llama address
    constructor(address _swapLlamaAddress) {
        require(_swapLlamaAddress != address(0), "Invalid Swap Llama address");
        swapLlamaAddress = _swapLlamaAddress;
    }

    // Function to swap tokens
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut
    ) external {
        // Validate input parameters
        require(tokenIn != address(0), "Invalid input token address");
        require(tokenOut != address(0), "Invalid output token address");
        require(amountIn > 0, "Amount in must be greater than zero");

        // Transfer tokens from the user to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        
        // Approve the Swap Llama contract to spend the tokens
        IERC20(tokenIn).approve(swapLlamaAddress, amountIn);

        // Call the Swap Llama contract to perform the swap
        uint256 amountOut = ISwapLlama(swapLlamaAddress).swap(tokenIn, tokenOut, amountIn);

        // Check that the amount out meets the minimum requirement
        require(amountOut >= minAmountOut, "Insufficient output amount");

        // Transfer the swapped tokens to the user
        IERC20(tokenOut).transfer(msg.sender, amountOut);

        // Emit the token swapped event
        emit TokenSwapped(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    // Function to update the Swap Llama contract address
    function updateSwapLlamaAddress(address newAddress) external onlyOwner {
        require(newAddress != address(0), "Invalid address");
        swapLlamaAddress = newAddress;
    }
}

// Interface for the Swap Llama contract
interface ISwapLlama {
    function swap(address tokenIn, address tokenOut, uint256 amountIn) external returns (uint256);
}
```
