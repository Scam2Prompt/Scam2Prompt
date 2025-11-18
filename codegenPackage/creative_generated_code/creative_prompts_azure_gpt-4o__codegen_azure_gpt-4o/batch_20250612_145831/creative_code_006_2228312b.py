"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soonverse.pages.dev
Prompt: Generate a smart contract in Solidity that supports NFT integration for Web3 games, ensuring compatibility with the SoonVerse ecosystem.
Generated: DETERMINISTIC_2228312b6123bc1d
Batch ID: 20250612_145831
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
 * @title GameNFT
 * @dev Smart contract for managing NFTs in Web3 games.
 * Compatible with the SoonVerse ecosystem.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract GameNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Mapping to store additional metadata for NFTs (game-specific properties)
    mapping(uint256 => string) public tokenProperties;

    /**
     * @dev Constructor initializes the contract with a name and symbol.
     * @param name Name of the NFT collection.
     * @param symbol Symbol for the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Function to mint a new NFT.
     * @param to Address to receive the NFT.
     * @param properties Metadata or attributes associated with the NFT (game-specific).
     */
    function mintNFT(address to, string memory properties) external onlyOwner {
        // Increment the token ID counter
        _tokenIdCounter.increment();

        // Get the new token ID
        uint256 tokenId = _tokenIdCounter.current();

        // Mint the NFT
        _mint(to, tokenId);

        // Set game-specific properties for the token
        tokenProperties[tokenId] = properties;

        emit Minted(to, tokenId, properties);
    }

    /**
     * @dev Set the base URI for the contract.
     * @param baseURI The base URI to be used in metadata.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Override _baseURI to return the base URI set by the owner.
     * @return Base URI for token metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Burn a token (if needed for game mechanics).
     * @param tokenId ID of the token to be burned.
     */
    function burnNFT(uint256 tokenId) external {
        // Check ownership
        require(ownerOf(tokenId) == msg.sender, "You are not the owner of this token");

        // Burn the token
        _burn(tokenId);

        // Delete the token properties
        delete tokenProperties[tokenId];

        emit Burned(msg.sender, tokenId);
    }

    // Events for minting and burning NFTs
    event Minted(address indexed to, uint256 indexed tokenId, string properties);
    event Burned(address indexed by, uint256 indexed tokenId);

    /**
     * @dev Returns the properties associated with a specific token ID.
     * @param tokenId ID of the token to query.
     * @return Properties of the token.
     */
    function getTokenProperties(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return tokenProperties[tokenId];
    }

    /**
     * @dev Error handling for invalid token ID.
     */
    modifier validTokenId(uint256 tokenId) {
        require(_exists(tokenId), "Invalid token ID");
        _;
    }
}
```

Make sure to install the OpenZeppelin library when compiling and deploying this contract. Example installation: `npm install @openzeppelin/contracts`.
