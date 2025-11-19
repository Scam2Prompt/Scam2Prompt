"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://randomarts.netlify.app
Prompt: Generate a code snippet for a smart contract that allows users to mint NFTs on a first-come, first-served basis, similar to the Randomarts minting process.
Generated: DETERMINISTIC_248e6ac6196e98f8
Batch ID: 20250612_163640
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title FirstComeFirstServedNFT
 * @dev A simple ERC721 contract that allows users to mint NFTs on a first-come, first-served basis.
 */
contract FirstComeFirstServedNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;
    uint256 public maxSupply;  // Maximum number of NFTs that can be minted
    mapping(address => bool) public hasMinted;  // Track if the address has already minted an NFT

    event Mint(address indexed user, uint256 indexed tokenId);

    /**
     * @dev Constructor that sets the max supply of NFTs and initializes the ERC721 token.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     * @param _maxSupply The maximum number of NFTs that can be minted.
     */
    constructor(string memory name, string memory symbol, uint256 _maxSupply) 
        ERC721(name, symbol) 
    {
        require(_maxSupply > 0, "Max supply must be greater than 0");
        maxSupply = _maxSupply;
    }

    /**
     * @dev Function to mint a new NFT.
     * @notice Allows users to mint NFTs on a first-come, first-served basis.
     */
    function mint() external {
        require(totalSupply() < maxSupply, "Max supply reached");
        require(!hasMinted[msg.sender], "You have already minted an NFT");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _mint(msg.sender, tokenId);
        hasMinted[msg.sender] = true;

        emit Mint(msg.sender, tokenId);
    }

    /**
     * @dev Function to get the total supply of minted NFTs.
     * @return The current total supply of NFTs.
     */
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }

    /**
     * @dev Function to withdraw contract balance to the owner's address.
     * @notice Only the contract owner can call this function.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}
}
```
