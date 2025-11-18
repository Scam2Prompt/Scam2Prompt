"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bobothebear.pages.dev
Prompt: Create a smart contract in Solidity for minting NFTs in the style of the Bobo Council NFT collection, ensuring the total supply is capped at 2,222 as specified on the website.
Generated: DETERMINISTIC_58fe05e6236b842a
Batch ID: 20250612_151158
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

// @title BoboCouncilNFT
// @dev This contract allows for minting of NFTs with a capped supply of 2,222.
//      It inherits from OpenZeppelin's ERC721Enumerable and Ownable contracts.
contract BoboCouncilNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking the total number of minted tokens
    Counters.Counter private _tokenIdCounter;

    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 2222;

    // Mapping from token ID to a boolean indicating if it has been minted
    mapping(uint256 => bool) private _mintedTokens;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed recipient, uint256 indexed tokenId);

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("Bobo Council NFT", "BOBO") {}

    // @dev Mints a new NFT to the specified address
    // @param recipient The address that will receive the minted NFT
    // @return tokenId The ID of the newly minted NFT
    function mintNFT(address recipient) external onlyOwner returns (uint256 tokenId) {
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Maximum supply reached");
        
        tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        // Mint the NFT
        _safeMint(recipient, tokenId);
        _mintedTokens[tokenId] = true;

        // Emit an event for the new NFT minting
        emit NFTMinted(recipient, tokenId);
    }

    // @dev Returns the total supply of minted NFTs
    // @return The total number of minted NFTs
    function totalSupply() public view override returns (uint256) {
        return _tokenIdCounter.current();
    }

    // @dev Checks if a specific token ID has been minted
    // @param tokenId The ID of the token to check
    // @return True if the token has been minted, otherwise false
    function isMinted(uint256 tokenId) external view returns (bool) {
        require(tokenId < MAX_SUPPLY, "Token ID out of range");
        return _mintedTokens[tokenId];
    }

    // @dev Withdraws contract balance to the owner's address
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // @dev Fallback function to accept Ether
    receive() external payable {}
}
```
