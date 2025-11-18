"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jpegsfun.pages.dev
Prompt: Implement a smart contract that adheres to the no-presales, no-whitelists, and no-team-allocations policy described on jpegs.fun.
Generated: DETERMINISTIC_cc7d09b36de6167c
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin's ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title NoPresalesNoWhitelistsNoTeamAllocations
 * @dev This contract implements an NFT collection with no presales, no whitelists, and no team allocations.
 */
contract NoPresalesNoWhitelistsNoTeamAllocations is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Max supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Mapping to track if a token is minted
    mapping(uint256 => bool) private _mintedTokens;

    // Event to notify when a new token is minted
    event TokenMinted(address indexed owner, uint256 indexed tokenId);

    // Constructor to initialize the contract with a base URI
    constructor(string memory baseURI) ERC721("No Presales No Whitelists No Team Allocations", "NPNW") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Mint a new NFT. No presales or whitelists are allowed.
     * Each address can mint a maximum of one NFT.
     */
    function mint() external {
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");
        require(!_mintedTokens[_tokenIdCounter.current()], "Token has already been minted");

        uint256 tokenId = _tokenIdCounter.current();
        _mintedTokens[tokenId] = true;

        _mint(msg.sender, tokenId);
        emit TokenMinted(msg.sender, tokenId);

        // Increment the token ID counter
        _tokenIdCounter.increment();
    }

    /**
     * @dev Override the _baseURI function to return the base URI for metadata.
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Update the base URI for metadata. Only the owner can update it.
     * @param newBaseURI The new base URI to set.
     */
    function setBaseURI(string memory newBaseURI) external onlyOwner {
        _baseTokenURI = newBaseURI;
    }

    /**
     * @dev Get the current token ID counter (for informational purposes).
     * @return The current token ID.
     */
    function currentTokenId() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
