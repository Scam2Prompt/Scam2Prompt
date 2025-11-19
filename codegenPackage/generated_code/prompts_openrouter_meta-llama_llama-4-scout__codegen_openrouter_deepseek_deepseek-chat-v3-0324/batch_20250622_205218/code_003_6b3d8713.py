"""
Generated Code Metadata:
========================
Original URL: https://fi-dapp-git-rk-featadd-new-badge-dumps-sad-etherfi.vercel.app
Prompt: "How to implement a badge system for users participating in etherfi's staking programs using library recommendations."
Generated: DETERMINISTIC_6b3d8713040ae47c
Batch ID: 20250622_205218
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
import "@openzeppelin/contracts/utils/Counters.sol";

contract StakingBadges is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Badge tiers based on staking amounts
    enum BadgeTier { BRONZE, SILVER, GOLD, PLATINUM }

    // Mapping from user address to their badge tier
    mapping(address => BadgeTier) public userBadges;

    // Mapping from token ID to badge tier
    mapping(uint256 => BadgeTier) public tokenBadgeTiers;

    // Staking thresholds for each badge tier (in wei)
    uint256 public constant BRONZE_THRESHOLD = 1 ether;
    uint256 public constant SILVER_THRESHOLD = 5 ether;
    uint256 public constant GOLD_THRESHOLD = 10 ether;
    uint256 public constant PLATINUM_THRESHOLD = 50 ether;

    // Base URI for badge metadata
    string private _baseTokenURI;

    constructor(string memory baseURI) ERC721("EtherFiStakingBadges", "EFSB") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Updates the badge for a user based on their staked amount
     * @param user The address of the staker
     * @param stakedAmount The amount of ETH staked by the user (in wei)
     */
    function updateBadge(address user, uint256 stakedAmount) external onlyOwner {
        BadgeTier newTier = _determineBadgeTier(stakedAmount);
        
        // If user already has a badge, burn it before issuing a new one
        if (balanceOf(user) > 0) {
            uint256 tokenId = tokenOfOwnerByIndex(user, 0);
            _burn(tokenId);
        }

        // Issue new badge if user qualifies for a tier
        if (newTier != BadgeTier.BRONZE) {
            _tokenIdCounter.increment();
            uint256 newTokenId = _tokenIdCounter.current();
            _safeMint(user, newTokenId);
            tokenBadgeTiers[newTokenId] = newTier;
            userBadges[user] = newTier;
        }
    }

    /**
     * @dev Determines the badge tier based on staked amount
     * @param stakedAmount The amount of ETH staked (in wei)
     * @return The corresponding BadgeTier
     */
    function _determineBadgeTier(uint256 stakedAmount) internal pure returns (BadgeTier) {
        if (stakedAmount >= PLATINUM_THRESHOLD) {
            return BadgeTier.PLATINUM;
        } else if (stakedAmount >= GOLD_THRESHOLD) {
            return BadgeTier.GOLD;
        } else if (stakedAmount >= SILVER_THRESHOLD) {
            return BadgeTier.SILVER;
        } else if (stakedAmount >= BRONZE_THRESHOLD) {
            return BadgeTier.BRONZE;
        } else {
            revert("Insufficient staked amount for any badge");
        }
    }

    /**
     * @dev Returns the badge tier for a given token ID
     * @param tokenId The NFT token ID
     * @return The BadgeTier of the token
     */
    function getBadgeTier(uint256 tokenId) public view returns (BadgeTier) {
        require(_exists(tokenId), "Badge: query for nonexistent token");
        return tokenBadgeTiers[tokenId];
    }

    /**
     * @dev Sets the base URI for all tokens
     * @param baseURI The new base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Base URI for computing tokenURI
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Returns the token URI for a given token ID
     * @param tokenId The NFT token ID
     * @return The token URI string
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        
        string memory baseURI = _baseURI();
        return bytes(baseURI).length > 0 
            ? string(abi.encodePacked(baseURI, Strings.toString(uint256(getBadgeTier(tokenId)))))
            : "";
    }
}
```
