"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-omchain-io.pages.dev
Prompt: Develop a smart contract for minting NFTs on the Omchain platform, considering the unique features of the NFT Wall.
Generated: DETERMINISTIC_2a7b6a3e9353903b
Batch ID: 20250612_162207
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

// @title: NFT Wall Smart Contract
// @description: A smart contract for minting unique NFTs on the Omchain platform.
contract NFTWall is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking minted tokens
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to token URI
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    // Constructor to initialize the NFT contract with a name and symbol
    constructor() ERC721("NFT Wall", "NFTW") {}

    // @notice: Mint a new NFT
    // @param tokenURI: A string representing the metadata URI of the NFT
    function mint(string memory tokenURI) external onlyOwner {
        require(bytes(tokenURI).length > 0, "NFTWall: tokenURI cannot be empty");
        
        // Increment the token ID counter and get the new token ID
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the new token
        _safeMint(msg.sender, tokenId);
        
        // Set the token URI for the newly minted token
        _setTokenURI(tokenId, tokenURI);
        
        // Emit the NFTMinted event
        emit NFTMinted(msg.sender, tokenId, tokenURI);
    }

    // @notice: Set the token URI for a specific token ID
    // @param tokenId: The ID of the token
    // @param tokenURI: The new token URI
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "NFTWall: URI set of nonexistent token");
        _tokenURIs[tokenId] = tokenURI;
    }

    // @notice: Retrieve the token URI for a specific token ID
    // @param tokenId: The ID of the token
    // @return: The token URI of the specified token ID
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "NFTWall: URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }

    // @notice: Withdraw contract balance to the owner's address
    // Note: This function allows the owner to withdraw any Ether sent to the contract
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "NFTWall: No funds to withdraw");
        
        // Transfer the balance to the owner
        payable(owner()).transfer(balance);
    }

    // @notice: Fallback function to accept ETH transfers
    receive() external payable {}
}
```
