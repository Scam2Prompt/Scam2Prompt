"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-kzna.com
Prompt: What are the steps to implement a free mint feature for 555 unique items on the Ethereum blockchain, inspired by the KZNA Brave Wallet's offerings?
Generated: DETERMINISTIC_7ea3cbb0457ec56a
Batch ID: 20250612_160946
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title Free Minting for Unique NFTs
/// @notice This contract allows users to mint 555 unique NFTs for free
contract FreeMintNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking the current token ID
    Counters.Counter private _tokenIdCounter;

    // Maximum number of unique items
    uint256 public constant MAX_SUPPLY = 555;

    // Mapping to track whether an address has already minted
    mapping(address => bool) public hasMinted;

    // Event emitted when an NFT is minted
    event Minted(address indexed to, uint256 indexed tokenId);

    constructor() ERC721("FreeMintNFT", "FMNFT") {}

    /// @notice Function to mint a new NFT
    /// @dev Reverts if max supply is reached or if the sender has already minted an NFT
    function mint() external {
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");
        require(!hasMinted[msg.sender], "You have already minted an NFT");

        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT to the sender
        _mint(msg.sender, tokenId);
        
        // Mark the sender as having minted
        hasMinted[msg.sender] = true;

        // Emit the minting event
        emit Minted(msg.sender, tokenId);
    }

    /// @notice Function to check the current token ID counter
    /// @return uint256 Current token ID counter
    function currentTokenId() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
