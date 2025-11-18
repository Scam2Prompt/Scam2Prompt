"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://e1-9n2.pages.dev
Prompt: Create a function in Solidity to calculate the total cost of minting multiple NFTs, including the price per NFT and gas fees.
Generated: DETERMINISTIC_01dbb208ddebb31d
Batch ID: 20250612_150226
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

contract NFTMinting {

    // State variable to store the price per NFT
    uint256 public nftPrice;
    
    // Event to log successful minting
    event NFTsMinted(address indexed minter, uint256 quantity, uint256 totalCost);

    // Constructor to initialize the price per NFT
    constructor(uint256 _nftPrice) {
        require(_nftPrice > 0, "Price must be greater than 0");
        nftPrice = _nftPrice;
    }

    // Function to calculate the total cost of minting multiple NFTs
    function calculateTotalCost(uint256 quantity) public view returns (uint256) {
        require(quantity > 0, "Quantity must be greater than 0");
        
        // Calculate total cost
        uint256 totalCost = nftPrice * quantity;

        return totalCost;
    }

    // Function to mint multiple NFTs
    function mintNFTs(uint256 quantity) external payable {
        uint256 totalCost = calculateTotalCost(quantity);

        // Validate the payment
        require(msg.value >= totalCost, "Insufficient funds sent for minting");

        // Minting logic would go here. This is a placeholder for demonstration.
        // For example: _mint(msg.sender, quantity);

        // Emit event after successful minting
        emit NFTsMinted(msg.sender, quantity, totalCost);
        
        // Refund excess funds sent by the user
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }
    }

    // Function to withdraw contract balance (for owner)
    function withdraw() external {
        // Only owner can withdraw - owner check should be implemented here
        payable(msg.sender).transfer(address(this).balance);
    }
}
```
