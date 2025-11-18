"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rocketspool.pages.dev
Prompt: Write a Solidity function to simulate the penalty minimization mechanism used in Rocket Pool, where losses from bad nodes are socialized across the network.
Generated: DETERMINISTIC_c3248da4f26f9691
Batch ID: 20250612_151918
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

contract RocketPoolPenalty {

    // Event to log the distribution of penalties
    event PenaltyDistributed(uint256 totalPenalty, uint256 nodesAffected, uint256 penaltyPerNode);

    // Mapping to store the stake of each node
    mapping(address => uint256) public stakes;

    // Total amount of staked ETH in the network
    uint256 public totalStaked;

    // Modifier to check if sender has a stake
    modifier onlyStaker() {
        require(stakes[msg.sender] > 0, "Not a staker");
        _;
    }

    // Function to allow nodes to stake ETH
    function stake() external payable {
        require(msg.value > 0, "Stake must be greater than zero");
        
        stakes[msg.sender] += msg.value;
        totalStaked += msg.value;
    }

    // Function to simulate penalty distribution across affected nodes
    function distributePenalty(uint256 penaltyAmount, address[] memory affectedNodes) external onlyStaker {
        require(penaltyAmount > 0, "Penalty must be greater than zero");
        require(affectedNodes.length > 0, "No affected nodes");

        uint256 totalPenalty = penaltyAmount;
        uint256 nodesAffected = affectedNodes.length;
        uint256 penaltyPerNode = totalPenalty / nodesAffected;

        // Distributing penalties evenly among affected nodes
        for (uint256 i = 0; i < nodesAffected.length; i++) {
            address node = affectedNodes[i];
            require(stakes[node] >= penaltyPerNode, "Node does not have enough stake to cover penalty");
            
            // Deducting penalty amount from the node's stake
            stakes[node] -= penaltyPerNode;
            totalStaked -= penaltyPerNode;
        }

        // Emit event for penalty distribution
        emit PenaltyDistributed(totalPenalty, nodesAffected, penaltyPerNode);
    }

    // Function to allow nodes to withdraw their stake
    function withdrawStake() external onlyStaker {
        uint256 stakeAmount = stakes[msg.sender];
        require(stakeAmount > 0, "No stake to withdraw");

        // Resetting the staker's stake before the transfer to prevent reentrancy attacks
        stakes[msg.sender] = 0;
        totalStaked -= stakeAmount;

        // Transferring the stake back to the user
        (bool success, ) = msg.sender.call{value: stakeAmount}("");
        require(success, "Transfer failed");
    }

    // Fallback function to accept Ether
    receive() external payable {
        stake(); // Allowing users to stake directly through the fallback
    }
}
```
