"""
Generated Code Metadata:
========================
Original URL: https://xcad-staked.pages.dev
Prompt: Create a smart contract for managing gamified NFT collectibles based on XCAD Network’s NFT Moments system.
Generated: DETERMINISTIC_c6e0b6c6cfd9fb4f
Batch ID: 20250612_152358
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

contract XCADNFTMoments is ERC721, Ownable {
    using Counters for Counters.Counter;
    using SafeMath for uint256;

    // Token ID counter
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Moment details
    struct Moment {
        uint256 rarity;
        uint256 points;
        uint256 timestamp;
        string metadataURI;
    }

    // Mapping from token ID to Moment
    mapping(uint256 => Moment) private _moments;

    // Mapping from user to their collected points
    mapping(address => uint256) private _userPoints;

    // Mapping from rarity to max supply
    mapping(uint256 => uint256) public rarityMaxSupply;

    // Mapping from rarity to current minted count
    mapping(uint256 => uint256) public rarityMintedCount;

    // Events
    event MomentMinted(address indexed owner, uint256 tokenId, uint256 rarity, uint256 points);
    event PointsUpdated(address indexed user, uint256 newPoints);
    event RaritySupplyUpdated(uint256 rarity, uint256 newMaxSupply);

    constructor(string memory baseURI) ERC721("XCAD NFT Moments", "XCADMOMENT") {
        _baseTokenURI = baseURI;

        // Initialize rarity supplies (example values)
        rarityMaxSupply[1] = 10000; // Common
        rarityMaxSupply[2] = 5000;  // Uncommon
        rarityMaxSupply[3] = 1000;  // Rare
        rarityMaxSupply[4] = 100;   // Epic
        rarityMaxSupply[5] = 10;    // Legendary
    }

    /**
     * @dev Mints a new NFT Moment
     * @param rarity The rarity level of the moment
     * @param points The points awarded for this moment
     * @param metadataURI Additional metadata URI
     */
    function mintMoment(
        uint256 rarity,
        uint256 points,
        string memory metadataURI
    ) external onlyOwner {
        require(rarity >= 1 && rarity <= 5, "Invalid rarity level");
        require(rarityMintedCount[rarity] < rarityMaxSupply[rarity], "Max supply reached for this rarity");
        require(points > 0, "Points must be greater than zero");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _moments[tokenId] = Moment({
            rarity: rarity,
            points: points,
            timestamp: block.timestamp,
            metadataURI: metadataURI
        });

        rarityMintedCount[rarity] += 1;
        _safeMint(msg.sender, tokenId);

        emit MomentMinted(msg.sender, tokenId, rarity, points);
    }

    /**
     * @dev Transfers a moment and updates user points
     * @param from The current owner
     * @param to The new owner
     * @param tokenId The token being transferred
     */
    function _transfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        super._transfer(from, to, tokenId);

        // Update points for both users
        if (from != address(0)) {
            _userPoints[from] = _userPoints[from].sub(_moments[tokenId].points);
            emit PointsUpdated(from, _userPoints[from]);
        }

        _userPoints[to] = _userPoints[to].add(_moments[tokenId].points);
        emit PointsUpdated(to, _userPoints[to]);
    }

    /**
     * @dev Gets moment details by token ID
     * @param tokenId The token ID to query
     * @return Moment details
     */
    function getMoment(uint256 tokenId) external view returns (Moment memory) {
        require(_exists(tokenId), "Token does not exist");
        return _moments[tokenId];
    }

    /**
     * @dev Gets user's total points
     * @param user The address to query
     * @return Total points
     */
    function getUserPoints(address user) external view returns (uint256) {
        return _userPoints[user];
    }

    /**
     * @dev Updates the base URI for metadata
     * @param baseURI The new base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Updates max supply for a rarity level
     * @param rarity The rarity level to update
     * @param newMaxSupply The new max supply
     */
    function setRarityMaxSupply(uint256 rarity, uint256 newMaxSupply) external onlyOwner {
        require(rarity >= 1 && rarity <= 5, "Invalid rarity level");
        require(newMaxSupply >= rarityMintedCount[rarity], "New max supply cannot be less than already minted");
        rarityMaxSupply[rarity] = newMaxSupply;
        emit RaritySupplyUpdated(rarity, newMaxSupply);
    }

    /**
     * @dev Returns the base URI for metadata
     * @return The base URI
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Checks if a token exists
     * @param tokenId The token ID to check
     * @return Whether the token exists
     */
    function exists(uint256 tokenId) external view returns (bool) {
        return _exists(tokenId);
    }
}
```
