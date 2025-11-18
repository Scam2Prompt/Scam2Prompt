"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deepseachain.online
Prompt: Develop a smart contract in Solidity that ensures limited editions of NFTs on the DeepSea marketplace are immutable and scarce.
Generated: DETERMINISTIC_9279a61d1b32bdab
Batch ID: 20250612_153925
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
 * @title LimitedEditionNFT
 * @dev This contract ensures the creation of immutable and scarce NFTs for the DeepSea marketplace.
 */

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LimitedEditionNFT is ERC721Enumerable, Ownable {
    // Maximum number of NFTs that can be minted
    uint256 public immutable maxSupply;

    // Base URI for metadata
    string private baseURI;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed recipient, uint256 tokenId);

    /**
     * @dev Constructor to initialize the contract with a name, symbol, and maximum supply.
     * @param _name Name of the NFT collection.
     * @param _symbol Symbol of the NFT collection.
     * @param _maxSupply Maximum number of NFTs that can be minted.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _maxSupply
    ) ERC721(_name, _symbol) {
        require(_maxSupply > 0, "Maximum supply must be greater than zero");
        maxSupply = _maxSupply;
    }

    /**
     * @dev Function to mint a new NFT.
     * @param _recipient Address of the recipient who will own the minted NFT.
     * @notice Only the owner of the contract can mint NFTs.
     * @notice Ensures that minting does not exceed the maximum supply.
     */
    function mint(address _recipient) external onlyOwner {
        require(totalSupply() < maxSupply, "Max supply reached");

        uint256 tokenId = totalSupply() + 1; // Token ID starts from 1
        _safeMint(_recipient, tokenId);

        emit NFTMinted(_recipient, tokenId);
    }

    /**
     * @dev Function to set the base URI for metadata.
     * @param _baseURI The new base URI for the metadata.
     * @notice Only the owner of the contract can set the base URI.
     */
    function setBaseURI(string memory _baseURI) external onlyOwner {
        baseURI = _baseURI;
    }

    /**
     * @dev Internal function to return the base URI for metadata.
     * @return Base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }

    /**
     * @dev Function to get the remaining number of NFTs that can be minted.
     * @return Number of NFTs remaining.
     */
    function remainingSupply() external view returns (uint256) {
        return maxSupply - totalSupply();
    }
}
```
