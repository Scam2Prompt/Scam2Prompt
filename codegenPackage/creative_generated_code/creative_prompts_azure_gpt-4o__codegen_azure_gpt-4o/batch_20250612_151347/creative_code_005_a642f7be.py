"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sourcecopy.pages.dev
Prompt: Create a Solidity contract that emits a log event (`Log(string _msg)`) and uses the `receive()` function to handle incoming Ether, as demonstrated in the Oneinch Slippage Bot.
Generated: DETERMINISTIC_a642f7beee50dc21
Batch ID: 20250612_151347
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
 * @dev A simple contract to handle incoming Ether and emit log events
 */
contract EtherReceiverContract {
    
    // Event to log messages
    event Log(string _msg);

    /**
     * @dev Fallback function to handle direct transfers of Ether without data
     * Emits a log event with a predefined message
     */
    receive() external payable {
        // Emit log event when Ether is received
        emit Log("Ether received successfully");
    }

    /**
     * @dev Function to withdraw the Ether stored in the contract
     * @param _to Address to send the Ether to
     * @param _amount Amount of Ether to send in wei
     */
    function withdraw(address payable _to, uint256 _amount) external {
        require(_amount <= address(this).balance, "Insufficient funds in contract");
        require(_to != address(0), "Invalid recipient address");

        // Transfer Ether to the specified address
        (bool success, ) = _to.call{value: _amount}("");
        require(success, "Transfer failed");

        // Emit log event for successful withdrawal
        emit Log("Ether withdrawn successfully");
    }

    /**
     * @dev Function to check the balance of the contract
     * @return uint256 Balance of the contract in wei
     */
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
