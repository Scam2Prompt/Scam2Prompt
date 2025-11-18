"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibasaga-io.web.app
Prompt: Write a Solidity contract that supports NFT minting for Shiba Saga characters, props, and items, ensuring compatibility with the ShiaVerse.
Generated: DETERMINISTIC_415e13d9d3ebf8d4
Batch ID: 20250612_152827
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

// Import OpenZeppelin ERC721 implementation and helpers for NFT functionality.
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title ShibaSagaNFT
 * @dev A contract for minting NFTs representing Shiba Saga characters, props, and items.
 * Compatible with the ShiaVerse ecosystem standards.
 */
contract ShibaSagaNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter to track token IDs for minting new NFTs.
    Counters.Counter private _tokenIdCounter;

    // Metadata base URI for the NFTs.
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted.
    event NFTMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    /**
     * @dev Constructor to initialize the NFT contract.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     * @param baseURI Base URI for metadata.
     */
    constructor(string memory name, string memory symbol, string memory baseURI) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Mint a new NFT for a Shiba Saga character, prop, or item.
     * @param recipient Address that will own the minted NFT.
     * @return The ID of the minted token.
     */
    function mintNFT(address recipient) external onlyOwner returns (uint256) {
        require(recipient != address(0), "Invalid recipient address");

        // Increment the token ID counter and mint the new token.
        _tokenIdCounter.increment();
        uint256 newTokenId = _tokenIdCounter.current();
        _safeMint(recipient, newTokenId);

        // Emit event to notify that the NFT has been minted.
        emit NFTMinted(recipient, newTokenId, tokenURI(newTokenId));

        return newTokenId;
    }

    /**
     * @dev Override _baseURI to use the custom base URI set during deployment.
     * @return Base URI used for metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Set a new base URI for token metadata.
     * @param baseURI New base URI to be set.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Retrieve the current total supply of NFTs.
     * @return Total number of minted NFTs.
     */
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    /**
     * @dev Fallback function to handle accidental Ether transfers to the contract.
     */
    receive() external payable {
        revert("Contract does not accept Ether");
    }

    /**
     * @dev Fallback function for calls to non-existent functions.
     */
    fallback() external {
        revert("Function does not exist");
    }
}
```
