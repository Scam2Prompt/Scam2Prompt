"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapphashai.pages.dev
Prompt: Develop a smart contract for leasing nodes in the HashAI network using Solidity.
Generated: DETERMINISTIC_9bef1368c9c8dcef
Batch ID: 20250612_163915
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
 * @title NodeLeasingContract
 * @dev A smart contract for leasing nodes in the HashAI network.
 * Allows node owners to lease nodes to users on a time-based rental model.
 */
contract NodeLeasingContract {
    // Struct for lease details
    struct Lease {
        address lessee; // Address of the user leasing the node
        uint256 startTime; // Lease start time (Unix timestamp)
        uint256 endTime; // Lease end time (Unix timestamp)
        uint256 pricePerSecond; // Cost per second for leasing
        bool isActive; // Status of the lease
    }

    // Address of the node owner
    address public owner;

    // Mapping of node IDs to lease details
    mapping(uint256 => Lease) public leases;

    // Event emitted when a lease is initiated
    event LeaseInitiated(uint256 indexed nodeId, address indexed lessee, uint256 startTime, uint256 endTime, uint256 pricePerSecond);
    
    // Event emitted when a lease ends
    event LeaseEnded(uint256 indexed nodeId, address indexed lessee, uint256 endTime);

    // Modifier to restrict access to the node owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Modifier to validate active lease
    modifier activeLease(uint256 nodeId) {
        require(leases[nodeId].isActive, "No active lease for this node");
        _;
    }

    /**
     * @dev Constructor sets the owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Initiates a lease for a node.
     * @param nodeId ID of the node to lease.
     * @param lessee Address of the user leasing the node.
     * @param duration Duration of the lease in seconds.
     * @param pricePerSecond Cost per second for leasing the node.
     */
    function initiateLease(uint256 nodeId, address lessee, uint256 duration, uint256 pricePerSecond) external onlyOwner {
        require(leases[nodeId].isActive == false, "Node is already leased");
        require(lessee != address(0), "Invalid lessee address");
        require(duration > 0, "Duration must be greater than zero");
        require(pricePerSecond > 0, "Price per second must be greater than zero");

        uint256 startTime = block.timestamp;
        uint256 endTime = startTime + duration;

        leases[nodeId] = Lease({
            lessee: lessee,
            startTime: startTime,
            endTime: endTime,
            pricePerSecond: pricePerSecond,
            isActive: true
        });

        emit LeaseInitiated(nodeId, lessee, startTime, endTime, pricePerSecond);
    }

    /**
     * @dev Ends an active lease for a node.
     * @param nodeId ID of the node whose lease is being ended.
     */
    function endLease(uint256 nodeId) external onlyOwner activeLease(nodeId) {
        Lease storage lease = leases[nodeId];
        require(block.timestamp >= lease.endTime, "Lease duration has not ended yet");

        address lessee = lease.lessee;

        // Mark the lease as inactive
        lease.isActive = false;

        emit LeaseEnded(nodeId, lessee, block.timestamp);
    }

    /**
     * @dev Returns details of a node lease.
     * @param nodeId ID of the node.
     * @return Lease details for the node.
     */
    function getLeaseDetails(uint256 nodeId) external view returns (Lease memory) {
        return leases[nodeId];
    }
}
```
