"""
Generated Code Metadata:
========================
Original URL: https://rplanet-io.vercel.app
Prompt: Generate a code snippet for a smart contract that manages NFT assets for the R-Planet Conquest game, including land, hero, and artifact NFTs.
Generated: DETERMINISTIC_a2754f2669f81c70
Batch ID: 20250612_162913
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title RPlanetConquestNFT
 * @dev Manages NFT assets for R-Planet Conquest game (Land, Hero, Artifact)
 */
contract RPlanetConquestNFT is ERC721, ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // NFT Types
    enum NFTType { LAND, HERO, ARTIFACT }

    // Struct to store NFT metadata
    struct NFTMetadata {
        NFTType nftType;
        uint256 attributes; // Packed attributes for the NFT
        string tokenURI;
    }

    // Token ID counters for each NFT type
    Counters.Counter private _landTokenIds;
    Counters.Counter private _heroTokenIds;
    Counters.Counter private _artifactTokenIds;

    // Mapping from token ID to NFT metadata
    mapping(uint256 => NFTMetadata) private _tokenMetadata;

    // Base URI for token metadata
    string private _baseTokenURI;

    // Events
    event NFTMinted(address indexed owner, uint256 tokenId, NFTType nftType);
    event NFTAttributesUpdated(uint256 tokenId, uint256 newAttributes);

    /**
     * @dev Initializes the contract
     * @param name_ Name of the NFT collection
     * @param symbol_ Symbol of the NFT collection
     * @param baseTokenURI_ Base URI for token metadata
     */
    constructor(
        string memory name_,
        string memory symbol_,
        string memory baseTokenURI_
    ) ERC721(name_, symbol_) {
        _baseTokenURI = baseTokenURI_;
    }

    /**
     * @dev Mints a new NFT
     * @param to Address to mint the NFT to
     * @param nftType Type of NFT to mint
     * @param attributes Packed attributes for the NFT
     * @param tokenURI_ Optional token URI (empty for default)
     */
    function mintNFT(
        address to,
        NFTType nftType,
        uint256 attributes,
        string memory tokenURI_
    ) external onlyOwner returns (uint256) {
        Counters.Counter storage tokenIdCounter;
        if (nftType == NFTType.LAND) {
            tokenIdCounter = _landTokenIds;
        } else if (nftType == NFTType.HERO) {
            tokenIdCounter = _heroTokenIds;
        } else {
            tokenIdCounter = _artifactTokenIds;
        }

        tokenIdCounter.increment();
        uint256 newTokenId = tokenIdCounter.current();

        _mint(to, newTokenId);
        
        _tokenMetadata[newTokenId] = NFTMetadata({
            nftType: nftType,
            attributes: attributes,
            tokenURI: bytes(tokenURI_).length > 0 ? tokenURI_ : string(abi.encodePacked(_baseTokenURI, uint256(nftType), "/", newTokenId))
        });

        emit NFTMinted(to, newTokenId, nftType);
        return newTokenId;
    }

    /**
     * @dev Updates NFT attributes
     * @param tokenId ID of the NFT to update
     * @param newAttributes New packed attributes
     */
    function updateAttributes(uint256 tokenId, uint256 newAttributes) external {
        require(_isApprovedOrOwner(_msgSender(), tokenId), "Caller is not owner nor approved");
        _tokenMetadata[tokenId].attributes = newAttributes;
        emit NFTAttributesUpdated(tokenId, newAttributes);
    }

    /**
     * @dev Returns NFT metadata
     * @param tokenId ID of the NFT
     */
    function getNFTMetadata(uint256 tokenId) external view returns (NFTType, uint256, string memory) {
        require(_exists(tokenId), "NFT does not exist");
        NFTMetadata memory metadata = _tokenMetadata[tokenId];
        return (metadata.nftType, metadata.attributes, metadata.tokenURI);
    }

    /**
     * @dev Sets base URI for token metadata
     * @param baseTokenURI New base URI
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Overrides ERC721's tokenURI
     * @param tokenId ID of the token
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        return _tokenMetadata[tokenId].tokenURI;
    }

    // The following functions are overrides required by Solidity
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override(ERC721, ERC721Enumerable) {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
