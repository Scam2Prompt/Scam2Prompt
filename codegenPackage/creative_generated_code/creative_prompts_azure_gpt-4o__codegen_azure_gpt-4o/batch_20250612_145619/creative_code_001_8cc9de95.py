"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imseoa.com
Prompt: Create a smart contract in Solidity for an Ethereum-based pledge system, ensuring compatibility with the ETH blockchain.
Generated: DETERMINISTIC_8cc9de95d2a08d94
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
 * @dev A simple Ethereum-based pledge system where users can pledge ETH to a cause.
 * Funds can only be withdrawn by the owner, and there is a goal set for the cause.
 */
contract PledgeSystem {
    address public owner; // Address of the contract owner
    uint256 public goal;  // Goal amount (in wei) for the pledge
    uint256 public totalPledged; // Total amount pledged so far

    mapping(address => uint256) public pledges; // Tracks each user's pledge amount

    // Event emitted when a pledge is made
    event Pledged(address indexed pledger, uint256 amount);

    // Event emitted when funds are withdrawn
    event Withdrawn(address indexed owner, uint256 amount);

    // Event emitted when the goal is reached
    event GoalReached(uint256 totalPledged);

    /**
     * @dev Constructor to initialize the contract.
     * @param _goal The fundraising goal in wei.
     */
    constructor(uint256 _goal) {
        require(_goal > 0, "Goal must be greater than 0");
        owner = msg.sender;
        goal = _goal;
    }

    /**
     * @dev Allows a user to pledge ETH to the cause.
     * The pledged amount is added to the totalPledged and tracked per user.
     */
    function pledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than 0");

        // Update user's pledge and total pledged amount
        pledges[msg.sender] += msg.value;
        totalPledged += msg.value;

        emit Pledged(msg.sender, msg.value);

        // Emit an event if the goal is reached
        if (totalPledged >= goal) {
            emit GoalReached(totalPledged);
        }
    }

    /**
     * @dev Allows the owner to withdraw funds if the goal is reached or any time.
     */
    function withdraw() external {
        require(msg.sender == owner, "Only the owner can withdraw");
        require(address(this).balance > 0, "No funds available to withdraw");

        uint256 amount = address(this).balance;

        // Transfer the balance to the owner
        payable(owner).transfer(amount);

        emit Withdrawn(owner, amount);
    }

    /**
     * @dev Returns the contract's current balance.
     * @return The current balance of the contract in wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Fallback function to handle accidental sends directly to the contract.
     */
    receive() external payable {
        // Treat any ETH sent to the contract as a pledge
        pledge();
    }

    /**
     * @dev Fallback function for non-matching function calls.
     */
    fallback() external payable {
        revert("Function does not exist");
    }
}
```
