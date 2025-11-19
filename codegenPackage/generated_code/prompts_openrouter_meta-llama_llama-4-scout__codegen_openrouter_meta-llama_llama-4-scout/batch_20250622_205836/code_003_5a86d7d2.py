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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title SophonNodeSale
 * @author [Your Name]
 * @notice Smart contract for participating in the Sophon node sale on zkSync.
 */
contract SophonNodeSale is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of node tiers and their respective prices
    mapping(uint8 => uint256) public tierPrices;

    // Mapping of node buyers and their node details
    mapping(address => Node) public nodeBuyers;

    // Total number of nodes sold
    uint256 public totalNodesSold;

    // Timestamp for node transferability (1 year from deployment)
    uint256 public transferabilityTimestamp;

    // Sophon token contract
    IERC20 public sophonToken;

    // zkSync node sale address
    address public zkSyncNodeSaleAddress;

    // Event emitted when a node is purchased
    event NodePurchased(address indexed buyer, uint8 tier);

    // Event emitted when node transferability is enabled
    event TransferabilityEnabled();

    // Struct to represent a node's details
    struct Node {
        uint8 tier;
        uint256 purchaseTimestamp;
    }

    /**
     * @dev Constructor for the SophonNodeSale contract.
     * @param _sophonToken Address of the Sophon token contract.
     * @param _zkSyncNodeSaleAddress Address of the zkSync node sale.
     */
    constructor(address _sophonToken, address _zkSyncNodeSaleAddress) public {
        sophonToken = IERC20(_sophonToken);
        zkSyncNodeSaleAddress = _zkSyncNodeSaleAddress;

        // Initialize tier prices (example prices, adjust according to the tiered pricing system)
        tierPrices[1] = 1000 ether; // Tier 1 price
        tierPrices[2] = 5000 ether; // Tier 2 price
        tierPrices[3] = 10000 ether; // Tier 3 price

        // Set node transferability timestamp (1 year from deployment)
        transferabilityTimestamp = block.timestamp.add(365 days);
    }

    /**
     * @dev Purchase a node.
     * @param _tier The tier of the node to purchase.
     */
    function purchaseNode(uint8 _tier) external nonReentrant {
        // Check if the tier price exists
        require(tierPrices[_tier] > 0, "Tier price does not exist");

        // Check if the buyer has sufficient Sophon tokens
        require(sophonToken.balanceOf(msg.sender) >= tierPrices[_tier], "Insufficient Sophon tokens");

        // Check if the buyer already owns a node
        require(nodeBuyers[msg.sender].purchaseTimestamp == 0, "Buyer already owns a node");

        // Transfer Sophon tokens to the zkSync node sale address
        sophonToken.transferFrom(msg.sender, zkSyncNodeSaleAddress, tierPrices[_tier]);

        // Update node buyer details
        nodeBuyers[msg.sender] = Node(_tier, block.timestamp);
        totalNodesSold++;

        // Emit NodePurchased event
        emit NodePurchased(msg.sender, _tier);
    }

    /**
     * @dev Enable node transferability.
     */
    function enableTransferability() external {
        // Check if the transferability timestamp has been reached
        require(block.timestamp >= transferabilityTimestamp, "Transferability not yet enabled");

        // Emit TransferabilityEnabled event
        emit TransferabilityEnabled();
    }

    /**
     * @dev Transfer a node.
     * @param _to The address to transfer the node to.
     */
    function transferNode(address _to) external {
        // Check if node transferability is enabled
        require(block.timestamp >= transferabilityTimestamp, "Node transferability not yet enabled");

        // Check if the sender owns a node
        require(nodeBuyers[msg.sender].purchaseTimestamp > 0, "Sender does not own a node");

        // Transfer node ownership to the recipient
        nodeBuyers[_to] = nodeBuyers[msg.sender];
        nodeBuyers[msg.sender].purchaseTimestamp = 0;
    }
}
```
