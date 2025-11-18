"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1edsdoggggggggggggg.pages.dev
Prompt: Provide code for tracking ETH deposits in a smart contract and updating the presale progress, ensuring the cap of 1000 ETH is enforced.
Generated: DETERMINISTIC_73e43b9ae31e1a65
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
 * @title PresaleTracker
 * @dev A smart contract for tracking ETH deposits during a presale and updating progress.
 * Ensures that the total deposits do not exceed the cap of 1000 ETH.
 */
contract PresaleTracker {
    // State variables
    uint256 public constant CAP = 1000 ether; // Maximum cap of ETH deposits
    uint256 public totalDeposited; // Tracks the total ETH deposited
    address public owner; // Owner of the contract

    // Events
    event DepositReceived(address indexed depositor, uint256 amount);
    event CapReached(uint256 totalDeposited);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to set the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Public function to handle ETH deposits.
     * Ensures deposits do not exceed the CAP.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        require(totalDeposited + msg.value <= CAP, "Deposit would exceed the presale cap");

        // Update the total deposited amount
        totalDeposited += msg.value;

        // Emit event for successful deposit
        emit DepositReceived(msg.sender, msg.value);

        // Check if the cap has been reached
        if (totalDeposited == CAP) {
            emit CapReached(totalDeposited);
        }
    }

    /**
     * @dev Allows the owner to withdraw the collected ETH.
     */
    function withdraw() external onlyOwner {
        require(address(this).balance > 0, "No funds available for withdrawal");

        // Transfer the contract balance to the owner
        (bool success, ) = owner.call{value: address(this).balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct transfers are not allowed");
    }

    /**
     * @dev Receive function to reject ETH transfers without the deposit method.
     */
    receive() external payable {
        revert("Direct transfers are not allowed");
    }
}
```
