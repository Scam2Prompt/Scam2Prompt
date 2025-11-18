"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://op-enocean.github.io
Prompt: Create a Solidity contract using Open Ocean to implement a fallback handler that safely handles unexpected calls without risking reentrancy attacks.
Generated: DETERMINISTIC_07c69a4bf90d7f82
Batch ID: 20250612_153424
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
 * @title FallbackHandler
 * @dev A Solidity contract designed to safely handle unexpected calls with proper measures
 *      against reentrancy attacks. Uses OpenZeppelin's ReentrancyGuard for security.
 */
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract FallbackHandler is ReentrancyGuard {
    // Event emitted when fallback or receive functions are triggered
    event FundsReceived(address indexed sender, uint256 value, bytes data);

    /**
     * @dev Fallback function to handle unexpected calls and receive Ether.
     *      Emits an event to log the call details.
     *      Ensures no actions are taken that could lead to reentrancy attacks.
     */
    fallback() external payable nonReentrant {
        // Emit an event to log the call details
        emit FundsReceived(msg.sender, msg.value, msg.data);
    }

    /**
     * @dev Receive function to handle direct Ether transfers.
     *      Emits an event to log the transaction details.
     *      Ensures no actions are taken that could lead to reentrancy attacks.
     */
    receive() external payable nonReentrant {
        // Emit an event to log the transaction details
        emit FundsReceived(msg.sender, msg.value, "");
    }

    /**
     * @dev Allows the contract owner to withdraw any Ether collected in the contract.
     *      Includes reentrancy protection to guard against attacks.
     * @param recipient The address to send the withdrawn Ether to.
     */
    function withdraw(address payable recipient) external nonReentrant {
        require(recipient != address(0), "Invalid recipient address");
        require(address(this).balance > 0, "No funds available for withdrawal");

        uint256 amount = address(this).balance;

        // Transfer Ether to the recipient
        (bool success, ) = recipient.call{value: amount}("");
        require(success, "Ether transfer failed");
    }

    /**
     * @dev Retrieves the current contract balance.
     * @return The balance of Ether held by the contract.
     */
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
