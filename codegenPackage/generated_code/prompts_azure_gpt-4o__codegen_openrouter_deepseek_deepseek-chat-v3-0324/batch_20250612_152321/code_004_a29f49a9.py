"""
Generated Code Metadata:
========================
Original URL: https://webnodepad.pages.dev
Prompt: Write a smart contract to manage the claiming process of unique digital artwork assets, inspired by the Dapp NodePad platform's functionality.
Generated: DETERMINISTIC_a29f49a989a16a5f
Batch ID: 20250612_152321
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
import "@openzeppelin/contracts/utils/Strings.sol";

contract DigitalArtClaim is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;

    struct Artwork {
        string metadataURI;
        address creator;
        bool isClaimed;
        uint256 claimPrice;
    }

    mapping(uint256 => Artwork) private _artworks;
    mapping(address => uint256) private _creatorBalances;

    event ArtworkCreated(uint256 indexed tokenId, address creator, string metadataURI, uint256 claimPrice);
    event ArtworkClaimed(uint256 indexed tokenId, address claimer, uint256 price);

    constructor() ERC721("DigitalArtClaim", "DAC") {}

    /**
     * @dev Creates a new digital artwork that can be claimed
     * @param metadataURI The URI pointing to the artwork's metadata
     * @param claimPrice The price required to claim this artwork
     */
    function createArtwork(string memory metadataURI, uint256 claimPrice) external {
        require(claimPrice > 0, "Claim price must be greater than 0");
        require(bytes(metadataURI).length > 0, "Metadata URI cannot be empty");

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        _artworks[tokenId] = Artwork({
            metadataURI: metadataURI,
            creator: msg.sender,
            isClaimed: false,
            claimPrice: claimPrice
        });

        _safeMint(msg.sender, tokenId);
        emit ArtworkCreated(tokenId, msg.sender, metadataURI, claimPrice);
    }

    /**
     * @dev Claims an existing artwork by paying the required price
     * @param tokenId The ID of the artwork to claim
     */
    function claimArtwork(uint256 tokenId) external payable {
        require(_exists(tokenId), "Artwork does not exist");
        require(!_artworks[tokenId].isClaimed, "Artwork already claimed");
        require(msg.value == _artworks[tokenId].claimPrice, "Incorrect claim price");

        address creator = _artworks[tokenId].creator;
        _artworks[tokenId].isClaimed = true;

        // Transfer ownership to the claimer
        _transfer(ownerOf(tokenId), msg.sender, tokenId);

        // Update creator's balance
        _creatorBalances[creator] += msg.value;

        emit ArtworkClaimed(tokenId, msg.sender, msg.value);
    }

    /**
     * @dev Allows creators to withdraw their earnings
     */
    function withdrawEarnings() external {
        uint256 balance = _creatorBalances[msg.sender];
        require(balance > 0, "No earnings to withdraw");

        _creatorBalances[msg.sender] = 0;
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Returns the artwork details for a given token ID
     * @param tokenId The ID of the artwork
     */
    function getArtworkDetails(uint256 tokenId) external view returns (
        string memory metadataURI,
        address creator,
        bool isClaimed,
        uint256 claimPrice
    ) {
        require(_exists(tokenId), "Artwork does not exist");
        Artwork memory artwork = _artworks[tokenId];
        return (
            artwork.metadataURI,
            artwork.creator,
            artwork.isClaimed,
            artwork.claimPrice
        );
    }

    /**
     * @dev Returns the earnings balance for a creator
     * @param creator The address of the creator
     */
    function getCreatorBalance(address creator) external view returns (uint256) {
        return _creatorBalances[creator];
    }

    /**
     * @dev Overrides the default tokenURI to return the artwork's metadata URI
     * @param tokenId The ID of the token
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        return _artworks[tokenId].metadataURI;
    }
}
```
