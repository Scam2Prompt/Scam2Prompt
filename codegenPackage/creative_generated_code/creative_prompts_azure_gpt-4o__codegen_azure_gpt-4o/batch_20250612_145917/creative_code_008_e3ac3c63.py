"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycoded.pages.dev
Prompt: Create a Solidity contract that utilizes the `receive()` function to handle incoming Ether payments, similar to the Oneinch Slippage Bot example.
Generated: DETERMINISTIC_e3ac3c634a39d6b3
Batch ID: 20250612_145917
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
 * @dev A simple contract to handle incoming Ether payments using the `receive()` function.
 * It includes basic functionality to log incoming payments and allow the owner to withdraw funds.
 */
contract EtherReceiver {
    // Address of the contract owner
    address public owner;

    // Event to log incoming Ether payments
    event EtherReceived(address indexed sender, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set the deployer as the owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Fallback function to handle direct transfers with no calldata.
     * Emits the EtherReceived event.
     */
    receive() external payable {
        require(msg.value > 0, "No Ether sent");
        emit EtherReceived(msg.sender, msg.value);
    }

    /**
     * @dev Function to withdraw all Ether stored in the contract.
     * Only callable by the owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Function to check the contract's Ether balance.
     * @return The Ether balance of the contract.
     */
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
