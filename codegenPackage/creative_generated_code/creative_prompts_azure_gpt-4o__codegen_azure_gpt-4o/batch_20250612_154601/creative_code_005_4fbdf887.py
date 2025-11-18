"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okx000000000000000000131.pages.dev
Prompt: Create a smart contract in Solidity for managing TRX transfers with a limit on the maximum transfer amount per transaction.
Generated: DETERMINISTIC_4fbdf887a0541dd5
Batch ID: 20250612_154601
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
 * @title TRXTransferWithLimit
 * @dev This smart contract is designed to manage TRX transfers 
 * with a limit on the maximum transfer amount per transaction.
 */
contract TRXTransferWithLimit {
    address public owner;
    uint256 public maxTransferAmount;

    /**
     * @dev Event emitted when TRX is transferred.
     * @param sender The address that initiated the transfer.
     * @param receiver The address that received the transfer.
     * @param amount The amount of TRX transferred.
     */
    event Transfer(address indexed sender, address indexed receiver, uint256 amount);

    /**
     * @dev Event emitted when the maximum transfer amount is updated.
     * @param oldAmount The previous maximum transfer amount.
     * @param newAmount The new maximum transfer amount.
     */
    event MaxTransferAmountUpdated(uint256 oldAmount, uint256 newAmount);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize contract with owner and maximum transfer amount.
     * @param _maxTransferAmount The initial maximum transfer amount per transaction.
     */
    constructor(uint256 _maxTransferAmount) {
        require(_maxTransferAmount > 0, "Maximum transfer amount must be greater than zero");
        owner = msg.sender;
        maxTransferAmount = _maxTransferAmount;
    }

    /**
     * @dev Function to transfer TRX with a limit on the maximum transfer amount.
     * @param recipient The address to receive the TRX.
     * @param amount The amount of TRX to transfer.
     */
    function transfer(address payable recipient, uint256 amount) external payable {
        require(amount <= maxTransferAmount, "Transfer amount exceeds the maximum limit");
        require(msg.value == amount, "Sent value must match the transfer amount");

        // Perform the transfer
        recipient.transfer(amount);

        // Emit the transfer event
        emit Transfer(msg.sender, recipient, amount);
    }

    /**
     * @dev Function to update the maximum transfer amount.
     * @param _newMaxTransferAmount The new maximum transfer amount.
     */
    function updateMaxTransferAmount(uint256 _newMaxTransferAmount) external onlyOwner {
        require(_newMaxTransferAmount > 0, "Maximum transfer amount must be greater than zero");
        uint256 oldAmount = maxTransferAmount;
        maxTransferAmount = _newMaxTransferAmount;

        // Emit the update event
        emit MaxTransferAmountUpdated(oldAmount, _newMaxTransferAmount);
    }

    /**
     * @dev Fallback function to handle unexpected incoming TRX.
     */
    fallback() external payable {}

    /**
     * @dev Receive function to handle incoming TRX transfers.
     */
    receive() external payable {}
}
```
