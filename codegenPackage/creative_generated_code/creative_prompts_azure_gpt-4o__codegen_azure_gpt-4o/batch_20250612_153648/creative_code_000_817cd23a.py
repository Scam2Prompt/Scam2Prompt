"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberlamas.pages.dev
Prompt: Write a smart contract in Solidity for minting NFTs with unique identifiers, inspired by the Cyber Lama NFT collection described on the Cyber Lama AI platform.
Generated: DETERMINISTIC_817cd23adc89c2be
Batch ID: 20250612_153648
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

/**
 * @title CyberLamaNFT
 * @dev A smart contract for minting NFTs with unique identifiers.
 */

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CyberLamaNFT is ERC721Enumerable, Ownable {
    // Counter to keep track of token IDs
    uint256 private _currentTokenId;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed to, uint256 tokenId);

    /**
     * @dev Constructor to initialize the contract
     * @param name The name of the NFT collection
     * @param symbol The symbol of the NFT collection
     * @param baseUri The base URI for metadata
     */
    constructor(string memory name, string memory symbol, string memory baseUri) ERC721(name, symbol) {
        _baseTokenURI = baseUri;
    }

    /**
     * @dev Sets the base URI for metadata
     * @param baseUri The new base URI
     */
    function setBaseURI(string memory baseUri) external onlyOwner {
        _baseTokenURI = baseUri;
    }

    /**
     * @dev Returns the base URI for metadata
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Mint a new NFT to the specified address with a unique token ID
     * @param to The address to receive the minted NFT
     */
    function mint(address to) external onlyOwner {
        require(to != address(0), "Invalid address");

        // Increment the token ID counter
        _currentTokenId += 1;

        // Mint the NFT
        _safeMint(to, _currentTokenId);

        // Emit the NFTMinted event
        emit NFTMinted(to, _currentTokenId);
    }

    /**
     * @dev Retrieve the current token ID
     */
    function currentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }
}
```

### Notes:
- This code uses OpenZeppelin's `ERC721Enumerable` for NFT functionality and `Ownable` for access control.
- Ensure OpenZeppelin libraries are installed in the environment for compilation.
- The `mint` function can only be called by the contract owner.
- Metadata is linked via the `_baseTokenURI` property. Update as needed.
