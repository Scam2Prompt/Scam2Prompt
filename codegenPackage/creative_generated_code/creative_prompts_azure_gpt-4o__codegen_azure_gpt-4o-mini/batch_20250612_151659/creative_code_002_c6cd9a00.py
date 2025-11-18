"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enterart.rpmltech.com
Prompt: Develop a smart contract in Solidity for minting NFTs with metadata fields such as artist username, price, and type (visual, audio, video), as seen on enter.art.
Generated: DETERMINISTIC_c6cd9a003cec1392
Batch ID: 20250612_151659
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

// Import OpenZeppelin's ERC721 and Ownable contracts
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// NFT contract for minting unique tokens with artist metadata
contract ArtNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for token IDs
    Counters.Counter private _tokenIdCounter;

    // Structure for storing metadata for each NFT
    struct ArtMetadata {
        string artistUsername;
        uint256 price;
        string artType; // Types can be visual, audio, video
    }

    // Mapping from token ID to its metadata
    mapping(uint256 => ArtMetadata) private _artMetadata;

    // Event to emit when a new NFT is minted
    event NFTMinted(uint256 indexed tokenId, string artistUsername, uint256 price, string artType);

    // Constructor to initialize the contract with a name and symbol for the NFT
    constructor() ERC721("ArtNFT", "ANFT") {}

    // Function to mint a new NFT
    // @param artistUsername: Username of the artist
    // @param price: Price of the NFT in wei
    // @param artType: Type of the art (visual, audio, video)
    function mintNFT(string memory artistUsername, uint256 price, string memory artType) public onlyOwner {
        require(bytes(artistUsername).length > 0, "Artist username is required.");
        require(price > 0, "Price must be greater than zero.");
        require(keccak256(abi.encodePacked(artType)) == keccak256(abi.encodePacked("visual")) ||
                keccak256(abi.encodePacked(artType)) == keccak256(abi.encodePacked("audio")) ||
                keccak256(abi.encodePacked(artType)) == keccak256(abi.encodePacked("video")),
                "Art type must be either visual, audio, or video.");

        // Increment the token ID counter and assign a new token ID
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT to the caller's address
        _mint(msg.sender, tokenId);

        // Store the metadata for the new NFT
        _artMetadata[tokenId] = ArtMetadata(artistUsername, price, artType);

        // Emit an event for the minting action
        emit NFTMinted(tokenId, artistUsername, price, artType);
    }

    // Function to fetch the metadata of a specific token
    // @param tokenId: ID of the token
    // @return artistUsername: Username of the artist
    // @return price: Price of the NFT in wei
    // @return artType: Type of the art (visual, audio, video)
    function getArtMetadata(uint256 tokenId) public view returns (string memory artistUsername, uint256 price, string memory artType) {
        require(_exists(tokenId), "Token ID does not exist.");

        ArtMetadata memory metadata = _artMetadata[tokenId];
        return (metadata.artistUsername, metadata.price, metadata.artType);
    }
}
```
