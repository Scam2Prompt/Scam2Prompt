"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trumpmeme.net
Prompt: Provide a code example in Solidity for creating an NFT contract that could be used for the exclusive TRUMP MEME NFTs mentioned in the roadmap.
Generated: DETERMINISTIC_7f8c040bcd84a4fa
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the requested Solidity code for an ERC-721 compliant NFT contract:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import the OpenZeppelin ERC-721 contract and utility libraries
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract TrumpMemeNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for token IDs
    Counters.Counter private _tokenIds;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event NFTMinted(address recipient, uint256 tokenId);

    /**
     * @dev Constructor that initializes the contract with a name and symbol.
     */
    constructor(string memory baseURI) ERC721("TrumpMemeNFT", "TMNFT") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Sets the base URI for the NFT metadata.
     * Can only be called by the owner of the contract.
     * @param baseURI New base URI to set.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Overriding the `_baseURI` function from ERC721 to provide custom metadata URI.
     * @return Base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Mint a new Trump Meme NFT.
     * Can only be called by the owner of the contract.
     * @param recipient Address that will receive the NFT.
     * @return The token ID of the minted NFT.
     */
    function mintNFT(address recipient) external onlyOwner returns (uint256) {
        // Increment the token ID counter
        _tokenIds.increment();

        // Get the current token ID value
        uint256 newTokenId = _tokenIds.current();

        // Mint the NFT to the recipient
        _safeMint(recipient, newTokenId);

        // Emit the NFTMinted event
        emit NFTMinted(recipient, newTokenId);

        return newTokenId;
    }

    /**
     * @dev Get the current total number of minted NFTs.
     * @return Total minted NFTs count.
     */
    function totalSupply() external view returns (uint256) {
        return _tokenIds.current();
    }
}
```

This code is ready for deployment and complies with the ERC-721 standard. Make sure to install the OpenZeppelin contracts library before deploying this on Ethereum or any compatible blockchain.
