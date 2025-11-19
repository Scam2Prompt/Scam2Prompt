"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rapping-planet-prehistoric.on-fleek.app
Prompt: Generate a smart contract in Solidity for minting NFTs in a Web 3.0 environment, specifically for a collection like "Cats World" with unique ownership features.
Generated: DETERMINISTIC_27d324f033d12356
Batch ID: 20250612_164152
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

// Importing OpenZeppelin contracts for ERC721 implementation and utility functions
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CatsWorldNFT
 * @dev A smart contract for minting NFTs in the "Cats World" collection. 
 *      Allows unique ownership of tokens with metadata URI for each NFT.
 */
contract CatsWorldNFT is ERC721URIStorage, Ownable {
    // Counter to keep track of token IDs
    uint256 private _currentTokenId;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    /**
     * @dev Contract constructor that sets the name and symbol of the NFT collection.
     */
    constructor() ERC721("Cats World", "CAT") {
        _currentTokenId = 0; // Initialize token ID counter
    }

    /**
     * @dev Function to mint a new NFT.
     * @param recipient Address that will receive the minted NFT.
     * @param metadataURI URI pointing to the metadata of the NFT.
     * Requirements:
     * - Only the contract owner can mint NFTs.
     */
    function mintNFT(address recipient, string memory metadataURI) external onlyOwner {
        require(recipient != address(0), "Minting to the zero address is not allowed");
        require(bytes(metadataURI).length > 0, "Metadata URI cannot be empty");

        // Increment token ID counter
        _currentTokenId++;

        // Mint the NFT and set its metadata URI
        _safeMint(recipient, _currentTokenId);
        _setTokenURI(_currentTokenId, metadataURI);

        // Emit event for minting activity
        emit NFTMinted(recipient, _currentTokenId, metadataURI);
    }

    /**
     * @dev Function to get the current token ID counter value.
     * @return The latest token ID.
     */
    function getCurrentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }
}
```
