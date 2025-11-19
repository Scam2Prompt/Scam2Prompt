"""
Generated Code Metadata:
========================
Original URL: https://kevinland.pages.dev
Prompt: Write a smart contract in Solidity that reserves intellectual property rights for the NFT project team, while granting specific rights to NFT owners, as described in KevinLand's terms.
Generated: DETERMINISTIC_420f31433f30405c
Batch ID: 20250612_152827
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
import "@openzeppelin/contracts/utils/Strings.sol";

/**
 * @title KevinLandNFT
 * @dev NFT contract with intellectual property rights management
 */
contract KevinLandNFT is ERC721, Ownable {
    using Strings for uint256;

    // Base URI for metadata
    string private _baseTokenURI;

    // Mapping from token ID to IP rights
    mapping(uint256 => bool) private _commercialRightsGranted;

    /**
     * @dev Emitted when commercial rights are granted for a token
     */
    event CommercialRightsGranted(uint256 indexed tokenId, address indexed owner);

    /**
     * @dev Emitted when commercial rights are revoked for a token
     */
    event CommercialRightsRevoked(uint256 indexed tokenId, address indexed owner);

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
     * @param tokenId ID of the NFT to mint
     */
    function mint(address to, uint256 tokenId) public onlyOwner {
        _safeMint(to, tokenId);
    }

    /**
     * @dev Grants commercial rights for a specific NFT to its owner
     * @param tokenId ID of the NFT
     */
    function grantCommercialRights(uint256 tokenId) public {
        require(_isApprovedOrOwner(_msgSender(), tokenId), "Caller is not owner nor approved");
        require(!_commercialRightsGranted[tokenId], "Commercial rights already granted");
        
        _commercialRightsGranted[tokenId] = true;
        emit CommercialRightsGranted(tokenId, ownerOf(tokenId));
    }

    /**
     * @dev Revokes commercial rights for a specific NFT (only owner can call)
     * @param tokenId ID of the NFT
     */
    function revokeCommercialRights(uint256 tokenId) public onlyOwner {
        require(_commercialRightsGranted[tokenId], "Commercial rights not granted");
        
        _commercialRightsGranted[tokenId] = false;
        emit CommercialRightsRevoked(tokenId, ownerOf(tokenId));
    }

    /**
     * @dev Checks if commercial rights are granted for a specific NFT
     * @param tokenId ID of the NFT
     * @return bool True if commercial rights are granted
     */
    function hasCommercialRights(uint256 tokenId) public view returns (bool) {
        return _commercialRightsGranted[tokenId];
    }

    /**
     * @dev Returns the base URI for token metadata
     * @return string Base URI
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Updates the base URI for token metadata (only owner can call)
     * @param baseTokenURI New base URI
     */
    function setBaseURI(string memory baseTokenURI) public onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Returns the token URI for a given token ID
     * @param tokenId ID of the NFT
     * @return string Token URI
     */
    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        
        string memory baseURI = _baseURI();
        return bytes(baseURI).length > 0 
            ? string(abi.encodePacked(baseURI, tokenId.toString(), ".json")) 
            : "";
    }

    /**
     * @dev Overrides transfer functions to maintain IP rights status
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, tokenId);
        
        // Commercial rights are maintained during transfer
    }
}
```
