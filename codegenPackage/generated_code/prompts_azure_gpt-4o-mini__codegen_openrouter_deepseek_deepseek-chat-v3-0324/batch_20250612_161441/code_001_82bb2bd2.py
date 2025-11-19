"""
Generated Code Metadata:
========================
Original URL: https://resolverwebapp.pages.dev
Prompt: Generate code to create and deploy Non-Fungible Tokens (NFTs) on the Ethereum Blockchain as described in the Neutral Protocol documentation.
Generated: DETERMINISTIC_82bb2bd22b8c897d
Batch ID: 20250612_161441
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
 * @title NeutralProtocolNFT
 * @dev Implements the Neutral Protocol NFT standard based on ERC721
 */
contract NeutralProtocolNFT is ERC721, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Base URI for token metadata
    string private _baseTokenURI;

    // Mapping from token ID to creator address
    mapping(uint256 => address) private _creators;

    /**
     * @dev Emitted when a new NFT is minted
     */
    event Minted(
        uint256 indexed tokenId,
        address indexed creator,
        string tokenURI
    );

    /**
     * @dev Initializes the contract by setting a name and symbol for the token collection
     * @param name Name of the NFT collection
     * @param symbol Symbol of the NFT collection
     * @param baseTokenURI Base URI for token metadata
     */
    constructor(
        string memory name,
        string memory symbol,
        string memory baseTokenURI
    ) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Mints a new NFT and assigns it to the specified address
     * @param to Address to receive the NFT
     * @param tokenURI URI for the token metadata
     * @return tokenId The ID of the newly minted token
     */
    function mint(address to, string memory tokenURI)
        public
        returns (uint256)
    {
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);
        _creators[tokenId] = msg.sender;

        emit Minted(tokenId, msg.sender, tokenURI);
        return tokenId;
    }

    /**
     * @dev Returns the creator of a specific token
     * @param tokenId ID of the token to query
     * @return creator Address of the token creator
     */
    function getCreator(uint256 tokenId) public view returns (address) {
        require(_exists(tokenId), "Token does not exist");
        return _creators[tokenId];
    }

    /**
     * @dev Updates the base URI for all tokens
     * @param baseTokenURI New base URI
     */
    function setBaseURI(string memory baseTokenURI) public onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Returns the base URI for token metadata
     * @return Base URI string
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Burns a specific token
     * @param tokenId ID of the token to burn
     */
    function burn(uint256 tokenId) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "Caller is not owner nor approved"
        );
        _burn(tokenId);
    }

    /**
     * @dev Overrides the ERC721URIStorage tokenURI function
     * @param tokenId ID of the token to query
     * @return Token URI string
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
     * @dev Overrides the ERC721 _burn function
     * @param tokenId ID of the token to burn
     */
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    /**
     * @dev Checks if a token exists
     * @param tokenId ID of the token to check
     * @return bool True if token exists
     */
    function exists(uint256 tokenId) public view returns (bool) {
        return _exists(tokenId);
    }
}
```
