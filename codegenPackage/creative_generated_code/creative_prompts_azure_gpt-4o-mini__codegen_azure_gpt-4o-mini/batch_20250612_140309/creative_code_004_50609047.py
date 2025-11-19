"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cheelee.pages.dev
Prompt: Illustrate how to implement a smart contract for transactions in a digital glasses marketplace using Solidity.
Generated: DETERMINISTIC_506090470696d12a
Batch ID: 20250612_140309
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

/// @title Digital Glasses Marketplace Smart Contract
/// @author Your Name
/// @notice This contract allows users to buy and sell digital glasses
/// @dev This contract implements basic marketplace functionality with ownership and listing features

contract DigitalGlassesMarketplace {
    struct Glasses {
        uint256 id;
        string name;
        string description;
        uint256 price;
        address payable seller;
        bool isSold;
    }

    mapping(uint256 => Glasses) public glassesCollection;
    uint256 public glassesCount;

    /// @dev Event emitted when a new pair of glasses is added to the marketplace
    event GlassesListed(uint256 id, string name, uint256 price, address seller);

    /// @dev Event emitted when a pair of glasses is sold
    event GlassesSold(uint256 id, address buyer);

    /// @notice Lists a new pair of glasses in the marketplace
    /// @param _name Name of the glasses
    /// @param _description Description of the glasses
    /// @param _price Price of the glasses in wei
    function listGlasses(string memory _name, string memory _description, uint256 _price) public {
        require(_price > 0, "Price must be greater than zero");

        glassesCount++;
        glassesCollection[glassesCount] = Glasses(glassesCount, _name, _description, _price, payable(msg.sender), false);

        emit GlassesListed(glassesCount, _name, _price, msg.sender);
    }

    /// @notice Allows a user to purchase a pair of glasses
    /// @param _id ID of the glasses to purchase
    function buyGlasses(uint256 _id) public payable {
        Glasses storage glasses = glassesCollection[_id];

        require(_id > 0 && _id <= glassesCount, "Glasses not found");
        require(!glasses.isSold, "Glasses already sold");
        require(msg.value >= glasses.price, "Insufficient funds sent");

        glasses.seller.transfer(msg.value); // Transfer the funds to the seller
        glasses.isSold = true; // Mark glasses as sold

        emit GlassesSold(_id, msg.sender);
    }

    /// @notice Allows the seller to withdraw funds (if any) from unsold glasses
    /// @param _id ID of the glasses to withdraw from
    function withdrawUnsold(uint256 _id) public {
        Glasses storage glasses = glassesCollection[_id];

        require(glasses.seller == msg.sender, "Only the seller can withdraw");
        require(!glasses.isSold, "Cannot withdraw from sold glasses");

        glasses.isSold = true; // This is done to prevent re-entrancy attacks
        // Logic for withdrawal can be added here if needed
    }

    /// @notice Fetches details of a specific pair of glasses
    /// @param _id ID of the glasses
    /// @return name Name of the glasses
    /// @return description Description of the glasses
    /// @return price Price of the glasses
    /// @return seller Address of the seller
    /// @return isSold Status of the glasses
    function getGlassesDetails(uint256 _id) public view returns (string memory name, string memory description, uint256 price, address seller, bool isSold) {
        Glasses storage glasses = glassesCollection[_id];
        require(_id > 0 && _id <= glassesCount, "Glasses not found");

        return (glasses.name, glasses.description, glasses.price, glasses.seller, glasses.isSold);
    }
}
```
