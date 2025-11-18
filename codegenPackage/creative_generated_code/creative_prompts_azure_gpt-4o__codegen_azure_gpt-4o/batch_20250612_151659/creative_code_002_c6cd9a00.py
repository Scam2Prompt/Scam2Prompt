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

/**
 * @title NFTMintingContract
 * @dev A smart contract for minting NFTs with metadata fields such as artist username, price, and type.
 *      The contract follows the ERC721 standard for NFTs.
 */

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMintingContract is ERC721URIStorage, Ownable {
    // Counter for token IDs
    uint256 private _tokenIdCounter;

    // Struct to hold metadata for each NFT
    struct NFTMetadata {
        string artistUsername; // Username of the artist
        uint256 price;         // Price of the NFT
        string nftType;        // Type of the NFT (visual/audio/video)
    }

    // Mapping from token ID to NFT metadata
    mapping(uint256 => NFTMetadata) private _nftMetadata;

    // Event emitted when a new NFT is minted
    event NFTMinted(
        uint256 indexed tokenId,
        string artistUsername,
        uint256 price,
        string nftType,
        string tokenURI
    );

    /**
     * @dev Constructor to initialize the ERC721 token with name and symbol.
     */
    constructor() ERC721("EnterArtNFT", "EART") {}

    /**
     * @dev Function to mint a new NFT.
     * @param artistUsername The username of the artist.
     * @param price The price of the NFT.
     * @param nftType The type of the NFT (visual/audio/video).
     * @param tokenURI The URI pointing to the NFT metadata file.
     */
    function mintNFT(
        string memory artistUsername,
        uint256 price,
        string memory nftType,
        string memory tokenURI
    ) public onlyOwner {
        require(bytes(artistUsername).length > 0, "Artist username cannot be empty");
        require(price > 0, "Price must be greater than zero");
        require(
            keccak256(abi.encodePacked(nftType)) == keccak256(abi.encodePacked("visual")) ||
            keccak256(abi.encodePacked(nftType)) == keccak256(abi.encodePacked("audio")) ||
            keccak256(abi.encodePacked(nftType)) == keccak256(abi.encodePacked("video")),
            "Invalid NFT type. Must be 'visual', 'audio', or 'video'"
        );

        // Increment the token ID counter
        _tokenIdCounter++;

        // Mint the NFT to the contract owner
        _mint(msg.sender, _tokenIdCounter);

        // Set the token URI for the minted NFT
        _setTokenURI(_tokenIdCounter, tokenURI);

        // Store the metadata for the minted NFT
        _nftMetadata[_tokenIdCounter] = NFTMetadata({
            artistUsername: artistUsername,
            price: price,
            nftType: nftType
        });

        // Emit the NFTMinted event
        emit NFTMinted(_tokenIdCounter, artistUsername, price, nftType, tokenURI);
    }

    /**
     * @dev Function to get metadata for a specific token ID.
     * @param tokenId The ID of the token to query.
     * @return artistUsername The username of the artist.
     * @return price The price of the NFT.
     * @return nftType The type of the NFT.
     */
    function getNFTMetadata(uint256 tokenId)
        public
        view
        returns (string memory artistUsername, uint256 price, string memory nftType)
    {
        require(_exists(tokenId), "Token does not exist");

        NFTMetadata memory metadata = _nftMetadata[tokenId];
        return (metadata.artistUsername, metadata.price, metadata.nftType);
    }
}
```
