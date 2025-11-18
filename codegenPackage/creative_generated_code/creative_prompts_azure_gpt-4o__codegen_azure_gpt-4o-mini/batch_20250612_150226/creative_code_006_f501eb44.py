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

contract NFTMarketplace {
    // State variable to hold the price per NFT
    uint256 private nftPrice;

    // Event to log price changes
    event NFTPriceUpdated(uint256 oldPrice, uint256 newPrice);

    // Modifier to ensure the price is greater than zero
    modifier validPrice(uint256 _price) {
        require(_price > 0, "Price must be greater than zero");
        _;
    }

    /**
     * @dev Sets the price per NFT.
     * @param _price The new price to be set for each NFT.
     * Emits an {NFTPriceUpdated} event if the price is changed.
     */
    function setNFTPrice(uint256 _price) external validPrice(_price) {
        uint256 oldPrice = nftPrice;
        nftPrice = _price;
        emit NFTPriceUpdated(oldPrice, nftPrice);
    }

    /**
     * @dev Gets the price per NFT.
     * @return The current price of the NFT.
     */
    function getNFTPrice() external view returns (uint256) {
        return nftPrice;
    }
}
```
