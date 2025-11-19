"""
Generated Code Metadata:
========================
Original URL: https://hashai.pages.dev
Prompt: Create a Solidity contract that enables Hash & Node rental services, ensuring fair distribution of rewards to renters, as part of Hash AI's service expansion.
Generated: DETERMINISTIC_83631100dadc9024
Batch ID: 20250612_153517
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title HashNodeRentalContract
 * @author Hash AI
 * @notice Enables Hash & Node rental services with fair distribution of rewards to renters.
 */
contract HashNodeRentalContract is Ownable {
    using SafeMath for uint256;

    // Mapping of node IDs to their respective owners
    mapping (address => mapping (uint256 => Node)) public nodeOwners;

    // Mapping of renter addresses to their rented nodes
    mapping (address => mapping (uint256 => Rental)) public rentedNodes;

    // Mapping of node IDs to their rental status
    mapping (uint256 => bool) public isNodeRented;

    // Total rewards accumulated by the contract
    uint256 public totalRewards;

    // Reward distribution percentage for renters (in basis points)
    uint256 public constant RENTER_REWARD_PERCENTAGE = 5000; // 50%

    // ERC20 token used for rewards
    IERC20 public rewardsToken;

    /**
     * @notice Event emitted when a node is rented
     * @param nodeId ID of the rented node
     * @param renter Address of the renter
     * @param owner Address of the node owner
     */
    event NodeRented(uint256 nodeId, address renter, address owner);

    /**
     * @notice Event emitted when a node is returned
     * @param nodeId ID of the returned node
     * @param renter Address of the renter
     */
    event NodeReturned(uint256 nodeId, address renter);

    /**
     * @notice Event emitted when rewards are distributed
     * @param renter Address of the renter
     * @param amount Distributed reward amount
     */
    event RewardsDistributed(address renter, uint256 amount);

    /**
     * @param _rewardsToken Address of the ERC20 token used for rewards
     */
    constructor(address _rewardsToken) public {
        require(_rewardsToken != address(0), "Rewards token address cannot be zero");
        rewardsToken = IERC20(_rewardsToken);
    }

    /**
     * @notice Adds a new node to the network
     * @param _nodeId ID of the node to add
     */
    function addNode(uint256 _nodeId) public onlyOwner {
        require(!isNodeRented[_nodeId], "Node already exists");
        nodeOwners[msg.sender][_nodeId] = Node(_nodeId, msg.sender);
        isNodeRented[_nodeId] = false;
    }

    /**
     * @notice Rents a node
     * @param _nodeId ID of the node to rent
     */
    function rentNode(uint256 _nodeId) public {
        require(isNodeRented[_nodeId] == false, "Node is already rented");
        require(nodeOwners[msg.sender][_nodeId].owner == msg.sender, "You are not the owner of this node");

        // Mark node as rented
        isNodeRented[_nodeId] = true;

        // Initialize rental
        rentedNodes[msg.sender][_nodeId] = Rental(_nodeId, msg.sender, block.timestamp);

        emit NodeRented(_nodeId, msg.sender, msg.sender);
    }

    /**
     * @notice Returns a rented node
     * @param _nodeId ID of the node to return
     */
    function returnNode(uint256 _nodeId) public {
        require(isNodeRented[_nodeId] == true, "Node is not rented");
        require(rentedNodes[msg.sender][_nodeId].renter == msg.sender, "You are not the renter of this node");

        // Calculate rewards
        uint256 rentalDuration = block.timestamp.sub(rentedNodes[msg.sender][_nodeId].rentalStartTime);
        uint256 rewards = calculateRewards(rentalDuration);

        // Distribute rewards to renter
        distributeRewards(msg.sender, rewards);

        // Mark node as available
        isNodeRented[_nodeId] = false;

        emit NodeReturned(_nodeId, msg.sender);
    }

    /**
     * @notice Calculates rewards based on rental duration
     * @param _rentalDuration Rental duration in seconds
     * @return Calculated rewards
     */
    function calculateRewards(uint256 _rentalDuration) internal view returns (uint256) {
        // Assuming 1 node rewards 1 token per second
        uint256 rewards = _rentalDuration.mul(1 ether).mul(RENTER_REWARD_PERCENTAGE).div(10000);
        return rewards;
    }

    /**
     * @notice Distributes rewards to a renter
     * @param _renter Address of the renter
     * @param _amount Reward amount to distribute
     */
    function distributeRewards(address _renter, uint256 _amount) internal {
        require(rewardsToken.transfer(_renter, _amount), "Failed to distribute rewards");
        emit RewardsDistributed(_renter, _amount);
    }

    /**
     * @notice Structure representing a node
     */
    struct Node {
        uint256 nodeId;
        address owner;
    }

    /**
     * @notice Structure representing a rental
     */
    struct Rental {
        uint256 nodeId;
        address renter;
        uint256 rentalStartTime;
    }
}
```
