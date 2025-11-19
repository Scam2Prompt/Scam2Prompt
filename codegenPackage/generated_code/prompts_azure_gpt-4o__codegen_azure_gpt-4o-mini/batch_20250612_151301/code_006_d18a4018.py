"""
Generated Code Metadata:
========================
Original URL: https://somnia.pages.dev
Prompt: Generate a Solidity contract that leverages Somnia's blockchain to mint and transfer NFTs with interoperability across metaverses.
Generated: DETERMINISTIC_d18a40187dad6c7d
Batch ID: 20250612_151301
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

// Importing OpenZeppelin's ERC721 implementation for NFT standards
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract for minting and transferring NFTs with interoperability
contract SomniaNFT is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("SomniaNFT", "SNFT") {}

    // Function to mint a new NFT
    // @param to: address of the recipient
    // @param tokenURI: metadata URI for the NFT
    function mintNFT(address to, string memory tokenURI) public onlyOwner {
        require(to != address(0), "Invalid address: cannot mint to the zero address");
        require(bytes(tokenURI).length > 0, "Invalid token URI: cannot be empty");

        // Increment the token ID counter and mint the NFT
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _mint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);

        // Emit the NFTMinted event
        emit NFTMinted(to, tokenId, tokenURI);
    }

    // Function to transfer an NFT from one address to another
    // @param from: address of the current owner
    // @param to: address of the new owner
    // @param tokenId: ID of the NFT to transfer
    function transferNFT(address from, address to, uint256 tokenId) public {
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner nor approved");
        require(to != address(0), "Invalid address: cannot transfer to the zero address");

        // Transfer the NFT
        _transfer(from, to, tokenId);
    }

    // Function to get the total supply of NFTs minted
    // @return: total number of NFTs minted
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
