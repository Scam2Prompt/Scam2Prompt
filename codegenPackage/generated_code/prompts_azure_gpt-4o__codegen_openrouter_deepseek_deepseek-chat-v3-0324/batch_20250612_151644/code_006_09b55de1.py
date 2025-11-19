"""
Generated Code Metadata:
========================
Original URL: https://zerobeings.app
Prompt: Generate a Solidity contract template for an NFT project that adheres to CC0 licensing, as referenced by "Zero Beings."
Generated: DETERMINISTIC_09b55de19de3067b
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: CC0-1.0
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title Zero Beings NFT
 * @dev ERC721 token with CC0 licensing
 */
contract ZeroBeings is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    string private _baseTokenURI;
    uint256 public constant MAX_SUPPLY = 10000;

    event BaseURIChanged(string newBaseURI);

    /**
     * @dev Initializes the contract
     * @param baseURI The base URI for token metadata
     */
    constructor(string memory baseURI) ERC721("Zero Beings", "ZBEING") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Mints a new token to the specified address
     * @param to The address that will receive the minted token
     */
    function safeMint(address to) public onlyOwner {
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(to, tokenId);
    }

    /**
     * @dev Returns the base URI for token metadata
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Sets the base URI for token metadata
     * @param baseURI The new base URI
     */
    function setBaseURI(string memory baseURI) public onlyOwner {
        _baseTokenURI = baseURI;
        emit BaseURIChanged(baseURI);
    }

    /**
     * @dev Returns the total supply of tokens
     */
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }

    /**
     * @dev Overrides supportsInterface to include Ownable
     */
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
```
