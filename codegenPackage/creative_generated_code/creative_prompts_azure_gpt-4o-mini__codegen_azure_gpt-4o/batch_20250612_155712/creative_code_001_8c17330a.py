"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://para-swap.github.io
Prompt: What are the best practices for using ParaSwaps in Solidity to avoid reentrancy attacks and ensure safe execution of external functions?
Generated: DETERMINISTIC_8c17330a08c737eb
Batch ID: 20250612_155712
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

/**
 * @title ParaSwapIntegration
 * @dev Example contract demonstrating best practices for using ParaSwap in Solidity,
 * including safe execution of external functions and mitigation of reentrancy attacks.
 */

contract ParaSwapIntegration {
    address public paraSwapAddress;

    // Event to log swaps
    event SwapExecuted(address indexed user, uint256 inputAmount, uint256 outputAmount);

    /**
     * @dev Sets the ParaSwap contract address.
     * @param _paraSwapAddress The address of the ParaSwap contract.
     */
    constructor(address _paraSwapAddress) {
        require(_paraSwapAddress != address(0), "Invalid ParaSwap address");
        paraSwapAddress = _paraSwapAddress;
    }

    /**
     * @dev Executes a token swap using ParaSwap.
     * ReentrancyGuard is used to prevent reentrancy attacks.
     * @param inputToken Address of the input token.
     * @param outputToken Address of the output token.
     * @param inputAmount Amount of input tokens to swap.
     * @param minOutputAmount Minimum acceptable amount of output tokens.
     * @param swapData Encoded swap data required by ParaSwap.
     */
    function executeSwap(
        address inputToken,
        address outputToken,
        uint256 inputAmount,
        uint256 minOutputAmount,
        bytes calldata swapData
    ) external nonReentrant {
        require(inputToken != address(0) && outputToken != address(0), "Invalid token address");
        require(inputAmount > 0, "Input amount must be greater than 0");
        require(minOutputAmount > 0, "Minimum output amount must be greater than 0");

        // Transfer input tokens from the user to this contract
        IERC20(inputToken).transferFrom(msg.sender, address(this), inputAmount);

        // Approve ParaSwap to spend the input tokens
        IERC20(inputToken).approve(paraSwapAddress, inputAmount);

        // External call to ParaSwap contract
        // ParaSwap's swap function is executed with the provided data
        (bool success, bytes memory result) = paraSwapAddress.call(swapData);
        require(success, "ParaSwap swap failed");

        // Decode the result to check the output amount
        uint256 outputAmount = abi.decode(result, (uint256));
        require(outputAmount >= minOutputAmount, "Insufficient output amount");

        // Transfer output tokens to the user
        IERC20(outputToken).transfer(msg.sender, outputAmount);

        // Emit event for the executed swap
        emit SwapExecuted(msg.sender, inputAmount, outputAmount);
    }

    /**
     * @dev Modifier to prevent reentrancy attacks.
     */
    modifier nonReentrant() {
        require(!_locked, "ReentrancyGuard: reentrant call");
        _locked = true;
        _;
        _locked = false;
    }

    // Private variable to track reentrancy state
    bool private _locked = false;
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
}
```

This code demonstrates best practices for interacting with external contracts like ParaSwap in Solidity, including using reentrancy guards, input validation, and safe handling of external function calls.
