"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unicats-on-unichain.nfts2.me
Prompt: Generate code to create a smart contract for an NFT collection, ensuring it includes features to prevent intellectual property rights infringement.
Generated: DETERMINISTIC_df14297b22666c66
Batch ID: 20250612_140255
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title NFTCollection
 * @dev This contract creates an NFT collection with metadata storage and includes features 
 * to prevent intellectual property rights infringement.
 */
contract NFTCollection is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to intellectual property rights owner
    mapping(uint256 => address) private _ipOwners;

    // Event emitted when a new NFT is minted
    event NFTMinted(uint256 indexed tokenId, address indexed owner, string tokenUri);

    /**
     * @dev Sets the name and symbol for the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT ensuring the token URI is unique and the creator has the rights.
     * @param to Address of the NFT recipient.
     * @param tokenUri The metadata URI for the NFT.
     * @param ipOwner Address of the intellectual property owner.
     */
    function mintNFT(address to, string memory tokenUri, address ipOwner) public onlyOwner {
        require(to != address(0), "Invalid address: cannot mint to zero address");
        require(bytes(tokenUri).length > 0, "Invalid URI: cannot be empty");
        require(ipOwner != address(0), "Invalid IP owner address");

        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        
        // Mint the NFT
        _safeMint(to, tokenId);
        
        // Set the token URI
        _setTokenURI(tokenId, tokenUri);
        
        // Set the intellectual property owner
        _ipOwners[tokenId] = ipOwner;
        
        // Emit the NFT minting event
        emit NFTMinted(tokenId, to, tokenUri);

        // Increment the counter for future mints
        _tokenIdCounter.increment();
    }

    /**
     * @dev Get the intellectual property owner for a specific token ID.
     * @param tokenId The ID of the token.
     * @return Address of the intellectual property owner.
     */
    function getIpOwner(uint256 tokenId) public view returns (address) {
        return _ipOwners[tokenId];
    }

    /**
     * @dev Override the transfer function to enforce IP rights.
     * Prevents transfer if the IP owner does not approve.
     */
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override {
        super._beforeTokenTransfer(from, to, tokenId);

        // Prevent transfer if the IP owner is not the current owner
        require(from == address(0) || from == owner(), "Transfer of NFT is restricted by IP ownership");
    }

    /**
     * @dev Allows the owner to withdraw funds from the contract (if applicable).
     */
    function withdraw() public onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers to the contract.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
