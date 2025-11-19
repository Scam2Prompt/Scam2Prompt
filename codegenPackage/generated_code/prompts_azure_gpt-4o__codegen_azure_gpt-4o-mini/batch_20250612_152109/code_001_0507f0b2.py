"""
Generated Code Metadata:
========================
Original URL: https://godcandle404-en.web.app
Prompt: Create a Solidity contract for an ERC-721 NFT that integrates MEV revenue sharing, ensuring holders receive 37.77% of MEV revenue as specified in the God Candle ecosystem.
Generated: DETERMINISTIC_0507f0b24043603a
Batch ID: 20250612_152109
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract MEVRevenueSharingNFT is ERC721, Ownable {
    using SafeMath for uint256;

    // Mapping from token ID to holder's share of MEV revenue
    mapping(uint256 => address) private _tokenOwners;
    mapping(uint256 => uint256) private _mevShares;

    // Total MEV revenue collected
    uint256 public totalMEVRevenue;

    // MEV revenue share percentage (in basis points)
    uint256 public constant MEV_SHARE_PERCENTAGE = 3777; // 37.77%

    // Event emitted when MEV revenue is distributed
    event MEVRevenueDistributed(uint256 amount);

    // Constructor to initialize the NFT contract
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    // Function to mint a new NFT
    function mintNFT(address to, uint256 tokenId) external onlyOwner {
        _mint(to, tokenId);
        _tokenOwners[tokenId] = to;
    }

    // Function to receive MEV revenue
    function receiveMEVRevenue() external payable onlyOwner {
        require(msg.value > 0, "Must send MEV revenue");
        totalMEVRevenue = totalMEVRevenue.add(msg.value);
        emit MEVRevenueDistributed(msg.value);
    }

    // Function to distribute MEV revenue to NFT holders
    function distributeMEVRevenue() external onlyOwner {
        require(totalMEVRevenue > 0, "No MEV revenue to distribute");

        uint256 totalSupply = totalSupply();
        uint256 sharePerToken = totalMEVRevenue.mul(MEV_SHARE_PERCENTAGE).div(10000).div(totalSupply);

        for (uint256 i = 0; i < totalSupply; i++) {
            address owner = ownerOf(i);
            if (owner != address(0)) {
                _mevShares[i] = _mevShares[i].add(sharePerToken);
            }
        }

        // Reset total MEV revenue after distribution
        totalMEVRevenue = 0;
    }

    // Function to withdraw MEV revenue for a specific token holder
    function withdrawMEVRevenue(uint256 tokenId) external {
        require(msg.sender == ownerOf(tokenId), "Only the token owner can withdraw");
        uint256 amount = _mevShares[tokenId];
        require(amount > 0, "No MEV revenue to withdraw");

        // Reset the share after withdrawal
        _mevShares[tokenId] = 0;

        // Transfer the MEV revenue to the token holder
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
    }

    // Function to check the MEV revenue share for a specific token
    function getMEVShare(uint256 tokenId) external view returns (uint256) {
        return _mevShares[tokenId];
    }

    // Fallback function to accept ETH
    receive() external payable {
        receiveMEVRevenue();
    }
}
```
