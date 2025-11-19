"""
Generated Code Metadata:
========================
Original URL: https://ethbo.com
Prompt: Write a smart contract in Solidity for an Ethereum-based pledging system, referencing ETH-specific features like gas optimization and pledge tracking.
Generated: DETERMINISTIC_4eb95631d57477e6
Batch ID: 20250612_154016
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
 * @title ETHPledge
 * @dev A smart contract for tracking pledges in ETH with gas optimization features
 */
contract ETHPledge {
    // Struct to store pledge information
    struct Pledge {
        address pledger;
        uint256 amount;
        uint256 timestamp;
        bool isWithdrawn;
    }

    // State variables
    address public immutable owner;
    uint256 public totalPledges;
    uint256 public totalPledgedAmount;
    mapping(address => uint256) public userPledgeCount;
    mapping(address => mapping(uint256 => Pledge)) public pledges; // user => pledgeId => Pledge

    // Events
    event PledgeCreated(address indexed pledger, uint256 amount, uint256 pledgeId);
    event PledgeWithdrawn(address indexed pledger, uint256 amount, uint256 pledgeId);
    event FundsWithdrawn(address indexed owner, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Create a new pledge
     */
    function createPledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than 0");

        uint256 pledgeId = userPledgeCount[msg.sender];
        pledges[msg.sender][pledgeId] = Pledge({
            pledger: msg.sender,
            amount: msg.value,
            timestamp: block.timestamp,
            isWithdrawn: false
        });

        userPledgeCount[msg.sender]++;
        totalPledges++;
        totalPledgedAmount += msg.value;

        emit PledgeCreated(msg.sender, msg.value, pledgeId);
    }

    /**
     * @dev Withdraw a specific pledge
     * @param pledgeId The ID of the pledge to withdraw
     */
    function withdrawPledge(uint256 pledgeId) external {
        Pledge storage pledge = pledges[msg.sender][pledgeId];
        require(pledge.pledger == msg.sender, "Not the pledge owner");
        require(!pledge.isWithdrawn, "Pledge already withdrawn");
        require(pledge.amount > 0, "No funds to withdraw");

        pledge.isWithdrawn = true;
        totalPledgedAmount -= pledge.amount;

        (bool success, ) = msg.sender.call{value: pledge.amount}("");
        require(success, "Transfer failed");

        emit PledgeWithdrawn(msg.sender, pledge.amount, pledgeId);
    }

    /**
     * @dev Withdraw all collected funds (owner only)
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Transfer failed");

        emit FundsWithdrawn(owner, balance);
    }

    /**
     * @dev Get pledge details for a specific user and pledge ID
     * @param user Address of the pledger
     * @param pledgeId ID of the pledge
     * @return Pledge details
     */
    function getPledge(address user, uint256 pledgeId) external view returns (Pledge memory) {
        return pledges[user][pledgeId];
    }

    /**
     * @dev Get total number of pledges for a specific user
     * @param user Address of the pledger
     * @return Total pledges count
     */
    function getUserPledgeCount(address user) external view returns (uint256) {
        return userPledgeCount[user];
    }
}
```
