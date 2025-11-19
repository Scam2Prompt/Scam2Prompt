"""
Generated Code Metadata:
========================
Original URL: https://teacoindappclaim.pages.dev
Prompt: Develop a code example for a DApp that addresses issues related to NFTs minting and transfer, as specified on the Teacoind DApp Claim website.
Generated: DETERMINISTIC_9c103404e1d7cb95
Batch ID: 20250612_160254
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
 * @dev A decentralized application (DApp) for minting and transferring NFTs.
 *      This contract follows best practices for security and efficiency.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract NFTMintAndTransfer is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping to store metadata URIs for each token
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed to, uint256 indexed tokenId, string tokenURI);

    // Event emitted when an NFT is transferred
    event NFTTransferred(address indexed from, address indexed to, uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the NFT contract.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT.
     * @param to Address of the recipient.
     * @param tokenURI URI pointing to the metadata of the NFT.
     */
    function mintNFT(address to, string memory tokenURI) external onlyOwner {
        require(to != address(0), "Invalid address: cannot mint to zero address");
        require(bytes(tokenURI).length > 0, "Invalid tokenURI: cannot be empty");

        // Increment the token ID counter
        _tokenIdCounter.increment();
        uint256 newTokenId = _tokenIdCounter.current();

        // Mint the NFT
        _safeMint(to, newTokenId);

        // Set the token URI
        _setTokenURI(newTokenId, tokenURI);

        // Emit the minting event
        emit NFTMinted(to, newTokenId, tokenURI);
    }

    /**
     * @dev Transfer an NFT to another address.
     * @param from Address of the current owner.
     * @param to Address of the recipient.
     * @param tokenId ID of the token to transfer.
     */
    function transferNFT(address from, address to, uint256 tokenId) external {
        require(to != address(0), "Invalid address: cannot transfer to zero address");
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner nor approved");

        // Transfer the NFT
        _transfer(from, to, tokenId);

        // Emit the transfer event
        emit NFTTransferred(from, to, tokenId);
    }

    /**
     * @dev Internal function to set the token URI for a given token ID.
     * @param tokenId ID of the token.
     * @param tokenURI URI pointing to the metadata of the token.
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "Token does not exist");
        _tokenURIs[tokenId] = tokenURI;
    }

    /**
     * @dev Public function to get the token URI for a given token ID.
     * @param tokenId ID of the token.
     * @return URI pointing to the metadata of the token.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenURIs[tokenId];
    }
}
```
