"""
Generated Code Metadata:
========================
Original URL: https://iqratechpoint.pages.dev
Prompt: "Generate a Solidity code snippet for a basic NFT collection similar to the Iqranos, including functionality for exclusive access to rewards from IslamicCoin staking."
Generated: DETERMINISTIC_c5ce488b1540d825
Batch ID: 20250622_204712
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title: IslamicCoinNFT
// @dev: A basic NFT collection with exclusive access to rewards from IslamicCoin staking
contract IslamicCoinNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to staking status
    mapping(uint256 => bool) private _isStaked;

    // Event emitted when a token is staked
    event TokenStaked(uint256 indexed tokenId);
    // Event emitted when a token is unstaked
    event TokenUnstaked(uint256 indexed tokenId);

    // Base URI for metadata
    string private _baseTokenURI;

    // @dev: Constructor to initialize the NFT collection
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    // @dev: Function to mint a new NFT
    function mintNFT() external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _tokenIdCounter.increment();
    }

    // @dev: Function to stake an NFT for rewards
    function stakeToken(uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "You do not own this token");
        require(!_isStaked[tokenId], "Token is already staked");

        _isStaked[tokenId] = true;
        emit TokenStaked(tokenId);
    }

    // @dev: Function to unstake an NFT
    function unstakeToken(uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "You do not own this token");
        require(_isStaked[tokenId], "Token is not staked");

        _isStaked[tokenId] = false;
        emit TokenUnstaked(tokenId);
    }

    // @dev: Function to check if a token is staked
    function isTokenStaked(uint256 tokenId) external view returns (bool) {
        return _isStaked[tokenId];
    }

    // @dev: Override base URI function for metadata
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    // @dev: Function to set a new base URI (only owner)
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }
}
```
