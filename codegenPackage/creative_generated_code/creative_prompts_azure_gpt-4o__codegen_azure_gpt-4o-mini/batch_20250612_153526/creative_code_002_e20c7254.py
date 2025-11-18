"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snapshot-ethosmobileorg.pages.dev
Prompt: Create a smart contract function that facilitates the minting of NFTs for a limited-supply product, referencing the ethOS phone minting process.
Generated: DETERMINISTIC_e20c72546674495c
Batch ID: 20250612_153526
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

/// @title LimitedSupplyNFT
/// @notice A smart contract for minting limited supply NFTs
contract LimitedSupplyNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // Counter to keep track of the token IDs
    Counters.Counter private _tokenIdCounter;

    // Maximum number of NFTs allowed
    uint256 public maxSupply;

    // Mapping to track if an address has already minted an NFT
    mapping(address => bool) public hasMinted;

    // Event emitted when an NFT is minted
    event Mint(address indexed to, uint256 indexed tokenId);

    /// @param _name Name of the NFT collection
    /// @param _symbol Symbol of the NFT collection
    /// @param _maxSupply Maximum number of NFTs that can be minted
    constructor(string memory _name, string memory _symbol, uint256 _maxSupply) 
        ERC721(_name, _symbol) 
    {
        require(_maxSupply > 0, "Max supply must be greater than zero");
        maxSupply = _maxSupply;
    }

    /// @notice Function to mint a new NFT
    /// @dev Only the contract owner can mint NFTs
    function mint() external {
        // Check if the maximum supply has been reached
        require(totalSupply() < maxSupply, "Max supply reached");
        // Check if the sender has already minted an NFT
        require(!hasMinted[msg.sender], "Address has already minted");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT to the sender
        _mint(msg.sender, tokenId);
        hasMinted[msg.sender] = true;

        emit Mint(msg.sender, tokenId);
    }

    /// @notice Function to get the total supply of minted NFTs
    /// @return The current total supply of NFTs
    function totalMinted() external view returns (uint256) {
        return totalSupply();
    }

    /// @notice Function to withdraw the contract balance to the owner
    /// @dev Only the owner can withdraw funds
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        // Transfer the balance to the owner
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Transfer failed");
    }

    /// @notice Fallback function to accept ETH
    receive() external payable {}
}
```
