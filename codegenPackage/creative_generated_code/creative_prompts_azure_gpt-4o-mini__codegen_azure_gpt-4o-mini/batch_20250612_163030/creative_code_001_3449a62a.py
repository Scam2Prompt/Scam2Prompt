"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnm-io.web.app
Prompt: Write a code snippet to implement the 'Fractal Box' protocol for customizable Mystery Boxes in a Web3 application.
Generated: DETERMINISTIC_3449a62ab84fb949
Batch ID: 20250612_163030
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Interface for the Mystery Box
interface IMysteryBox {
    function createBox(string memory _name, string memory _description, uint256 _price, uint256 _maxSupply) external;
    function purchaseBox(uint256 _boxId) external payable;
    function openBox(uint256 _boxId) external returns (uint256[] memory);
}

// Implementation of the Fractal Box protocol
contract FractalBox is IMysteryBox, Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a Mystery Box
    struct MysteryBox {
        string name;
        string description;
        uint256 price;
        uint256 maxSupply;
        uint256 currentSupply;
        bool isActive;
    }

    // Mapping to store all created Mystery Boxes
    mapping(uint256 => MysteryBox) private boxes;
    // Counter to track box IDs
    Counters.Counter private boxIdCounter;

    // Event to emit when a new box is created
    event BoxCreated(uint256 indexed boxId, string name, string description, uint256 price, uint256 maxSupply);
    // Event to emit when a box is purchased
    event BoxPurchased(uint256 indexed boxId, address indexed buyer);
    // Event to emit when a box is opened
    event BoxOpened(uint256 indexed boxId, uint256[] rewards);

    // Function to create a new Mystery Box
    function createBox(string memory _name, string memory _description, uint256 _price, uint256 _maxSupply) external onlyOwner {
        require(_maxSupply > 0, "Max supply must be greater than zero");
        require(_price > 0, "Price must be greater than zero");

        uint256 currentBoxId = boxIdCounter.current();
        boxes[currentBoxId] = MysteryBox({
            name: _name,
            description: _description,
            price: _price,
            maxSupply: _maxSupply,
            currentSupply: 0,
            isActive: true
        });

        boxIdCounter.increment();
        emit BoxCreated(currentBoxId, _name, _description, _price, _maxSupply);
    }

    // Function to purchase a Mystery Box
    function purchaseBox(uint256 _boxId) external payable override {
        MysteryBox storage box = boxes[_boxId];
        
        require(box.isActive, "Box is not active");
        require(msg.value == box.price, "Incorrect payment amount");
        require(box.currentSupply < box.maxSupply, "Max supply reached");

        box.currentSupply++;
        emit BoxPurchased(_boxId, msg.sender);
    }

    // Function to open a purchased Mystery Box
    function openBox(uint256 _boxId) external override returns (uint256[] memory) {
        MysteryBox storage box = boxes[_boxId];
        
        require(box.currentSupply > 0, "No boxes to open");
        
        // Generate random rewards (for demonstration, we are using a simple example)
        uint256[] memory rewards = new uint256[](3);
        for (uint256 i = 0; i < 3; i++) {
            rewards[i] = uint256(keccak256(abi.encodePacked(block.timestamp, msg.sender, i))) % 1000; // Random reward id
        }

        emit BoxOpened(_boxId, rewards);
        return rewards;
    }

    // Function to deactivate a box (onlyOwner)
    function deactivateBox(uint256 _boxId) external onlyOwner {
        MysteryBox storage box = boxes[_boxId];
        box.isActive = false;
    }
}
```
