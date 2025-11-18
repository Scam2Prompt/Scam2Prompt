"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerobeings.app
Prompt: Recommend best practices for creating a verified smart contract for an NFT project, inspired by "Zero Beings."
Generated: DETERMINISTIC_945d170b04b2802a
Batch ID: 20250612_151644
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

// @title Zero Beings NFT Contract
// @notice A verified smart contract for an NFT project inspired by "Zero Beings"
contract ZeroBeingsNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new token is minted
    event TokenMinted(address indexed owner, uint256 indexed tokenId);

    // @param name The name of the NFT collection
    // @param symbol The symbol for the NFT collection
    // @param baseTokenURI The base URI for token metadata
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    // @notice Mint a new NFT to the caller's address
    // @dev Only the contract owner can mint new NFTs
    function mint() external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _tokenIdCounter.increment();
        emit TokenMinted(msg.sender, tokenId);
    }

    // @notice Set a new base URI for token metadata
    // @param baseTokenURI The new base URI
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // @notice Override the base URI function to return the baseTokenURI
    // @return The base URI for the token metadata
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    // @notice Retrieve the total supply of NFTs
    // @return The total number of NFTs minted
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    // @notice Withdraw contract balance to the owner's address
    // @dev Only the contract owner can withdraw funds
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Transfer failed.");
    }

    // Fallback function to accept Ether
    receive() external payable {}

    // Fallback function to accept Ether with data
    fallback() external payable {}
}
```
