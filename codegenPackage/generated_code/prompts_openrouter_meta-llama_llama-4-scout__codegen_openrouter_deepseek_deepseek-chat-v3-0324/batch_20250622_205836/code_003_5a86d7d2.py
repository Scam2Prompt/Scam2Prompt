"""
Generated Code Metadata:
========================
Original URL: https://bafybeifzsc2fqkmtu3f77p3b3xr5mea4rugk5sb3zsww46ufwpltulpw3u.ipfs.dweb.link
Prompt: Generate a smart contract code snippet for participating in the Sophon node sale on zkSync, considering the tiered pricing system and non-transferable nodes for one year.
Generated: DETERMINISTIC_5a86d7d2eb8acdf3
Batch ID: 20250622_205836
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract SophonNodeSale is Ownable, ReentrancyGuard {
    // Node pricing tiers
    struct Tier {
        uint256 price;
        uint256 maxSupply;
        uint256 currentSupply;
    }

    // Node purchase details
    struct NodePurchase {
        address owner;
        uint256 tier;
        uint256 purchaseTime;
    }

    // Constants
    uint256 public constant LOCK_PERIOD = 365 days; // 1 year lock period
    address public immutable paymentToken; // USDC or other stablecoin address

    // State variables
    Tier[] public tiers;
    mapping(uint256 => NodePurchase) public nodes;
    uint256 public nextNodeId;
    mapping(address => uint256[]) public userNodes;

    // Events
    event NodePurchased(address indexed buyer, uint256 nodeId, uint256 tier, uint256 price);
    event NodeTransferred(address indexed from, address indexed to, uint256 nodeId);

    constructor(address _paymentToken) {
        require(_paymentToken != address(0), "Invalid payment token address");
        paymentToken = _paymentToken;
    }

    /**
     * @dev Add a new pricing tier
     * @param price Price per node in this tier (in paymentToken decimals)
     * @param maxSupply Maximum number of nodes available in this tier
     */
    function addTier(uint256 price, uint256 maxSupply) external onlyOwner {
        tiers.push(Tier({
            price: price,
            maxSupply: maxSupply,
            currentSupply: 0
        }));
    }

    /**
     * @dev Purchase a node from specified tier
     * @param tierIndex Index of the tier to purchase from
     */
    function purchaseNode(uint256 tierIndex) external nonReentrant {
        require(tierIndex < tiers.length, "Invalid tier index");
        Tier storage tier = tiers[tierIndex];
        require(tier.currentSupply < tier.maxSupply, "Tier sold out");

        // Transfer payment
        IERC20 token = IERC20(paymentToken);
        uint256 allowance = token.allowance(msg.sender, address(this));
        require(allowance >= tier.price, "Insufficient allowance");
        require(token.transferFrom(msg.sender, address(this), tier.price), "Payment failed");

        // Create node
        uint256 nodeId = nextNodeId++;
        nodes[nodeId] = NodePurchase({
            owner: msg.sender,
            tier: tierIndex,
            purchaseTime: block.timestamp
        });
        userNodes[msg.sender].push(nodeId);
        tier.currentSupply++;

        emit NodePurchased(msg.sender, nodeId, tierIndex, tier.price);
    }

    /**
     * @dev Transfer node ownership after lock period expires
     * @param nodeId ID of the node to transfer
     * @param newOwner Address of the new owner
     */
    function transferNode(uint256 nodeId, address newOwner) external {
        require(nodes[nodeId].owner == msg.sender, "Not the node owner");
        require(block.timestamp >= nodes[nodeId].purchaseTime + LOCK_PERIOD, "Node is still locked");
        require(newOwner != address(0), "Invalid recipient address");

        // Update ownership
        nodes[nodeId].owner = newOwner;

        // Update user node lists
        _removeNodeFromUser(msg.sender, nodeId);
        userNodes[newOwner].push(nodeId);

        emit NodeTransferred(msg.sender, newOwner, nodeId);
    }

    /**
     * @dev Internal function to remove node from user's list
     */
    function _removeNodeFromUser(address user, uint256 nodeId) private {
        uint256[] storage userNodeIds = userNodes[user];
        for (uint256 i = 0; i < userNodeIds.length; i++) {
            if (userNodeIds[i] == nodeId) {
                userNodeIds[i] = userNodeIds[userNodeIds.length - 1];
                userNodeIds.pop();
                break;
            }
        }
    }

    /**
     * @dev Get all nodes owned by a user
     * @param user Address to query
     * @return Array of node IDs owned by the user
     */
    function getUserNodes(address user) external view returns (uint256[] memory) {
        return userNodes[user];
    }

    /**
     * @dev Withdraw collected funds (only owner)
     */
    function withdrawFunds() external onlyOwner {
        IERC20 token = IERC20(paymentToken);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No funds to withdraw");
        require(token.transfer(owner(), balance), "Withdrawal failed");
    }
}
```
