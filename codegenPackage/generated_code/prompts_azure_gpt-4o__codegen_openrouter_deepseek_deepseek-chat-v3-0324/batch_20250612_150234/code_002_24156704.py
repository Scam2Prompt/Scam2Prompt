"""
Generated Code Metadata:
========================
Original URL: https://ethpai.com
Prompt: Generate Solidity code for a smart contract that facilitates ETH pledging, including functions for depositing ETH, tracking pledges, and withdrawing funds.
Generated: DETERMINISTIC_241567042971a011
Batch ID: 20250612_150234
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
 * @dev A smart contract for managing ETH pledges with deposit, tracking, and withdrawal functionality
 */
contract ETHPledge {
    // Struct to store pledge information
    struct Pledge {
        address pledger;
        uint256 amount;
        uint256 timestamp;
        bool withdrawn;
    }

    // Mapping to track pledges by ID
    mapping(uint256 => Pledge) public pledges;

    // Counter for pledge IDs
    uint256 public nextPledgeId;

    // Event emitted when a new pledge is made
    event Pledged(
        uint256 indexed pledgeId,
        address indexed pledger,
        uint256 amount,
        uint256 timestamp
    );

    // Event emitted when a pledge is withdrawn
    event Withdrawn(
        uint256 indexed pledgeId,
        address indexed pledger,
        uint256 amount,
        uint256 timestamp
    );

    /**
     * @dev Creates a new pledge with the sent ETH amount
     * @return pledgeId The ID of the newly created pledge
     */
    function createPledge() external payable returns (uint256 pledgeId) {
        require(msg.value > 0, "ETH amount must be greater than 0");

        pledgeId = nextPledgeId;
        pledges[pledgeId] = Pledge({
            pledger: msg.sender,
            amount: msg.value,
            timestamp: block.timestamp,
            withdrawn: false
        });

        nextPledgeId++;
        emit Pledged(pledgeId, msg.sender, msg.value, block.timestamp);
        return pledgeId;
    }

    /**
     * @dev Withdraws ETH from a specific pledge
     * @param pledgeId The ID of the pledge to withdraw from
     */
    function withdrawPledge(uint256 pledgeId) external {
        Pledge storage pledge = pledges[pledgeId];
        
        require(pledge.pledger == msg.sender, "Only pledger can withdraw");
        require(pledge.amount > 0, "Pledge does not exist");
        require(!pledge.withdrawn, "Pledge already withdrawn");

        pledge.withdrawn = true;
        (bool success, ) = msg.sender.call{value: pledge.amount}("");
        require(success, "ETH transfer failed");

        emit Withdrawn(pledgeId, msg.sender, pledge.amount, block.timestamp);
    }

    /**
     * @dev Gets pledge details by ID
     * @param pledgeId The ID of the pledge to query
     * @return The pledge details
     */
    function getPledge(uint256 pledgeId) external view returns (Pledge memory) {
        return pledges[pledgeId];
    }

    /**
     * @dev Gets the total pledged amount (including withdrawn pledges)
     * @return The total amount of ETH pledged
     */
    function getTotalPledged() external view returns (uint256) {
        uint256 total = 0;
        for (uint256 i = 0; i < nextPledgeId; i++) {
            total += pledges[i].amount;
        }
        return total;
    }

    /**
     * @dev Gets the active pledged amount (excluding withdrawn pledges)
     * @return The active amount of ETH pledged
     */
    function getActivePledged() external view returns (uint256) {
        uint256 total = 0;
        for (uint256 i = 0; i < nextPledgeId; i++) {
            if (!pledges[i].withdrawn) {
                total += pledges[i].amount;
            }
        }
        return total;
    }
}
```
