"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://permasolution.pages.dev
Prompt: Write a script to deploy a smart contract on the peaq blockchain for managing community nodes, inspired by Teneo Protocol's use case.
Generated: DETERMINISTIC_8422519501f00e33
Batch ID: 20250612_154913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// This contract manages community nodes for the peaq blockchain
contract CommunityNodeManager is Ownable {
    using Counters for Counters.Counter;

    // Event emitted when a new node is added
    event NodeAdded(address indexed nodeAddress, string nodeName);

    // Event emitted when a node is removed
    event NodeRemoved(address indexed nodeAddress);

    // Struct representing a community node
    struct Node {
        string name;
        bool exists;
    }

    // Mapping to store nodes
    mapping(address => Node) private nodes;

    // Counter to keep track of the number of nodes
    Counters.Counter private nodeCount;

    // Modifier to check if the node exists
    modifier onlyExistingNode(address nodeAddress) {
        require(nodes[nodeAddress].exists, "Node does not exist");
        _;
    }

    // Modifier to check if the node does not exist
    modifier onlyNonExistingNode(address nodeAddress) {
        require(!nodes[nodeAddress].exists, "Node already exists");
        _;
    }

    // Function to add a new community node
    // @param nodeAddress: address of the node to be added
    // @param nodeName: name of the node
    function addNode(address nodeAddress, string memory nodeName) 
        external 
        onlyNonExistingNode(nodeAddress) 
        onlyOwner 
    {
        require(nodeAddress != address(0), "Invalid address");
        require(bytes(nodeName).length > 0, "Invalid node name");

        // Add the node
        nodes[nodeAddress] = Node({
            name: nodeName,
            exists: true
        });

        nodeCount.increment();

        emit NodeAdded(nodeAddress, nodeName);
    }

    // Function to remove an existing community node
    // @param nodeAddress: address of the node to be removed
    function removeNode(address nodeAddress) 
        external 
        onlyExistingNode(nodeAddress) 
        onlyOwner 
    {
        // Remove the node
        delete nodes[nodeAddress];
        nodeCount.decrement();

        emit NodeRemoved(nodeAddress);
    }

    // Function to get the details of a specific node
    // @param nodeAddress: address of the node to query
    // @return name of the node and existence status
    function getNode(address nodeAddress) 
        external 
        view 
        onlyExistingNode(nodeAddress) 
        returns (string memory) 
    {
        return nodes[nodeAddress].name;
    }

    // Function to get the total number of nodes
    // @return total number of nodes managed by this contract
    function getTotalNodes() 
        external 
        view 
        returns (uint256) 
    {
        return nodeCount.current();
    }
}
```
