"""
Generated Code Metadata:
========================
Original URL: https://para-swap.github.io
Prompt: What are the best practices for using ParaSwaps in Solidity to avoid reentrancy attacks and ensure safe execution of external functions?
Generated: DETERMINISTIC_8c17330a08c737eb
Batch ID: 20250612_155712
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title ParaSwap Executor
 * @author [Your Name]
 * @notice This contract provides a safe way to interact with ParaSwap's AugustusSwapper contract.
 */
contract ParaSwapExecutor {
    using SafeMath for uint256;

    // Address of the ParaSwap AugustusSwapper contract
    address public constant AUGUSTUS_SWAPPER = 0x0bC9e67cA0b9B3A08bE5C841F2cA9A609a6f9A8f;

    /**
     * @dev Swaps tokens using ParaSwap's AugustusSwapper contract.
     * @param fromToken Token to swap from (address)
     * @param toToken Token to swap to (address)
     * @param fromAmount Amount of tokens to swap (uint256)
     * @param toAmountMin Minimum amount of tokens to receive (uint256)
     * @param swapCalldata Calldata for the swap (bytes)
     * @param affiliate Affiliate address (address)
     * @return uint256 The amount of tokens received
     */
    function swap(
        address fromToken,
        address toToken,
        uint256 fromAmount,
        uint256 toAmountMin,
        bytes calldata swapCalldata,
        address affiliate
    ) external payable returns (uint256) {
        // Check if the fromToken is not the zero address
        require(fromToken != address(0), "Invalid from token address");

        // Check if the toToken is not the zero address
        require(toToken != address(0), "Invalid to token address");

        // Check if the fromAmount is greater than zero
        require(fromAmount > 0, "Invalid from amount");

        // Check if the toAmountMin is greater than zero
        require(toAmountMin > 0, "Invalid to amount min");

        // Approve the AugustusSwapper contract to spend the fromToken
        IERC20(fromToken).approve(AUGUSTUS_SWAPPER, fromAmount);

        // Execute the swap using the provided calldata
        (bool success, bytes memory returnData) = AUGUSTUS_SWAPPER.call{value: msg.value}(swapCalldata);
        require(success, "Swap failed");

        // Get the amount of tokens received
        uint256 receivedAmount = abi.decode(returnData, (uint256));

        // Check if the received amount is greater than or equal to the minimum amount
        require(receivedAmount >= toAmountMin, "Received amount is less than the minimum");

        // Transfer the received tokens to the msg.sender
        IERC20(toToken).transfer(msg.sender, receivedAmount);

        // If affiliate is provided, transfer a percentage of the received tokens
        if (affiliate != address(0)) {
            uint256 affiliateFee = receivedAmount.mul(10).div(100); // 10% fee
            IERC20(toToken).transfer(affiliate, affiliateFee);
        }

        return receivedAmount;
    }

    /**
     * @dev Swaps tokens using ParaSwap's AugustusSwapper contract with reentrancy protection.
     * @param fromToken Token to swap from (address)
     * @param toToken Token to swap to (address)
     * @param fromAmount Amount of tokens to swap (uint256)
     * @param toAmountMin Minimum amount of tokens to receive (uint256)
     * @param swapCalldata Calldata for the swap (bytes)
     * @param affiliate Affiliate address (address)
     * @return uint256 The amount of tokens received
     */
    function swapSafe(
        address fromToken,
        address toToken,
        uint256 fromAmount,
        uint256 toAmountMin,
        bytes calldata swapCalldata,
        address affiliate
    ) external payable returns (uint256) {
        // Use a reentrancy guard to prevent reentrancy attacks
        _lock();

        try {
            uint256 receivedAmount = swap(
                fromToken,
                toToken,
                fromAmount,
                toAmountMin,
                swapCalldata,
                affiliate
            );

            _unlock();
            return receivedAmount;
        } catch Error(string memory error) {
            _unlock();
            revert(error);
        } catch Panic(uint256) {
            _unlock();
            revert("Swap panic");
        } catch (bytes memory lowLevelData) {
            _unlock();
            revert(string(lowLevelData));
        }
    }

    // Reentrancy guard
    bool private locked;

    function _lock() internal {
        require(!locked, "Reentrancy guard: already locked");
        locked = true;
    }

    function _unlock() internal {
        locked = false;
    }

    modifier noReentrancy() {
        _lock();
        _;
        _unlock();
    }
}
```
