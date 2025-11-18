"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abstract-9fmrav.testnet.nfts2.me
Prompt: Generate a smart contract example for minting NFTs on the Abstract Testnet, ensuring compatibility with NFTs2Me tools.
Generated: DETERMINISTIC_7ec7d5a9b2bbb90d
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

/**
 * @title SimpleNFT
 * @dev A smart contract to mint NFTs on the Abstract Testnet, compatible with NFTs2Me tools.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract SimpleNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter to track the token IDs
    Counters.Counter private _tokenIds;

    // Base URI for the metadata
    string private _baseURIExtended;

    /**
     * @dev Constructor to initialize the NFT contract.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Function to set the base URI for the metadata.
     * @param baseURI_ The base URI string.
     */
    function setBaseURI(string memory baseURI_) external onlyOwner {
        _baseURIExtended = baseURI_;
    }

    /**
     * @dev Overrides the _baseURI function from ERC721 to return the custom base URI.
     * @return Base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseURIExtended;
    }

    /**
     * @dev Function to mint a new NFT.
     * @param to The address that will receive the NFT.
     * @return The ID of the minted token.
     */
    function mintNFT(address to) external onlyOwner returns (uint256) {
        require(to != address(0), "Cannot mint to zero address");

        // Increment the token ID counter
        _tokenIds.increment();

        uint256 newTokenId = _tokenIds.current();

        // Mint the token
        _safeMint(to, newTokenId);

        return newTokenId;
    }

    /**
     * @dev Function to get the current token supply.
     * @return The total number of minted tokens.
     */
    function totalSupply() external view returns (uint256) {
        return _tokenIds.current();
    }
}
```

This contract uses OpenZeppelin libraries for standard NFT functionality, ensuring compatibility and best practices.
