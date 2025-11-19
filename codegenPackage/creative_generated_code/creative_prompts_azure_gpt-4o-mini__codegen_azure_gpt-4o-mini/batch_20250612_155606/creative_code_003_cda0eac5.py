"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnm-rectify-presale-url.pages.dev
Prompt: Provide an example of how to implement a Mystery Box feature in a decentralized application using the principles outlined in the EARN'Mopoly section.
Generated: DETERMINISTIC_cda0eac5cdf29c76
Batch ID: 20250612_155606
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MysteryBox
 * @dev Smart contract to manage the Mystery Box feature in a decentralized application.
 */
contract MysteryBox is Ownable {
    // State variables
    IERC20 public token; // The ERC20 token used for purchasing mystery boxes
    uint256 public boxPrice; // Price of a single mystery box
    uint256 public totalBoxes; // Total number of mystery boxes created
    uint256 public boxCounter; // Counter for the number of boxes sold

    // Events
    event BoxPurchased(address indexed buyer, uint256 boxId);
    event BoxPriceUpdated(uint256 newPrice);
    event BoxesCreated(uint256 totalBoxes);

    // Struct to represent a Mystery Box
    struct MysteryBoxDetails {
        uint256 id;
        string contents; // Placeholder for contents, can be replaced with a more complex structure
        bool exists; // Check if the box exists
    }

    mapping(uint256 => MysteryBoxDetails) public boxes; // Mapping of box IDs to their details

    /**
     * @dev Constructor to initialize the contract with token address and box price.
     * @param _token The address of the ERC20 token.
     * @param _boxPrice The price for purchasing a mystery box.
     */
    constructor(IERC20 _token, uint256 _boxPrice) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_boxPrice > 0, "Box price must be greater than zero");
        
        token = _token;
        boxPrice = _boxPrice;
    }

    /**
     * @dev Allows the owner to update the box price.
     * @param _newPrice The new price for the mystery box.
     */
    function updateBoxPrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "New price must be greater than zero");
        boxPrice = _newPrice;
        emit BoxPriceUpdated(_newPrice);
    }

    /**
     * @dev Allows the owner to create a specified number of mystery boxes with unique contents.
     * @param _totalBoxes The number of mystery boxes to create.
     * @param _contents Array of contents for each mystery box.
     */
    function createBoxes(uint256 _totalBoxes, string[] calldata _contents) external onlyOwner {
        require(_totalBoxes == _contents.length, "Contents length must match the number of boxes");
        
        for (uint256 i = 0; i < _totalBoxes; i++) {
            totalBoxes++;
            boxes[totalBoxes] = MysteryBoxDetails(totalBoxes, _contents[i], true);
        }

        emit BoxesCreated(totalBoxes);
    }

    /**
     * @dev Allows users to purchase a mystery box.
     */
    function purchaseBox() external {
        require(boxCounter < totalBoxes, "No more boxes available");
        
        // Transfer tokens from buyer to the contract
        bool success = token.transferFrom(msg.sender, address(this), boxPrice);
        require(success, "Token transfer failed");

        // Increment the box counter and emit an event
        boxCounter++;
        emit BoxPurchased(msg.sender, boxCounter);
    }

    /**
     * @dev Allows the owner to withdraw collected tokens from the contract.
     */
    function withdrawTokens() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        
        bool success = token.transfer(owner(), balance);
        require(success, "Token withdrawal failed");
    }
}
```
