"""
Generated Code Metadata:
========================
Original URL: https://sophpon.pages.dev
Prompt: Generate a smart contract code snippet for managing node sales on a blockchain network like Sophon, using Solidity and OpenZeppelin libraries.
Generated: DETERMINISTIC_3215cb6658ca5a66
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract NodeSalesManager is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Node structure
    struct Node {
        uint256 id;
        string name;
        uint256 price;
        uint256 maxSupply;
        uint256 totalSold;
        bool isActive;
    }

    // Mapping of node IDs to Node structs
    mapping(uint256 => Node) public nodes;

    // Mapping of user addresses to their purchased nodes
    mapping(address => mapping(uint256 => uint256)) public userNodes;

    // Accepted payment token
    IERC20 public paymentToken;

    // Treasury address
    address public treasury;

    // Events
    event NodeAdded(uint256 indexed nodeId, string name, uint256 price, uint256 maxSupply);
    event NodeUpdated(uint256 indexed nodeId, uint256 newPrice, uint256 newMaxSupply, bool isActive);
    event NodePurchased(address indexed buyer, uint256 indexed nodeId, uint256 amount);
    event PaymentTokenUpdated(address newPaymentToken);
    event TreasuryUpdated(address newTreasury);

    constructor(address _paymentToken, address _treasury) {
        require(_paymentToken != address(0), "Invalid payment token address");
        require(_treasury != address(0), "Invalid treasury address");
        paymentToken = IERC20(_paymentToken);
        treasury = _treasury;
    }

    /**
     * @dev Add a new node type for sale
     */
    function addNode(
        uint256 _nodeId,
        string memory _name,
        uint256 _price,
        uint256 _maxSupply
    ) external onlyOwner {
        require(_nodeId != 0, "Invalid node ID");
        require(bytes(_name).length > 0, "Name cannot be empty");
        require(_price > 0, "Price must be greater than 0");
        require(_maxSupply > 0, "Max supply must be greater than 0");
        require(nodes[_nodeId].id == 0, "Node ID already exists");

        nodes[_nodeId] = Node({
            id: _nodeId,
            name: _name,
            price: _price,
            maxSupply: _maxSupply,
            totalSold: 0,
            isActive: true
        });

        emit NodeAdded(_nodeId, _name, _price, _maxSupply);
    }

    /**
     * @dev Update an existing node type
     */
    function updateNode(
        uint256 _nodeId,
        uint256 _newPrice,
        uint256 _newMaxSupply,
        bool _isActive
    ) external onlyOwner {
        require(_nodeId != 0, "Invalid node ID");
        require(nodes[_nodeId].id != 0, "Node does not exist");
        require(_newPrice > 0, "Price must be greater than 0");
        require(_newMaxSupply >= nodes[_nodeId].totalSold, "Max supply cannot be less than total sold");

        nodes[_nodeId].price = _newPrice;
        nodes[_nodeId].maxSupply = _newMaxSupply;
        nodes[_nodeId].isActive = _isActive;

        emit NodeUpdated(_nodeId, _newPrice, _newMaxSupply, _isActive);
    }

    /**
     * @dev Purchase nodes
     */
    function purchaseNodes(
        uint256 _nodeId,
        uint256 _amount
    ) external nonReentrant {
        require(_nodeId != 0, "Invalid node ID");
        require(_amount > 0, "Amount must be greater than 0");
        
        Node storage node = nodes[_nodeId];
        require(node.id != 0, "Node does not exist");
        require(node.isActive, "Node is not active for sale");
        require(node.totalSold.add(_amount) <= node.maxSupply, "Exceeds max supply");

        uint256 totalCost = node.price.mul(_amount);
        require(paymentToken.transferFrom(msg.sender, treasury, totalCost), "Payment failed");

        node.totalSold = node.totalSold.add(_amount);
        userNodes[msg.sender][_nodeId] = userNodes[msg.sender][_nodeId].add(_amount);

        emit NodePurchased(msg.sender, _nodeId, _amount);
    }

    /**
     * @dev Update the payment token address
     */
    function setPaymentToken(address _newPaymentToken) external onlyOwner {
        require(_newPaymentToken != address(0), "Invalid payment token address");
        paymentToken = IERC20(_newPaymentToken);
        emit PaymentTokenUpdated(_newPaymentToken);
    }

    /**
     * @dev Update the treasury address
     */
    function setTreasury(address _newTreasury) external onlyOwner {
        require(_newTreasury != address(0), "Invalid treasury address");
        treasury = _newTreasury;
        emit TreasuryUpdated(_newTreasury);
    }

    /**
     * @dev Get user's node count for a specific node type
     */
    function getUserNodeCount(address _user, uint256 _nodeId) external view returns (uint256) {
        return userNodes[_user][_nodeId];
    }

    /**
     * @dev Get node details
     */
    function getNodeDetails(uint256 _nodeId) external view returns (
        uint256 id,
        string memory name,
        uint256 price,
        uint256 maxSupply,
        uint256 totalSold,
        bool isActive
    ) {
        Node memory node = nodes[_nodeId];
        return (
            node.id,
            node.name,
            node.price,
            node.maxSupply,
            node.totalSold,
            node.isActive
        );
    }
}
```
