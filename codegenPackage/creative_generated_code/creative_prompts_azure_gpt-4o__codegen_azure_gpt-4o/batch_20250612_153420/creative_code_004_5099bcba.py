"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixtoearn-migration.pages.dev
Prompt: Create a relayer system in Solidity that allows users to process withdrawals without pre-funding their accounts, deducting transaction fees directly from the transferred amount, as described in the MixToEarn protocol.
Generated: DETERMINISTIC_5099bcba5200a687
Batch ID: 20250612_153420
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
 * @title Relayer System for Withdrawal Processing
 * @author MixToEarn
 * @dev This contract allows users to withdraw funds without pre-funding their accounts.
 *      Transaction fees are deducted directly from the transferred amount.
 */
contract Relayer {
    // Event emitted when a withdrawal occurs
    event Withdrawal(address indexed user, uint256 amount, uint256 fee);

    // Address of the relayer (owner)
    address public relayer;

    // Fee percentage deducted for relayer services (e.g., 1% = 100 basis points)
    uint256 public feeBasisPoints;

    // Modifier to restrict access to relayer-only functions
    modifier onlyRelayer() {
        require(msg.sender == relayer, "Access restricted to relayer");
        _;
    }

    /**
     * @dev Constructor initializes the contract with the relayer address and fee percentage.
     * @param _feeBasisPoints Fee percentage in basis points (100 basis points = 1%)
     */
    constructor(uint256 _feeBasisPoints) {
        require(_feeBasisPoints <= 10000, "Fee basis points must be <= 10000");
        relayer = msg.sender;
        feeBasisPoints = _feeBasisPoints;
    }

    /**
     * @dev Allows the relayer to update the fee percentage.
     * @param _feeBasisPoints New fee percentage in basis points.
     */
    function setFeeBasisPoints(uint256 _feeBasisPoints) external onlyRelayer {
        require(_feeBasisPoints <= 10000, "Fee basis points must be <= 10000");
        feeBasisPoints = _feeBasisPoints;
    }

    /**
     * @dev Processes withdrawals for users, deducts fees, and forwards the net amount.
     * @param recipient Address of the user to receive the funds.
     */
    function processWithdrawal(address payable recipient) external payable {
        require(msg.value > 0, "Transaction amount must be greater than zero");
        require(recipient != address(0), "Recipient address cannot be zero");

        // Calculate fee and net amount
        uint256 fee = (msg.value * feeBasisPoints) / 10000;
        uint256 netAmount = msg.value - fee;

        require(netAmount > 0, "Net amount must be greater than zero");

        // Transfer net amount to the recipient
        (bool sentToRecipient, ) = recipient.call{value: netAmount}("");
        require(sentToRecipient, "Failed to send funds to recipient");

        // Transfer fee to the relayer
        (bool sentToRelayer, ) = relayer.call{value: fee}("");
        require(sentToRelayer, "Failed to send fee to relayer");

        // Emit withdrawal event
        emit Withdrawal(recipient, netAmount, fee);
    }

    /**
     * @dev Allows relayer to withdraw any funds accidentally sent to the contract.
     * @param amount Amount to withdraw.
     */
    function withdrawFunds(uint256 amount) external onlyRelayer {
        require(amount <= address(this).balance, "Insufficient contract balance");
        (bool success, ) = relayer.call{value: amount}("");
        require(success, "Failed to withdraw funds");
    }

    /**
     * @dev Fallback function to receive Ether. Prevents accidental contract locking.
     */
    receive() external payable {
        // Accept Ether deposits to the contract
    }
}
```
