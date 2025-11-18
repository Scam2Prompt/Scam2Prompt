"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://be-solana-methods-v1.docs-62t.pages.dev
Prompt: Generate a decentralized supply chain management smart contract using Código's CIDL, ensuring compatibility with Solana and including event definitions for tracking goods.
Generated: DETERMINISTIC_b766027f6c77fc00
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cidl
// SPDX-License-Identifier: MIT
// Smart contract for decentralized supply chain management on Solana

contract SupplyChainManagement {

    // Event definitions
    event GoodsAdded(uint256 indexed goodsId, string name, string origin);
    event GoodsShipped(uint256 indexed goodsId, string destination);
    event GoodsReceived(uint256 indexed goodsId, address indexed recipient);

    // Structure to hold goods information
    struct Goods {
        uint256 id;
        string name;
        string origin;
        string currentStatus;
        address currentOwner;
    }

    // Mapping to store goods using their ID
    mapping(uint256 => Goods) private goodsRegistry;
    uint256 private nextGoodsId;

    // Constructor to initialize the contract
    constructor() {
        nextGoodsId = 1; // Start goods ID from 1
    }

    // Function to add new goods to the supply chain
    // Emits GoodsAdded event
    function addGoods(string memory _name, string memory _origin) public {
        Goods memory newGoods = Goods({
            id: nextGoodsId,
            name: _name,
            origin: _origin,
            currentStatus: "Created",
            currentOwner: msg.sender
        });

        goodsRegistry[nextGoodsId] = newGoods;
        emit GoodsAdded(nextGoodsId, _name, _origin);
        nextGoodsId++;
    }

    // Function to ship goods
    // Emits GoodsShipped event
    function shipGoods(uint256 _goodsId, string memory _destination) public {
        require(goodsRegistry[_goodsId].currentOwner == msg.sender, "You are not the owner of these goods.");
        
        // Update the current status and owner
        goodsRegistry[_goodsId].currentStatus = "Shipped";
        goodsRegistry[_goodsId].currentOwner = address(0); // Ownership transferred to the system

        emit GoodsShipped(_goodsId, _destination);
    }

    // Function to receive goods
    // Emits GoodsReceived event
    function receiveGoods(uint256 _goodsId) public {
        require(goodsRegistry[_goodsId].currentOwner == address(0), "Goods are not in transit.");

        // Update the current status and owner
        goodsRegistry[_goodsId].currentStatus = "Received";
        goodsRegistry[_goodsId].currentOwner = msg.sender;

        emit GoodsReceived(_goodsId, msg.sender);
    }

    // Function to get goods details
    function getGoods(uint256 _goodsId) public view returns (uint256, string memory, string memory, string memory, address) {
        Goods storage goods = goodsRegistry[_goodsId];
        return (goods.id, goods.name, goods.origin, goods.currentStatus, goods.currentOwner);
    }
}
```
