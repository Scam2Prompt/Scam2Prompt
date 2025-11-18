"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftnovamarket.com
Prompt: Create a smart contract in Solidity for minting NFTs that aligns with Nftnovamarket's roadmap phase 04, ensuring blockchain verification and secure ownership.
Generated: DETERMINISTIC_39541482c18115b0
Batch ID: 20250612_151626
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

// Importing the ERC721 standard interface
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title NFTMinting
 * @dev Smart contract for minting NFTs with ownership verification.
 */
contract NFTMinting is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for generating unique token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed to, uint256 tokenId);

    /**
     * @dev Constructor to initialize the NFT contract with a name and symbol.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     * @param baseURI The base URI for the NFT metadata.
     */
    constructor(string memory name, string memory symbol, string memory baseURI) 
        ERC721(name, symbol) {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Function to mint a new NFT.
     * @param to The address that will own the minted NFT.
     * Requires that `to` is not the zero address.
     */
    function mintNFT(address to) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");

        // Increment the token ID for the new NFT
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        // Mint the NFT and assign it to the recipient
        _mint(to, tokenId);
        
        // Emit the NFTMinted event
        emit NFTMinted(to, tokenId);
    }

    /**
     * @dev Override the base URI for the NFT metadata.
     * @return The base URI as a string.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Function to update the base URI for NFT metadata.
     * @param baseURI The new base URI for the NFT metadata.
     * Only callable by the contract owner.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Function to withdraw funds from the contract (if applicable).
     * Only callable by the contract owner.
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
