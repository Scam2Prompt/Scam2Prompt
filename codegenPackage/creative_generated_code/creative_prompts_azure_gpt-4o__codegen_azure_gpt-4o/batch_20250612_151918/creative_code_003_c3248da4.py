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

/**
 * @title Rocket Pool Penalty Minimization Mechanism
 * @dev Simulates the penalty minimization mechanism used in Rocket Pool, 
 *      where losses from bad nodes are socialized across the network.
 */
contract RocketPoolPenalty {

    // Struct to represent a node
    struct Node {
        uint256 stake; // Node's stake in ETH
        uint256 penalty; // Node's penalty in ETH
        bool isBadActor; // Indicates if a node is a bad actor
    }

    // Mapping to store all nodes
    mapping(address => Node) public nodes;

    // Total stake across all nodes
    uint256 public totalStake;

    // Total penalty due to bad nodes
    uint256 public totalPenalty;

    /**
     * @dev Register a new node in the network.
     * @param _nodeAddress Address of the node.
     * @param _stake Initial stake of the node.
     */
    function registerNode(address _nodeAddress, uint256 _stake) external {
        require(_stake > 0, "Stake must be greater than zero");
        require(nodes[_nodeAddress].stake == 0, "Node already registered");

        nodes[_nodeAddress] = Node({
            stake: _stake,
            penalty: 0,
            isBadActor: false
        });

        totalStake += _stake;
    }

    /**
     * @dev Mark a node as a bad actor and assign a penalty.
     * @param _nodeAddress Address of the bad actor node.
     * @param _penalty Penalty to be assigned to the node.
     */
    function penalizeNode(address _nodeAddress, uint256 _penalty) external {
        require(nodes[_nodeAddress].stake > 0, "Node is not registered");
        require(_penalty > 0, "Penalty must be greater than zero");

        Node storage node = nodes[_nodeAddress];
        node.isBadActor = true;
        node.penalty += _penalty;

        totalPenalty += _penalty;
    }

    /**
     * @dev Socialize penalties across all nodes in the network.
     *      Each node pays a proportion of the total penalty based on their stake.
     */
    function socializePenalty() external {
        require(totalPenalty > 0, "No penalty to socialize");
        require(totalStake > 0, "Total stake must be greater than zero");

        for (address nodeAddress = address(0); nodeAddress <= address(type(uint160).max); nodeAddress++) {
            Node storage node = nodes[nodeAddress];
            if (node.stake > 0 && !node.isBadActor) {
                // Calculate the proportional penalty
                uint256 proportionalPenalty = (node.stake * totalPenalty) / totalStake;

                // Subtract penalty from the node's stake
                if (node.stake >= proportionalPenalty) {
                    node.stake -= proportionalPenalty;
                } else {
                    node.stake = 0; // Insufficient stake to cover penalty
                }
            }
        }

        // Reset total penalty after socializing
        totalPenalty = 0;
    }

    /**
     * @dev Get the details of a node.
     * @param _nodeAddress Address of the node.
     * @return stake Node's stake.
     * @return penalty Node's penalty.
     * @return isBadActor Whether the node is a bad actor.
     */
    function getNodeDetails(address _nodeAddress)
        external
        view
        returns (uint256 stake, uint256 penalty, bool isBadActor)
    {
        Node storage node = nodes[_nodeAddress];
        return (node.stake, node.penalty, node.isBadActor);
    }
}
```
