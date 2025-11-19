"""
Generated Code Metadata:
========================
Original URL: https://casinotg.pages.dev
Prompt: Write a Solidity smart contract to manage TG.Casino's High Roller NFT rewards, including rakeback and staking bonuses.
Generated: DETERMINISTIC_f5aa9e86c6262e93
Batch ID: 20250612_150435
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

contract HighRollerNFT is ERC721, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to store NFT reward details
    struct NFTReward {
        uint256 tokenId;
        uint256 rakebackPercentage; // Basis points (100 = 1%)
        uint256 stakingBonus; // Fixed bonus amount
        uint256 lastClaimedTimestamp;
        bool isActive;
    }

    // Mapping from token ID to reward details
    mapping(uint256 => NFTReward) public nftRewards;

    // Mapping from user address to their staked token IDs
    mapping(address => uint256[]) public userStakes;

    // Total rakeback pool
    uint256 public totalRakebackPool;
    
    // Total staking rewards pool
    uint256 public totalStakingRewardsPool;

    // Token ID counter
    uint256 private _tokenIdCounter;

    // Events
    event NFTMinted(address indexed owner, uint256 tokenId, uint256 rakeback, uint256 stakingBonus);
    event Staked(address indexed user, uint256 tokenId);
    event Unstaked(address indexed user, uint256 tokenId);
    event RakebackClaimed(address indexed user, uint256 amount);
    event StakingRewardsClaimed(address indexed user, uint256 amount);
    event RewardsPoolFunded(address indexed funder, uint256 rakebackAmount, uint256 stakingAmount);

    constructor() ERC721("TG.Casino High Roller NFT", "TGHR") {}

    /**
     * @dev Mint a new High Roller NFT with specified rewards
     */
    function mintNFT(address to, uint256 rakebackPercentage, uint256 stakingBonus) external onlyOwner {
        require(rakebackPercentage <= 10000, "Rakeback cannot exceed 100%");
        
        _tokenIdCounter++;
        uint256 newTokenId = _tokenIdCounter;
        
        _safeMint(to, newTokenId);
        
        nftRewards[newTokenId] = NFTReward({
            tokenId: newTokenId,
            rakebackPercentage: rakebackPercentage,
            stakingBonus: stakingBonus,
            lastClaimedTimestamp: block.timestamp,
            isActive: true
        });

        emit NFTMinted(to, newTokenId, rakebackPercentage, stakingBonus);
    }

    /**
     * @dev Stake an NFT to start earning rewards
     */
    function stakeNFT(uint256 tokenId) external nonReentrant {
        require(ownerOf(tokenId) == msg.sender, "Not the NFT owner");
        require(nftRewards[tokenId].isActive, "NFT not active for rewards");

        userStakes[msg.sender].push(tokenId);
        nftRewards[tokenId].lastClaimedTimestamp = block.timestamp;

        emit Staked(msg.sender, tokenId);
    }

    /**
     * @dev Unstake an NFT and claim pending rewards
     */
    function unstakeNFT(uint256 tokenId) external nonReentrant {
        require(ownerOf(tokenId) == msg.sender, "Not the NFT owner");
        
        _removeStake(msg.sender, tokenId);
        
        // Claim any pending rewards
        _claimRakeback(tokenId);
        _claimStakingRewards(tokenId);

        emit Unstaked(msg.sender, tokenId);
    }

    /**
     * @dev Claim rakeback rewards for a specific NFT
     */
    function claimRakeback(uint256 tokenId) external nonReentrant {
        require(ownerOf(tokenId) == msg.sender, "Not the NFT owner");
        _claimRakeback(tokenId);
    }

    /**
     * @dev Claim staking rewards for a specific NFT
     */
    function claimStakingRewards(uint256 tokenId) external nonReentrant {
        require(ownerOf(tokenId) == msg.sender, "Not the NFT owner");
        _claimStakingRewards(tokenId);
    }

    /**
     * @dev Fund the rewards pools
     */
    function fundRewardsPools(uint256 rakebackAmount, uint256 stakingAmount) external payable onlyOwner {
        totalRakebackPool = totalRakebackPool.add(rakebackAmount);
        totalStakingRewardsPool = totalStakingRewardsPool.add(stakingAmount);
        
        emit RewardsPoolFunded(msg.sender, rakebackAmount, stakingAmount);
    }

    /**
     * @dev Get pending rakeback for a specific NFT
     */
    function getPendingRakeback(uint256 tokenId) public view returns (uint256) {
        NFTReward memory reward = nftRewards[tokenId];
        if (!reward.isActive) return 0;
        
        uint256 timeStaked = block.timestamp.sub(reward.lastClaimedTimestamp);
        uint256 rakebackShare = totalRakebackPool.mul(reward.rakebackPercentage).div(10000);
        
        return rakebackShare.mul(timeStaked).div(1 days);
    }

    /**
     * @dev Get pending staking rewards for a specific NFT
     */
    function getPendingStakingRewards(uint256 tokenId) public view returns (uint256) {
        NFTReward memory reward = nftRewards[tokenId];
        if (!reward.isActive) return 0;
        
        uint256 timeStaked = block.timestamp.sub(reward.lastClaimedTimestamp);
        return reward.stakingBonus.mul(timeStaked).div(1 days);
    }

    /**
     * @dev Get all staked NFTs for a user
     */
    function getUserStakes(address user) external view returns (uint256[] memory) {
        return userStakes[user];
    }

    /**
     * @dev Internal function to claim rakeback
     */
    function _claimRakeback(uint256 tokenId) internal {
        uint256 pending = getPendingRakeback(tokenId);
        if (pending > 0) {
            nftRewards[tokenId].lastClaimedTimestamp = block.timestamp;
            totalRakebackPool = totalRakebackPool.sub(pending);
            
            (bool success, ) = msg.sender.call{value: pending}("");
            require(success, "Transfer failed");
            
            emit RakebackClaimed(msg.sender, pending);
        }
    }

    /**
     * @dev Internal function to claim staking rewards
     */
    function _claimStakingRewards(uint256 tokenId) internal {
        uint256 pending = getPendingStakingRewards(tokenId);
        if (pending > 0) {
            nftRewards[tokenId].lastClaimedTimestamp = block.timestamp;
            totalStakingRewardsPool = totalStakingRewardsPool.sub(pending);
            
            (bool success, ) = msg.sender.call{value: pending}("");
            require(success, "Transfer failed");
            
            emit StakingRewardsClaimed(msg.sender, pending);
        }
    }

    /**
     * @dev Remove a stake from user's staked NFTs
     */
    function _removeStake(address user, uint256 tokenId) internal {
        uint256[] storage stakes = userStakes[user];
        for (uint256 i = 0; i < stakes.length; i++) {
            if (stakes[i] == tokenId) {
                stakes[i] = stakes[stakes.length - 1];
                stakes.pop();
                break;
            }
        }
    }

    /**
     * @dev Override transfer functions to handle staking
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, tokenId);

        if (from != address(0)) {
            _removeStake(from, tokenId);
        }
    }
}
```
