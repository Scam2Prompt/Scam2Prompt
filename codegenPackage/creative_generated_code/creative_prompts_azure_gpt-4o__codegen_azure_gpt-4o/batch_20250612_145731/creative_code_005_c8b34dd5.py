"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copiedcode.pages.dev
Prompt: Create a Solidity contract that includes an event logging mechanism for debugging purposes, similar to the `Log` event in the Oneinch Slippage Bot.
Generated: DETERMINISTIC_c8b34dd521149948
Batch ID: 20250612_145731
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

/// @title DebuggableContract
/// @dev A Solidity contract with an event logging mechanism for debugging purposes.
contract DebuggableContract {
    /// @notice Event for logging debugging information
    /// @param message A string message containing debugging information
    /// @param sender The address of the sender triggering the log
    /// @param value An optional uint256 value for additional context
    event DebugLog(string message, address indexed sender, uint256 value);

    /// @notice Example function that triggers a debug event
    /// @dev This is a sample function to demonstrate the use of DebugLog
    /// @param input A uint256 input used for the demonstration
    function exampleDebugFunction(uint256 input) external {
        // Emit a debug log with relevant context
        emit DebugLog("exampleDebugFunction called", msg.sender, input);

        // Example logic: Ensure input is greater than zero
        require(input > 0, "Input must be greater than zero");

        // Emit another log after successful validation
        emit DebugLog("Input validated successfully", msg.sender, input);
    }

    /// @notice Fallback function to demonstrate event logging on fallback calls
    /// @dev Emits a DebugLog whenever the fallback function is triggered
    fallback() external payable {
        emit DebugLog("Fallback called", msg.sender, msg.value);
    }

    /// @notice Receive function to handle incoming ETH
    /// @dev Emits a DebugLog whenever ETH is received
    receive() external payable {
        emit DebugLog("ETH received", msg.sender, msg.value);
    }

    /// @notice Withdraws all contract balance to the owner's address
    /// @dev Example function to showcase logging and error handling
    function withdraw() external {
        // Emit a debug log prior to withdrawal
        emit DebugLog("Withdrawal initiated", msg.sender, address(this).balance);

        // Ensure the contract has ETH to withdraw
        require(address(this).balance > 0, "Contract balance is zero");

        // Transfer the entire balance to the caller
        (bool success, ) = msg.sender.call{value: address(this).balance}("");
        require(success, "Transfer failed");

        // Emit a debug log after successful withdrawal
        emit DebugLog("Withdrawal successful", msg.sender, 0);
    }
}
```
