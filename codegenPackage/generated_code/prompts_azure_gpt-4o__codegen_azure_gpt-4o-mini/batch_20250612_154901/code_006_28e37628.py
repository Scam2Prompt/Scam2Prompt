"""
Generated Code Metadata:
========================
Original URL: https://msk-rk.ru
Prompt: Write a Solidity function that integrates with Hop Protocol to verify the successful completion of a token transfer between blockchains.
Generated: DETERMINISTIC_28e37628b2c61d14
Batch ID: 20250612_154901
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

// Importing the interface for the Hop Protocol
import "@hop-protocol/core/contracts/interfaces/IHop.sol";

contract TokenTransferVerifier {
    // Address of the Hop Protocol contract
    IHop public hopProtocol;

    // Event to emit when a transfer is verified
    event TransferVerified(address indexed sender, uint256 amount, uint256 timestamp);

    // Constructor to set the Hop Protocol contract address
    constructor(address _hopProtocolAddress) {
        require(_hopProtocolAddress != address(0), "Invalid Hop Protocol address");
        hopProtocol = IHop(_hopProtocolAddress);
    }

    /**
     * @dev Verifies the successful completion of a token transfer between blockchains.
     * @param sender The address of the sender who initiated the transfer.
     * @param amount The amount of tokens transferred.
     * @param transferId The unique identifier for the transfer.
     * @return success A boolean indicating whether the transfer was successful.
     */
    function verifyTransfer(
        address sender,
        uint256 amount,
        bytes32 transferId
    ) external returns (bool success) {
        // Check if the transferId is valid and exists in the Hop Protocol
        (bool exists, uint256 completedAmount) = hopProtocol.getTransferStatus(transferId);

        // Ensure the transfer exists and the completed amount matches the expected amount
        require(exists, "Transfer does not exist");
        require(completedAmount == amount, "Transfer amount mismatch");

        // Emit an event to log the successful verification
        emit TransferVerified(sender, amount, block.timestamp);

        // Return true indicating the transfer was verified successfully
        return true;
    }
}
```
