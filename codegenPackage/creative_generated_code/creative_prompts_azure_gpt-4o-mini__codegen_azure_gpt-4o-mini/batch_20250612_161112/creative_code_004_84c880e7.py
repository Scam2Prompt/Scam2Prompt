"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reg-dmailapp.pages.dev
Prompt: Create a function that leverages Dmail's messaging protocol to send notifications from a smart contract.
Generated: DETERMINISTIC_84c880e788c7d19c
Batch ID: 20250612_161112
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

// Importing the necessary interfaces for Dmail protocol
interface IDmail {
    function sendMessage(address to, string calldata message) external returns (bool);
}

contract NotificationContract {
    // Address of the Dmail contract
    IDmail private dmail;

    // Event to log notifications
    event NotificationSent(address indexed to, string message);

    // Constructor to set the Dmail contract address
    constructor(address _dmailAddress) {
        require(_dmailAddress != address(0), "Invalid Dmail address");
        dmail = IDmail(_dmailAddress);
    }

    /**
     * @dev Sends a notification message to a specified address using Dmail's messaging protocol.
     * @param to The address of the recipient.
     * @param message The notification message to be sent.
     */
    function sendNotification(address to, string calldata message) external {
        require(to != address(0), "Recipient address cannot be zero");
        require(bytes(message).length > 0, "Message cannot be empty");

        // Send the message using Dmail protocol
        bool success = dmail.sendMessage(to, message);
        
        // Check if the message was sent successfully
        require(success, "Failed to send notification");

        // Emit an event for successful notification
        emit NotificationSent(to, message);
    }
}
```
