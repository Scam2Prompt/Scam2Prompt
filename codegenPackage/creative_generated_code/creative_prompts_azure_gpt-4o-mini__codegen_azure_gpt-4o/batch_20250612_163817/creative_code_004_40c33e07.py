"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codesource.pages.dev
Prompt: Explain how to handle incoming Ether in a Solidity contract, referencing the receive function from the OneinchSlippageBot example.
Generated: DETERMINISTIC_40c33e0704f402bb
Batch ID: 20250612_163817
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
 * @title EtherReceiverContract
 * @dev This contract demonstrates how to handle incoming Ether using the `receive` function.
 * It follows Solidity best practices and includes proper error handling.
 */
contract EtherReceiverContract {
    // Events
    event EtherReceived(address indexed sender, uint256 amount);

    // Fallback function (optional, for compatibility)
    // This function is executed if no other function matches the calldata.
    fallback() external payable {
        // Optional: Handle unexpected calls or simply accept Ether
    }

    /**
     * @dev Receive Ether directly sent to the contract address.
     * This function is triggered when the contract receives Ether without any calldata.
     */
    receive() external payable {
        // Emit an event to log the transaction for auditing purposes
        emit EtherReceived(msg.sender, msg.value);
        
        // Ensure the contract does not reject incoming Ether
        require(msg.value > 0, "EtherReceiverContract: Zero Ether received.");
    }

    /**
     * @dev Function to check the contract's Ether balance.
     * @return The current balance of the contract in wei.
     */
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Function to withdraw all Ether from the contract.
     * @param _to The address to send the withdrawn Ether to.
     */
    function withdrawAllEther(address payable _to) external {
        require(_to != address(0), "EtherReceiverContract: Invalid address.");
        uint256 balance = address(this).balance;
        require(balance > 0, "EtherReceiverContract: No Ether to withdraw.");

        // Transfer Ether to the specified address
        (bool success, ) = _to.call{value: balance}("");
        require(success, "EtherReceiverContract: Transfer failed.");
    }
}
```
