"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://groovesup.pages.dev
Prompt: Write a Solidity contract for creating artist NFTs that can be sold in the GrooveUP marketplace, enabling artists to raise seed funds while rewarding fans for streaming and sharing their music.
Generated: DETERMINISTIC_d5096ed77f5cacc7
Batch ID: 20250612_145923
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title GrooveUP Marketplace NFT Contract
 * @dev This contract allows artists to create NFTs for their music
 *      and enables fans to purchase and hold these NFTs.
 */
contract GrooveUPNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to store artist information
    struct Artist {
        string name;
        string musicUrl;
        uint256 fundsRaised;
        bool exists;
    }

    // Mapping from token ID to artist information
    mapping(uint256 => Artist) public artists;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 tokenId, string artistName, string musicUrl);

    // Event emitted when an NFT is purchased
    event NFTPurchased(uint256 tokenId, address buyer);

    // Modifier to check if the artist exists
    modifier artistExists(uint256 tokenId) {
        require(artists[tokenId].exists, "Artist does not exist");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with a name and symbol for the NFTs.
     * @param name The name of the NFT collection
     * @param symbol The symbol for the NFT collection
     */
    constructor(string memory name, string memory symbol) 
        ERC721(name, symbol) 
    {}

    /**
     * @dev Function to create a new NFT for an artist.
     * @param artistName The name of the artist
     * @param musicUrl The URL to the artist's music
     * @return tokenId The ID of the newly created token
     */
    function createArtistNFT(string memory artistName, string memory musicUrl) 
        external 
        onlyOwner 
        returns (uint256 tokenId) 
    {
        tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        artists[tokenId] = Artist({
            name: artistName,
            musicUrl: musicUrl,
            fundsRaised: 0,
            exists: true
        });

        _mint(msg.sender, tokenId);
        emit NFTCreated(tokenId, artistName, musicUrl);
    }

    /**
     * @dev Function to purchase an NFT.
     * @param tokenId The ID of the token to be purchased
     */
    function purchaseNFT(uint256 tokenId) 
        external 
        payable 
        artistExists(tokenId) 
    {
        require(msg.value > 0, "Price must be greater than zero");
        address owner = ownerOf(tokenId);
        require(owner != msg.sender, "You cannot purchase your own NFT");

        // Transfer the NFT to the buyer
        _transfer(owner, msg.sender, tokenId);

        // Transfer funds to the artist
        payable(owner).transfer(msg.value);

        // Update funds raised for the artist
        artists[tokenId].fundsRaised += msg.value;

        emit NFTPurchased(tokenId, msg.sender);
    }

    /**
     * @dev Function to retrieve artist information.
     * @param tokenId The ID of the token
     * @return The artist's name, music URL, and funds raised
     */
    function getArtistInfo(uint256 tokenId) 
        external 
        view 
        artistExists(tokenId) 
        returns (string memory, string memory, uint256) 
    {
        Artist memory artist = artists[tokenId];
        return (artist.name, artist.musicUrl, artist.fundsRaised);
    }

    /**
     * @dev Function to withdraw contract balance (if any).
     * @param to The address to withdraw funds to
     * @param amount The amount to withdraw
     */
    function withdrawFunds(address payable to, uint256 amount) 
        external 
        onlyOwner 
    {
        require(address(this).balance >= amount, "Insufficient contract balance");
        to.transfer(amount);
    }

    /**
     * @dev Fallback function to receive ETH.
     */
    receive() external payable {}
}
```
