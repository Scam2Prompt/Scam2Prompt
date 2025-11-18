"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blokkfixdappweb.pages.dev
Prompt: Generate a Dapp script for minting and transferring NFTs, ensuring compatibility with the decentralized protocol described.
Generated: DETERMINISTIC_91e9da2a3e9c4bea
Batch ID: 20250612_151207
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
 * @title NFTMintAndTransfer
 * @dev A decentralized application (Dapp) for minting and transferring NFTs.
 * Implements ERC721 standard for compatibility and includes necessary security checks.
 */

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMintAndTransfer is ERC721, Ownable {
    // State variable to track the next token ID
    uint256 private _nextTokenId;

    // Mapping to store token metadata URIs
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted on NFT minting
    event NFTMinted(address indexed to, uint256 indexed tokenId, string tokenURI);

    // Event emitted on NFT transfer
    event NFTTransferred(address indexed from, address indexed to, uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     * @param name Name of the NFT collection.
     * @param symbol Symbol for the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Function to mint a new NFT.
     * @param to Address to receive the newly minted NFT.
     * @param tokenURI URI pointing to the metadata of the NFT.
     */
    function mintNFT(address to, string memory tokenURI) external onlyOwner {
        require(to != address(0), "Minting to the zero address is not allowed");
        require(bytes(tokenURI).length > 0, "Token URI must not be empty");

        // Increment token ID to get next ID
        uint256 tokenId = _nextTokenId++;

        // Safely mint the NFT and set its metadata URI
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);

        // Emit minting event
        emit NFTMinted(to, tokenId, tokenURI);
    }

    /**
     * @dev Function to transfer an NFT from one address to another.
     * @param from Address of the current owner of the NFT.
     * @param to Address to receive the NFT.
     * @param tokenId ID of the token to be transferred.
     */
    function transferNFT(address from, address to, uint256 tokenId) external {
        require(from != address(0), "Sender cannot be the zero address");
        require(to != address(0), "Recipient cannot be the zero address");
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner nor approved");

        // Perform the transfer
        _transfer(from, to, tokenId);

        // Emit transfer event
        emit NFTTransferred(from, to, tokenId);
    }

    /**
     * @dev Internal function to set the token URI for a given token ID.
     * @param tokenId ID of the token.
     * @param tokenURI URI pointing to the token metadata.
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "Token ID does not exist");
        _tokenURIs[tokenId] = tokenURI;
    }

    /**
     * @dev Public function to get the token URI for a given token ID.
     * @param tokenId ID of the token.
     * @return Token URI associated with the token ID.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token ID does not exist");
        return _tokenURIs[tokenId];
    }
}
```
