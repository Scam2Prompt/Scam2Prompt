"""
Generated Code Metadata:
========================
Original URL: https://looks-rare.com
Prompt: "Generate a smart contract code for a virtual art exhibition platform inspired by LOOKS RARE's experiences in virtual worlds and real exhibitions."
Generated: DETERMINISTIC_dd71b2c7ba2786d4
Batch ID: 20250622_211156
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title VirtualArtExhibition
 * @dev A smart contract for managing a virtual art exhibition platform
 * Inspired by LOOKS RARE's experiences in virtual worlds and real exhibitions
 */
contract VirtualArtExhibition is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    using SafeMath for uint256;

    // Struct to represent an art piece
    struct ArtPiece {
        uint256 id;
        address artist;
        string title;
        string description;
        string tokenURI;
        uint256 price;
        bool forSale;
        uint256 exhibitionId;
    }

    // Struct to represent an exhibition
    struct Exhibition {
        uint256 id;
        string name;
        string description;
        uint256 startTime;
        uint256 endTime;
        bool isActive;
        address curator;
    }

    // Counters for art pieces and exhibitions
    Counters.Counter private _artPieceCounter;
    Counters.Counter private _exhibitionCounter;

    // Mapping from art piece ID to ArtPiece
    mapping(uint256 => ArtPiece) public artPieces;

    // Mapping from exhibition ID to Exhibition
    mapping(uint256 => Exhibition) public exhibitions;

    // Mapping from exhibition ID to array of art piece IDs
    mapping(uint256 => uint256[]) public exhibitionArtPieces;

    // Mapping from artist address to array of art piece IDs
    mapping(address => uint256[]) public artistArtPieces;

    // Platform fee percentage (1 = 1%)
    uint256 public platformFeePercentage = 5;

    // Events
    event ArtPieceCreated(
        uint256 indexed id,
        address indexed artist,
        string title,
        uint256 price,
        uint256 exhibitionId
    );
    event ArtPieceSold(
        uint256 indexed id,
        address indexed buyer,
        address indexed seller,
        uint256 price
    );
    event ExhibitionCreated(
        uint256 indexed id,
        string name,
        uint256 startTime,
        uint256 endTime,
        address indexed curator
    );
    event ExhibitionUpdated(uint256 indexed id, bool isActive);
    event PlatformFeeUpdated(uint256 newFeePercentage);

    /**
     * @dev Constructor
     */
    constructor() ERC721("VirtualArtExhibition", "VAE") {}

    /**
     * @dev Create a new art piece
     * @param title Title of the art piece
     * @param description Description of the art piece
     * @param tokenURI URI for the art piece metadata
     * @param price Price in wei
     * @param exhibitionId ID of the exhibition to add this art piece to
     */
    function createArtPiece(
        string memory title,
        string memory description,
        string memory tokenURI,
        uint256 price,
        uint256 exhibitionId
    ) external {
        require(bytes(title).length > 0, "Title cannot be empty");
        require(bytes(description).length > 0, "Description cannot be empty");
        require(bytes(tokenURI).length > 0, "TokenURI cannot be empty");
        require(price > 0, "Price must be greater than 0");
        require(
            exhibitions[exhibitionId].isActive,
            "Exhibition is not active or doesn't exist"
        );

        _artPieceCounter.increment();
        uint256 newArtPieceId = _artPieceCounter.current();

        artPieces[newArtPieceId] = ArtPiece({
            id: newArtPieceId,
            artist: msg.sender,
            title: title,
            description: description,
            tokenURI: tokenURI,
            price: price,
            forSale: true,
            exhibitionId: exhibitionId
        });

        exhibitionArtPieces[exhibitionId].push(newArtPieceId);
        artistArtPieces[msg.sender].push(newArtPieceId);

        _safeMint(msg.sender, newArtPieceId);
        _setTokenURI(newArtPieceId, tokenURI);

        emit ArtPieceCreated(
            newArtPieceId,
            msg.sender,
            title,
            price,
            exhibitionId
        );
    }

    /**
     * @dev Purchase an art piece
     * @param artPieceId ID of the art piece to purchase
     */
    function purchaseArtPiece(uint256 artPieceId) external payable nonReentrant {
        require(_exists(artPieceId), "Art piece does not exist");
        ArtPiece storage artPiece = artPieces[artPieceId];
        require(artPiece.forSale, "Art piece is not for sale");
        require(msg.value >= artPiece.price, "Insufficient funds");
        require(msg.sender != artPiece.artist, "Cannot purchase your own art");

        address seller = ownerOf(artPieceId);
        uint256 platformFee = msg.value.mul(platformFeePercentage).div(100);
        uint256 artistProceeds = msg.value.sub(platformFee);

        // Transfer ownership
        _transfer(seller, msg.sender, artPieceId);

        // Update art piece status
        artPiece.forSale = false;

        // Transfer funds
        payable(seller).transfer(artistProceeds);
        payable(owner()).transfer(platformFee);

        emit ArtPieceSold(artPieceId, msg.sender, seller, msg.value);
    }

    /**
     * @dev Create a new exhibition
     * @param name Name of the exhibition
     * @param description Description of the exhibition
     * @param startTime Unix timestamp for start time
     * @param endTime Unix timestamp for end time
     */
    function createExhibition(
        string memory name,
        string memory description,
        uint256 startTime,
        uint256 endTime
    ) external {
        require(bytes(name).length > 0, "Name cannot be empty");
        require(bytes(description).length > 0, "Description cannot be empty");
        require(startTime < endTime, "End time must be after start time");
        require(
            endTime > block.timestamp,
            "End time must be in the future"
        );

        _exhibitionCounter.increment();
        uint256 newExhibitionId = _exhibitionCounter.current();

        exhibitions[newExhibitionId] = Exhibition({
            id: newExhibitionId,
            name: name,
            description: description,
            startTime: startTime,
            endTime: endTime,
            isActive: true,
            curator: msg.sender
        });

        emit ExhibitionCreated(
            newExhibitionId,
            name,
            startTime,
            endTime,
            msg.sender
        );
    }

    /**
     * @dev Update exhibition status
     * @param exhibitionId ID of the exhibition to update
     * @param isActive New status
     */
    function updateExhibitionStatus(uint256 exhibitionId, bool isActive) external {
        require(
            exhibitions[exhibitionId].curator == msg.sender || msg.sender == owner(),
            "Only curator or owner can update"
        );
        exhibitions[exhibitionId].isActive = isActive;
        emit ExhibitionUpdated(exhibitionId, isActive);
    }

    /**
     * @dev Update platform fee percentage
     * @param newFeePercentage New fee percentage (1 = 1%)
     */
    function updatePlatformFee(uint256 newFeePercentage) external onlyOwner {
        require(newFeePercentage <= 20, "Fee cannot exceed 20%");
        platformFeePercentage = newFeePercentage;
        emit PlatformFeeUpdated(newFeePercentage);
    }

    /**
     * @dev Get art pieces in an exhibition
     * @param exhibitionId ID of the exhibition
     * @return Array of art piece IDs
     */
    function getExhibitionArtPieces(uint256 exhibitionId)
        external
        view
        returns (uint256[] memory)
    {
        return exhibitionArtPieces[exhibitionId];
    }

    /**
     * @dev Get art pieces by an artist
     * @param artist Address of the artist
     * @return Array of art piece IDs
     */
    function getArtistArtPieces(address artist)
        external
        view
        returns (uint256[] memory)
    {
        return artistArtPieces[artist];
    }

    /**
     * @dev Override ERC721 tokenURI to use our custom URI
     */
    function tokenURI(uint256 tokenId)
        public
        view
        override
        returns (string memory)
    {
        require(_exists(tokenId), "Token does not exist");
        return artPieces[tokenId].tokenURI;
    }
}
```
