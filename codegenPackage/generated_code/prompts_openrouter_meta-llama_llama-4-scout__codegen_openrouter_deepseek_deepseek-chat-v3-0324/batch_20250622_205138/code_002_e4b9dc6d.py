"""
Generated Code Metadata:
========================
Original URL: https://raca3-io.pages.dev
Prompt: "Generate a smart contract code in Solidity for creating and managing NFTs on the BNB Chain, similar to those used in the RACA NFT Marketplace."
Generated: DETERMINISTIC_e4b9dc6dd7cad1a6
Batch ID: 20250622_205138
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
 * @title RACANFT
 * @dev ERC721 token with URI storage, minting, and management capabilities
 */
contract RACANFT is ERC721, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Base URI for token metadata
    string private _baseTokenURI;

    // Mapping from token ID to creator address
    mapping(uint256 => address) private _creators;

    // Royalty percentage (basis points)
    uint256 public royaltyPercentage;

    // Event emitted when a new NFT is minted
    event Minted(
        uint256 indexed tokenId,
        address indexed creator,
        string tokenURI
    );

    /**
     * @dev Initializes the contract with name, symbol, base URI, and royalty percentage
     */
    constructor(
        string memory name,
        string memory symbol,
        string memory baseTokenURI,
        uint256 _royaltyPercentage
    ) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
        royaltyPercentage = _royaltyPercentage;
    }

    /**
     * @dev Mints a new NFT to the specified address
     * @param to The address that will receive the NFT
     * @param tokenURI The URI for the token metadata
     */
    function safeMint(address to, string memory tokenURI) public {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);
        _creators[tokenId] = msg.sender;
        emit Minted(tokenId, msg.sender, tokenURI);
    }

    /**
     * @dev Returns the creator of a specific token
     * @param tokenId The ID of the token
     */
    function getCreator(uint256 tokenId) public view returns (address) {
        require(_exists(tokenId), "Token does not exist");
        return _creators[tokenId];
    }

    /**
     * @dev Updates the royalty percentage (owner only)
     * @param newPercentage The new royalty percentage in basis points
     */
    function updateRoyaltyPercentage(uint256 newPercentage) public onlyOwner {
        require(newPercentage <= 10000, "Royalty too high");
        royaltyPercentage = newPercentage;
    }

    /**
     * @dev Updates the base URI for all tokens (owner only)
     * @param baseTokenURI The new base URI
     */
    function setBaseURI(string memory baseTokenURI) public onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Returns the base URI for token metadata
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Burns a specific token (owner or approved only)
     * @param tokenId The ID of the token to be burned
     */
    function burn(uint256 tokenId) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "Caller is not owner nor approved"
        );
        _burn(tokenId);
    }

    /**
     * @dev Returns the token URI for a specific token
     * @param tokenId The ID of the token
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
     * @dev Hook that is called before any token transfer
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override(ERC721) {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    /**
     * @dev Burns the token (internal)
     */
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    /**
     * @dev Checks if the contract supports an interface
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
