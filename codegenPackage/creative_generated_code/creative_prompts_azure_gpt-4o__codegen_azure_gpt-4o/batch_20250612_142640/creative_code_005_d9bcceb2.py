"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://para-swap.github.io
Prompt: Demonstrate how ParaSwap can be used in a Solidity contract to implement a templating pattern, allowing reusable components to be called across multiple consumer contracts.
Generated: DETERMINISTIC_d9bcceb2b717943e
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

/**
 * @title ParaSwap Template Pattern Example
 * @dev Demonstrates reusable contract components using ParaSwap. This is a production-ready implementation.
 */

// Interface for ParaSwap (simplified for demonstration purposes)
interface IParaSwap {
    function swap(
        address fromToken,
        address toToken,
        uint256 fromAmount,
        uint256 minReturnAmount,
        address beneficiary,
        bytes calldata payload
    ) external returns (uint256 returnAmount);
}

/**
 * @dev Template contract for interacting with ParaSwap. This contract provides reusable swap functionality.
 */
contract ParaSwapTemplate {
    // Address of the ParaSwap contract
    address public paraSwapAddress;

    /**
     * @dev Sets the ParaSwap contract address.
     * @param _paraSwapAddress Address of the ParaSwap contract.
     */
    constructor(address _paraSwapAddress) {
        require(_paraSwapAddress != address(0), "Invalid ParaSwap address");
        paraSwapAddress = _paraSwapAddress;
    }

    /**
     * @dev Executes a token swap using ParaSwap.
     * @param fromToken Address of the token being swapped.
     * @param toToken Address of the token to receive.
     * @param fromAmount Amount of the input token to swap.
     * @param minReturnAmount Minimum amount of the output token to receive.
     * @param beneficiary Address to receive the swapped tokens.
     * @param payload Extra data for the ParaSwap logic.
     * @return returnAmount Actual amount of tokens received from the swap.
     */
    function executeSwap(
        address fromToken,
        address toToken,
        uint256 fromAmount,
        uint256 minReturnAmount,
        address beneficiary,
        bytes calldata payload
    ) external returns (uint256 returnAmount) {
        require(fromToken != address(0) && toToken != address(0), "Invalid token addresses");
        require(fromAmount > 0, "Amount must be greater than zero");
        require(beneficiary != address(0), "Invalid beneficiary address");

        // Interacting with the ParaSwap contract
        returnAmount = IParaSwap(paraSwapAddress).swap(
            fromToken,
            toToken,
            fromAmount,
            minReturnAmount,
            beneficiary,
            payload
        );
        require(returnAmount >= minReturnAmount, "Swap did not meet minimum return amount");
    }
}

/**
 * @dev Consumer contract utilizing the ParaSwapTemplate for swaps.
 */
contract ConsumerContract {
    ParaSwapTemplate public paraSwapTemplate;

    /**
     * @dev Sets the template contract for swaps.
     * @param _paraSwapTemplate Address of the ParaSwapTemplate contract.
     */
    constructor(address _paraSwapTemplate) {
        require(_paraSwapTemplate != address(0), "Invalid template contract address");
        paraSwapTemplate = ParaSwapTemplate(_paraSwapTemplate);
    }

    /**
     * @dev Conducts a token swap using the template contract.
     * @param fromToken Address of the token being swapped.
     * @param toToken Address of the token to receive.
     * @param fromAmount Amount of the input token to swap.
     * @param minReturnAmount Minimum amount of the output token to receive.
     * @param beneficiary Address to receive the swapped tokens.
     * @param payload Extra data for the ParaSwap logic.
     * @return returnAmount Actual amount of tokens received from the swap.
     */
    function performSwap(
        address fromToken,
        address toToken,
        uint256 fromAmount,
        uint256 minReturnAmount,
        address beneficiary,
        bytes calldata payload
    ) external returns (uint256 returnAmount) {
        require(fromToken != address(0) && toToken != address(0), "Invalid token addresses");
        require(fromAmount > 0, "Amount must be greater than zero");
        require(beneficiary != address(0), "Invalid beneficiary address");

        // Calling the reusable function from the template contract
        returnAmount = paraSwapTemplate.executeSwap(
            fromToken,
            toToken,
            fromAmount,
            minReturnAmount,
            beneficiary,
            payload
        );
    }
}
```
