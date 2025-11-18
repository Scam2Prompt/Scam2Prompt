"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerobeings.app
Prompt: Generate a Solidity contract template for an NFT project that adheres to CC0 licensing, as referenced by "Zero Beings."
Generated: DETERMINISTIC_09b55de19de3067b
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: CC0-1.0
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title Zero Beings NFT Contract
/// @notice This contract implements a simple NFT with CC0 licensing.
contract ZeroBeings is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Variable to keep track of the token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event to emit when the base URI is updated
    event BaseURIUpdated(string newBaseURI);

    /// @notice Constructor to initialize the contract
    /// @param name The name of the NFT collection
    /// @param symbol The symbol for the NFT collection
    /// @param baseURI The initial base URI for metadata
    constructor(string memory name, string memory symbol, string memory baseURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseURI;
    }

    /// @notice Mint a new NFT to the specified address
    /// @param to The address to receive the newly minted NFT
    /// @dev Only the contract owner can mint new tokens
    function mint(address to) external onlyOwner {
        require(to != address(0), "Cannot mint to zero address");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
    }

    /// @notice Set the base URI for the metadata
    /// @param baseURI The new base URI for metadata
    /// @dev Only the contract owner can update the base URI
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
        emit BaseURIUpdated(baseURI);
    }

    /// @notice Override base URI for retrieving metadata
    /// @return The base URI for the token metadata
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /// @notice Return the total supply of minted NFTs
    /// @return The total number of NFTs minted
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    /// @notice Withdraws contract balance to owner
    /// @dev Only the contract owner can withdraw funds
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        
        // Transfer the balance to the owner
        payable(owner()).transfer(balance);
    }

    /// @notice Fallback function to receive Ether
    receive() external payable {}
}
```
