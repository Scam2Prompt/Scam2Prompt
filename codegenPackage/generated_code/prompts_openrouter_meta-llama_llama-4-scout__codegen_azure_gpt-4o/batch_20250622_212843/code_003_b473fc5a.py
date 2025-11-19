"""
Generated Code Metadata:
========================
Original URL: https://galxestargatoronft.com
Prompt: Generate a smart contract code for a simple NFT minting process similar to Galxe Stargator's campaign on Optimism Network.
Generated: DETERMINISTIC_b473fc5a132f96f7
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SimpleNFT
 * @dev A smart contract for minting NFTs on the Optimism network.
 *      This contract follows ERC721 standards and includes basic minting functionality.
 */

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract SimpleNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter to keep track of token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Maximum supply of NFTs
    uint256 public maxSupply;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed recipient, uint256 tokenId);

    /**
     * @dev Constructor to initialize the contract.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     * @param baseTokenURI Base URI for the metadata.
     * @param _maxSupply Maximum number of NFTs that can be minted.
     */
    constructor(
        string memory name,
        string memory symbol,
        string memory baseTokenURI,
        uint256 _maxSupply
    ) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
        maxSupply = _maxSupply;
    }

    /**
     * @dev Function to mint a new NFT.
     * @param recipient Address to receive the minted NFT.
     */
    function mint(address recipient) external onlyOwner {
        require(_tokenIdCounter.current() < maxSupply, "Max supply reached");

        // Increment the token ID counter
        _tokenIdCounter.increment();

        // Get the new token ID
        uint256 newTokenId = _tokenIdCounter.current();

        // Mint the NFT to the recipient
        _safeMint(recipient, newTokenId);

        // Emit the minting event
        emit NFTMinted(recipient, newTokenId);
    }

    /**
     * @dev Override the _baseURI function to return the base URI.
     * @return Base URI for the metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Function to update the base URI for metadata.
     * @param newBaseURI New base URI to set.
     */
    function setBaseURI(string memory newBaseURI) external onlyOwner {
        _baseTokenURI = newBaseURI;
    }

    /**
     * @dev Function to get the current token ID counter.
     * @return Current token ID counter.
     */
    function currentTokenId() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
