"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://e1-9n2.pages.dev
Prompt: Write a Solidity smart contract function to set the price per NFT and ensure it updates correctly when queried.
Generated: DETERMINISTIC_f501eb444e93c5b5
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

/**
 * @title NFTPriceManager
 * @dev A simple contract to manage the price of NFTs.
 */
contract NFTPriceManager {
    // State variable to store the price of the NFT
    uint256 private nftPrice;

    // Address of the contract owner
    address private owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor that sets the initial owner of the contract to the deployer.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to set the price of an NFT.
     * @param _price New price to be set (in wei).
     */
    function setNFTPrice(uint256 _price) external onlyOwner {
        require(_price > 0, "Price must be greater than zero");
        nftPrice = _price;
    }

    /**
     * @dev Function to get the current price of the NFT.
     * @return Current NFT price (in wei).
     */
    function getNFTPrice() external view returns (uint256) {
        return nftPrice;
    }
}
```
