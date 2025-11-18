"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abstractdog.testnet.nfts2.me
Prompt: Write a smart contract for minting abstract art-inspired dog meme NFTs on the Abstract Testnet, compatible with NFTs2Me.com.
Generated: DETERMINISTIC_656ea9c671dd39c6
Batch ID: 20250612_155102
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

// Import OpenZeppelin's ERC721 implementation and helpers
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// AbstractArtDogNFT is a contract for minting dog meme NFTs inspired by abstract art
contract AbstractArtDogNFT is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;

    // Counter to keep track of token IDs
    Counters.Counter private _tokenIds;

    // Base URI for metadata
    string private _baseTokenURI;

    /**
     * @dev Constructor to initialize the token name and symbol.
     * @param baseTokenURI Base URI for NFT metadata.
     */
    constructor(string memory baseTokenURI) ERC721("AbstractArtDogNFT", "AADOG") {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Function to mint a new NFT.
     * @param recipient Address of the NFT recipient.
     * @param tokenURI Metadata URI specific to the NFT being minted.
     */
    function mintNFT(address recipient, string memory tokenURI) external onlyOwner {
        // Increment the token ID
        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();

        // Mint the NFT
        _mint(recipient, newTokenId);

        // Set the token URI for metadata
        _setTokenURI(newTokenId, tokenURI);
    }

    /**
     * @dev Function to set the base URI for NFT metadata.
     * @param baseTokenURI New base URI.
     */
    function setBaseTokenURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Override the baseURI function to use the custom baseTokenURI.
     * @return The base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }
}
```
