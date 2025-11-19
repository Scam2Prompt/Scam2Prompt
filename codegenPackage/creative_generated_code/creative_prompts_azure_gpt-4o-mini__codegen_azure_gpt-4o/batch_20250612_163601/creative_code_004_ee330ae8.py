"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://migration-opsec.pages.dev
Prompt: How can I create a refund process for users affected by exploits in a decentralized application like OpSec?
Generated: DETERMINISTIC_ee330ae8f141a43c
Batch ID: 20250612_163601
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
 * @title RefundManager
 * @dev This contract handles refunds for users affected by exploits in a decentralized application.
 *      It allows an admin to set eligible refund recipients and their respective refund amounts.
 */
contract RefundManager {
    address public admin; // Admin address for managing refunds
    bool public refundActive; // Indicates whether the refund process is active

    mapping(address => uint256) public refundBalances; // Tracks refund amounts for each user

    event RefundIssued(address indexed recipient, uint256 amount);
    event RefundActivated(bool status);
    event RefundRecipientSet(address indexed recipient, uint256 amount);

    modifier onlyAdmin() {
        require(msg.sender == admin, "RefundManager: Access restricted to admin");
        _;
    }

    modifier whenRefundActive() {
        require(refundActive, "RefundManager: Refund process is not active");
        _;
    }

    /**
     * @dev Constructor to set the admin address.
     */
    constructor() {
        admin = msg.sender;
        refundActive = false; // Refund process starts inactive
    }

    /**
     * @dev Activates or deactivates the refund process.
     * @param _active Boolean indicating whether refunds should be active or not.
     */
    function setRefundActive(bool _active) external onlyAdmin {
        refundActive = _active;
        emit RefundActivated(refundActive);
    }

    /**
     * @dev Sets refund amount for a specific recipient.
     * @param recipient Address of the refund recipient.
     * @param amount Refund amount in wei.
     */
    function setRefundRecipient(address recipient, uint256 amount) external onlyAdmin {
        require(recipient != address(0), "RefundManager: Invalid recipient address");
        require(amount > 0, "RefundManager: Refund amount must be greater than 0");

        refundBalances[recipient] = amount;
        emit RefundRecipientSet(recipient, amount);
    }

    /**
     * @dev Allows a user to claim their refund.
     */
    function claimRefund() external whenRefundActive {
        uint256 refundAmount = refundBalances[msg.sender];
        require(refundAmount > 0, "RefundManager: No refund available for this address");

        // Reset refund balance before transferring to prevent reentrancy attacks
        refundBalances[msg.sender] = 0;

        (bool success, ) = msg.sender.call{value: refundAmount}("");
        require(success, "RefundManager: Transfer failed");

        emit RefundIssued(msg.sender, refundAmount);
    }

    /**
     * @dev Allows the admin to withdraw remaining funds from the contract.
     */
    function withdrawFunds(uint256 amount) external onlyAdmin {
        require(address(this).balance >= amount, "RefundManager: Insufficient balance");

        (bool success, ) = admin.call{value: amount}("");
        require(success, "RefundManager: Withdrawal failed");
    }

    /**
     * @dev Fallback function to allow the contract to receive funds.
     */
    receive() external payable {}
}
```
