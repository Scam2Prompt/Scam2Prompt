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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the ParaSwap liquidity aggregator
interface IParaSwap {
    function swap(
        address srcToken,
        address destToken,
        uint256 amount,
        uint256 minReturn,
        address payable destAddress,
        bytes calldata swapData
    ) external returns (uint256);
}

// Abstract contract to define the templated pattern for ParaSwap usage
abstract contract ParaSwapTemplate is Ownable {
    IParaSwap public paraSwap;

    // Event to emit swap details for tracking
    event SwapExecuted(address indexed srcToken, address indexed destToken, uint256 amount, uint256 received);

    constructor(IParaSwap _paraSwap) {
        require(address(_paraSwap) != address(0), "Invalid ParaSwap address");
        paraSwap = _paraSwap;
    }

    // Function to execute token swap on ParaSwap
    function executeSwap(
        address srcToken,
        address destToken,
        uint256 amount,
        uint256 minReturn,
        address payable destAddress,
        bytes calldata swapData
    ) internal returns (uint256) {
        require(amount > 0, "Amount must be greater than 0");
        require(IERC20(srcToken).balanceOf(address(this)) >= amount, "Insufficient balance");

        // Approve the ParaSwap contract to spend the source token
        IERC20(srcToken).approve(address(paraSwap), amount);

        // Perform the swap
        uint256 receivedAmount = paraSwap.swap(srcToken, destToken, amount, minReturn, destAddress, swapData);

        // Emit event for tracking
        emit SwapExecuted(srcToken, destToken, amount, receivedAmount);

        return receivedAmount;
    }
}

// Consumer contract that uses the ParaSwap template
contract ParaSwapConsumer is ParaSwapTemplate {
    constructor(IParaSwap _paraSwap) ParaSwapTemplate(_paraSwap) {}

    // Public function to allow users to swap tokens
    function swapTokens(
        address srcToken,
        address destToken,
        uint256 amount,
        uint256 minReturn,
        address payable destAddress,
        bytes calldata swapData
    ) external {
        // Transfer tokens from user to this contract
        IERC20(srcToken).transferFrom(msg.sender, address(this), amount);

        // Execute the swap using the templated function
        uint256 receivedAmount = executeSwap(srcToken, destToken, amount, minReturn, destAddress, swapData);

        // Transfer received tokens to the user
        IERC20(destToken).transfer(destAddress, receivedAmount);
    }
}
```
