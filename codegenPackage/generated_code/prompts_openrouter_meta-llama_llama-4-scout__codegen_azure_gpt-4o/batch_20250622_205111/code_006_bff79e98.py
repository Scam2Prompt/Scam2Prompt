"""
Generated Code Metadata:
========================
Original URL: https://opsecintergrateddevblock.pages.dev
Prompt: Design a code solution to address NFT minting and transfer issues on various blockchain networks, such as Ethereum and Polygon, using the decentralized protocol.
Generated: DETERMINISTIC_bff79e982fbcb52e
Batch ID: 20250622_205111
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
 * @title NFTMintAndTransfer
 * @dev A contract for minting and transferring NFTs on Ethereum and Polygon networks.
 *      This contract follows ERC721 standards and includes error handling for production readiness.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract NFTMintAndTransfer is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter to keep track of token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed to, uint256 indexed tokenId);

    // Event emitted when an NFT is transferred
    event NFTTransferred(address indexed from, address indexed to, uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     * @param baseURI Base URI for the metadata.
     */
    constructor(string memory name, string memory symbol, string memory baseURI) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Function to mint a new NFT.
     * @param to Address to receive the minted NFT.
     * @return tokenId The ID of the newly minted NFT.
     */
    function mintNFT(address to) external onlyOwner returns (uint256) {
        require(to != address(0), "Invalid address: cannot mint to the zero address");

        // Increment the token ID counter
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        // Mint the NFT
        _safeMint(to, tokenId);

        // Emit the minting event
        emit NFTMinted(to, tokenId);

        return tokenId;
    }

    /**
     * @dev Function to transfer an NFT from one address to another.
     * @param from Address of the current owner of the NFT.
     * @param to Address to receive the NFT.
     * @param tokenId ID of the NFT to transfer.
     */
    function transferNFT(address from, address to, uint256 tokenId) external {
        require(to != address(0), "Invalid address: cannot transfer to the zero address");
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner nor approved");

        // Transfer the NFT
        _transfer(from, to, tokenId);

        // Emit the transfer event
        emit NFTTransferred(from, to, tokenId);
    }

    /**
     * @dev Override the base URI function to return the custom base URI.
     * @return Base URI for the metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Function to update the base URI for metadata.
     * @param baseURI New base URI.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Function to retrieve the current token ID counter value.
     * @return Current token ID counter value.
     */
    function getCurrentTokenId() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
