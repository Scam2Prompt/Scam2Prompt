"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantle-xyz.pages.dev
Prompt: Develop a dApp using Mantle Network's Ethereum layer-2 rollup to enable low-fee and fast-finality token swaps, leveraging Mantle's hyperscale performance features.
Generated: DETERMINISTIC_b7626249a8842b21
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the ERC20 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Creating a contract for the token swap dApp
contract TokenSwap {
    // Event to log successful swaps
    event TokensSwapped(address indexed sender, address tokenIn, address tokenOut, uint256 amountIn, uint256 amountOut);

    // Function to swap tokens between two ERC20 tokens
    // Requires approval for the tokenIn before calling this function
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address to
    ) external {
        // Validating the input parameters
        require(tokenIn != address(0), "Invalid input token address");
        require(tokenOut != address(0), "Invalid output token address");
        require(amountIn > 0, "AmountIn must be greater than zero");
        
        // Transfer the input tokens from the sender to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Placeholder for swap logic (to be implemented)
        // Here, you would normally call a DEX or other on-chain protocol to perform the swap
        uint256 amountOut = _performSwap(tokenIn, tokenOut, amountIn);

        // Checking if the output amount is sufficient
        require(amountOut >= amountOutMin, "Insufficient output amount");

        // Transfer the swapped tokens to the specified recipient
        IERC20(tokenOut).transfer(to, amountOut);

        // Emitting an event for the swap
        emit TokensSwapped(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    // Mock function to represent the swap logic
    // This should be replaced with actual swap logic in production
    function _performSwap(address tokenIn, address tokenOut, uint256 amountIn) internal returns (uint256) {
        // Simulated swap logic (replace with actual implementation)
        // For example, you could integrate with Uniswap, Sushiswap, or other DEX
        return amountIn; // Mock return value, should be replaced with real amountOut
    }
}
```

### Important Notes:
- Make sure to implement the actual swap logic in `_performSwap`, which can interface with DEX protocols like Uniswap or Sushiswap.
- Ensure that the contract is deployed on the Mantle Network and has been audited for security best practices.
- Include tests to validate all functionalities.
