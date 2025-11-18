"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://para-swap.github.io
Prompt: Generate code for a fallback handler in Solidity that uses ParaSwap to prevent reentrancy attacks during unexpected external calls.
Generated: DETERMINISTIC_2256c41ee2fbce83
Batch ID: 20250612_142640
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

interface IParaSwap {
    function swap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        address recipient,
        bytes calldata data
    ) external returns (uint256 amountOut);
}

contract FallbackHandler {
    // Address of the ParaSwap contract
    IParaSwap public paraSwap;

    // Mapping to track the status of each address to prevent reentrancy
    mapping(address => bool) private _locked;

    // Event emitted after a successful swap
    event SwapExecuted(address indexed user, address tokenIn, address tokenOut, uint256 amountIn, uint256 amountOut);

    constructor(address _paraSwapAddress) {
        require(_paraSwapAddress != address(0), "Invalid ParaSwap address");
        paraSwap = IParaSwap(_paraSwapAddress);
    }

    // Modifier to prevent reentrancy
    modifier nonReentrant() {
        require(!_locked[msg.sender], "Reentrancy attack detected");
        _locked[msg.sender] = true;
        _;
        _locked[msg.sender] = false;
    }

    /**
     * @notice Execute a token swap using ParaSwap with reentrancy protection.
     * @param tokenIn The address of the token to swap from.
     * @param tokenOut The address of the token to swap to.
     * @param amountIn The amount of tokens to swap.
     * @param minAmountOut The minimum amount of tokens to receive.
     * @param recipient The address that will receive the output tokens.
     * @param data Additional data to pass to ParaSwap (if needed).
     */
    function executeSwap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        address recipient,
        bytes calldata data
    ) external nonReentrant {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(recipient != address(0), "Invalid recipient address");

        // Call the ParaSwap swap function
        uint256 amountOut = paraSwap.swap(tokenIn, tokenOut, amountIn, minAmountOut, recipient, data);

        // Emit event after successful swap
        emit SwapExecuted(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }
}
```
