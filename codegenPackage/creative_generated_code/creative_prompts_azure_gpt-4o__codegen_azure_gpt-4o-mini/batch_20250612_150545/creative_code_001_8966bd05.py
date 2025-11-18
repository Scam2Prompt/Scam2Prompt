"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stealt-mint.web.app
Prompt: Generate code to implement a minting function for NFTs using the Open Creator Protocol, ensuring enforced and dynamic royalties as outlined in the Magic Box stealth mint event.
Generated: DETERMINISTIC_8966bd0531e19716
Batch ID: 20250612_150545
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";

contract NFTCollection is ERC721Enumerable, Ownable, ERC721Burnable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to hold royalty information
    struct RoyaltyInfo {
        address receiver;
        uint96 percentage; // percentage in basis points (e.g., 500 = 5%)
    }

    // Mapping from token ID to royalty info
    mapping(uint256 => RoyaltyInfo) private _royalties;

    // Event to emit when a new NFT is minted
    event NFTMinted(address indexed to, uint256 indexed tokenId, uint96 royalty);

    // Constructor to set the NFT collection name and symbol
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    // Function to mint a new NFT
    function mintNFT(address to, uint96 royaltyPercentage) external onlyOwner {
        require(to != address(0), "Mint to the zero address");
        require(royaltyPercentage <= 10000, "Royalty percentage exceeds 100%"); // Ensure it's not more than 100%

        // Increment the token ID and mint the NFT
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _mint(to, tokenId);

        // Set the royalty info for the minted NFT
        _royalties[tokenId] = RoyaltyInfo(to, royaltyPercentage);

        // Emit the NFT minting event
        emit NFTMinted(to, tokenId, royaltyPercentage);
    }

    // Function to get royalty information for a given token ID
    function getRoyaltyInfo(uint256 tokenId) external view returns (address, uint96) {
        RoyaltyInfo memory royaltyInfo = _royalties[tokenId];
        return (royaltyInfo.receiver, royaltyInfo.percentage);
    }

    // Override the supportsInterface function to include ERC2981 for royalty standards
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721, IERC721) returns (bool) {
        return super.supportsInterface(interfaceId);
    }

    // Function to withdraw funds (if applicable)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    // Fallback function to receive ETH
    receive() external payable {}

    // Function to handle receiving royalties
    function onRoyaltyReceived(uint256 tokenId, uint256 salePrice) external {
        RoyaltyInfo memory royaltyInfo = _royalties[tokenId];
        uint256 royaltyAmount = (salePrice * royaltyInfo.percentage) / 10000; // Calculate royalty
        require(royaltyAmount <= address(this).balance, "Not enough funds for royalty");
        payable(royaltyInfo.receiver).transfer(royaltyAmount);
    }
}
```
