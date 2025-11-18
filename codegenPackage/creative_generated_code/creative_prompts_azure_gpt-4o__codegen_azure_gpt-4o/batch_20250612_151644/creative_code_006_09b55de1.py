"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerobeings.app
Prompt: Generate a Solidity contract template for an NFT project that adheres to CC0 licensing, as referenced by "Zero Beings."
Generated: DETERMINISTIC_09b55de19de3067b
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: CC0-1.0
pragma solidity ^0.8.0;

/**
 * @title ZeroBeingsNFT
 * @dev A CC0-licensed ERC721 NFT contract for the "Zero Beings" project.
 * @notice This contract adheres to the CC0 (Creative Commons Zero) licensing, allowing all works to be freely shared and reused.
 */

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract ZeroBeingsNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter to keep track of token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when base URI is updated
    event BaseURIUpdated(string newBaseURI);

    // Event emitted when a new token is minted
    event NFTMinted(address indexed to, uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the NFT contract.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Sets the base URI for all token metadata.
     * @param baseURI The new base URI.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
        emit BaseURIUpdated(baseURI);
    }

    /**
     * @dev Returns the base URI for the token metadata.
     * @return The base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Mints a new NFT to the specified address.
     * @param to The address to receive the minted NFT.
     * @return tokenId The ID of the newly minted token.
     */
    function mint(address to) external onlyOwner returns (uint256 tokenId) {
        require(to != address(0), "ZeroBeingsNFT: Cannot mint to the zero address");

        _tokenIdCounter.increment();
        tokenId = _tokenIdCounter.current();
        _safeMint(to, tokenId);

        emit NFTMinted(to, tokenId);
    }

    /**
     * @dev Returns the total number of tokens minted.
     * @return Total token count.
     */
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("ZeroBeingsNFT: Contract does not accept ETH");
    }

    /**
     * @dev Function to receive ETH (if applicable). Reverts by default.
     */
    receive() external payable {
        revert("ZeroBeingsNFT: Contract does not accept ETH");
    }
}
```
