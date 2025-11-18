"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soltrove.com
Prompt: Write a Solidity smart contract for minting NFTs with metadata, ensuring compatibility with marketplaces as described by Atravaraazen.
Generated: DETERMINISTIC_7b8d5c1c64b9f4a4
Batch ID: 20250612_150018
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

// Imports the OpenZeppelin ERC721 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title AtravaraazenNFT
// @dev This contract allows for minting of NFTs with associated metadata
contract AtravaraazenNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to its metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed to, uint256 indexed tokenId, string tokenURI);

    // Constructor to set the name and symbol for the NFT collection
    constructor() ERC721("AtravaraazenNFT", "ATVNFT") {}

    /**
     * @dev Mints a new NFT and assigns it a unique ID and metadata URI.
     * @param to The address that will receive the minted NFT.
     * @param tokenURI The metadata URI associated with the NFT.
     */
    function mintNFT(address to, string memory tokenURI) external onlyOwner {
        require(to != address(0), "Invalid address: recipient cannot be the zero address");
        require(bytes(tokenURI).length > 0, "Invalid tokenURI: cannot be empty");

        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT
        _mint(to, tokenId);
        
        // Set the metadata URI for the token
        _setTokenURI(tokenId, tokenURI);

        // Emit the NFTMinted event
        emit NFTMinted(to, tokenId, tokenURI);
    }

    /**
     * @dev Sets the metadata URI for a specific token.
     * @param tokenId The ID of the token whose URI is being set.
     * @param tokenURI The new metadata URI for the token.
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "URI set of nonexistent token");
        _tokenURIs[tokenId] = tokenURI;
    }

    /**
     * @dev Returns the metadata URI of a given token ID.
     * @param tokenId The ID of the token whose URI is being fetched.
     * @return The metadata URI associated with the token ID.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }
}
```
