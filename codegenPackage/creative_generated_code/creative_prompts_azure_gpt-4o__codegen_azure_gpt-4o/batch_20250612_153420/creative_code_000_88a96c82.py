"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-apedvip.pages.dev
Prompt: Write a smart contract in Solidity for a presale mechanism that enforces a minimum contribution of 0.1 ETH and a maximum contribution of 0.5 ETH, similar to the APED token presale described on the website.
Generated: DETERMINISTIC_88a96c82d66a86fd
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
 * @title Presale Contract
 * @dev This contract implements a presale mechanism with enforced minimum and maximum contributions.
 */
contract Presale {
    // State variables
    address public owner; // Address of the contract owner
    uint256 public minContribution = 0.1 ether; // Minimum contribution amount
    uint256 public maxContribution = 0.5 ether; // Maximum contribution amount
    uint256 public totalContributions; // Total contributions made to the presale
    mapping(address => uint256) public contributions; // Mapping to track contributions per address

    /**
     * @dev Event emitted when a contribution is successfully made.
     * @param contributor The address of the contributor.
     * @param amount The amount contributed.
     */
    event ContributionReceived(address indexed contributor, uint256 amount);

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor sets the owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to contribute to the presale.
     * Enforces minimum and maximum contribution limits.
     */
    function contribute() external payable {
        // Ensure the contribution amount is within allowed limits
        require(msg.value >= minContribution, "Contribution is below the minimum limit");
        require(msg.value <= maxContribution, "Contribution exceeds the maximum limit");
        require(contributions[msg.sender] + msg.value <= maxContribution, "Total contributions exceed the maximum limit");

        // Update contributions
        contributions[msg.sender] += msg.value;
        totalContributions += msg.value;

        // Emit the ContributionReceived event
        emit ContributionReceived(msg.sender, msg.value);
    }

    /**
     * @dev Function for the owner to withdraw funds collected during the presale.
     */
    function withdrawFunds() external onlyOwner {
        // Transfer the contract's balance to the owner
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Transfer failed");
    }

    /**
     * @dev Function to check the contract's balance.
     * @return The current balance of the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
