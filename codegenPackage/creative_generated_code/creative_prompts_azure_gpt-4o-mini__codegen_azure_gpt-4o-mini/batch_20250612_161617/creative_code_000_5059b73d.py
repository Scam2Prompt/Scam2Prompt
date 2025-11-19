"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kevinland.pages.dev
Prompt: Generate a smart contract in Solidity for minting NFTs on the Ethereum network, specifically for a project like KevinLand where users can adopt multiple NFTs at once.
Generated: DETERMINISTIC_5059b73d92ab3bc3
Batch ID: 20250612_161617
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title KevinLandNFT
// @dev A smart contract for minting and managing NFTs for the KevinLand project
contract KevinLandNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Base URI for the token metadata
    string private _baseTokenURI;

    // Event emitted when new NFTs are minted
    event NFTsMinted(address indexed owner, uint256[] tokenIds);

    // Mapping to track adopted NFTs per user
    mapping(address => uint256[]) public userAdoptedTokens;

    // @dev Sets the name and symbol of the NFT collection
    // @param name The name of the NFT collection
    // @param symbol The symbol of the NFT collection
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    // @dev Allows the owner to set the base URI for the token metadata
    // @param baseURI The base URI to set
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    // @dev Returns the base URI for the token metadata
    // @return The base URI string
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    // @dev Mints multiple NFTs for the sender
    // @param quantity The number of NFTs to mint
    function mintNFTs(uint256 quantity) external {
        require(quantity > 0, "Quantity must be greater than zero");
        require(quantity <= 10, "Cannot mint more than 10 NFTs at once");

        uint256[] memory tokenIds = new uint256[](quantity);
        for (uint256 i = 0; i < quantity; i++) {
            uint256 tokenId = _tokenIdCounter.current();
            _mint(msg.sender, tokenId);
            tokenIds[i] = tokenId;
            _tokenIdCounter.increment();
        }

        userAdoptedTokens[msg.sender] = tokenIds;

        emit NFTsMinted(msg.sender, tokenIds);
    }

    // @dev Retrieves the token IDs adopted by a user
    // @param user The address of the user
    // @return An array of token IDs adopted by the user
    function getAdoptedTokens(address user) external view returns (uint256[] memory) {
        return userAdoptedTokens[user];
    }
}
```
