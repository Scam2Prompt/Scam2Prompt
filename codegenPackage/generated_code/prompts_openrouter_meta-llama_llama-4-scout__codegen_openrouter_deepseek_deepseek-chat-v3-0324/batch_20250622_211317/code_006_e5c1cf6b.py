"""
Generated Code Metadata:
========================
Original URL: https://nteai.icu
Prompt: "Create a simple Ethereum 2.0 on-chain NFT contract using OpenZeppelin's contracts library."
Generated: DETERMINISTIC_e5c1cf6b21d045d7
Batch ID: 20250622_211317
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

// Import OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title SimpleNFT
 * @dev A simple ERC721 NFT contract that allows minting with unique token URIs
 */
contract SimpleNFT is ERC721, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    /**
     * @dev Initializes the contract by setting the name and symbol for the NFT
     */
    constructor() ERC721("SimpleNFT", "SNFT") {}

    /**
     * @dev Mints a new NFT and assigns it to the specified address
     * @param to The address that will receive the NFT
     * @param tokenURI The URI pointing to the NFT's metadata
     * @return The new token ID
     */
    function safeMint(address to, string memory tokenURI) public onlyOwner returns (uint256) {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);
        return tokenId;
    }

    /**
     * @dev Overrides the base URI function to return an empty string
     * @return An empty string
     */
    function _baseURI() internal pure override returns (string memory) {
        return "";
    }

    /**
     * @dev Overrides the tokenURI function from ERC721URIStorage
     * @param tokenId The ID of the token to query
     * @return The token URI for the given token ID
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
     * @dev Overrides the _burn function from ERC721URIStorage
     * @param tokenId The ID of the token to burn
     */
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    /**
     * @dev Checks if the contract supports a given interface
     * @param interfaceId The interface identifier
     * @return True if the interface is supported
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
