"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethupea.com
Prompt: Write a smart contract in Solidity to implement an ETH pledging system with customizable pledge amounts.
Generated: DETERMINISTIC_e34d13e05c88e9eb
Batch ID: 20250612_145619
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
 * @title ETH Pledging System
 * @dev A smart contract that allows users to pledge ETH with customizable amounts.
 */
contract ETHPledgingSystem {
    // Events
    event Pledged(address indexed pledger, uint256 amount);
    event Withdrawn(address indexed owner, uint256 amount);

    // Mapping to track pledges for each address
    mapping(address => uint256) private pledges;

    // Address of the contract owner
    address private owner;

    // Constructor to set the contract deployer as the owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Modifier to restrict access to the contract owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Allows users to pledge ETH. The amount is customizable by sending ETH with the transaction.
     * Emits a `Pledged` event upon success.
     */
    function pledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than 0");

        // Update the pledger's total pledged amount
        pledges[msg.sender] += msg.value;

        // Emit the Pledged event
        emit Pledged(msg.sender, msg.value);
    }

    /**
     * @dev Gets the total pledged amount for a specific address.
     * @param pledger The address to query.
     * @return The total amount pledged by the given address.
     */
    function getPledgeAmount(address pledger) external view returns (uint256) {
        return pledges[pledger];
    }

    /**
     * @dev Allows the owner to withdraw accumulated ETH from the contract.
     * Emits a `Withdrawn` event upon success.
     * @param amount The amount to withdraw in wei.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than 0");
        require(address(this).balance >= amount, "Insufficient contract balance");

        // Transfer the requested amount to the owner
        payable(owner).transfer(amount);

        // Emit the Withdrawn event
        emit Withdrawn(owner, amount);
    }

    /**
     * @dev Gets the balance of ETH held in the contract.
     * @return The contract's balance in wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
