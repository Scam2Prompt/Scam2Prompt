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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract GodCandleNFT is ERC721, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // MEV revenue share percentage (37.77%)
    uint256 public constant MEV_REVENUE_SHARE = 3777; // Basis points (37.77%)
    uint256 public constant BASIS_POINTS = 10000;

    // Total MEV revenue collected
    uint256 public totalMEVRevenue;

    // Mapping from token ID to accumulated MEV rewards
    mapping(uint256 => uint256) public tokenIdToRewards;

    // Mapping from token ID to last claimed block
    mapping(uint256 => uint256) public lastClaimedBlock;

    // Counter for token IDs
    uint256 private _tokenIdCounter;

    // Events
    event MEVRevenueReceived(uint256 amount);
    event RewardsClaimed(uint256 tokenId, address recipient, uint256 amount);
    event TokenMinted(uint256 tokenId, address recipient);

    constructor() ERC721("GodCandleNFT", "GCNFT") {}

    /**
     * @dev Mint a new NFT to the specified address
     * @param to The address that will receive the NFT
     */
    function mint(address to) external onlyOwner {
        uint256 tokenId = _tokenIdCounter;
        _tokenIdCounter++;
        _safeMint(to, tokenId);
        emit TokenMinted(tokenId, to);
    }

    /**
     * @dev Receive MEV revenue and distribute according to shares
     */
    receive() external payable nonReentrant {
        require(msg.value > 0, "No value sent");
        totalMEVRevenue = totalMEVRevenue.add(msg.value);

        uint256 distributedAmount = msg.value.mul(MEV_REVENUE_SHARE).div(BASIS_POINTS);
        uint256 remainingAmount = msg.value.sub(distributedAmount);

        // Distribute to NFT holders
        if (_tokenIdCounter > 0) {
            uint256 perTokenShare = distributedAmount.div(_tokenIdCounter);
            for (uint256 i = 0; i < _tokenIdCounter; i++) {
                if (_exists(i)) {
                    tokenIdToRewards[i] = tokenIdToRewards[i].add(perTokenShare);
                }
            }
        }

        // Send remaining to contract owner
        if (remainingAmount > 0) {
            (bool success, ) = owner().call{value: remainingAmount}("");
            require(success, "Transfer failed");
        }

        emit MEVRevenueReceived(msg.value);
    }

    /**
     * @dev Claim accumulated MEV rewards for a specific token
     * @param tokenId The token ID to claim rewards for
     */
    function claimRewards(uint256 tokenId) external nonReentrant {
        require(ownerOf(tokenId) == msg.sender, "Not token owner");
        require(tokenIdToRewards[tokenId] > 0, "No rewards to claim");

        uint256 rewards = tokenIdToRewards[tokenId];
        tokenIdToRewards[tokenId] = 0;
        lastClaimedBlock[tokenId] = block.number;

        (bool success, ) = msg.sender.call{value: rewards}("");
        require(success, "Transfer failed");

        emit RewardsClaimed(tokenId, msg.sender, rewards);
    }

    /**
     * @dev Get claimable rewards for a specific token
     * @param tokenId The token ID to check
     * @return The amount of claimable rewards
     */
    function getClaimableRewards(uint256 tokenId) external view returns (uint256) {
        return tokenIdToRewards[tokenId];
    }

    /**
     * @dev Get total MEV revenue collected
     * @return The total MEV revenue
     */
    function getTotalMEVRevenue() external view returns (uint256) {
        return totalMEVRevenue;
    }
}
```
