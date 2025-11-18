"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycodegpt.pages.dev
Prompt: Develop a Solidity contract that listens for incoming Ether payments using the `receive()` function and logs a custom event, inspired by the Oneinch Slippage Bot implementation.
Generated: DETERMINISTIC_acb8dd54f5cba529
Batch ID: 20250612_150902
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
 * @title EtherReceiver
 * @dev A contract that listens for incoming Ether payments using the `receive()` function
 *      and logs a custom event.
 */
contract EtherReceiver {
    // Event to log the details of received Ether
    event EtherReceived(address indexed sender, uint256 value, uint256 timestamp);

    /**
     * @dev Function to receive Ether. msg.data must be empty.
     * Emits an `EtherReceived` event.
     */
    receive() external payable {
        // Emit an event with the sender address, value sent, and current timestamp
        emit EtherReceived(msg.sender, msg.value, block.timestamp);
    }

    /**
     * @dev Fallback function to prevent accidental calls to undefined functions.
     * If msg.data is not empty, this fallback function will handle it.
     */
    fallback() external payable {
        revert("Fallback function triggered: invalid call or transaction.");
    }

    /**
     * @dev Function to retrieve the contract's Ether balance.
     * @return uint256 Current balance of the contract.
     */
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Owner-only function to withdraw all Ether from the contract.
     * @param _to Address to which the Ether will be sent.
     */
    function withdraw(address payable _to) external {
        require(_to != address(0), "Invalid address");
        require(address(this).balance > 0, "Insufficient balance");

        // Transfer the entire contract balance to the specified address
        uint256 amount = address(this).balance;
        (bool success, ) = _to.call{value: amount}("");
        require(success, "Transfer failed");
    }
}
```
