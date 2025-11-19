"""
Generated Code Metadata:
========================
Original URL: https://claimlootbot.pages.dev
Prompt: Create a Solidity contract that includes functionality for distributing revenue shares in ETH to $xLOOT NFT holders based on their holdings, as described in the LootBot documentation.
Generated: DETERMINISTIC_e29102124f63012f
Batch ID: 20250612_153648
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract xLOOTRevenueShare is Ownable, ReentrancyGuard {
    IERC721 public immutable xLOOT;
    uint256 public totalDistributed;
    uint256 public totalShares;
    uint256 public constant MAX_SUPPLY = 8000;

    // Mapping from token ID to claimed amount
    mapping(uint256 => uint256) public claimedAmounts;

    event RevenueDistributed(uint256 amount);
    event RevenueClaimed(address indexed recipient, uint256 tokenId, uint256 amount);

    constructor(address _xLOOT) {
        require(_xLOOT != address(0), "Invalid xLOOT address");
        xLOOT = IERC721(_xLOOT);
        totalShares = MAX_SUPPLY;
    }

    /**
     * @dev Distribute revenue to the contract
     */
    function distributeRevenue() external payable onlyOwner {
        require(msg.value > 0, "No ETH sent");
        totalDistributed += msg.value;
        emit RevenueDistributed(msg.value);
    }

    /**
     * @dev Calculate claimable amount for a token ID
     */
    function calculateClaimable(uint256 tokenId) public view returns (uint256) {
        require(tokenId > 0 && tokenId <= MAX_SUPPLY, "Invalid token ID");
        uint256 totalClaimable = (totalDistributed * 1 ether) / totalShares;
        return totalClaimable - claimedAmounts[tokenId];
    }

    /**
     * @dev Claim revenue for a specific xLOOT token
     */
    function claimRevenue(uint256 tokenId) external nonReentrant {
        require(xLOOT.ownerOf(tokenId) == msg.sender, "Not token owner");
        
        uint256 claimableAmount = calculateClaimable(tokenId);
        require(claimableAmount > 0, "Nothing to claim");

        claimedAmounts[tokenId] += claimableAmount;
        
        (bool success, ) = msg.sender.call{value: claimableAmount}("");
        require(success, "ETH transfer failed");

        emit RevenueClaimed(msg.sender, tokenId, claimableAmount);
    }

    /**
     * @dev Claim revenue for multiple xLOOT tokens
     */
    function batchClaimRevenue(uint256[] calldata tokenIds) external nonReentrant {
        uint256 totalClaimable = 0;

        for (uint256 i = 0; i < tokenIds.length; i++) {
            uint256 tokenId = tokenIds[i];
            require(xLOOT.ownerOf(tokenId) == msg.sender, "Not token owner");
            
            uint256 claimableAmount = calculateClaimable(tokenId);
            if (claimableAmount > 0) {
                claimedAmounts[tokenId] += claimableAmount;
                totalClaimable += claimableAmount;
                emit RevenueClaimed(msg.sender, tokenId, claimableAmount);
            }
        }

        require(totalClaimable > 0, "Nothing to claim");
        (bool success, ) = msg.sender.call{value: totalClaimable}("");
        require(success, "ETH transfer failed");
    }

    /**
     * @dev Withdraw any remaining ETH (only owner)
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        (bool success, ) = owner().call{value: balance}("");
        require(success, "ETH transfer failed");
    }
}
```
