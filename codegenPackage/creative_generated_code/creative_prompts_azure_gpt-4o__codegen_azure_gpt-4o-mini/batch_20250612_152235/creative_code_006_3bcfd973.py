"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mintlama.pages.dev
Prompt: Generate code for testing and securing smart contracts for an NFT collection, ensuring compliance with the Cyber Lama roadmap's Phase 2 requirements.
Generated: DETERMINISTIC_3bcfd97360c5224c
Batch ID: 20250612_152235
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

// Import OpenZeppelin's ERC721 implementation for NFT standards
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title CyberLamaNFT
 * @dev Smart contract for Cyber Lama NFT Collection
 * It implements an ERC721 token with enumerable capabilities and owner control.
 */
contract CyberLamaNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Mapping from token ID to the creator's address
    mapping(uint256 => address) private _creators;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed creator, uint256 tokenId);

    /**
     * @dev Constructor to set the name and symbol of the NFT collection
     * @param name The name of the NFT collection
     * @param symbol The symbol of the NFT collection
     * @param baseTokenURI The base URI for the NFT metadata
     */
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Function to mint a new NFT
     * @param to The address to which the NFT will be minted
     * @return The ID of the newly minted token
     */
    function mintNFT(address to) external onlyOwner returns (uint256) {
        require(to != address(0), "Invalid address: zero address");
        
        // Increment the token ID counter
        _tokenIdCounter.increment();
        uint256 newTokenId = _tokenIdCounter.current();
        
        // Mint the token and set the creator
        _mint(to, newTokenId);
        _creators[newTokenId] = msg.sender;

        emit NFTMinted(msg.sender, newTokenId);
        return newTokenId;
    }

    /**
     * @dev Function to get the creator of a specific token
     * @param tokenId The ID of the token
     * @return The address of the token creator
     */
    function getCreator(uint256 tokenId) external view returns (address) {
        require(_exists(tokenId), "Query for nonexistent token");
        return _creators[tokenId];
    }

    /**
     * @dev Override baseURI to return the custom base URI for metadata
     * @return The base URI for the NFT metadata
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Function to set a new base URI for metadata
     * @param baseTokenURI The new base URI
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Function to withdraw contract balance (in native currency, e.g., ETH)
     * Only callable by the contract owner
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        // Transfer the balance to the owner
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Transfer failed");
    }

    /**
     * @dev Fallback function to receive ETH
     */
    receive() external payable {}
}
```
