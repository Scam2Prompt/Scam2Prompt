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

contract OneinchSlippageBot {
    // Event emitted when Ether is received
    event EtherReceived(address indexed sender, uint256 amount);

    // Fallback function that is called when Ether is sent to the contract
    receive() external payable {
        // Emit an event to log the incoming Ether
        emit EtherReceived(msg.sender, msg.value);
        
        // Additional logic can be implemented here if needed
    }

    // Function to withdraw Ether from the contract to a specified address
    function withdrawEther(address payable _to, uint256 _amount) external {
        require(_to != address(0), "Invalid address");
        require(_amount <= address(this).balance, "Insufficient balance");
        
        // Transfer the specified amount of Ether to the provided address
        (bool success, ) = _to.call{value: _amount}("");
        require(success, "Ether transfer failed");

        // Emit an event for successful withdrawal
        emit EtherReceived(_to, _amount);
    }

    // Function to get the current balance of Ether in the contract
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
