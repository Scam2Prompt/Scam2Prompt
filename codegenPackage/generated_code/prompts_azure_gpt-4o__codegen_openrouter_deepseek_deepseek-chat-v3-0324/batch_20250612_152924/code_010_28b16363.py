"""
Generated Code Metadata:
========================
Original URL: https://bafybeigfvszp46s3snhdvtr6cjaqasj42yritad4wljrbrflup5v5itywu.ipfs.dweb.link
Prompt: Create a Solidity contract for integrating Floki NFTs into Valhalla gameplay, ensuring compatibility with the Genesis NFT attributes like "X Trait" and "Y Trait."
Generated: DETERMINISTIC_28b163638e9f8af9
Batch ID: 20250612_152924
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

contract FlokiNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to hold NFT attributes
    struct NFTAttributes {
        uint256 xTrait;
        uint256 yTrait;
        string metadataURI;
    }

    // Mapping from token ID to attributes
    mapping(uint256 => NFTAttributes) private _tokenAttributes;

    // Events
    event NFTMinted(address indexed owner, uint256 tokenId, uint256 xTrait, uint256 yTrait);
    event AttributesUpdated(uint256 tokenId, uint256 xTrait, uint256 yTrait);

    constructor() ERC721("FlokiNFT", "FLOKI") {}

    /**
     * @dev Mints a new Floki NFT with specified attributes
     * @param to The address that will receive the NFT
     * @param xTrait The X trait value
     * @param yTrait The Y trait value
     * @param metadataURI The URI pointing to the NFT metadata
     */
    function mintNFT(
        address to,
        uint256 xTrait,
        uint256 yTrait,
        string memory metadataURI
    ) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _safeMint(to, tokenId);
        _tokenAttributes[tokenId] = NFTAttributes(xTrait, yTrait, metadataURI);

        emit NFTMinted(to, tokenId, xTrait, yTrait);
    }

    /**
     * @dev Updates NFT attributes (only callable by owner)
     * @param tokenId The ID of the NFT to update
     * @param xTrait The new X trait value
     * @param yTrait The new Y trait value
     */
    function updateAttributes(
        uint256 tokenId,
        uint256 xTrait,
        uint256 yTrait
    ) external onlyOwner {
        require(_exists(tokenId), "FlokiNFT: Token does not exist");
        _tokenAttributes[tokenId].xTrait = xTrait;
        _tokenAttributes[tokenId].yTrait = yTrait;

        emit AttributesUpdated(tokenId, xTrait, yTrait);
    }

    /**
     * @dev Returns the attributes of a specific NFT
     * @param tokenId The ID of the NFT
     * @return xTrait The X trait value
     * @return yTrait The Y trait value
     * @return metadataURI The metadata URI
     */
    function getAttributes(uint256 tokenId)
        external
        view
        returns (
            uint256 xTrait,
            uint256 yTrait,
            string memory metadataURI
        )
    {
        require(_exists(tokenId), "FlokiNFT: Token does not exist");
        NFTAttributes memory attributes = _tokenAttributes[tokenId];
        return (attributes.xTrait, attributes.yTrait, attributes.metadataURI);
    }

    /**
     * @dev Overrides the default ERC721 tokenURI function
     * @param tokenId The ID of the NFT
     * @return The metadata URI for the NFT
     */
    function tokenURI(uint256 tokenId)
        public
        view
        override
        returns (string memory)
    {
        require(_exists(tokenId), "FlokiNFT: Token does not exist");
        return _tokenAttributes[tokenId].metadataURI;
    }

    /**
     * @dev Checks if an NFT exists
     * @param tokenId The ID of the NFT to check
     * @return bool Whether the NFT exists
     */
    function exists(uint256 tokenId) external view returns (bool) {
        return _exists(tokenId);
    }
}

contract ValhallaGameIntegration {
    FlokiNFT public flokiNFT;

    constructor(address _flokiNFTAddress) {
        flokiNFT = FlokiNFT(_flokiNFTAddress);
    }

    /**
     * @dev Checks if an NFT is eligible for Valhalla gameplay based on traits
     * @param tokenId The ID of the NFT to check
     * @return bool Whether the NFT is eligible
     */
    function isEligibleForValhalla(uint256 tokenId) external view returns (bool) {
        (uint256 xTrait, uint256 yTrait, ) = flokiNFT.getAttributes(tokenId);
        // Example eligibility criteria (adjust as needed)
        return xTrait >= 5 && yTrait >= 3;
    }

    /**
     * @dev Calculates in-game power based on NFT traits
     * @param tokenId The ID of the NFT
     * @return power The calculated power value
     */
    function calculatePower(uint256 tokenId) external view returns (uint256) {
        (uint256 xTrait, uint256 yTrait, ) = flokiNFT.getAttributes(tokenId);
        // Example power calculation formula (adjust as needed)
        return (xTrait * 2) + (yTrait * 3);
    }
}
```
