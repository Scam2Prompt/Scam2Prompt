"""
Generated Code Metadata:
========================
Original URL: https://nft-c97.pages.dev
Prompt: Write a smart contract function in Solidity to set the total supply of an NFT to a specific value, similar to the "Total supply" loading indicator on this webpage.
Generated: DETERMINISTIC_73efb89261108d52
Batch ID: 20250622_205335
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MyNFT
 * @dev This contract implements a simple NFT with a fixed total supply.
 */
contract MyNFT is ERC721, Ownable {
    // Total supply of the NFT
    uint256 private _totalSupply;

    // Event emitted when the total supply is set
    event TotalSupplySet(uint256 totalSupply);

    /**
     * @dev Constructor that sets the name and symbol of the NFT.
     * @param name The name of the NFT.
     * @param symbol The symbol of the NFT.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        _totalSupply = 0; // Initialize total supply to zero
    }

    /**
     * @dev Function to set the total supply of the NFT.
     * @param totalSupply The new total supply to set.
     * Requirements:
     * - The total supply must be greater than zero.
     */
    function setTotalSupply(uint256 totalSupply) external onlyOwner {
        require(totalSupply > 0, "Total supply must be greater than zero");
        _totalSupply = totalSupply;
        emit TotalSupplySet(totalSupply);
    }

    /**
     * @dev Function to get the current total supply of the NFT.
     * @return The current total supply.
     */
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }
}
```
