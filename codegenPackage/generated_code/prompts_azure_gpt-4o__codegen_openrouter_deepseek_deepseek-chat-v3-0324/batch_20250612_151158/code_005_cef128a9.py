"""
Generated Code Metadata:
========================
Original URL: https://live-tensorians.pages.dev
Prompt: Create a smart contract example for managing digital assets or collectibles, inspired by the Tensorians platform.
Generated: DETERMINISTIC_cef128a98bbbb56a
Batch ID: 20250612_151158
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

/**
 * @title DigitalAssetManager
 * @dev A smart contract for managing digital assets/collectibles with features inspired by Tensorians
 */
contract DigitalAssetManager is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    // Token counter
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Maximum supply of tokens
    uint256 public constant MAX_SUPPLY = 10000;

    // Royalty information
    struct RoyaltyInfo {
        address recipient;
        uint24 amount;
    }

    // Mapping from token ID to royalty info
    mapping(uint256 => RoyaltyInfo) private _royalties;

    // Event emitted when a new token is minted
    event TokenMinted(address indexed to, uint256 indexed tokenId);

    // Event emitted when royalty info is updated
    event RoyaltyUpdated(uint256 indexed tokenId, address recipient, uint256 amount);

    /**
     * @dev Constructor
     * @param name_ Name of the token
     * @param symbol_ Symbol of the token
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
     * @dev Mints a new token to the specified address
     * @param to Address to mint the token to
     * @param royaltyRecipient Address to receive royalties
     * @param royaltyValue Royalty percentage (basis points)
     */
    function safeMint(
        address to,
        address royaltyRecipient,
        uint24 royaltyValue
    ) external onlyOwner {
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");
        require(royaltyValue <= 10000, "Royalty too high");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(to, tokenId);
        _setRoyaltyInfo(tokenId, royaltyRecipient, royaltyValue);
        
        emit TokenMinted(to, tokenId);
    }

    /**
     * @dev Returns the total supply of tokens
     * @return uint256 Total supply
     */
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }

    /**
     * @dev Sets royalty information for a token
     * @param tokenId ID of the token
     * @param recipient Address to receive royalties
     * @param value Royalty percentage (basis points)
     */
    function _setRoyaltyInfo(
        uint256 tokenId,
        address recipient,
        uint24 value
    ) internal {
        require(_exists(tokenId), "Nonexistent token");
        require(value <= 10000, "Royalty too high");
        
        _royalties[tokenId] = RoyaltyInfo(recipient, value);
        emit RoyaltyUpdated(tokenId, recipient, value);
    }

    /**
     * @dev Updates royalty information for a token
     * @param tokenId ID of the token
     * @param recipient Address to receive royalties
     * @param value Royalty percentage (basis points)
     */
    function updateRoyaltyInfo(
        uint256 tokenId,
        address recipient,
        uint24 value
    ) external onlyOwner {
        _setRoyaltyInfo(tokenId, recipient, value);
    }

    /**
     * @dev Returns royalty information for a token
     * @param tokenId ID of the token
     * @return recipient Address to receive royalties
     * @return amount Royalty percentage (basis points)
     */
    function royaltyInfo(uint256 tokenId)
        external
        view
        returns (address recipient, uint256 amount)
    {
        require(_exists(tokenId), "Nonexistent token");
        RoyaltyInfo memory royalty = _royalties[tokenId];
        return (royalty.recipient, royalty.amount);
    }

    /**
     * @dev Sets the base URI for all tokens
     * @param baseURI New base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Returns the base URI
     * @return string Base URI
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Returns the token URI for a given token ID
     * @param tokenId ID of the token
     * @return string Token URI
     */
    function tokenURI(uint256 tokenId)
        public
        view
        override
        returns (string memory)
    {
        require(_exists(tokenId), "Nonexistent token");
        return string(abi.encodePacked(_baseTokenURI, tokenId.toString()));
    }

    /**
     * @dev Overrides supportsInterface to include royalty interface
     * @param interfaceId Interface ID to check
     * @return bool Whether the interface is supported
     */
    function supportsInterface(bytes4 interfaceId)
        public
        view
        override
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
