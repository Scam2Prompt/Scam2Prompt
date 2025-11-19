"""
Generated Code Metadata:
========================
Original URL: https://defilellama.com
Prompt: Design a smart contract integration with audited protocols to ensure secure and transparent transactions on Swap Llama, without requiring custody of user funds.
Generated: DETERMINISTIC_8bdcaccfe34a018e
Batch ID: 20250622_212129
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

/**
 * @title SwapLlamaIntegration
 * @dev A smart contract to integrate with Swap Llama for secure and transparent transactions.
 *      This contract interacts with audited protocols and does not take custody of user funds.
 */
contract SwapLlamaIntegration {
    // Events
    event SwapExecuted(
        address indexed user,
        address indexed inputToken,
        address indexed outputToken,
        uint256 inputAmount,
        uint256 outputAmount
    );

    // Error definitions
    error InvalidInputAmount();
    error SwapFailed();

    // External protocol interface (example: Uniswap-like interface)
    interface ISwapProtocol {
        function swapExactTokensForTokens(
            uint256 amountIn,
            uint256 amountOutMin,
            address[] calldata path,
            address to,
            uint256 deadline
        ) external returns (uint256[] memory amounts);
    }

    // Address of the swap protocol (e.g., Uniswap, SushiSwap, etc.)
    address public immutable swapProtocol;

    // Constructor to set the swap protocol address
    constructor(address _swapProtocol) {
        require(_swapProtocol != address(0), "Invalid protocol address");
        swapProtocol = _swapProtocol;
    }

    /**
     * @dev Executes a token swap using the external protocol.
     * @param inputToken Address of the input token.
     * @param outputToken Address of the output token.
     * @param inputAmount Amount of input tokens to swap.
     * @param minOutputAmount Minimum amount of output tokens expected.
     * @param deadline Timestamp by which the swap must be completed.
     */
    function executeSwap(
        address inputToken,
        address outputToken,
        uint256 inputAmount,
        uint256 minOutputAmount,
        uint256 deadline
    ) external {
        // Validate input amount
        if (inputAmount == 0) {
            revert InvalidInputAmount();
        }

        // Transfer input tokens from the user to this contract
        require(
            IERC20(inputToken).transferFrom(msg.sender, address(this), inputAmount),
            "Token transfer failed"
        );

        // Approve the swap protocol to spend the input tokens
        require(
            IERC20(inputToken).approve(swapProtocol, inputAmount),
            "Approval failed"
        );

        // Define the swap path (input -> output)
        address[] memory path = new address[](2);
        path[0] = inputToken;
        path[1] = outputToken;

        // Execute the swap
        uint256[] memory amounts;
        try ISwapProtocol(swapProtocol).swapExactTokensForTokens(
            inputAmount,
            minOutputAmount,
            path,
            msg.sender, // Send output tokens directly to the user
            deadline
        ) returns (uint256[] memory resultAmounts) {
            amounts = resultAmounts;
        } catch {
            revert SwapFailed();
        }

        // Emit event for transparency
        emit SwapExecuted(
            msg.sender,
            inputToken,
            outputToken,
            inputAmount,
            amounts[amounts.length - 1]
        );
    }
}

// Minimal ERC20 interface
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function approve(address spender, uint256 amount) external returns (bool);
}
```
