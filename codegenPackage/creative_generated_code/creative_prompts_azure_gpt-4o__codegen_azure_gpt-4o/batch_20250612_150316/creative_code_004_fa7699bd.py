"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raca3-io.pages.dev
Prompt: Write a smart contract for managing decentralized donations in a Web3 social dApp, referencing the Friend3 partnership mentioned on the RACA website.
Generated: DETERMINISTIC_fa7699bd1896e52e
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an Ethereum smart contract written in Solidity, following industry best practices and adhering to your requirements.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title Decentralized Donations Smart Contract
 * @dev This contract is designed for managing donations in a Web3 social dApp,
 * inspired by the Friend3 partnership mentioned on the RACA website.
 */
contract DecentralizedDonations {
    // Address of the contract owner (social dApp administrator)
    address public owner;

    // Event emitted when a donation is made
    event DonationReceived(
        address indexed donor,
        uint256 amount,
        string message,
        uint256 timestamp
    );

    // Event emitted when funds are withdrawn from the contract
    event FundsWithdrawn(
        address indexed withdrawnBy,
        uint256 amount,
        uint256 timestamp
    );

    // Mapping to track total donations by each donor address
    mapping(address => uint256) public totalDonations;

    // Constructor: Initializes the contract and sets the deployer as the owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Access restricted to owner only");
        _;
    }

    /**
     * @dev Public function to send a donation. Emits a DonationReceived event.
     * @param message A custom message from the donor (optional).
     */
    function donate(string calldata message) external payable {
        require(msg.value > 0, "Donation amount must be greater than zero");

        // Update the total donations for the sender
        totalDonations[msg.sender] += msg.value;

        // Emit the donation event
        emit DonationReceived(msg.sender, msg.value, message, block.timestamp);
    }

    /**
     * @dev Public function to check the contract's current balance.
     * @return The contract's current Ether balance.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Owner-only function to withdraw funds from the contract.
     * @param amount The amount of Ether to withdraw.
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(
            amount > 0 && amount <= address(this).balance,
            "Invalid withdrawal amount"
        );

        // Transfer the requested amount to the owner's address
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Withdrawal failed");

        // Emit the withdrawal event
        emit FundsWithdrawn(owner, amount, block.timestamp);
    }

    /**
     * @dev Owner-only function to transfer ownership of the contract.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        owner = newOwner;
    }

    /**
     * @dev Fallback function to handle Ether sent directly to the contract.
     */
    receive() external payable {
        totalDonations[msg.sender] += msg.value;
        emit DonationReceived(msg.sender, msg.value, "Direct donation", block.timestamp);
    }
}
```

This Solidity smart contract is designed for managing decentralized donations in a Web3 social dApp. It supports donation tracking, ownership management, and withdrawal functionality. It is production-ready and adheres to best practices.
