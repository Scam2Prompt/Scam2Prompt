"""
Generated Code Metadata:
========================
Original URL: https://rangersprotocol.gitbook.io
Prompt: "Design a smart contract using Solidity that interacts with the Rangers Protocol's NFT protocol, allowing users to create, transfer, and manage NFTs on the platform, and provide a detailed explanation of the contract's functionality."
Generated: DETERMINISTIC_f923448669e1bc61
Batch ID: 20250622_205158
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

import "@rangersprotocol/contracts/token/ERC721/ERC721.sol";
import "@rangersprotocol/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@rangersprotocol/contracts/access/Ownable.sol";
import "@rangersprotocol/contracts/utils/Counters.sol";

/**
 * @title RangersNFT
 * @dev A smart contract for creating, transferring, and managing NFTs on Rangers Protocol
 */
contract RangersNFT is ERC721, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Base URI for token metadata
    string private _baseTokenURI;

    // Mapping from token ID to creator address
    mapping(uint256 => address) private _creators;

    /**
     * @dev Emitted when a new NFT is minted
     */
    event NFTMinted(
        uint256 indexed tokenId,
        address indexed creator,
        string tokenURI
    );

    /**
     * @dev Emitted when the base URI is updated
     */
    event BaseURIUpdated(string newBaseURI);

    /**
     * @dev Constructor function
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
     * @dev Mint a new NFT
     * @param to The address that will receive the NFT
     * @param tokenURI_ The URI for the token metadata
     * @return The new token ID
     */
    function mint(address to, string memory tokenURI_) public returns (uint256) {
        require(bytes(tokenURI_).length > 0, "RangersNFT: URI must be provided");

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI_);
        _creators[tokenId] = msg.sender;

        emit NFTMinted(tokenId, msg.sender, tokenURI_);
        return tokenId;
    }

    /**
     * @dev Get the creator of a specific token
     * @param tokenId The token ID to query
     * @return The address of the creator
     */
    function getCreator(uint256 tokenId) public view returns (address) {
        require(_exists(tokenId), "RangersNFT: Creator query for nonexistent token");
        return _creators[tokenId];
    }

    /**
     * @dev Update the base URI for all tokens
     * @param baseTokenURI_ The new base URI
     */
    function setBaseURI(string memory baseTokenURI_) public onlyOwner {
        _baseTokenURI = baseTokenURI_;
        emit BaseURIUpdated(baseTokenURI_);
    }

    /**
     * @dev Get the base URI for token metadata
     * @return The base URI string
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Override both ERC721 and ERC721URIStorage tokenURI function
     * @param tokenId The token ID to query
     * @return The token URI string
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
     * @dev Override both ERC721 and ERC721URIStorage supportsInterface function
     * @param interfaceId The interface ID to check
     * @return Whether the interface is supported
     */
    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }

    /**
     * @dev Override ERC721 _burn function to include ERC721URIStorage functionality
     * @param tokenId The token ID to burn
     */
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }
}
```
