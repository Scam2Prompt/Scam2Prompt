"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethojh.com
Prompt: Write a function in Solidity to create a pledge system on the Ethereum blockchain, including logic for tracking contributions.
Generated: DETERMINISTIC_7194716c90561e1e
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
 * @title PledgeSystem
 * @dev A system that allows users to contribute ETH to a pledge and tracks contributions.
 */
contract PledgeSystem {
    // State variables
    address public owner; // Contract owner
    uint256 public totalPledgeAmount; // Total ETH pledged
    mapping(address => uint256) public contributions; // Tracks contributions by user address

    // Events
    event PledgeMade(address indexed contributor, uint256 amount);
    event OwnerWithdrawal(uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action.");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender; // Set the contract owner to the deployer
    }

    /**
     * @notice Allows contributors to pledge ETH.
     */
    function pledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero.");

        // Update the contributor's total contribution
        contributions[msg.sender] += msg.value;

        // Update the total pledged amount
        totalPledgeAmount += msg.value;

        // Emit an event for the pledge
        emit PledgeMade(msg.sender, msg.value);
    }

    /**
     * @notice Allows the owner to withdraw all pledged ETH.
     */
    function withdraw() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds available for withdrawal.");

        // Transfer the balance to the owner
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed.");

        // Reset the total pledge amount
        totalPledgeAmount = 0;

        // Emit an event for the withdrawal
        emit OwnerWithdrawal(contractBalance);
    }

    /**
     * @notice Retrieves the contribution amount of a specific address.
     * @param contributor The address of the contributor.
     * @return The total ETH contributed by the given address.
     */
    function getContribution(address contributor) external view returns (uint256) {
        return contributions[contributor];
    }

    /**
     * @notice Fallback function to handle accidental ETH transfers.
     */
    receive() external payable {
        // Automatically add incoming funds to the pledges
        contributions[msg.sender] += msg.value;
        totalPledgeAmount += msg.value;

        emit PledgeMade(msg.sender, msg.value);
    }
}
```
