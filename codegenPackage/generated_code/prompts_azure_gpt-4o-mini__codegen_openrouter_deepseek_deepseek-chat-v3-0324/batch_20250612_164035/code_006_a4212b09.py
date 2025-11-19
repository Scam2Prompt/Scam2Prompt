"""
Generated Code Metadata:
========================
Original URL: https://doglibretoken.web.app
Prompt: Design a simple NFT minting function for DogLibre's gamified NFTs, ensuring it aligns with their multichain strategy across Ethereum and Polygon.
Generated: DETERMINISTIC_a4212b09a32b21ef
Batch ID: 20250612_164035
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title DogLibreNFT
 * @dev A gamified NFT contract supporting multichain minting (Ethereum & Polygon)
 * with metadata storage and ownership control
 */
contract DogLibreNFT is ERC721, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Chain constants
    uint256 public constant ETHEREUM_CHAIN_ID = 1;
    uint256 public constant POLYGON_CHAIN_ID = 137;

    // Base URI for metadata
    string private _baseTokenURI;

    // Chain ID this contract is deployed on
    uint256 public immutable chainId;

    // Mapping from token ID to game attributes
    mapping(uint256 => bytes32) private _gameAttributes;

    // Event emitted when NFT is minted
    event Minted(
        address indexed to,
        uint256 indexed tokenId,
        uint256 chainId,
        bytes32 gameAttributes
    );

    /**
     * @dev Constructor
     * @param name NFT name
     * @param symbol NFT symbol
     * @param baseTokenURI Base URI for token metadata
     * @param _chainId Chain ID (1 for Ethereum, 137 for Polygon)
     */
    constructor(
        string memory name,
        string memory symbol,
        string memory baseTokenURI,
        uint256 _chainId
    ) ERC721(name, symbol) {
        require(
            _chainId == ETHEREUM_CHAIN_ID || _chainId == POLYGON_CHAIN_ID,
            "Unsupported chain"
        );
        _baseTokenURI = baseTokenURI;
        chainId = _chainId;
    }

    /**
     * @dev Mints a new NFT with game attributes
     * @param to Address to mint NFT to
     * @param tokenURI URI for token metadata
     * @param attributes Game-specific attributes encoded as bytes32
     */
    function safeMint(
        address to,
        string memory tokenURI,
        bytes32 attributes
    ) external onlyOwner {
        require(to != address(0), "Cannot mint to zero address");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);
        _gameAttributes[tokenId] = attributes;

        emit Minted(to, tokenId, chainId, attributes);
    }

    /**
     * @dev Returns the game attributes for a given token ID
     * @param tokenId Token ID to query
     * @return Game attributes in bytes32 format
     */
    function getGameAttributes(uint256 tokenId) external view returns (bytes32) {
        require(_exists(tokenId), "Token does not exist");
        return _gameAttributes[tokenId];
    }

    /**
     * @dev Updates the base URI for all tokens
     * @param baseURI New base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Returns the base URI for token metadata
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Burns a token. Only callable by owner or token owner
     * @param tokenId Token ID to burn
     */
    function burn(uint256 tokenId) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "Not owner nor approved"
        );
        _burn(tokenId);
    }

    /**
     * @dev Override required by Solidity for ERC721 & ERC721URIStorage
     * @param tokenId Token ID
     */
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
        delete _gameAttributes[tokenId];
    }

    /**
     * @dev Returns token URI
     * @param tokenId Token ID
     */
    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    /**
     * @dev Validates if contract supports an interface
     * @param interfaceId Interface ID to check
     */
    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
