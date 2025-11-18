"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minthidden.web.app
Prompt: Write code to implement a free NFT minting process with a limit of 3 NFTs per wallet, as seen in the Magic Box minting example.
Generated: DETERMINISTIC_ed36b7697e6cdec0
Batch ID: 20250612_150601
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

// Custom NFT contract that allows free minting with a limit of 3 NFTs per wallet
contract FreeMintNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    // State variables
    Counters.Counter private _tokenIdCounter; // Counter for token IDs
    mapping(address => uint256) public mintCount; // Tracks the number of NFTs minted per wallet
    uint256 public constant MAX_NFTS_PER_WALLET = 3; // Limit of NFTs that can be minted per wallet

    // Event to emit when an NFT is minted
    event NFTMinted(address indexed owner, uint256 tokenId);

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("FreeMintNFT", "FMNFT") {}

    // Function to mint a new NFT
    function mintNFT() external {
        require(mintCount[msg.sender] < MAX_NFTS_PER_WALLET, "Mint limit reached for this wallet");
        
        // Increment the token ID counter and get the new token ID
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        // Mint the NFT to the caller's address
        _mint(msg.sender, tokenId);
        
        // Update the mint count for the caller
        mintCount[msg.sender]++;
        
        // Emit the NFTMinted event
        emit NFTMinted(msg.sender, tokenId);
    }

    // Function to get the total number of NFTs minted by a specific wallet
    function getMintCount(address owner) external view returns (uint256) {
        return mintCount[owner];
    }

    // Function to withdraw any funds (if any) from the contract (onlyOwner)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to prevent ether from being sent to this contract
    receive() external payable {
        revert("No ether accepted");
    }
}
```
