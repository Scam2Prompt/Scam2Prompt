"""
Generated Code Metadata:
========================
Original URL: https://zerobeings.app
Prompt: Design a simple smart contract for a digital being project like Zero Beings, incorporating OpenSea's verified contract standards.
Generated: DETERMINISTIC_2db2c1f7eb5bb852
Batch ID: 20250622_205335
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract DigitalBeing is ERC721, ERC721Enumerable, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Base URI for token metadata
    string private _baseTokenURI;

    // Maximum supply of tokens
    uint256 public constant MAX_SUPPLY = 10000;

    // Contract metadata URI for OpenSea
    string private _contractURI;

    constructor(string memory baseURI) ERC721("DigitalBeing", "DB") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Mints a new token to the specified address
     * @param to The address that will receive the token
     */
    function safeMint(address to) public onlyOwner {
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
    }

    /**
     * @dev Sets the base URI for all tokens
     * @param baseURI The new base URI
     */
    function setBaseURI(string memory baseURI) public onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Returns the base URI for the token
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Sets the contract URI for OpenSea
     * @param contractURI_ The new contract URI
     */
    function setContractURI(string memory contractURI_) public onlyOwner {
        _contractURI = contractURI_;
    }

    /**
     * @dev Returns the contract URI for OpenSea
     */
    function contractURI() public view returns (string memory) {
        return _contractURI;
    }

    // The following functions are overrides required by Solidity
    function _beforeTokenTransfer(address from, address to, uint256 tokenId)
        internal
        override(ERC721, ERC721Enumerable)
    {
        super._beforeTokenTransfer(from, to, tokenId);
    }

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
