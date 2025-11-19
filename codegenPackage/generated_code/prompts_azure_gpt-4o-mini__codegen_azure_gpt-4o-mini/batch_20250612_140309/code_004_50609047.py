"""
Generated Code Metadata:
========================
Original URL: https://cheelee.pages.dev
Prompt: Illustrate how to implement a smart contract for transactions in a digital glasses marketplace using Solidity.
Generated: DETERMINISTIC_506090470696d12a
Batch ID: 20250612_140309
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

/// @title Digital Glasses Marketplace Smart Contract
/// @author Your Name
/// @notice This contract allows users to buy and sell digital glasses
/// @dev This contract implements basic functionalities for a marketplace

contract DigitalGlassesMarketplace {
    // Struct to represent a digital glass item
    struct Glass {
        uint256 id;
        string name;
        string description;
        uint256 price;
        address payable seller;
        bool isSold;
    }

    // Mapping to store glasses by their ID
    mapping(uint256 => Glass) public glasses;
    // Counter for generating unique IDs for glasses
    uint256 public glassesCount;

    // Event emitted when a new glass is listed
    event GlassListed(uint256 id, string name, uint256 price, address seller);
    // Event emitted when a glass is sold
    event GlassSold(uint256 id, address buyer);

    /// @notice List a new digital glass for sale
    /// @param _name The name of the glass
    /// @param _description The description of the glass
    /// @param _price The price of the glass in wei
    function listGlass(string memory _name, string memory _description, uint256 _price) public {
        require(_price > 0, "Price must be greater than zero");

        // Increment the glass count to get a new ID
        glassesCount++;
        // Create a new glass item
        glasses[glassesCount] = Glass(glassesCount, _name, _description, _price, payable(msg.sender), false);

        // Emit an event for the new listing
        emit GlassListed(glassesCount, _name, _price, msg.sender);
    }

    /// @notice Buy a digital glass
    /// @param _id The ID of the glass to buy
    function buyGlass(uint256 _id) public payable {
        Glass storage glass = glasses[_id];

        // Ensure the glass exists and is not already sold
        require(glass.id > 0 && glass.id <= glassesCount, "Glass does not exist");
        require(!glass.isSold, "Glass is already sold");
        require(msg.value >= glass.price, "Insufficient funds sent");

        // Mark the glass as sold
        glass.isSold = true;
        // Transfer the funds to the seller
        glass.seller.transfer(msg.value);

        // Emit an event for the sale
        emit GlassSold(_id, msg.sender);
    }

    /// @notice Get details of a glass by its ID
    /// @param _id The ID of the glass
    /// @return The details of the glass
    function getGlass(uint256 _id) public view returns (Glass memory) {
        require(_id > 0 && _id <= glassesCount, "Glass does not exist");
        return glasses[_id];
    }
}
```
