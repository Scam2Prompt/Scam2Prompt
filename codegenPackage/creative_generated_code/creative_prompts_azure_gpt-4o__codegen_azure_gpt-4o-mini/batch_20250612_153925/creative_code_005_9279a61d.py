"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deepseachain.online
Prompt: Develop a smart contract in Solidity that ensures limited editions of NFTs on the DeepSea marketplace are immutable and scarce.
Generated: DETERMINISTIC_9279a61d1b32bdab
Batch ID: 20250612_153925
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.deepsea.com/metadata/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title LimitedEditionNFT
 * @dev This contract implements a limited edition NFT on the DeepSea marketplace.
 * The NFTs are immutable and scarce, with a fixed supply.
 */
contract LimitedEditionNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for generating unique token IDs
    Counters.Counter private _tokenIdCounter;

    // Maximum supply of limited edition NFTs
    uint256 public maxSupply;

    // Mapping from token ID to the edition number
    mapping(uint256 => uint256) private _editionNumber;

    // Event emitted when a new NFT is minted
    event Minted(uint256 indexed tokenId, address indexed owner, uint256 editionNumber);

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     * @param name The name of the NFT collection
     * @param symbol The symbol of the NFT collection
     * @param supply The maximum supply of NFTs
     */
    constructor(string memory name, string memory symbol, uint256 supply) 
        ERC721(name, symbol) 
    {
        require(supply > 0, "Supply must be greater than zero");
        maxSupply = supply;
    }

    /**
     * @dev Mint a new NFT. Only the owner can call this function.
     * @param recipient The address that will receive the NFT
     */
    function mint(address recipient) external onlyOwner {
        require(_tokenIdCounter.current() < maxSupply, "Max supply reached");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _mint(recipient, tokenId);
        _editionNumber[tokenId] = tokenId + 1; // Edition number starts from 1

        emit Minted(tokenId, recipient, _editionNumber[tokenId]);
    }

    /**
     * @dev Get the edition number of a given token ID.
     * @param tokenId The ID of the token
     * @return The edition number of the token
     */
    function getEditionNumber(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        return _editionNumber[tokenId];
    }

    /**
     * @dev Override the _baseURI function to provide a base URI for metadata.
     * @return The base URI for the metadata
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return "https://api.deepsea.com/metadata/";
    }
}
```
