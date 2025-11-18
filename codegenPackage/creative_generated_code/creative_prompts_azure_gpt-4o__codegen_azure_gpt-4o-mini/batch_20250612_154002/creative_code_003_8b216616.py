"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://e-digitsr.com
Prompt: Create a smart contract that automatically allocates node interest based on activity standards, as described in the E-DIGITS contract activity system.
Generated: DETERMINISTIC_8b216616e7490bd9
Batch ID: 20250612_154002
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

contract EDigitsNodeInterest {
    // Event emitted when interest is allocated
    event InterestAllocated(address indexed node, uint256 amount);

    // Struct to represent node information
    struct Node {
        uint256 activityScore;  // Activity score based on node activity
        uint256 lastInterestAllocation; // Timestamp of last interest allocation
        uint256 totalInterest;  // Total interest earned by the node
    }

    // Mapping to store node information
    mapping(address => Node) private nodes;

    // Interest rate (in wei) per activity score
    uint256 public interestRate = 1e18; // 1 ether for simplicity

    // Modifier to check if the caller is a valid node
    modifier onlyNode() {
        require(nodes[msg.sender].activityScore > 0, "Not a valid node.");
        _;
    }

    // Function to register a node with an initial activity score
    function registerNode(uint256 _activityScore) external {
        require(_activityScore > 0, "Activity score must be greater than zero.");
        nodes[msg.sender] = Node({
            activityScore: _activityScore,
            lastInterestAllocation: block.timestamp,
            totalInterest: 0
        });
    }

    // Function to update activity score of the node
    function updateActivityScore(uint256 _newActivityScore) external onlyNode {
        require(_newActivityScore > 0, "Activity score must be greater than zero.");
        nodes[msg.sender].activityScore = _newActivityScore;
    }

    // Function to calculate interest for a node based on their activity score
    function calculateInterest(Node memory node) internal view returns (uint256) {
        uint256 timeElapsed = block.timestamp - node.lastInterestAllocation;
        return (node.activityScore * interestRate * timeElapsed) / 1 days;
    }

    // Function to allocate interest to a node automatically
    function allocateInterest() external onlyNode {
        Node storage node = nodes[msg.sender];
        
        // Calculate interest based on the current activity score
        uint256 interest = calculateInterest(node);
        require(interest > 0, "No interest to allocate.");

        // Update node's total interest and last allocation timestamp
        node.totalInterest += interest;
        node.lastInterestAllocation = block.timestamp;

        // Emit an event for interest allocation
        emit InterestAllocated(msg.sender, interest);
    }

    // Function to retrieve node information
    function getNodeInfo(address _node) external view returns (uint256 activityScore, uint256 totalInterest, uint256 lastInterestAllocation) {
        Node memory node = nodes[_node];
        return (node.activityScore, node.totalInterest, node.lastInterestAllocation);
    }
}
```
