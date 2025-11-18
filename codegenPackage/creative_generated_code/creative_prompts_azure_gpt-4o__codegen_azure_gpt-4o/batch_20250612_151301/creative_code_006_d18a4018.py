"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somnia.pages.dev
Prompt: Generate a Solidity contract that leverages Somnia's blockchain to mint and transfer NFTs with interoperability across metaverses.
Generated: DETERMINISTIC_d18a40187dad6c7d
Batch ID: 20250612_151301
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

// Importing OpenZeppelin libraries for ERC721 standard and utility functions.
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title SomniaNFT
 * @dev A contract for minting and transferring NFTs with interoperability across metaverses.
 * Implements the ERC721 standard and includes functionality for metadata management.
 */
contract SomniaNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for unique token IDs.
    Counters.Counter private _tokenIdCounter;

    // Mapping to store metadata for interoperability across metaverses.
    mapping(uint256 => string) private _tokenURIs;

    // Events
    event Minted(address indexed owner, uint256 indexed tokenId, string tokenURI);
    event Transferred(address indexed from, address indexed to, uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the contract with a name and symbol for the NFT collection.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT with metadata for metaverse interoperability.
     * @param to The address of the recipient to whom the NFT will be minted.
     * @param tokenURI The URI pointing to the metadata of the NFT.
     */
    function mint(address to, string memory tokenURI) external onlyOwner {
        require(to != address(0), "Invalid address: Cannot mint to zero address");
        require(bytes(tokenURI).length > 0, "Invalid tokenURI: Cannot be empty");

        // Increment the token counter for a unique ID.
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        // Mint the token to the specified address.
        _safeMint(to, tokenId);

        // Set the token's metadata URI.
        _setTokenURI(tokenId, tokenURI);

        // Emit a Minted event.
        emit Minted(to, tokenId, tokenURI);
    }

    /**
     * @dev Override the base ERC721 tokenURI function to return the custom metadata URI.
     * @param tokenId The ID of the token to fetch the metadata URI for.
     * @return The metadata URI linked to the specified tokenId.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Internal function to set the token's metadata URI.
     * @param tokenId The ID of the token to set the metadata URI for.
     * @param tokenURI_ The URI pointing to the metadata of the token.
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI_) internal {
        _tokenURIs[tokenId] = tokenURI_;
    }

    /**
     * @dev Transfer an NFT from one address to another.
     * @param from The address transferring the NFT.
     * @param to The address receiving the NFT.
     * @param tokenId The ID of the token being transferred.
     * Note: This function uses ERC721's transferFrom implementation.
     */
    function transfer(address from, address to, uint256 tokenId) external {
        require(to != address(0), "Invalid address: Cannot transfer to zero address");
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner nor approved");

        // Transfer the token.
        transferFrom(from, to, tokenId);

        // Emit a Transferred event.
        emit Transferred(from, to, tokenId);
    }

    /**
     * @dev Get the current total supply of minted tokens.
     * @return The total number of tokens that have been minted.
     */
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
