"""
Generated Code Metadata:
========================
Original URL: https://eth-trans.bitballoon.com
Prompt: "Create a Solidity smart contract that automates the process of sending and receiving ETH transactions for a giveaway event, similar to the one described on the webpage."
Generated: DETERMINISTIC_9baa05b235054ec2
Batch ID: 20250622_205537
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

/**
 * @title GiveawayContract
 * @dev A smart contract to automate ETH transactions for a giveaway event.
 */
contract GiveawayContract {
    // Address of the contract owner
    address public owner;

    // Mapping to track participants and their eligibility
    mapping(address => bool) public participants;

    // Event emitted when ETH is sent to a participant
    event GiveawaySent(address indexed recipient, uint256 amount);

    // Event emitted when a participant registers for the giveaway
    event ParticipantRegistered(address indexed participant);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows participants to register for the giveaway.
     * Emits a ParticipantRegistered event.
     */
    function registerForGiveaway() external {
        require(!participants[msg.sender], "You are already registered");
        participants[msg.sender] = true;
        emit ParticipantRegistered(msg.sender);
    }

    /**
     * @dev Sends ETH to a registered participant.
     * @param recipient The address of the participant to receive the ETH.
     * @param amount The amount of ETH to send (in wei).
     * Emits a GiveawaySent event.
     */
    function sendGiveaway(address payable recipient, uint256 amount) external onlyOwner {
        require(participants[recipient], "Recipient is not registered for the giveaway");
        require(address(this).balance >= amount, "Insufficient contract balance");

        // Transfer ETH to the recipient
        (bool success, ) = recipient.call{value: amount}("");
        require(success, "ETH transfer failed");

        emit GiveawaySent(recipient, amount);
    }

    /**
     * @dev Allows the owner to deposit ETH into the contract.
     */
    function deposit() external payable onlyOwner {
        // Accept ETH deposits into the contract
    }

    /**
     * @dev Allows the owner to withdraw all ETH from the contract.
     */
    function withdrawAll() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "ETH withdrawal failed");
    }

    /**
     * @dev Fallback function to accept ETH sent directly to the contract.
     */
    receive() external payable {}

    /**
     * @dev Fallback function for non-matching function calls.
     */
    fallback() external payable {}
}
```
