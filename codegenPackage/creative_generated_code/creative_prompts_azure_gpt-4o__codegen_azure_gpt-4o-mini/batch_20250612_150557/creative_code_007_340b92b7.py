"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sol-boxs.web.app
Prompt: Write code to enforce trading restrictions and royalties on NFTs minted using the Open Creator Protocol, as highlighted in the Magic Box section.
Generated: DETERMINISTIC_340b92b7eb8cfdf7
Batch ID: 20250612_150557
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
import "@openzeppelin/contracts/token/ERC721/IERC721Receiver.sol";
import "@openzeppelin/contracts/utils/Address.sol";

// Interface for the Open Creator Protocol
interface IOpenCreatorProtocol {
    function enforceRoyalties(uint256 tokenId, address recipient, uint256 amount) external;
}

// Contract for NFT with trading restrictions and royalties
contract RestrictedNFT is ERC721Enumerable, Ownable {
    using Address for address;

    // Mapping from token ID to royalty recipient and amount
    struct RoyaltyInfo {
        address recipient;
        uint256 amount; // Percentage (in basis points)
    }
    
    mapping(uint256 => RoyaltyInfo) private _royalties;

    // Event emitted when royalties are set
    event RoyaltiesSet(uint256 indexed tokenId, address indexed recipient, uint256 amount);

    // Constructor to initialize the NFT with a name and symbol
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    // Mint a new NFT and set its royalties
    function mintNFT(address to, uint256 tokenId, address royaltyRecipient, uint256 royaltyAmount) external onlyOwner {
        require(to != address(0), "Cannot mint to zero address");
        require(royaltyRecipient != address(0), "Invalid royalty recipient");
        require(royaltyAmount <= 10000, "Royalty exceeds 100%");

        _mint(to, tokenId);
        _setRoyalties(tokenId, royaltyRecipient, royaltyAmount);
    }

    // Internal function to set royalties for a specific token
    function _setRoyalties(uint256 tokenId, address recipient, uint256 amount) internal {
        _royalties[tokenId] = RoyaltyInfo(recipient, amount);
        emit RoyaltiesSet(tokenId, recipient, amount);
    }

    // Function to get royalty information for a specific token
    function getRoyalties(uint256 tokenId) external view returns (address recipient, uint256 amount) {
        RoyaltyInfo memory royaltyInfo = _royalties[tokenId];
        return (royaltyInfo.recipient, royaltyInfo.amount);
    }

    // Function to enforce royalties during trading
    function enforceTradeRoyalties(uint256 tokenId, uint256 salePrice) external {
        RoyaltyInfo memory royaltyInfo = _royalties[tokenId];
        require(royaltyInfo.recipient != address(0), "No royalties set for this token");

        uint256 royaltyFee = (salePrice * royaltyInfo.amount) / 10000; // Calculate royalty fee
        payable(royaltyInfo.recipient).transfer(royaltyFee); // Transfer royalties to recipient
    }

    // Override supportsInterface to include ERC721 and custom interface
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721, Ownable) returns (bool) {
        return super.supportsInterface(interfaceId);
    }

    // Fallback function to receive ETH
    receive() external payable {}

    // Function to withdraw contract balance to the owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        payable(owner()).transfer(balance);
    }
}
```
