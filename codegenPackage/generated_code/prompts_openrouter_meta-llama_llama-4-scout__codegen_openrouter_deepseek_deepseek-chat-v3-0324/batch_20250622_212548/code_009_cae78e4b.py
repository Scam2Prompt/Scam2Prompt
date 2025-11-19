"""
Generated Code Metadata:
========================
Original URL: https://saitachaincoin.live
Prompt: "Design a simple NFT minting contract on SaitaChain, allowing users to create and manage their own unique digital assets."
Generated: DETERMINISTIC_cae78e4bd062e9aa
Batch ID: 20250622_212548
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

contract SaitaChainNFT is ERC721, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Base URI for token metadata
    string private _baseTokenURI;

    // Mapping to track minted token URIs to prevent duplicates
    mapping(string => bool) private _mintedURIs;

    // Events
    event NFTMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);
    event BaseURIUpdated(string newBaseURI);

    constructor(string memory name, string memory symbol, string memory baseTokenURI) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Mints a new NFT with the given URI
     * @param to The address that will own the minted NFT
     * @param tokenURI The URI pointing to the NFT metadata
     */
    function safeMint(address to, string memory tokenURI) public {
        require(bytes(tokenURI).length > 0, "SaitaChainNFT: Token URI cannot be empty");
        require(!_mintedURIs[tokenURI], "SaitaChainNFT: Token URI already minted");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _mintedURIs[tokenURI] = true;
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);

        emit NFTMinted(to, tokenId, tokenURI);
    }

    /**
     * @dev Updates the base URI for all tokens
     * @param newBaseURI The new base URI
     */
    function updateBaseURI(string memory newBaseURI) public onlyOwner {
        require(bytes(newBaseURI).length > 0, "SaitaChainNFT: Base URI cannot be empty");
        _baseTokenURI = newBaseURI;
        emit BaseURIUpdated(newBaseURI);
    }

    /**
     * @dev Returns the base URI for the contract
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Burns a specific NFT
     * @param tokenId The ID of the NFT to burn
     */
    function burn(uint256 tokenId) public {
        require(_isApprovedOrOwner(_msgSender(), tokenId), "SaitaChainNFT: Caller is not owner nor approved");
        _burn(tokenId);
    }

    /**
     * @dev Returns whether the specified token URI has been minted
     * @param tokenURI The token URI to check
     */
    function isURIMinted(string memory tokenURI) public view returns (bool) {
        return _mintedURIs[tokenURI];
    }

    /**
     * @dev Returns the current token ID counter value
     */
    function getCurrentTokenId() public view returns (uint256) {
        return _tokenIdCounter.current();
    }

    // The following functions are overrides required by Solidity
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }
}
```
