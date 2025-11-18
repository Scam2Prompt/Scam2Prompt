"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupagdex.com
Prompt: Write a Solidity contract that interacts with Jupiter's API to execute swaps and ensure the best rates for Solana-based tokens.
Generated: DETERMINISTIC_9838f33ed8b91b48
Batch ID: 20250612_154731
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
import "@openzeppelin/contracts/utils/Address.sol";

// Interface for the Jupiter API interaction
interface IJupiter {
    function getBestRoute(
        address tokenIn,
        address tokenOut,
        uint256 amountIn
    ) external view returns (address[] memory, uint256[] memory);

    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        address recipient,
        uint256 deadline
    ) external returns (uint256 amountOut);
}

// Main contract for executing swaps
contract TokenSwap is Ownable {
    using Address for address;

    IJupiter public jupiter;

    // Event emitted after a successful swap
    event SwapExecuted(address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Constructor to set the Jupiter API address
    constructor(address _jupiter) {
        require(_jupiter != address(0), "Invalid Jupiter address");
        jupiter = IJupiter(_jupiter);
    }

    // Function to execute a token swap
    function executeSwap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        uint256 deadline
    ) external {
        require(amountIn > 0, "Invalid input amount");
        require(deadline > block.timestamp, "Deadline must be in the future");
        
        // Transfer tokens from the sender to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the Jupiter contract to spend the tokens
        IERC20(tokenIn).approve(address(jupiter), amountIn);

        // Get the best route for the swap
        (address[] memory routes, uint256[] memory amounts) = jupiter.getBestRoute(tokenIn, tokenOut, amountIn);
        
        // Ensure that a valid route exists
        require(routes.length > 0, "No valid route found");

        // Execute the swap
        uint256 amountOut = jupiter.swapTokens(tokenIn, tokenOut, amountIn, minAmountOut, msg.sender, deadline);

        // Emit the swap event
        emit SwapExecuted(tokenIn, tokenOut, amountIn, amountOut);
    }

    // Allow the owner to update the Jupiter API address if necessary
    function updateJupiterAddress(address _jupiter) external onlyOwner {
        require(_jupiter != address(0), "Invalid Jupiter address");
        jupiter = IJupiter(_jupiter);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```
