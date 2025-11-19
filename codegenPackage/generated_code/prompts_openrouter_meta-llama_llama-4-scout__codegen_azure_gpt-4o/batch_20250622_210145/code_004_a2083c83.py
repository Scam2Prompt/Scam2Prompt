"""
Generated Code Metadata:
========================
Original URL: https://ethkind.com
Prompt: Design a basic Ethereum pledge smart contract and provide example code.
Generated: DETERMINISTIC_a2083c8330dbfbbb
Batch ID: 20250622_210145
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
 * @title PledgeContract
 * @dev A simple Ethereum smart contract to allow users to pledge ETH.
 * Users can pledge ETH, and the contract owner can withdraw the total balance.
 */
contract PledgeContract {
    // Address of the contract owner
    address public owner;

    // Mapping to track pledges made by each address
    mapping(address => uint256) public pledges;

    // Event emitted when a pledge is made
    event PledgeMade(address indexed pledger, uint256 amount);

    // Event emitted when the owner withdraws funds
    event FundsWithdrawn(address indexed owner, uint256 amount);

    /**
     * @dev Constructor sets the contract deployer as the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function");
        _;
    }

    /**
     * @dev Function to allow users to pledge ETH to the contract.
     * Emits a PledgeMade event.
     */
    function pledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        // Update the pledges mapping
        pledges[msg.sender] += msg.value;

        // Emit the PledgeMade event
        emit PledgeMade(msg.sender, msg.value);
    }

    /**
     * @dev Function for the owner to withdraw all funds from the contract.
     * Emits a FundsWithdrawn event.
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds available to withdraw");

        // Transfer the contract balance to the owner
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Transfer failed");

        // Emit the FundsWithdrawn event
        emit FundsWithdrawn(owner, contractBalance);
    }

    /**
     * @dev Function to get the total balance of the contract.
     * @return The total balance of the contract in wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
